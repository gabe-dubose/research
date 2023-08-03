#!/bin/bash

#sum species
qiime feature-table group \
    --i-table /home/jdubos2/NCDMIC/data/process_data/quality_control/NCDMIC_table_mito_chloro_D0_q80_wolbachia_sepp_filtered.qza \
    --p-axis sample \
    --m-metadata-file /home/jdubos2/NCDMIC/data/process_data/NCDMIC_metadata.tsv \
    --m-metadata-column species \
    --p-mode sum \
    --o-grouped-table /home/jdubos2/NCDMIC/data/process_data/groupings/summed.qza

qiime metadata tabulate \
--m-input-file /home/jdubos2/NCDMIC/data/process_data/groupings/summed.qza \
--o-visualization /home/jdubos2/NCDMIC/data/process_data/groupings/summed.qzv

#median species
qiime feature-table group \
    --i-table /home/jdubos2/NCDMIC/data/process_data/quality_control/NCDMIC_table_mito_chloro_D0_q80_wolbachia_sepp_filtered.qza \
    --p-axis sample \
    --m-metadata-file /home/jdubos2/NCDMIC/data/process_data/NCDMIC_metadata.tsv \
    --m-metadata-column species \
    --p-mode median-ceiling \
    --o-grouped-table /home/jdubos2/NCDMIC/data/process_data/groupings/medianed.qza

qiime metadata tabulate \
--m-input-file /home/jdubos2/NCDMIC/data/process_data/groupings/medianed.qza \
--o-visualization /home/jdubos2/NCDMIC/data/process_data/groupings/medianed.qzv

#mean species
qiime feature-table group \
    --i-table /home/jdubos2/NCDMIC/data/process_data/quality_control/NCDMIC_table_mito_chloro_D0_q80_wolbachia_sepp_filtered.qza \
    --p-axis sample \
    --m-metadata-file /home/jdubos2/NCDMIC/data/process_data/NCDMIC_metadata.tsv \
    --m-metadata-column species \
    --p-mode mean-ceiling \
    --o-grouped-table /home/jdubos2/NCDMIC/data/process_data/groupings/meaned.qza

qiime metadata tabulate \
--m-input-file /home/jdubos2/NCDMIC/data/process_data/groupings/meaned.qza \
--o-visualization /home/jdubos2/NCDMIC/data/process_data/groupings/meaned.qzv