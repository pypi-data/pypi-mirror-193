# -*- coding: utf8 -*-
#
from collections import defaultdict
from typing import Union

import torch
from transformers import optimization


def build_optimizer_for_pretrained(model: torch.nn.Module,
                                   pretrained: torch.nn.Module,
                                   lr=1e-5,
                                   weight_decay=0.01,
                                   eps=1e-8,
                                   transformer_lr=None,
                                   transformer_weight_decay=None,
                                   no_decay=('bias', 'LayerNorm.bias', 'LayerNorm.weight'),
                                   **kwargs):
    """
    copied from HanLP
    :param model:
    :param pretrained:
    :param lr:
    :param weight_decay:
    :param eps:
    :param transformer_lr:
    :param transformer_weight_decay:
    :param no_decay:
    :param kwargs:
    :return:
    """
    if transformer_lr is None:
        transformer_lr = lr
    if transformer_weight_decay is None:
        transformer_weight_decay = weight_decay
    params = defaultdict(lambda: defaultdict(list))
    pretrained = set(pretrained.parameters())
    if isinstance(no_decay, tuple):
        def no_decay_fn(name):
            return any(nd in name for nd in no_decay)
    else:
        assert callable(no_decay), 'no_decay has to be callable or a tuple of str'
        no_decay_fn = no_decay
    for n, p in model.named_parameters():
        is_pretrained = 'pretrained' if p in pretrained else 'non_pretrained'
        is_no_decay = 'no_decay' if no_decay_fn(n) else 'decay'
        params[is_pretrained][is_no_decay].append(p)

    grouped_parameters = [
        {'params': params['pretrained']['decay'], 'weight_decay': transformer_weight_decay, 'lr': transformer_lr},
        {'params': params['pretrained']['no_decay'], 'weight_decay': 0.0, 'lr': transformer_lr},
        {'params': params['non_pretrained']['decay'], 'weight_decay': weight_decay, 'lr': lr},
        {'params': params['non_pretrained']['no_decay'], 'weight_decay': 0.0, 'lr': lr},
    ]

    return optimization.AdamW(
        grouped_parameters,
        lr=lr,
        weight_decay=weight_decay,
        eps=eps,
        **kwargs)


def build_optimizer_scheduler_with_transformer(model: torch.nn.Module,
                                               transformer: torch.nn.Module,
                                               lr: float,
                                               transformer_lr: float,
                                               num_training_steps: int,
                                               warmup_steps: Union[float, int],
                                               weight_decay: float,
                                               adam_epsilon: float,
                                               no_decay=('bias', 'LayerNorm.bias', 'LayerNorm.weight')):
    optimizer = build_optimizer_for_pretrained(model,
                                               transformer,
                                               lr,
                                               weight_decay,
                                               eps=adam_epsilon,
                                               transformer_lr=transformer_lr,
                                               no_decay=no_decay)
    if isinstance(warmup_steps, float):
        assert 0 < warmup_steps < 1, 'warmup_steps has to fall in range (0, 1) when it is float.'
        warmup_steps = num_training_steps * warmup_steps
    scheduler = optimization.get_linear_schedule_with_warmup(optimizer, warmup_steps, num_training_steps)
    return optimizer, scheduler
