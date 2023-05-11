import FWCore.ParameterSet.Config as cms

uGTADEmulator = cms.EDProducer(
    "uGTADEmulator",
    egToken = cms.untracked.InputTag("caloStage2Digis","EGamma"),
    jetToken = cms.untracked.InputTag("caloStage2Digis","Jet"),
    muonToken = cms.untracked.InputTag("gmtStage2Digis","Muon"),
    sumToken = cms.untracked.InputTag("caloStage2Digis","EtSum"),
    anomalyModelLocation = cms.string("/src/anomalyDetection/anomalyTriggerSkunkworks/data/uGTADModel/uGTModel/"),
)
