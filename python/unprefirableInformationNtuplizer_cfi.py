import FWCore.ParameterSet.Config as cms

unprefirableInformationNtuplizer = cms.EDAnalyzer(
    'unprefirableInformationNtuplizer',
    GlobalExtSrc = cms.InputTag("gtStage2Digis"),
    #GlobalExtSrc = cms.InputTag("simGtExtFakeStage2Digis"),
    #GlobalExtSrc = cms.InputTag("simGtExtUnprefireable"),
)
