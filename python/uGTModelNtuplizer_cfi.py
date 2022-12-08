import FWCore.ParameterSet.Config as cms

uGTModelNtuplizer = cms.EDAnalyzer(
    'uGTModelNtuplizer',
    scoreSource = cms.InputTag('uGTADEmulator:uGTAnomalyScore')
)