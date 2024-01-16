import FWCore.ParameterSet.Config as cms

cicadaFilter = cms.EDFilter(
    'CICADAFilter',
    scoreSource = cms.InputTag("L1TCaloSummaryCICADAv2","anomalyScore"),
    anomalyThreshold = cms.double(9.531)
)