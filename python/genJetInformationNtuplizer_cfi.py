# config for gen jet information inclusion

import FWCore.ParameterSet.Config as cms

genJetInformationNtuplizer = cms.EDAnalyzer(
    'genJetInformationNtuplizer',
    genJetSrc = cms.InputTag("slimmedGenJets"),
)