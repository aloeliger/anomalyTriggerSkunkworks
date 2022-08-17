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
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10000) )

process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
                                #'/store/data/Run2018D/ZeroBias/MINIAOD/PromptReco-v2/000/325/270/00000/D75162E0-8310-1C45-8DE3-1A853C04DAA7.root', #cosmics
                                '/store/data/Run2018D/ZeroBias/MINIAOD/PromptReco-v2/000/320/674/00000/E6A17BFC-F097-E811-A72A-FA163E7FB452.root',
                                '/store/data/Run2018D/ZeroBias/MINIAOD/PromptReco-v2/000/320/674/00000/E2B40669-EF97-E811-B1C7-FA163EB78F97.root',
                                '/store/data/Run2018D/ZeroBias/MINIAOD/PromptReco-v2/000/320/674/00000/BCB1B043-FD97-E811-BA77-FA163EA968FD.root',
                                '/store/data/Run2018D/ZeroBias/MINIAOD/PromptReco-v2/000/320/674/00000/BAFCD892-F197-E811-B948-FA163E35213F.root',

                            ),
                            secondaryFileNames = cms.untracked.vstring(
                                #'/store/data/Run2018D/ZeroBias/RAW/v1/000/325/270/00000/D5748A03-3B4E-624E-A70F-A7CC3F4A506F.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/674/00000/002632FE-6A95-E811-BFE5-FA163E11B3E0.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/674/00000/04ADB8F9-7B95-E811-BD5C-FA163EC08F3E.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/674/00000/14AC1E7C-7595-E811-AC7F-FA163E22267B.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/674/00000/30729629-7395-E811-AB45-02163E017F02.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/674/00000/40321CDE-7795-E811-9F8B-02163E01A0FF.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/674/00000/5220CC6E-6495-E811-8306-FA163E5A0D37.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/674/00000/58FA7BDA-7C95-E811-BE19-FA163EC3883A.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/674/00000/6C165BF3-6D95-E811-B09D-FA163E20727F.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/674/00000/7013C522-6A95-E811-B5BB-02163E019FD9.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/674/00000/8A28354E-8195-E811-A8F7-02163E017748.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/674/00000/92EE455B-7795-E811-AE9C-FA163EE3F92D.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/674/00000/A2267F7A-7295-E811-BBD3-FA163EB83949.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/674/00000/B01D29DE-7895-E811-99DC-02163E01A0D0.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/674/00000/B4F23F15-5196-E811-9203-FA163E0BB3A6.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/674/00000/B60C1F68-6D95-E811-849C-FA163E43848F.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/674/00000/B8269473-6C95-E811-8264-FA163E2AA51E.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/674/00000/BE77472A-6595-E811-BC19-FA163EB70861.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/674/00000/C8CC122B-6795-E811-8A8B-FA163E64116F.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/674/00000/C8E0DC10-7195-E811-987B-02163E010C51.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/674/00000/D8FB18FC-6E95-E811-B6AA-FA163E7B5F86.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/674/00000/E6F4B19F-7195-E811-BB2F-FA163E9393A6.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/674/00000/EEE017BA-7F95-E811-A221-FA163EF3D9F3.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/674/00000/F2C53294-7995-E811-AD1F-FA163E092C74.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/674/00000/FE911D0C-7B95-E811-9914-FA163E9E06D4.root',

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
	fileName = cms.string("l1TNtuple-ZeroBias-2018D.root")
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

