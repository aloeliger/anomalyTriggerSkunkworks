import FWCore.ParameterSet.Config as cms

pileupNetworkProducer = cms.EDProducer(
    'pileupNetworkProducer',
    pileupModelLocation = cms.string("/src/anomalyDetection/anomalyTriggerSkunkworks/data/pileupModel/"),
    regionSource = cms.InputTag('simCaloStage2Layer1Digis'),
)