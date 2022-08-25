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
                                #'/store/data/Run2018B/ZeroBias/MINIAOD/PromptReco-v1/000/317/428/00000/747A37C5-3D6A-E811-A11E-FA163E5AB6C8.root', #cosmics
                                
                                #'/store/data/Run2018B/ZeroBias/MINIAOD/PromptReco-v1/000/317/434/00000/7E23B938-596A-E811-A3EB-FA163E038E39.root',

                                '/store/data/Run2018B/ZeroBias/MINIAOD/PromptReco-v1/000/317/511/00000/B6272DB3-5F6B-E811-8B83-02163E019EBE.root'
                            ),
                            secondaryFileNames = cms.untracked.vstring(
                                #'/store/data/Run2018B/ZeroBias/RAW/v1/000/317/428/00000/46DBD2A7-4D68-E811-B5F0-02163E017EF6.root',
                                
                                '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/2C1A98D4-4D6A-E811-8A7F-FA163E4E7FD0.root',
                                '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/22A599F7-4D6A-E811-8FB2-FA163E9414B2.root',
                                '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/CE4D37C4-4D6A-E811-AFCB-FA163E78F50B.root',
                                '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/621852D2-4D6A-E811-A816-FA163E198F4C.root',
                                '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/884993C6-4D6A-E811-9910-FA163E10052D.root',
                                '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/3E22E5EA-4D6A-E811-BF9E-FA163E337911.root',
                                '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/C6AFF2D1-4D6A-E811-8D64-FA163E2640F4.root',
                                '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/D0916CC6-4D6A-E811-B63B-FA163E279E4C.root',
                                '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/E267FC11-4E6A-E811-98D6-FA163E0EE1E4.root',
                                '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/98A5B6D2-4D6A-E811-B675-FA163E4E7FD0.root',
                                '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/D2B025CE-4D6A-E811-B51E-FA163E631526.root',
                                '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/525BAFC9-4D6A-E811-84A6-FA163E490F23.root',
                                '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/82558BC8-4D6A-E811-8D07-FA163E6F4029.root',
                                '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/CA4D66D5-4D6A-E811-9E95-FA163E5738F8.root',
                                '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/D28D7ECF-4D6A-E811-8C65-FA163E8F9CBA.root',
                                '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/B4B812CA-4D6A-E811-A63F-FA163E9ADC84.root',
                                '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/60435FC9-4D6A-E811-A576-FA163EF4C633.root',
                                '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/2C1A64F9-4D6A-E811-AC57-FA163E7C479F.root',
                                '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/9232B1C9-4D6A-E811-A45F-FA163E490F23.root',
                                '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/60CF23EC-4D6A-E811-B97E-FA163EC27161.root',
                                '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/B0CE29CE-4D6A-E811-9AAC-FA163E29007B.root',
                                '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/511/00000/7088EDC7-4D6A-E811-86D9-FA163E6E9B93.root',

                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/0040DCDC-4F68-E811-9526-FA163E0226BA.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/00BFABD3-4B68-E811-BBB3-FA163E852485.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/0228B0AB-4F68-E811-A1C0-FA163E17A15F.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/08DEAF97-5268-E811-86EE-FA163ECCF441.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/14E162B6-4E68-E811-905C-FA163E9C495B.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/18E26D78-5468-E811-9CAF-FA163E6F7000.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/18EFB8AC-4F68-E811-A358-FA163E17A15F.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/1CE14B77-5168-E811-B010-FA163EB68402.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/22999CD3-5468-E811-8741-FA163E25E9FD.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/2A9579B7-4E68-E811-9592-FA163E9ADC84.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/36FFF1DB-5468-E811-A3B8-FA163E49433D.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/3AA6DFE0-5268-E811-932D-FA163EBC1FCE.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/3AC5C5E5-4D68-E811-B07B-FA163EFD58CC.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/407E385F-5268-E811-8CA6-FA163EB3873F.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/46E83C13-4D68-E811-8F6D-FA163E8D01A3.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/4EB6F39B-5068-E811-AFB0-FA163EBE6DD0.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/503B9D67-5468-E811-96CF-FA163E97BF6C.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/520BEEE3-4B68-E811-ADFF-FA163E3479EA.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/589F0384-5168-E811-B886-FA163E401182.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/6008A4D2-4B68-E811-B244-FA163ECC03D8.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/626C14E6-4D68-E811-8B3E-FA163E62FAB2.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/667DDF99-5068-E811-8EF9-FA163EFD7515.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/6832558C-4A68-E811-90F4-02163E01A15C.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/74E270DD-4E68-E811-B1AA-02163E01A136.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/8218EFE4-5268-E811-B458-FA163E1A3CDC.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/8604FB76-5168-E811-96A0-FA163EC72C45.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/92E6B9DB-4E68-E811-9344-FA163E19119E.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/94CE189B-5068-E811-ADD7-FA163E23E7A6.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/982B386C-5468-E811-AA4F-FA163E39F017.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/9A3F60D2-4B68-E811-90B4-FA163EBAF405.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/ACB9E499-5068-E811-A50E-FA163E5234B3.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/B0F52B61-5268-E811-BCA5-02163E019F07.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/B27FC680-4D68-E811-853E-02163E019EA3.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/B8DC6DB6-4E68-E811-9D26-FA163E9C495B.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/BA6D6AF8-4A68-E811-A3D2-02163E01A10B.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/BAB7599B-5068-E811-979D-FA163EBE6DD0.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/BCE009BF-4C68-E811-B7B4-FA163EAEF412.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/BCE28B43-5368-E811-B85F-02163E01A00D.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/C0B93E87-4A68-E811-9F88-FA163E108FC3.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/C0DF319D-5268-E811-8D26-FA163E5BAA39.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/C483C3BE-4C68-E811-8E5D-FA163E3C0C41.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/CCB515BF-4C68-E811-AD61-FA163EBB9A14.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/D003BF68-5268-E811-A431-FA163E742E53.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/D2F3C292-2269-E811-8021-FA163E5D6003.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/D603F677-5168-E811-B302-FA163E79C06A.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/D843AC68-5468-E811-8DD4-FA163EEAC38E.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/DC9B648C-5368-E811-B3A5-FA163E7C479F.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/E25174C3-5568-E811-842E-FA163E2224F0.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/E42ADBD9-4D68-E811-8110-FA163E600F07.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/E4FDE25E-5268-E811-8DCB-FA163E8D39C1.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/E62F0FF7-4A68-E811-B6E9-FA163EEC39B2.root',
                                # '/store/data/Run2018B/ZeroBias/RAW/v1/000/317/434/00000/F093C09A-5568-E811-9F3C-FA163E3D470E.root',
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
	fileName = cms.string("l1TNtuple-ZeroBias-2018B.root")
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

