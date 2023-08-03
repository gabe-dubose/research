#!/bin/bash

#faith phylogenetic
qiime diversity alpha-group-significance \
  --i-alpha-diversity /home/jdubos2/NCDMIC/data/process_data/diversity/core_metrics_19K/faith_pd_vector.qza \
  --m-metadata-file /home/jdubos2/NCDMIC/data/process_data/NCDMIC_metadata.tsv \
  --o-visualization /home/jdubos2/NCDMIC/data/process_data/diversity/faith_pd_stats.qzv

#observed features
qiime diversity alpha-group-significance \
  --i-alpha-diversity /home/jdubos2/NCDMIC/data/process_data/diversity/core_metrics_19K/observed_features_vector.qza \
  --m-metadata-file /home/jdubos2/NCDMIC/data/process_data/NCDMIC_metadata.tsv \
  --o-visualization /home/jdubos2/NCDMIC/data/process_data/diversity/observed_features_stats.qzv

#shannon
qiime diversity alpha-group-significance \
  --i-alpha-diversity /home/jdubos2/NCDMIC/data/process_data/diversity/core_metrics_19K/shannon_vector.qza \
  --m-metadata-file /home/jdubos2/NCDMIC/data/process_data/NCDMIC_metadata.tsv \
  --o-visualization /home/jdubos2/NCDMIC/data/process_data/diversity/shannon_stats.qzv

#evenness
qiime diversity alpha-group-significance \
  --i-alpha-diversity /home/jdubos2/NCDMIC/data/process_data/diversity/core_metrics_19K/evenness_vector.qza \
  --m-metadata-file /home/jdubos2/NCDMIC/data/process_data/NCDMIC_metadata.tsv \
  --o-visualization /home/jdubos2/NCDMIC/data/process_data/diversity/evenness_stats.qzv