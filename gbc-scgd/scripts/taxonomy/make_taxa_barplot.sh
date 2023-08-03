#!/bin/bash

qiime taxa barplot \
  --i-table /home/jdubos2/NCDMIC/data/process_data/quality_control/NCDMIC_table_mito_chloro_D0_q80_wolbachia_filtered.qza \
  --i-taxonomy /home/jdubos2/NCDMIC/data/process_data/classifier/NCDMIC_taxonomy.qza \
  --m-metadata-file /home/jdubos2/NCDMIC/data/process_data/NCDMIC_metadata.tsv \
  --o-visualization /home/jdubos2/NCDMIC/data/process_data/taxonomy/NCDMIC_taxa_barplot_wolbachia_filtered.qzv