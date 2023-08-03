#!/bin/bash

qiime diversity core-metrics-phylogenetic \
  --i-phylogeny /home/jdubos2/NCDMIC/data/process_data/phylogeny/insertion-tree.qza \
  --i-table /home/jdubos2/NCDMIC/data/process_data/quality_control/NCDMIC_table_mito_chloro_D0_q80_wolbachia_sepp_filtered.qza \
  --p-sampling-depth 19000 \
  --m-metadata-file /home/jdubos2/NCDMIC/data/process_data/NCDMIC_metadata.tsv \
  --output-dir /home/jdubos2/NCDMIC/data/process_data/diversity/core_metrics_19K