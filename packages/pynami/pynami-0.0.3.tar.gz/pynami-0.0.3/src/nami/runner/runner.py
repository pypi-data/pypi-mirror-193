import os
import shutil
from typing import Dict, Union

import torch.nn as nn
from franky.logging import OPLogger
from franky.model import is_model_wrapper
from franky.registry import MODELS
from franky.runner import Runner as Franky_Runner

from nami.registry import MODELS

logger = OPLogger.get_current_instance()


class Runner(Franky_Runner):
    def build_model(self, model: Union[nn.Module, Dict]) -> nn.Module:
        """Build model.

        If ``model`` is a dict, it will be used to build a nn.Module object.
        Else, if ``model`` is a nn.Module object it will be returned directly.

        An demo of ``model``::

            model = dict(type='ResNet')

        Args:
            model (nn.Module or dict): A ``nn.Module`` object or a dict to
                build nn.Module object. If ``model`` is a nn.Module object,
                just returns itself.

        Note:
            The returned model must implement ``train_step``, ``test_step``
            if ``runner.train`` or ``runner.test`` will be called. If
            ``runner.val`` will be called or ``val_cfg`` is configured,
            model must implement `val_step`.

        Returns:
            nn.Module: Model build from ``model``.
        """
        if isinstance(model, nn.Module):
            return model
        elif isinstance(model, dict):
            model = MODELS.build(model)
            return model  # type: ignore
        else:
            raise TypeError('model should be a nn.Module object or dict, '
                            f'but got {model}')

    def train(self) -> nn.Module:
        """Launch training.

        Returns:
            nn.Module: The model after training.
        """
        if is_model_wrapper(self.model):
            ori_model = self.model.module
        else:
            ori_model = self.model
        assert hasattr(ori_model, 'train_step'), (
            'If you want to train your model, please make sure your model '
            'has implemented `train_step`.')

        if self._val_loop is not None:
            assert hasattr(ori_model, 'val_step'), (
                'If you want to validate your model, please make sure your '
                'model has implemented `val_step`.')

        if self._train_loop is None:
            raise RuntimeError(
                '`self._train_loop` should not be None when calling train '
                'method. Please provide `train_dataloader`, `train_cfg`, '
                '`optimizer` and `param_scheduler` arguments when '
                'initializing runner.')

        self._train_loop = self.build_train_loop(
            self._train_loop)  # type: ignore

        # `build_optimizer` should be called before `build_param_scheduler`
        #  because the latter depends on the former
        self.optim_wrapper = self.build_optim_wrapper(self.optim_wrapper)
        # Automatically scaling lr by linear scaling rule
        self.scale_lr(self.optim_wrapper, self.auto_scale_lr)

        if self.param_schedulers is not None:
            self.param_schedulers = self.build_param_scheduler(  # type: ignore
                self.param_schedulers)  # type: ignore

        if self._val_loop is not None:
            self._val_loop = self.build_val_loop(
                self._val_loop)  # type: ignore
        # TODO: add a contextmanager to avoid calling `before_run` many times
        self.call_hook('before_run')

        # initialize the model weights
        # not init, prevent repeat initialization
        # self._init_model_weights()
        # make sure checkpoint-related hooks are triggered after `before_run`
        self.load_or_resume()

        # Initiate inner count of `optim_wrapper`.
        self.optim_wrapper.initialize_count_status(
            self.model,
            self._train_loop.iter,  # type: ignore
            self._train_loop.max_iters)  # type: ignore

        model = self.train_loop.run()  # type: ignore
        self.call_hook('after_run')
        return model

    def save_transformers_format(self, load_from=None, saved_dir='./saved_transformers',
                                 copy_tokenizer=True, tokenizer_dir='./tokenizer', **kwargs):
        if load_from is None:
            load_from = self.cfg['load_from']
        self.load_checkpoint(load_from)
        self.model.save_pretrained(saved_dir)
        logger.info('Save model to {} completed, from {}'.format(saved_dir, load_from))
        if copy_tokenizer is False:
            logger.warning('Tokenizer is not copied to {}'.format(saved_dir))
        else:
            shutil.copytree(tokenizer_dir, saved_dir, dirs_exist_ok=True)
            logger.info('Save tokenizer to {} completed, from {}'.format(saved_dir, tokenizer_dir))
