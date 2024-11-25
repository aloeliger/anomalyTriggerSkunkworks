import FWCore.ParameterSet.Config as cms

unpackedCICADAScoreNtuplizer = cms.EDAnalyzer(
    'unpackedCICADAScoreNtuplizer',
    unpackedCICADAScoreSrc = cms.InputTag("gtStage2Digis", "CICADAScore")
)
