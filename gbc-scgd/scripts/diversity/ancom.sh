#!/bin/bash

qiime composition add-pseudocount \
  --i-table /home/jdubos2/NCDMIC/data/process_data/quality_control/NCDMIC_table_mito_chloro_D0_q80_wolbachia_sepp_filtered.qza \
  --o-composition-table /home/jdubos2/NCDMIC/data/process_data/quality_control/NCDMIC_table_mito_chloro_D0_q80_wolbachia_sepp_filtered_pseudocount.qza

qiime composition ancom \
  --i-table /home/jdubos2/NCDMIC/data/process_data/quality_control/NCDMIC_table_mito_chloro_D0_q80_wolbachia_sepp_filtered_pseudocount.qza \
  --m-metadata-file /home/jdubos2/NCDMIC/data/process_data/NCDMIC_metadata.tsv \
  --m-metadata-column species \
  --o-visualization /home/jdubos2/NCDMIC/data/process_data/diversity/ancom-species.qzv