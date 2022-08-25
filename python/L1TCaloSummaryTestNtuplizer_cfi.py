#specific config to determine the L1TCaloSummary test ntuplizer 

import FWCore.ParameterSet.Config as cms

L1TCaloSummaryTestNtuplizer = cms.EDAnalyzer('L1TCaloSummaryTestNtuplizer',
                                             scoreSource = cms.InputTag("uct2016EmulatorDigis:anomalyScore"),
                                             includePUInfo = cms.bool(False),
                                             #pvSrc = cms.InputTag("slimmedSecondaryVertices"),
                                             pvSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
                                             #pvSrc = cms.InputTag("offlinePrimaryVertices"),
                                             includeDetailedTPInfo = cms.bool(False),
                                             ecalToken = cms.InputTag("l1tCaloLayer1Digis"),
                                             hcalToken = cms.InputTag("l1tCaloLayer1Digis"),
                                             includeBasicDebugInfo = cms.bool(False)
)
