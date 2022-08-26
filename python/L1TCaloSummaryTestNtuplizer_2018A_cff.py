import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2018_cff import Run2_2018

process = cms.Process("L1TCaloSummaryTest", Run2_2018)
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
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10000) )

process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
                                '/store/data/Run2018A/ZeroBias/MINIAOD/PromptReco-v1/000/315/420/00000/063DB17F-4E4E-E811-925C-FA163E278EA6.root',
                                # '/store/data/Run2018A/ZeroBias/MINIAOD/PromptReco-v1/000/315/320/00000/CE15F648-DE4B-E811-8372-FA163EBE682B.root', #17274 events, total: 17274
                                # #'/store/data/Run2018A/ZeroBias/MINIAOD/PromptReco-v1/000/315/373/00000/E296E264-7B4D-E811-9200-02163E01A033.root', #2404 events, total: 19678 #cosmic
                                # '/store/data/Run2018A/ZeroBias/MINIAOD/PromptReco-v1/000/315/390/00000/98533841-7C4D-E811-A616-FA163E16957B.root', #4080 events, total: 23758
                                # '/store/data/Run2018A/ZeroBias/MINIAOD/PromptReco-v1/000/315/402/00000/60AA7C90-884D-E811-80CD-FA163EFD9234.root', #22389 events, total: 46147
                                # '/store/data/Run2018A/ZeroBias/MINIAOD/PromptReco-v1/000/315/403/00000/E8B5D61B-884D-E811-936F-02163E019F67.root', #40381 events, total: 86528
                                # '/store/data/Run2018A/ZeroBias/MINIAOD/PromptReco-v1/000/315/404/00000/A83978AE-884D-E811-93CA-FA163EFA1AD6.root', #27165 events, total: 113693
                                # '/store/data/Run2018A/ZeroBias/MINIAOD/PromptReco-v1/000/315/405/00000/6A515AC6-874D-E811-B811-FA163E9C8F11.root',
                            ),
                            secondaryFileNames = cms.untracked.vstring(
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/420/00000/7A30404E-0D4D-E811-9EEE-FA163E3C37D4.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/420/00000/109D7750-0D4D-E811-9723-FA163EE72804.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/420/00000/109D7750-0D4D-E811-9723-FA163EE72804.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/420/00000/9E851261-0E4D-E811-AC5C-FA163E0286FE.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/420/00000/36E07674-0D4D-E811-BE2A-FA163ED532A6.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/420/00000/92726551-0D4D-E811-B968-FA163EB0C6EB.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/420/00000/C8BA7D65-0D4D-E811-96E7-FA163E884B58.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/420/00000/66DC0866-0D4D-E811-B660-FA163E9A1F85.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/420/00000/307E0198-0D4D-E811-BF01-FA163EEE3FEF.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/420/00000/469D0031-0E4D-E811-B108-FA163E7CF739.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/420/00000/0EAA2B31-0E4D-E811-B898-FA163E32EA54.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/420/00000/E45F9225-0E4D-E811-B6CA-FA163E9ECA9A.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/420/00000/6E243399-384C-E811-804A-02163E019F84.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/420/00000/2E5811F1-0D4D-E811-B551-FA163EEE21BE.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/420/00000/6295093C-0E4D-E811-BBF5-FA163EB0C6EB.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/420/00000/145124F5-0D4D-E811-9FA0-FA163E80AD1D.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/420/00000/4CD062F7-3E4C-E811-868B-FA163E781D28.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/420/00000/8AFF2C6E-404C-E811-B77D-FA163E832FBF.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/420/00000/A2D7DB3D-404C-E811-B191-02163E01A11B.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/420/00000/C2DBA56F-4D4C-E811-8454-FA163EC0DFF4.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/420/00000/587F666B-4D4C-E811-BBD9-FA163EB41A13.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/420/00000/EA07C0D3-4D4C-E811-B7CB-FA163EF250BA.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/420/00000/307CABC0-234D-E811-9987-FA163E7B3281.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/420/00000/5469FC05-554C-E811-892E-FA163E06E023.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/420/00000/42FBB49B-264D-E811-A1FD-FA163E946B87.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/420/00000/0A37FDC5-564C-E811-AA26-FA163E40BFD6.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/420/00000/FE1D959F-2C4D-E811-B400-FA163EA883BD.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/420/00000/FCE8238E-2C4D-E811-91AC-FA163E5F28A9.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/420/00000/1042D047-314D-E811-92A4-02163E01535A.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/420/00000/5C3A56B4-364D-E811-A36F-FA163E9666C9.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/420/00000/5C3A56B4-364D-E811-A36F-FA163E9666C9.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/420/00000/DA25AB51-0D4D-E811-9032-FA163EA0C012.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/420/00000/423BFA52-0D4D-E811-A382-FA163EF3CD68.root',
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

print(process.schedule)
print(process.p)
print([x for x in process.schedule])
