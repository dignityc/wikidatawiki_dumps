#!/bin/bash -l
#SBATCH --output=/scratch/prj/inf_wqp/Wikidatawiki_dumps/download_log-2.out

st_idx=462
python meta_history_download.py $st_idx


