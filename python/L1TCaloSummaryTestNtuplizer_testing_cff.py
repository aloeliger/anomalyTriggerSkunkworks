import FWCore.ParameterSet.Config as cms

process = cms.Process("L1TCaloSummaryTest")

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '112X_dataRun2_v7', '')

process.load('L1Trigger.Configuration.CaloTriggerPrimitives_cff')

process.load('EventFilter.L1TXRawToDigi.caloLayer1Stage2Digis_cfi')

process.load('L1Trigger.L1TCaloLayer1.simCaloStage2Layer1Digis_cfi')
process.simCaloStage2Layer1Digis.ecalToken = cms.InputTag("l1tCaloLayer1Digis")
process.simCaloStage2Layer1Digis.hcalToken = cms.InputTag("l1tCaloLayer1Digis")

process.load('L1Trigger.L1TCaloLayer1.uct2016EmulatorDigis_cfi')

process.load("L1Trigger.Run3Ntuplizer.l1BoostedJetStudies_cfi")

process.load("L1Trigger.anomalyTriggerSkunkworks.L1TCaloSummaryTestNtuplizer_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10000) )

process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
                                '/store/data/Run2022C/ZeroBias/RAW/v1/000/355/862/00000/20d97865-1ae0-4fb1-b910-23a662c96af0.root',
                                #'/store/data/Run2018D/ZeroBias/RAW/v1/000/323/940/00000/090F7307-7EB4-CA45-A6B9-542C3AE60FD4.root',
                                #'/store/data/Run2018D/ZeroBias/RAW/v1/000/323/940/00000/B3EFCFDD-7111-9647-B720-D2B33AFE35A2.root',
                                #'/store/data/Run2018D/ZeroBias/RAW/v1/000/323/954/00000/10A4D333-9B72-A342-9085-CE56DC16A380.root',
                                #'/store/data/Run2022C/EphemeralZeroBias0/RAW/v1/000/355/862/00000/624ee423-5248-4a87-8f37-dacad83c29ee.root',
                                #'/store/data/Run2022C/EphemeralZeroBias0/RAW/v1/000/355/863/00000/1b904ea5-e732-4f1b-89a9-9fb72229bd21.root',
                                #'/store/data/Run2022C/EphemeralZeroBias0/RAW/v1/000/355/865/00000/3801031c-17a7-4640-ba9d-0e17f6316816.root',
                                #'/store/data/Run2022C/EphemeralZeroBias0/RAW/v1/000/355/869/00000/9d015216-a99d-47ac-b1d6-684b3c589746.root',
                                #'/store/data/Run2022C/EphemeralZeroBias0/RAW/v1/000/355/870/00000/a46a0591-fa4c-4fe1-9ece-63caa6c89bae.root',
                                #'/store/data/Run2018A/ZeroBias/RAW/v1/000/315/252/00000/32ED3ECF-9949-E811-9D23-FA163E081C30.root',
                                #'/store/data/Run2018A/ZeroBias/RAW/v1/000/315/252/00000/38E89422-9F49-E811-8436-FA163ED637E6.root',
                                #'/store/data/Run2018A/ZeroBias/RAW/v1/000/315/252/00000/3A8A92F4-9949-E811-996D-FA163EFF76BB.root',
                                #'/store/data/Run2018A/ZeroBias/RAW/v1/000/315/252/00000/7E9C97C1-9E49-E811-A25F-FA163EBB779E.root',
                                #'/store/data/Run2018A/ZeroBias/RAW/v1/000/315/252/00000/CC905368-9F49-E811-908D-FA163E7121A5.root',
                            )
                            #fileNames = cms.untracked.vstring('/store/data/Run2018D/EphemeralZeroBias8/RAW/v1/000/325/057/00000/2003CE91-DBBF-A34F-8880-B6B20DF0C349.root')
                            #fileNames = cms.untracked.vstring('/store/data/Run2018D/EphemeralZeroBias8/MINIAOD/PromptReco-v2/000/325/057/00000/954F1BEB-75FC-ED43-AA3A-6F032EF62093.root'),
                            #secondaryFileNames = cms.untracked.vstring('/store/data/Run2018D/EphemeralZeroBias8/RAW/v1/000/325/057/00000/2003CE91-DBBF-A34F-8880-B6B20DF0C349.root')
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step2 nevts:1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)


#Output
process.TFileService = cms.Service(
	"TFileService",
	fileName = cms.string("l1TNtuple-ZeroBias.root")
)

process.L1TRawToDigi_Stage2 = cms.Task(process.caloLayer1Digis, process.caloStage2Digis)
process.RawToDigi_short = cms.Sequence(process.L1TRawToDigi_Stage2)
process.p = cms.Path(process.RawToDigi_short * 
                     process.l1tCaloLayer1Digis *
                     process.simCaloStage2Layer1Digis * 
                     process.uct2016EmulatorDigis * 
                     #process.l1NtupleProducer
                     process.L1TCaloSummaryTestNtuplizer
)
#process.e = cms.EndPath(process.out)

#process.schedule = cms.Schedule(process.p,process.e)
process.schedule = cms.Schedule(process.p)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)

# Multi-threading
process.options.numberOfThreads=cms.untracked.uint32(8)
process.options.numberOfStreams=cms.untracked.uint32(0)

