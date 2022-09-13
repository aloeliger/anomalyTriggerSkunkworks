from L1Trigger.anomalyTriggerSkunkworks.L1TComparisonConfigs.comparison_base_cff import process
import FWCore.ParameterSet.Config as cms

import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing ('analysis')
options.parseArguments()

process.source.fileNames = cms.untracked.vstring(options.inputFiles)

process.source.secondaryFileNames = cms.untracked.vstring(
    '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/323/716/00000/4701C43F-D298-1D46-8F4D-E6C6580887FA.root',
)
process.TFileService.fileName=cms.string(options.outputFile)

#process.TFileService.fileName = cms.string("l1TNtuple_TriggerBitsComparison_2018D_320571.root")
