import FWCore.ParameterSet.Config as cms

pileupNetworkNtuplizer = cms.EDAnalyzer(
    'pileupNetworkNtuplizer',
    pileupSource = cms.InputTag('pileupNetworkProducer:pileupPrediction'),
)