#!/bin/bash

qiime tools import \
  --type 'SampleData[PairedEndSequencesWithQuality]' \
  --input-path /home/jdubos2/NCDMIC/data/process_data/NCDMIC_manifest.tsv \
  --output-path /home/jdubos2/NCDMIC/data/process_data/NCDMIC_raw_sequences.qza \
  --input-format PairedEndFastqManifestPhred33V2