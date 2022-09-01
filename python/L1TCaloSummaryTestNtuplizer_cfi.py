#specific config to determine the L1TCaloSummary test ntuplizer 

import FWCore.ParameterSet.Config as cms

L1TCaloSummaryTestNtuplizer = cms.EDAnalyzer('L1TCaloSummaryTestNtuplizer',
                                             scoreSource = cms.InputTag("uct2016EmulatorDigis:anomalyScore"),
                                             includePUInfo = cms.bool(False),
                                             verboseDebug = cms.bool(False),
                                             #pvSrc = cms.InputTag("slimmedSecondaryVertices"),
                                             pvSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
                                             #pvSrc = cms.InputTag("offlinePrimaryVertices"),
                                             ecalToken = cms.InputTag("l1tCaloLayer1Digis"),
                                             hcalToken = cms.InputTag("l1tCaloLayer1Digis"),
                                             emuRegionsToken = cms.InputTag("simCaloStage2Layer1Digis"),
)
