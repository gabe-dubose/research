#!/bin/bash

qiime dada2 denoise-paired \
--i-demultiplexed-seqs /home/jdubos2/NCDMIC/data/process_data/NCDMIC_raw_sequences.qza \
--p-trim-left-f 0 \
--p-trim-left-r 0 \
--p-trunc-len-f 227 \
--p-trunc-len-r 224 \
--o-table /home/jdubos2/NCDMIC/data/process_data/quality_control/NCDMIC_sequences_table.qza \
--o-representative-sequences /home/jdubos2/NCDMIC/data/process_data/quality_control/NCDMIC_rep_seqs.qza \
--o-denoising-stats /home/jdubos2/NCDMIC/data/process_data/quality_control/NCDMIC_denoising_stats.qza