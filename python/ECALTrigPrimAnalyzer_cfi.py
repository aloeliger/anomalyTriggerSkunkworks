import FWCore.ParameterSet.Config as cms

ECALTrigPrimAnalyzer = cms.EDAnalyzer(
    'ECALTrigPrimAnalyzer',
    ecalTpSource = cms.InputTag('simEcalTriggerPrimitiveDigis')
)
