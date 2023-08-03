#!/bin/bash
#SBATCH --partition=3day-long

qiime fragment-insertion sepp \
--i-representative-sequences /home/jdubos2/NCDMIC/data/process_data/quality_control/NCDMIC_rep_seqs_mito_chloro_D0_q80_wolbachia_filtered.qza \
--i-reference-database /home/jdubos2/NCDMIC/data/process_data/databases/sepp-refs-silva-128.qza \
--o-tree /home/jdubos2/NCDMIC/data/process_data/phylogeny/insertion-tree.qza \
--o-placements /home/jdubos2/NCDMIC/data/process_data/phylogeny/insertion-placements.qza \
--p-threads 2

qiime fragment-insertion filter-features \
  --i-table /home/jdubos2/NCDMIC/data/process_data/quality_control/NCDMIC_table_mito_chloro_D0_q80_wolbachia_filtered.qza \
  --i-tree /home/jdubos2/NCDMIC/data/process_data/phylogeny/insertion-tree.qza \
  --o-filtered-table /home/jdubos2/NCDMIC/data/process_data/quality_control/NCDMIC_table_mito_chloro_D0_q80_wolbachia_sepp_filtered.qza \
  --o-removed-table /home/jdubos2/NCDMIC/data/process_data/quality_control/NCDMIC_table_mito_chloro_D0_q80_wolbachia_sepp_removed.qza