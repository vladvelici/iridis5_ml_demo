#!/bin/bash

#SBATCH --time=16:20:00

#SBATCH --mail-user=vsv1g12@soton.ac.uk
#SBATCH --mail-type=ALL

i=${SLURM_ARRAY_TASK_ID}

./train.py --lr_index $i
