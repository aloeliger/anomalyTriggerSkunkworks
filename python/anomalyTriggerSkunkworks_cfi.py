#specific config to define the anomaly trigger skunkworks path

import FWCore.ParameterSet.Config as cms

anomalyTriggerSkunkworks = cms.EDAnalyzer('anomalyTriggerSkunkworks',
                                          regionalInformation = cms.InputTag("simCaloStage2Layer1Digis"),
                                          ecalDigis = cms.InputTag("simEcalTriggerPrimitiveDigis"),
                                          hcalDigis = cms.InputTag("simHcalTriggerPrimitiveDigis")
)
