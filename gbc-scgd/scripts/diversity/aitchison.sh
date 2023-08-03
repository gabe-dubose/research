#!/bin/bash

#run deicode
qiime deicode rpca \
  --i-table /home/jdubos2/NCDMIC/data/process_data/quality_control/NCDMIC_table_mito_chloro_D0_q80_wolbachia_sepp_filtered.qza \
  --p-min-feature-count 10 \
  --p-min-sample-count 500 \
  --o-biplot /home/jdubos2/NCDMIC/data/process_data/diversity/aithcison_ordination_results.qza \
  --o-distance-matrix /home/jdubos2/NCDMIC/data/process_data/diversity/aithcison_distance_matrix.qza

#make plot
qiime emperor biplot \
    --i-biplot /home/jdubos2/NCDMIC/data/process_data/diversity/aithcison_ordination_results.qza \
    --m-sample-metadata-file /home/jdubos2/NCDMIC/data/process_data/NCDMIC_metadata.tsv \
    --m-feature-metadata-file /home/jdubos2/NCDMIC/data/process_data/classifier/NCDMIC_taxonomy.qza \
    --o-visualization /home/jdubos2/NCDMIC/data/process_data/diversity/aitchison_biplot.qzv \
    --p-number-of-features 8

#permanova:species
qiime diversity beta-group-significance \
    --i-distance-matrix /home/jdubos2/NCDMIC/data/process_data/diversity/aithcison_distance_matrix.qza \
    --m-metadata-file /home/jdubos2/NCDMIC/data/process_data/NCDMIC_metadata.tsv \
    --m-metadata-column species \
    --p-method permanova \
    --p-pairwise \
    --o-visualization /home/jdubos2/NCDMIC/data/process_data/diversity/aitchison_species_permanova.qzv

#permdisp:species
qiime diversity beta-group-significance \
    --i-distance-matrix /home/jdubos2/NCDMIC/data/process_data/diversity/aithcison_distance_matrix.qza \
    --m-metadata-file /home/jdubos2/NCDMIC/data/process_data/NCDMIC_metadata.tsv \
    --m-metadata-column species \
    --p-method permdisp \
    --p-pairwise \
    --o-visualization /home/jdubos2/NCDMIC/data/process_data/diversity/aitchison_species_permdisp.qzv