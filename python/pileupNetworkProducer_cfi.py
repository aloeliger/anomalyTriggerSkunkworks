import FWCore.ParameterSet.Config as cms

pileupNetworkProducer = cms.EDProducer(
    'pileupNetworkProducer',
    pileupModelLocation = cms.string("/src/anomalyDetection/anomalyTriggerSkunkworks/data/pileupModel/"),
    regionSource = cms.InputTag('simCaloStage2Layer1Digis'),
)

inciSNAILv0p1Producer = cms.EDProducer(
    'pileupNetworkProducer',
    pileupModelLocation = cms.string('/src/anomalyDetection/anomalyTriggerSkunkworks/data/inciSNAILv0p1/'),
    regionSource = cms.InputTag('simCaloStage2Layer1Digis'),
    inputLayerName = cms.string("serving_default_conv2d_input:0")
)