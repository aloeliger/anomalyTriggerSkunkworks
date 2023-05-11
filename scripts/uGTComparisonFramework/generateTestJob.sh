#1/usr/bin/env bash

NFS_LOCATION="/nfs_scratch/aloeliger/L1TriggerBitTest/test/"
DAGS_LOCATION="${NFS_LOCATION}/dags/"
SUBMIT_LOCATION="${NFS_LOCATION}/submit/"
OUTPUT_DIR="/hdfs/store/user/aloeliger/test/"
INPUT_FILES="$CMSSW_BASE/src/anomalyDetection/anomalyTriggerSkunkworks/metaData/inputFiles_oneTestFile.txt"
CONFIG="$CMSSW_BASE/src/anomalyDetection/anomalyTriggerSkunkworks/python/emulateCompleteL1_cff.py"

mkdir -p $DAGS_LOCATION

farmoutAnalysisJobs --vsize-limit 8000 --memory-requirements 8000 --infer-cmssw-path \
    --submit-dir=${SUBMIT_LOCATION} \
    --output-dag-file="${DAGS_LOCATION}/dag" \
    --output-dir="${OUTPUT_DIR}" \
    --input-files-per-job=1 \
    --input-file-list="${INPUT_FILES}" \
    --assume-input-files-exist \
    --opsys="CentOS7" \
    --input-dir=/ \
    --extra-usercode-files=$CMSSW_BASE/src/L1Trigger/CICADA/ \
    "testRun" "${CONFIG}" 'outputFile=$outputFileName' 'inputFiles=$inputFileNames'
