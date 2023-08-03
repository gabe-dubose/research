#!/bin/bash

qiime feature-classifier classify-sklearn \
  --i-classifier /home/jdubos2/NCDMIC/data/process_data/classifier/silva138.1-341f-806r-classifier.qza \
  --i-reads /home/jdubos2/NCDMIC/data/process_data/quality_control/NCDMIC_rep_seqs.qza \
  --o-classification /home/jdubos2/NCDMIC/data/process_data/classifier/NCDMIC_taxonomy.qza