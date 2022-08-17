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

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100000) )

process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
                                '/store/data/Run2022B/ZeroBias/MINIAOD/PromptReco-v1/000/355/100/00000/0b00a373-a1ce-4c3f-b17a-0aa208ed706d.root'
                            ),
                            secondaryFileNames = cms.untracked.vstring(
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/187d3de1-e41d-4368-8f28-b8a01af2088b.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/51ef6870-126d-40f5-a70e-97a5d8d69ee1.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/9658d3d4-a6fb-4e4c-85eb-c2051603d848.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/988087a2-e41b-4540-bd91-b5d56e832c50.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/3ae33c52-b069-416b-a6c2-3d33b7b6d1ad.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/3e23cc4f-93c1-490b-b4a6-58e0d1af8c7e.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/9cfbbbcc-4a1d-40ff-86a1-c824806b4186.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/37975a42-603d-45cb-9ffd-f279c238a49c.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/698f1fec-c6d5-42dd-969e-c2022ff3e811.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/53d4f161-9a00-4c2f-8089-9cd6ba7e2530.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/c3e7591f-2085-464b-a09d-d03d72bca862.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/6e93204d-91fa-4241-88a0-305de3eb422e.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/5fbefbb4-0640-4745-af0a-1eb8179ff43b.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/713f171d-f34a-42ef-b687-5e1dedd56bdf.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/38e8057f-8f0e-416b-863d-45322186b0bf.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/e704b536-fbb8-426a-967e-f61b3d7a65eb.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/3f737458-e15a-4e73-b095-a7857b43cb6c.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/76414e9e-59ed-4ecc-aac3-4f1e97635854.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/cfef2d72-f82b-4551-8e59-60ff09ace734.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/67cf7fa1-0a39-4fc1-b999-bdc92a0f491c.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/83e33daa-5e1d-4b06-b5a6-3c7fb51ab0e2.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/cfdd52cf-f7dc-434e-a928-60c5a1a8108c.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/4f38c343-e1e2-4de8-b5e0-1f408b27ddee.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/7c3a6339-248b-480c-85d2-1a57e6707477.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/9f6e52e2-792d-41ec-9f17-c28e45c55ae0.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/1120df7a-aa8f-496e-bab8-a87132c2a700.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/7f94cf65-a0b3-47b0-aeeb-ba3ccff75c66.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/a9f08763-78ed-4e8d-88d3-07aad6b54b04.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/51ddc58c-1186-453d-b914-20b8df112b1f.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/cc30b3a2-29a1-4b8e-8ee8-0782c6a240a6.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/3637c31a-e12d-4768-be2a-7012487f57f1.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/90dd59e4-beb4-480e-9e9b-bf41cf0fdd97.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/11c592ae-1b21-44db-8c0c-6dd02f6b64a2.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/97ff0efc-3501-4a6a-ada3-5363a4187cef.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/052bdd12-cd02-457f-af83-f1589929b0ee.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/2b9b935e-70d0-498a-9100-ef260732be16.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/ca62ca3e-33db-445b-ad81-c756e0a08570.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/adc8e99e-ddda-4b05-9b79-ed7b3cd9fb2d.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/93ed4c83-dbf5-45a8-b09a-e6fb18cd4e73.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/1504958a-cc72-41dc-89ee-9629036fd3ab.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/956aa28c-1dfd-45a6-9789-3819cc9cc428.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/db51cf1b-6224-4604-9d17-917bc8e55bce.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/fc50f649-6ce9-40a7-b400-5def2cbf69cb.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/2a245bbc-d3ca-4937-aeae-5540c3932194.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/b296dea4-6f03-4269-9644-76ad9d89a264.root',
                                '/store/data/Run2022B/ZeroBias/RAW/v1/000/355/100/00000/112bd894-7c84-422e-b08d-0b88056a5eea.root',
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
	fileName = cms.string("l1TNtuple-ZeroBias-2022B.root")
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

