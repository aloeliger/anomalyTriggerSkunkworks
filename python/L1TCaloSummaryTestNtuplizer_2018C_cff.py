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
                                '/store/data/Run2018C/ZeroBias/MINIAOD/PromptReco-v3/000/319/910/00000/3A309C66-258D-E811-8115-FA163E942E01.root',
                            ),
                            secondaryFileNames = cms.untracked.vstring(
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/70668535-178B-E811-8A61-FA163E3E7C16.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/EADBDD24-178B-E811-893F-FA163E5819DC.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/B6A8022A-188B-E811-A764-FA163E9ED5E5.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/5677E082-188B-E811-9C1C-FA163E36351C.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/56BF00AC-188B-E811-A5C1-FA163E29DB10.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/FE06964A-188B-E811-B2EF-FA163EFF9EA7.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/3266216B-1A8B-E811-ABD1-FA163E5BAF7F.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/80E51A11-1C8B-E811-A199-FA163ED39CC9.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/BC5625FC-1E8B-E811-AA9D-FA163EB615BD.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/0A20C34F-208B-E811-9E5C-FA163EC4066E.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/0AE0ED3B-218B-E811-AEC5-FA163E74B46D.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/86161A16-228B-E811-8274-FA163E8ED26E.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/F214B99F-258B-E811-8A8D-FA163E1E3B31.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/E23F3FF9-258B-E811-BE47-FA163E74B46D.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/7E4038E5-268B-E811-A41C-FA163E5BCB73.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/12D2A1F1-268B-E811-BC0D-FA163EF3E48B.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/5A6EE65E-278B-E811-8703-FA163E283070.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/36C8E233-2A8B-E811-81C8-FA163E4F9F51.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/F2385B26-2E8B-E811-9005-FA163E1D8104.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/E2A0A7AE-2E8B-E811-AC41-FA163E6D1BE2.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/248E86C2-2F8B-E811-8C9A-FA163E2890BA.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/C6FD30A2-2F8B-E811-AC65-FA163EB9D708.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/04C818C1-2F8B-E811-A848-02163E00B00D.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/B2D8F8AE-2F8B-E811-AB03-FA163E492CEB.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/A8F3AC19-328B-E811-B7C1-FA163EA274D0.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/28754719-328B-E811-9767-FA163E4D3C24.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/A230C6C3-328B-E811-BFE6-02163E01A035.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/82DAA7F3-328B-E811-9F5B-FA163ED141EE.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/48CF9617-338B-E811-9D6F-FA163E3C37D4.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/E842AA9A-338B-E811-8073-A4BF012CB7F9.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/CE90558E-338B-E811-A4D7-FA163E4959A4.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/54FD6666-348B-E811-BB00-FA163E44F377.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/8A6C6FAE-348B-E811-849C-FA163EE0B264.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/54BECAAF-348B-E811-AF72-02163E01A0AB.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/C2C0A6B8-348B-E811-BCE0-FA163E7A7521.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/1074E545-358B-E811-9921-FA163E981033.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/705895BF-358B-E811-8077-FA163E9E8E7B.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/E4F19C36-368B-E811-BE83-FA163EE3D13F.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/CA983151-368B-E811-B7A5-FA163EAFF551.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/78334E09-378B-E811-B1B2-FA163EE7A04A.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/28A98A42-378B-E811-A9D1-FA163E9C6DAA.root',
                                '/store/data/Run2018C/ZeroBias/RAW/v1/000/319/910/00000/26CA6165-378B-E811-9991-FA163E6586F8.root',
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
	fileName = cms.string("l1TNtuple-ZeroBias-2018C.root")
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

