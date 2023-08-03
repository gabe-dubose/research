#!/bin/bash

qiime feature-table summarize \
--i-table /home/jdubos2/NCDMIC/data/process_data/quality_control/NCDMIC_sequences_table.qza \
--o-visualization /home/jdubos2/NCDMIC/data/process_data/quality_control/NCDMIC_sequences_table.qzv \
--m-sample-metadata-file /home/jdubos2/NCDMIC/data/process_data/NCDMIC_metadata.tsv

qiime feature-table tabulate-seqs \
--i-data /home/jdubos2/NCDMIC/data/process_data/quality_control/NCDMIC_rep_seqs.qza \
--o-visualization /home/jdubos2/NCDMIC/data/process_data/quality_control/NCDMIC_rep_seqs.qzv

qiime metadata tabulate \
--m-input-file /home/jdubos2/NCDMIC/data/process_data/quality_control/NCDMIC_denoising_stats.qza \
--o-visualization /home/jdubos2/NCDMIC/data/process_data/quality_control/NCDMIC_denoising_stats.qzv