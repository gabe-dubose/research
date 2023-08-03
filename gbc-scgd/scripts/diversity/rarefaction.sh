#!/bin/bash

qiime diversity alpha-rarefaction \
  --i-table /home/jdubos2/NCDMIC/data/process_data/quality_control/NCDMIC_table_mito_chloro_D0_q80_wolbachia_sepp_filtered.qza \
  --i-phylogeny /home/jdubos2/NCDMIC/data/process_data/phylogeny/insertion-tree.qza \
  --p-max-depth 25000 \
  --m-metadata-file /home/jdubos2/NCDMIC/data/process_data/NCDMIC_metadata.tsv \
  --o-visualization /home/jdubos2/NCDMIC/data/process_data/diversity/alpha_rarefaction_25k.qzv