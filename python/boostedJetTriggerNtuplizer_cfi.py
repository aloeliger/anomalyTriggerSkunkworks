import FWCore.ParameterSet.Config as cms

boostedJetTriggerNtuplizer = cms.EDAnalyzer('boostedJetTriggerNtuplizer',
                                            boostedJetCollection = cms.InputTag('uct2016EmulatorDigis:Boosted'),
                                            verboseDebug = cms.bool(False))
