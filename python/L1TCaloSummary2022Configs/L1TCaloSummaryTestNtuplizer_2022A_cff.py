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
#We want PU info
process.L1TCaloSummaryTestNtuplizer.includePUInfo = cms.bool(True)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100000) )

process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
                                '/store/data/Run2022A/ZeroBias/MINIAOD/PromptReco-v1/000/352/417/00000/8d746d7a-c36e-4620-841a-878203304765.root',
                            ),
                            secondaryFileNames = cms.untracked.vstring(
                                '/store/data/Run2022A/ZeroBias/RAW/v1/000/352/417/00000/a9b9c9f9-7d91-4262-85c7-81d113f1be6c.root',
                                '/store/data/Run2022A/ZeroBias/RAW/v1/000/352/417/00000/db85960e-890d-4cce-9469-3d7ea57cc9f9.root',
                                '/store/data/Run2022A/ZeroBias/RAW/v1/000/352/417/00000/efaf65dd-4053-44c1-beec-e3ec4b8eb7e9.root',
                                '/store/data/Run2022A/ZeroBias/RAW/v1/000/352/417/00000/0873dd4e-9952-4846-a7b7-388e460746ae.root',
                                '/store/data/Run2022A/ZeroBias/RAW/v1/000/352/417/00000/a5bd2b59-2064-4062-a463-39d91bdc7962.root',
                                '/store/data/Run2022A/ZeroBias/RAW/v1/000/352/417/00000/89b69f9d-bb15-4886-a71a-fdbfe7ed83fd.root',
                                '/store/data/Run2022A/ZeroBias/RAW/v1/000/352/417/00000/4e6bd5cc-7d54-4e7f-8412-029d620ea6a8.root',
                                '/store/data/Run2022A/ZeroBias/RAW/v1/000/352/417/00000/9cc38c66-1cdb-43b5-af39-b77271109008.root',
                                '/store/data/Run2022A/ZeroBias/RAW/v1/000/352/417/00000/89a7629a-6eb9-4601-abde-1e82d118ef1b.root',
                                '/store/data/Run2022A/ZeroBias/RAW/v1/000/352/417/00000/d9dbbdb5-15c1-4da0-81ea-5937ef63c4c9.root',
                                '/store/data/Run2022A/ZeroBias/RAW/v1/000/352/417/00000/5f3d2af7-9ab8-46e1-bb3c-17bc1c1a1845.root',
                                '/store/data/Run2022A/ZeroBias/RAW/v1/000/352/417/00000/f4402fa1-22c3-4493-a23a-6ff4e1d3dc03.root',
                                '/store/data/Run2022A/ZeroBias/RAW/v1/000/352/417/00000/85e7ae4e-2065-499e-8de1-e64e33b8db25.root',
                            ),
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
	fileName = cms.string("l1TNtuple-ZeroBias-2022A.root")
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

