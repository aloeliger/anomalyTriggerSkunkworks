#!/usr/bin/env bash

samples=('GluGluToHHTo4B_node_cHHH1' 'GluGluToHHTo4B_node_cHHH5' 'HTo2LongLivedTo4b' 'TT' 'VBFHToTauTau', 'SUSYGluGluToBBHToBB_NarrowWidth_M-350' 'ZToEE')
#samples=('ZToEE')

for sample in "${samples[@]}"; do

mkdir -p "/nfs_scratch/aloeliger/uGTComparison/${sample}/dags/"

farmoutAnalysisJobs --vsize-limit 8000 --memory-requirements 8000 --infer-cmssw-path "--submit-dir=/nfs_scratch/aloeliger/uGTComparison/${sample}/submit/" \
    --output-dag-file="/nfs_scratch/aloeliger/uGTComparison/${sample}/dags/dag" --output-dir="/hdfs/store/user/aloeliger/uGTComparisons/${sample}/" \
    --input-files-per-job=1 --input-file-list="$CMSSW_BASE/src/L1Trigger/anomalyTriggerSkunkworks/metaData/${sample}_files.txt" --assume-input-files-exist \
    --opsys="CentOS7" \
    --input-dir=/ uGTComparison "$CMSSW_BASE/src/L1Trigger/anomalyTriggerSkunkworks/python/emulateCompleteL1_SUEP_cff.py" 'outputFile=$outputFileName' 'inputFiles=$inputFileNames'

done