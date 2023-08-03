#!/bin/bash

#unweighted unifrac permanova and permdisp: drosophila species
qiime diversity beta-group-significance \
  --i-distance-matrix /home/jdubos2/NCDMIC/data/process_data/diversity/core_metrics_19K/unweighted_unifrac_distance_matrix.qza \
  --m-metadata-file /home/jdubos2/NCDMIC/data/process_data/NCDMIC_metadata.tsv \
  --m-metadata-column species \
  --o-visualization /home/jdubos2/NCDMIC/data/process_data/diversity/unweighted_unifrac_species_permanova.qzv \
  --p-pairwise \
  --p-method permanova

qiime diversity beta-group-significance \
  --i-distance-matrix /home/jdubos2/NCDMIC/data/process_data/diversity/core_metrics_19K/unweighted_unifrac_distance_matrix.qza \
  --m-metadata-file /home/jdubos2/NCDMIC/data/process_data/NCDMIC_metadata.tsv \
  --m-metadata-column species \
  --o-visualization /home/jdubos2/NCDMIC/data/process_data/diversity/unweighted_unifrac_species_permdisp.qzv \
  --p-pairwise \
  --p-method permdisp


#weighted unifrac permanova: drosophila species
qiime diversity beta-group-significance \
  --i-distance-matrix /home/jdubos2/NCDMIC/data/process_data/diversity/core_metrics_19K/weighted_unifrac_distance_matrix.qza \
  --m-metadata-file /home/jdubos2/NCDMIC/data/process_data/NCDMIC_metadata.tsv \
  --m-metadata-column species \
  --o-visualization /home/jdubos2/NCDMIC/data/process_data/diversity/weighted_unifrac_species_permanova.qzv \
  --p-pairwise \
  --p-method permanova

qiime diversity beta-group-significance \
  --i-distance-matrix /home/jdubos2/NCDMIC/data/process_data/diversity/core_metrics_19K/weighted_unifrac_distance_matrix.qza \
  --m-metadata-file /home/jdubos2/NCDMIC/data/process_data/NCDMIC_metadata.tsv \
  --m-metadata-column species \
  --o-visualization /home/jdubos2/NCDMIC/data/process_data/diversity/weighted_unifrac_species_permdisp.qzv \
  --p-pairwise \
  --p-method permdisp

#bray-curtis permanova and permdisp: drosophila species
qiime diversity beta-group-significance \
  --i-distance-matrix /home/jdubos2/NCDMIC/data/process_data/diversity/core_metrics_19K/bray_curtis_distance_matrix.qza \
  --m-metadata-file /home/jdubos2/NCDMIC/data/process_data/NCDMIC_metadata.tsv \
  --m-metadata-column species \
  --o-visualization /home/jdubos2/NCDMIC/data/process_data/diversity/bray_curtis_species_permanova.qzv \
  --p-pairwise \
  --p-method permanova

qiime diversity beta-group-significance \
  --i-distance-matrix /home/jdubos2/NCDMIC/data/process_data/diversity/core_metrics_19K/bray_curtis_distance_matrix.qza \
  --m-metadata-file /home/jdubos2/NCDMIC/data/process_data/NCDMIC_metadata.tsv \
  --m-metadata-column species \
  --o-visualization /home/jdubos2/NCDMIC/data/process_data/diversity/bray_curtis_species_permdisp.qzv \
  --p-pairwise \
  --p-method permdisp

#jaccard permanova and permdisp: drosophila species
qiime diversity beta-group-significance \
  --i-distance-matrix /home/jdubos2/NCDMIC/data/process_data/diversity/core_metrics_19K/jaccard_distance_matrix.qza \
  --m-metadata-file /home/jdubos2/NCDMIC/data/process_data/NCDMIC_metadata.tsv \
  --m-metadata-column species \
  --o-visualization /home/jdubos2/NCDMIC/data/process_data/diversity/jaccard_species_permanova.qzv \
  --p-pairwise \
  --p-method permanova

qiime diversity beta-group-significance \
  --i-distance-matrix /home/jdubos2/NCDMIC/data/process_data/diversity/core_metrics_19K/jaccard_distance_matrix.qza \
  --m-metadata-file /home/jdubos2/NCDMIC/data/process_data/NCDMIC_metadata.tsv \
  --m-metadata-column species \
  --o-visualization /home/jdubos2/NCDMIC/data/process_data/diversity/jaccard_species_permdisp.qzv \
  --p-pairwise \
  --p-method permdisp