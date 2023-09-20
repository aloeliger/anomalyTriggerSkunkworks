import FWCore.ParameterSet.Config as cms
from anomalyDetection.anomalyTriggerSkunkworks.newFrameworkNtuplization.ntuplizeSkim_2023_MC import process, options

process.source.fileNames = cms.untracked.vstring(
    options.inputFiles
)

process.source.secondaryFileNames = cms.untracked.vstring(
    options.secondaryFiles
)