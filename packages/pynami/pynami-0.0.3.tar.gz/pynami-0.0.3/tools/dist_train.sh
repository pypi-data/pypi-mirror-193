#!/usr/bin/env bash

TRAIN_PY='../nami_project/tools/train.py'
CONFIG='configs/cifar_vit.py'
GPUS=2
NNODES=${NNODES:-1}
NODE_RANK=${NODE_RANK:-0}
PORT=${PORT:-29502}
MASTER_ADDR=${MASTER_ADDR:-"127.0.0.1"}

PYTHONPATH="../mmclassification":$PYTHONPATH \
python -m torch.distributed.launch \
    --nnodes=$NNODES \
    --node_rank=$NODE_RANK \
    --master_addr=$MASTER_ADDR \
    --nproc_per_node=$GPUS \
    --master_port=$PORT \
    $TRAIN_PY \
    $CONFIG \
    --launcher pytorch
