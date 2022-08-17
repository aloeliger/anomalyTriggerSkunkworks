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
                                '/store/data/Run2018A/ZeroBias/MINIAOD/PromptReco-v1/000/315/320/00000/CE15F648-DE4B-E811-8372-FA163EBE682B.root', #17274 events, total: 17274
                                #'/store/data/Run2018A/ZeroBias/MINIAOD/PromptReco-v1/000/315/373/00000/E296E264-7B4D-E811-9200-02163E01A033.root', #2404 events, total: 19678 #cosmic
                                '/store/data/Run2018A/ZeroBias/MINIAOD/PromptReco-v1/000/315/390/00000/98533841-7C4D-E811-A616-FA163E16957B.root', #4080 events, total: 23758
                                '/store/data/Run2018A/ZeroBias/MINIAOD/PromptReco-v1/000/315/402/00000/60AA7C90-884D-E811-80CD-FA163EFD9234.root', #22389 events, total: 46147
                                '/store/data/Run2018A/ZeroBias/MINIAOD/PromptReco-v1/000/315/403/00000/E8B5D61B-884D-E811-936F-02163E019F67.root', #40381 events, total: 86528
                                '/store/data/Run2018A/ZeroBias/MINIAOD/PromptReco-v1/000/315/404/00000/A83978AE-884D-E811-93CA-FA163EFA1AD6.root', #27165 events, total: 113693
                                '/store/data/Run2018A/ZeroBias/MINIAOD/PromptReco-v1/000/315/405/00000/6A515AC6-874D-E811-B811-FA163E9C8F11.root',
                            ),
                            secondaryFileNames = cms.untracked.vstring(
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/320/00000/B8D4BCA2-2A4A-E811-BAFF-FA163EBBB8E2.root',
                                #'/store/data/Run2018A/ZeroBias/RAW/v1/000/315/373/00000/5237BDAD-C14B-E811-8EAA-FA163E0481A2.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/390/00000/A0CCEE86-E24B-E811-9765-FA163E905D20.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/402/00000/D0165A8B-EE4B-E811-AEFB-FA163EC3883A.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/403/00000/785FB013-F24B-E811-89A0-FA163EF38772.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/404/00000/AC613757-EC4B-E811-BA1A-FA163E1DC155.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/405/00000/5A407030-E94B-E811-AD64-FA163EC7BCE0.root',
                            )
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
	fileName = cms.string("l1TNtuple-ZeroBias-2018A.root")
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

