#!/bin/sh
#SBATCH -o train.%j.out
#SBATCH -p gpu
#SBATCH -w gpunode[3-4]
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=4
#SBATCH --gres=gpu:4
#SBATCH --cpus-per-task=5
CONFIG='configs/cifar_memory.py'
TRAIN_PY='../nami_project/tools/train.py'
PYTHONPATH="../mmclassification":$PYTHONPATH \
  srun python -u $TRAIN_PY $CONFIG --launcher=slurm
