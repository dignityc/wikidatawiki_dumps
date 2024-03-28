#!/bin/bash -l
#SBATCH --output=/scratch/prj/inf_wqp/Wikidatawiki_dumps/download_log-3.out

st_idx=924
python meta_history_download.py $st_idx


