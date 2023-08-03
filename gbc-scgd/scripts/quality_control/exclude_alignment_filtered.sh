#!/bin/bash

qiime feature-table filter-features \
--i-table /home/jdubos2/NCDMIC/data/process_data/quality_control/NCDMIC_table_mito_chloro_D0_filtered.qza \
--m-metadata-file /home/jdubos2/NCDMIC/data/process_data/quality_control/NCDMIC_rep_seqs_q80_misses.tsv \
--p-exclude-ids \
--o-filtered-table /home/jdubos2/NCDMIC/data/process_data/quality_control/NCDMIC_table_mito_chloro_D0_q80_filtered.qza

qiime metadata tabulate \
--m-input-file /home/jdubos2/NCDMIC/data/process_data/quality_control/NCDMIC_table_mito_chloro_D0_q80_filtered.qza \
--o-visualization /home/jdubos2/NCDMIC/data/process_data/quality_control/NCDMIC_table_mito_chloro_D0_q80_filtered.qza