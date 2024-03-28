#!/bin/bash -l
#SBATCH --output=/scratch/prj/inf_wqp/Wikidatawiki_dumps/download_log-1.out

st_idx=0
python meta_history_download.py $st_idx


