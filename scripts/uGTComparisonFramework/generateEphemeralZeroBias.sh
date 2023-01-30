#!/usr/bin/env bash

runs=('1' '2' '3' '4' '5' '6' '7')
for i in "${runs[@]}"; do

mkdir -p "/nfs_scratch/aloeliger/L1TriggerBitTest/allv7/EphemeralZeroBias${i}/dags/"

farmoutAnalysisJobs --vsize-limit 8000 --memory-requirements 8000 --infer-cmssw-path "--submit-dir=/nfs_scratch/aloeliger/L1TriggerBitTest/allv7/EphemeralZeroBias${i}/submit/" \
    --output-dag-file="/nfs_scratch/aloeliger/L1TriggerBitTest/allv7/EphemeralZeroBias${i}/dags/dag" --output-dir="/hdfs/store/user/aloeliger/L1TriggerBitTest/allv7/" \
    --input-files-per-job=1 --input-file-list="$CMSSW_BASE/src/L1Trigger/anomalyTriggerSkunkworks/metaData/ephemeralZeroBias${i}_files.txt" --assume-input-files-exist \
    --opsys="CentOS7" \
    --input-dir=/ uGTComparison "$CMSSW_BASE/src/L1Trigger/anomalyTriggerSkunkworks/python/emulateCompleteL1_cff.py" 'outputFile=$outputFileName' 'inputFiles=$inputFileNames'

done