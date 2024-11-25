import FWCore.ParameterSet.Config as cms

HCALTrigPrimAnalyzer = cms.EDAnalyzer(
    'HCALTrigPrimAnalyzer',
    hcalTpSource = cms.InputTag('simHcalTriggerPrimitiveDigis')
)
