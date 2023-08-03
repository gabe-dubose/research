#!/bin/bash

qiime taxa filter-table \
--i-table /home/jdubos2/NCDMIC/data/process_data/quality_control/NCDMIC_sequences_table.qza \
--i-taxonomy /home/jdubos2/NCDMIC/data/process_data/classifier/NCDMIC_taxonomy.qza \
--p-exclude mitochondria,chloroplast \
--p-include d__Bacteria \
--o-filtered-table /home/jdubos2/NCDMIC/data/process_data/quality_control/NCDMIC_table_mito_chloro_D0_filtered.qza

qiime feature-table filter-seqs \
--i-data /home/jdubos2/NCDMIC/data/process_data/quality_control/NCDMIC_rep_seqs.qza \
--i-table /home/jdubos2/NCDMIC/data/process_data/quality_control/NCDMIC_table_mito_chloro_D0_filtered.qza \
--o-filtered-data /home/jdubos2/NCDMIC/data/process_data/quality_control/NCDMIC_rep_seqs_mito_chloro_D0_filtered.qza