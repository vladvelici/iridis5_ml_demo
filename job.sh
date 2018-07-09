#!/bin/bash


#SBATCH --time=01:20:00

#SBATCH --mail-user=vsv1g12@soton.ac.uk
#SBATCH --mail-type=ALL

source venv/bin/activate

i=${SLURM_ARRAY_TASK_ID}

./train.py --index-array $i -o $1 --epochs 25
