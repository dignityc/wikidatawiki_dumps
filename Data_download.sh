#!/bin/bash -l
#SBATCH --output=/scratch/prj/inf_wqp/download_log.out
#SBATCH --job-name=gpu
#SBATCH --gres=gpu:1

python Wikidatawiki_dumps/meta_history_download.py 
