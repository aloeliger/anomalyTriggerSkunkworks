#!/usr/bin/env bash

runs=('A' 'B' 'C' 'D')
for i in "${runs[@]}"; do

farmoutAnalysisJobs --vsize-limit 8000 --memory-requirements 8000 --infer-cmssw-path "--submit-dir=/nfs_scratch/aloeliger/uGTComparison/Run${i}/submit/" \
    --output-dag-file="/nfs_scratch/aloeliger/uGTComparison/Run${i}/dags/dag" --output-dir="/hdfs/store/user/aloeliger/uGTComparisons/Run${i}/" \
    --input-files-per-job=1 --input-file-list="$CMSSW_BASE/src/L1Trigger/anomalyTriggerSkunkworks/metaData/Run${i}Files.txt" --assume-input-files-exist \
    --opsys="CentOS7" \
    --input-dir=/ uGTComparison "$CMSSW_BASE/src/L1Trigger/anomalyTriggerSkunkworks/python/emulateCompleteL1_cff.py" 'outputFile=$outputFileName' 'inputFiles=$inputFileNames'

done