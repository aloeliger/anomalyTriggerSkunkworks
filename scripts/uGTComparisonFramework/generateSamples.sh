#!/usr/bin/env bash

VERSION=3
runs=('A' 'B' 'C' 'D')
#runs=('C')

for i in "${runs[@]}"; do

NFS_LOCATION="/nfs_scratch/aloeliger/uGTComparison/v_${VERSION}/Run${i}/"
DAGS_LOCATION="${NFS_LOCATION}/dags/"
SUBMIT_LOCATION="${NFS_LOCATION}/submit/"
OUTPUT_DIR="/hdfs/store/user/aloeliger/uGTComparisons/v_${VERSION}/Run${i}/"
INPUT_FILES="$CMSSW_BASE/src/L1Trigger/anomalyTriggerSkunkworks/metaData/Run${i}Files.txt"
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