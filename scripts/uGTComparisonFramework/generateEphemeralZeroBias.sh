#!/usr/bin/env bash

VERSION=9
runs=('1' '2' '3' '4' '5' '6' '7')
for i in "${runs[@]}"; do

NFS_LOCATION="/nfs_scratch/aloeliger/L1TriggerBitTest/allv${VERSION}/EphemeralZeroBias${i}/"
DAGS_LOCATION="${NFS_LOCATION}/dags/"
SUBMIT_LOCATION="${NFS_LOCATION}/submit/"
OUTPUT_DIR="/hdfs/store/user/aloeliger/L1TriggerBitTest/allv${VERSION}/"
INPUT_FILES="$CMSSW_BASE/src/L1Trigger/anomalyTriggerSkunkworks/metaData/ephemeralZeroBias${i}_files.txt"
CONFIG="$CMSSW_BASE/src/L1Trigger/anomalyTriggerSkunkworks/python/emulateCompleteL1_cff.py"

mkdir -p ${DAGS_LOCATION}

farmoutAnalysisJobs --vsize-limit 8000 --memory-requirements 8000 --infer-cmssw-path \
    "--submit-dir=${SUBMIT_LOCATION}" \
    --output-dag-file="${DAGS_LOCATION}/dag" \
    --output-dir="${OUTPUT_DIR}" \
    --input-files-per-job=1 \
    --input-file-list="${INPUT_FILES}" \
    --assume-input-files-exist \
    --opsys="CentOS7" \
    --input-dir=/ \
    "uGTComparison_v_${VERSION}" "${CONFIG}" 'outputFile=$outputFileName' 'inputFiles=$inputFileNames'

done