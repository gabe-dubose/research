#!/bin/bash

qiime quality-control exclude-seqs \
--i-query-sequences /home/jdubos2/NCDMIC/data/process_data/quality_control/NCDMIC_rep_seqs_mito_chloro_D0_filtered.qza \
--i-reference-sequences /home/jdubos2/NCDMIC/data/process_data/databases/silva-138.1-ssu-nr99-rna-seqs-341f-806r-derep.qza \
--p-perc-identity 0.80 \
--p-perc-query-aligned 0.80 \
--o-sequence-hits /home/jdubos2/NCDMIC/data/process_data/quality_control/NCDMIC_rep_seqs_mito_chloro_D0_q80_filtered.qza \
--o-sequence-misses  /home/jdubos2/NCDMIC/data/process_data/quality_control/NCDMIC_rep_seqs_q80_misses.qza