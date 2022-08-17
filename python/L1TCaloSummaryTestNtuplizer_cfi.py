#specific config to determine the L1TCaloSummary test ntuplizer 

import FWCore.ParameterSet.Config as cms

L1TCaloSummaryTestNtuplizer = cms.EDAnalyzer('L1TCaloSummaryTestNtuplizer',
                                             scoreSource = cms.InputTag("uct2016EmulatorDigis:anomalyScore"),
                                             pvSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
                                             #pvSrc = cms.InputTag("offlinePrimaryVertices"),
)
