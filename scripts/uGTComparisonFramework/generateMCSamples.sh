#!/usr/bin/env bash

VERSION=3
samples=('GluGlutoHHto4B_kl-0p00_kt-1p00_c2-0p00' 'GluGlutoHHto4B_kl-1p00_kt-1p00_c2-3p00' 'HTo2LongLivedTo4b' 'TT' 'VBFHToTauTau', 'SUSYGluGluToBBHToBB_NarrowWidth_M-120' 'DYTo2L_MLL-4to50' 'GluGluHToTauTau' 'VBFHToTauTau')

#samples=('VBFHToTauTau')

for sample in "${samples[@]}"; do

NFS_LOCATION="/nfs_scratch/aloeliger/uGTComparison/v_${VERSION}/${sample}"
DAGS_LOCATION="${NFS_LOCATION}/dags/"
SUBMIT_LOCATION="${NFS_LOCATION}/submit/"
OUTPUT_DIR="/hdfs/store/user/aloeliger/uGTComparisons/v_${VERSION}/${sample}/"
INPUT_FILES="${CMSSW_BASE}/src/anomalyDetection/anomalyTriggerSkunkworks/metaData/${sample}_files.txt"
CONFIG="$CMSSW_BASE/src/anomalyDetection/anomalyTriggerSkunkworks/python/emulateCompleteL1_MC_cff.py"

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
