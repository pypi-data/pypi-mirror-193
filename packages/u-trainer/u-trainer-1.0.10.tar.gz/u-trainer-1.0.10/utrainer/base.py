# -*- coding: utf8 -*-
#
import logging
import math
import os
from abc import ABC, abstractmethod
from typing import Union, Type, Dict

import torch
from torch import nn
from torch.utils.data import dataloader
from torch.utils.tensorboard import SummaryWriter
from tqdm import tqdm
from transformers import set_seed, get_linear_schedule_with_warmup
from torch.optim import AdamW

from utrainer.logger import trainer_log
from utrainer.metric import Metric
from utrainer.attack_train_utils import FGM, PGD


class UTrainer(ABC):
    def __init__(self):
        set_seed(1000)
        self.save_path = os.environ.get("SAVE_PATH", os.path.join(os.path.expanduser('~'), '.u-trainer', type(self).__name__))
        os.makedirs(self.save_path, exist_ok=True)

        self.tb_writer = SummaryWriter(os.path.join(self.save_path, 'tb_log'))

        self.device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

        self._model = None
        # 使用对抗训练
        self.attack_cls = {"FGM": FGM, "PGD": PGD}.get(os.environ.get('ATTACK_ALGO', "").upper())

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model
        self._model.to(self.device)
        if self.attack_cls:
            self.attack_ins = self.attack_cls(self._model)
            trainer_log.info(f'use attack {type(self.attack_ins).__name__}')

    def build_optimizer(
            self,
            warmup_steps: Union[float, int],
            num_training_steps: int,
            lr=1e-5,
            weight_decay=0.01
    ):
        if warmup_steps <= 1:
            warmup_steps = int(num_training_steps * warmup_steps)
        # Prepare optimizer and schedule (linear warmup and decay)
        no_decay = ["bias", "LayerNorm.weight"]
        optimizer_grouped_parameters = [
            {
                "params": [p for n, p in self.model.named_parameters() if not any(nd in n for nd in no_decay)],
                "weight_decay": weight_decay,
            },
            {
                "params": [p for n, p in self.model.named_parameters() if any(nd in n for nd in no_decay)],
                "weight_decay": 0.0,
            },
        ]
        optimizer = AdamW(optimizer_grouped_parameters, lr=lr)

        scheduler = get_linear_schedule_with_warmup(
            optimizer, num_warmup_steps=warmup_steps, num_training_steps=num_training_steps
        )
        return optimizer, scheduler

    def fit(
            self,
            train_dl: dataloader.DataLoader,
            dev_dl: dataloader.DataLoader,
            epochs: int = 30,
            lr: Union[int, float] = 1e-5,
            warmup_steps: Union[int, float] = 0.1,
            metric_cls: Type[Metric] = None,
            fine_tune_model=None
    ):
        optimizer, scheduler = self.build_optimizer(
            warmup_steps=warmup_steps,
            num_training_steps=len(train_dl) * epochs,
            lr=lr
        )
        if fine_tune_model:
            self.load_weights(fine_tune_model)

        min_loss = math.inf

        for epoch in range(epochs):
            train_loss = self._fit_dataloader(
                train_dl=train_dl,
                optimizer=optimizer,
                scheduler=scheduler,
                epoch=epoch
            )
            self.tb_writer.add_scalar('train_loss', train_loss, epoch)

            train_metric = self._evaluate_dataloader(
                dl=train_dl,
                metric=metric_cls(),
                epoch=epoch
            )
            train_metric_score = train_metric.score()
            train_metric_report = train_metric.report() or {}

            self.tb_writer.add_scalar('train_metric_score', train_metric_score, epoch)
            trainer_log.info(f'[Epoch: {epoch}] train_metric_score: {train_metric_score} train_loss: {train_loss}')
            if train_metric_report:
                self.tb_writer.add_scalars('train_metric_report', train_metric_report, epoch)
                trainer_log.info(f'[Epoch: {epoch}] train_metric_report: {train_metric_report}')

            dev_metric = self._evaluate_dataloader(
                dl=dev_dl,
                metric=metric_cls(),
                epoch=epoch
            )
            dev_metric_score = dev_metric.score()
            dev_metric_report = dev_metric.report() or {}

            self.tb_writer.add_scalar('dev_metric_score', dev_metric_score, epoch)
            trainer_log.info(f'[Epoch: {epoch}] dev_metric_score: {dev_metric_score}')

            if dev_metric_report:
                self.tb_writer.add_scalars('dev_metric_report', dev_metric_report, epoch)
                trainer_log.info(f'[Epoch: {epoch}] dev_metric_report: {dev_metric_report}')

            # savepoint
            if train_loss < min_loss:
                self.save_weights(f'loss_{train_loss:.4f}_epoch_{epoch}.pt')
                min_loss = train_loss
            self.save_weights(f'dev_{dev_metric_score:.4f}_epoch_{epoch}.pt')

    def _fit_dataloader(
            self,
            train_dl: dataloader.DataLoader,
            optimizer,
            scheduler,
            epoch
    ) -> float:
        self.model.train()
        total_loss = 0
        for batch_idx, batch_data in tqdm(enumerate(train_dl), desc=f'fit[{epoch}]'):
            train_info = self.train_steps(batch_idx, batch_data)
            loss = train_info['loss']
            detail_loss = train_info.get('detail_loss', {})
            total_loss += loss.item()
            loss.backward()

            if hasattr(self, "attack_ins"):
                self.attack_ins.attack()
                train_info = self.train_steps(batch_idx, batch_data)
                adv_loss = train_info['loss']
                adv_loss.backward()
                self.attack_ins.restore()

            self._step(optimizer=optimizer, scheduler=scheduler)

            if detail_loss:
                detail_loss = {key: getattr(value, "item", lambda: value)() for key, value in detail_loss.items()}
                self.tb_writer.add_scalars('detail_loss', detail_loss, epoch * len(train_dl) + batch_idx)
            # 删除
            del train_info
        return total_loss / len(train_dl)

    @abstractmethod
    def train_steps(self, batch_idx, batch_data) -> Dict:
        raise NotImplementedError

    @abstractmethod
    def evaluate_steps(self, batch_idx, batch_data):
        raise NotImplementedError

    @torch.no_grad()
    def _evaluate_dataloader(self, dl: dataloader.DataLoader, metric: Metric, epoch):
        self.model.eval()
        for batch_idx, batch_data in tqdm(enumerate(dl), desc=f'eval[{epoch}]'):
            out = self.evaluate_steps(batch_idx, batch_data)
            metric.step(out)
        return metric

    def _step(self, optimizer, scheduler):
        torch.nn.utils.clip_grad_norm_(self.model.parameters(), 5)
        optimizer.step()
        optimizer.zero_grad()
        scheduler.step()

    def save_weights(self, save_name):
        dir_path = os.path.join(self.save_path, 'savepoint')
        os.makedirs(dir_path, exist_ok=True)
        save_path = os.path.join(dir_path, save_name)

        if not isinstance(self.model, nn.DataParallel):
            torch.save(self.model.state_dict(), save_path)
        else:
            torch.save(self.model.module.state_dict(), save_path)

    def load_weights(self, save_path):
        if not isinstance(self.model, nn.DataParallel):
            self.model.load_state_dict(torch.load(save_path))
        else:
            self.model.module.load_state_dict(torch.load(save_path))
