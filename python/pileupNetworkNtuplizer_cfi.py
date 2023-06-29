import FWCore.ParameterSet.Config as cms

pileupNetworkNtuplizer = cms.EDAnalyzer(
    'pileupNetworkNtuplizer',
    pileupSource = cms.InputTag('pileupNetworkProducer:pileupPrediction'),
)

inciSNAILv0p1Ntuplizer = cms.EDAnalyzer(
    'pileupNetworkNtuplizer',
    pileupSource = cms.InputTag('inciSNAILv0p1Producer','pileupPrediction')
)