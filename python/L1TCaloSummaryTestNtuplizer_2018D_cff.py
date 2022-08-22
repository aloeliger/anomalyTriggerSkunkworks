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
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10000) )

process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
                                #'/store/data/Run2018D/ZeroBias/MINIAOD/PromptReco-v2/000/325/270/00000/D75162E0-8310-1C45-8DE3-1A853C04DAA7.root', #cosmics
                                '/store/data/Run2018D/ZeroBias/MINIAOD/PromptReco-v2/000/320/804/00000/10AAF080-7399-E811-A671-FA163E963D8E.root', #29314 events
                                '/store/data/Run2018D/ZeroBias/MINIAOD/PromptReco-v2/000/320/804/00000/3865B93A-4A99-E811-9B59-FA163EE96337.root'#~90000 events
                            ),
                            secondaryFileNames = cms.untracked.vstring(
                                #'/store/data/Run2018D/ZeroBias/RAW/v1/000/325/270/00000/D5748A03-3B4E-624E-A70F-A7CC3F4A506F.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/804/00000/E6B9B695-F196-E811-AF2B-FA163EF0557D.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/804/00000/B4BF240D-F296-E811-9AAC-FA163E6788A6.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/804/00000/4631A079-F296-E811-A06D-FA163ECF9759.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/804/00000/62DBDA8C-F296-E811-906D-FA163E80361E.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/804/00000/2C8D0ADC-F796-E811-90A0-FA163E6FB017.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/804/00000/9A6C9936-F896-E811-B434-FA163E7A6C11.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/804/00000/E01E515E-F896-E811-B1F1-FA163ECB9FF9.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/804/00000/5A86FF7C-1797-E811-BB90-FA163ED0377A.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/804/00000/DE1E6DA7-1797-E811-B7D6-FA163E8CECB8.root',

                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/804/00000/5AA2D066-F096-E811-AE6D-02163E019FAC.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/804/00000/F610BA59-F096-E811-8932-FA163EF1AD57.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/804/00000/82769070-0297-E811-B995-FA163E396B84.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/804/00000/D88F13FB-0297-E811-9FE4-FA163E4DFDDE.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/804/00000/263D3519-0497-E811-807E-FA163EEB45BD.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/804/00000/627985DC-0497-E811-B0FD-FA163E355156.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/804/00000/FE9A191C-0597-E811-B9C8-FA163E251E18.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/804/00000/9AF51810-0797-E811-BCC9-FA163E77F338.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/804/00000/285E28D9-0F97-E811-BCCB-02163E010C72.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/804/00000/5A26BFCF-0F97-E811-887D-FA163E0B8998.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/804/00000/2E98345A-1097-E811-AF34-FA163EEA238B.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/804/00000/D2FBA57C-1097-E811-A410-FA163E97963B.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/804/00000/C2A7AE9D-1397-E811-9E59-FA163E98BEC0.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/804/00000/18D43DF0-1397-E811-B26B-FA163E3EB063.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/804/00000/3ACCA42D-1497-E811-8CC5-FA163EFD4E69.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/804/00000/7C37760D-1597-E811-A2B1-FA163EE3F004.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/804/00000/F4BAC90E-1597-E811-8D75-FA163EC1DE16.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/804/00000/CE00AD46-1B97-E811-A8E8-FA163EA6B93A.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/804/00000/DE88A90A-1D97-E811-9991-FA163EB005BF.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/804/00000/CA026DC6-2397-E811-8BB6-FA163EF1FB9C.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/804/00000/4A2E3219-2497-E811-A69B-FA163E2224F0.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/804/00000/E82B2C04-2697-E811-930C-02163E01A140.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/804/00000/20D5821C-2697-E811-BDA4-02163E019FF7.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/804/00000/98D7848C-2A97-E811-AF2E-FA163E29007B.root',
                                '/store/data/Run2018D/ZeroBias/RAW/v1/000/320/804/00000/AE30A950-3297-E811-8971-FA163EC0DFF4.root',
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

