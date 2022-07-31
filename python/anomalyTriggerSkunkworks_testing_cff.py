#just a quick framework to test the analyzer/producer framework to make sure that 
#all the insanity I am trying to pull will actually fly inside CMSSW

import FWCore.ParameterSet.Config as cms

process = cms.Process('anomalyTriggerTesting')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.Geometry.GeometryExtended2016Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')

#custom loads for the L1 summary setup

process.load('L1Trigger.Configuration.CaloTriggerPrimitives_cff')

process.load('EventFilter.L1TXRawToDigi.caloLayer1Stage2Digis_cfi')

#load for the simulated region information?

process.load('L1Trigger.L1TCaloLayer1.simCaloStage2Layer1Digis_cfi')

#Set-up general process information
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

process.MessageLogger.cerr.FwkReport.reportEvery = 10

process.source = cms.Source('PoolSource',
                            fileNames = cms.untracked.vstring(
                                #'/store/data/Run2018C/ZeroBias/MINIAOD/17Sep2018-v1/120000/257FD10B-6D35-7441-BA80-EC6F5205715A.root',
                                #'/store/data/Run2018C/ZeroBias/MINIAOD/17Sep2018-v1/120000/45960F97-D686-9C48-9217-18B01B2C2171.root',
                                #'/store/data/Run2018C/ZeroBias/MINIAOD/17Sep2018-v1/120000/51C2690F-6EE4-FB4A-9085-59E2EEDB915A.root',
                                #'/store/data/Run2018C/ZeroBias/MINIAOD/17Sep2018-v1/120000/C8C9C76B-C6CD-3B41-A187-0F476F68A8F3.root',
                                #'/store/data/Run2018C/ZeroBias/MINIAOD/17Sep2018-v1/120000/6541FFB6-9673-2641-9C1D-AAFE0CE36D1E.root',
                                #'/store/data/Run2018C/ZeroBias/MINIAOD/17Sep2018-v1/120000/7A4F1CEA-9005-EB47-B4A0-2C9163205D6D.root',
                                #'/store/data/Run2018C/ZeroBias/MINIAOD/17Sep2018-v1/120000/A92D9A3F-848E-8949-94AB-51FA607F3095.root',
                                #'/store/data/Run2018C/ZeroBias/MINIAOD/17Sep2018-v1/120000/77E4AD09-EFC0-2D41-8A72-D9A58D7B8611.root',
                                #'/store/data/Run2018C/ZeroBias/MINIAOD/17Sep2018-v1/120000/B3A2CADC-75F3-A242-9060-A290CDE14221.root'
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/252/00000/32ED3ECF-9949-E811-9D23-FA163E081C30.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/252/00000/38E89422-9F49-E811-8436-FA163ED637E6.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/252/00000/3A8A92F4-9949-E811-996D-FA163EFF76BB.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/252/00000/7E9C97C1-9E49-E811-A25F-FA163EBB779E.root',
                                '/store/data/Run2018A/ZeroBias/RAW/v1/000/315/252/00000/CC905368-9F49-E811-908D-FA163E7121A5.root',
                            )
)

process.options = cms.untracked.PSet(

)

#Get some things for the simulated digi modules
process.es_pool = cms.ESSource("PoolDBESSource",
                               timetype = cms.string('runnumber'),
                               toGet = cms.VPSet(
                                   cms.PSet(record = cms.string("HcalLutMetadataRcd"),
                                            tag = cms.string("HcalLutMetadata_HFTP_1x1")
                                        ),
                                   cms.PSet(record = cms.string("HcalElectronicsMapRcd"),
                                            tag = cms.string("HcalElectronicsMap_HFTP_1x1")
                                        )
                               ),
                               connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
                               authenticationMethod = cms.untracked.uint32(0)
)
process.es_prefer_es_pool = cms.ESPrefer( "PoolDBESSource", "es_pool" )

#Set some simCaloStage2Layer1Digi options
process.simCaloStage2Layer1Digis.useECALLUT = cms.bool(True)
process.simCaloStage2Layer1Digis.useHCALLUT = cms.bool(True)
process.simCaloStage2Layer1Digis.useHFLUT = cms.bool(True)
process.simCaloStage2Layer1Digis.useLSB = cms.bool(True)
process.simCaloStage2Layer1Digis.verbose = cms.bool(True)
process.simCaloStage2Layer1Digis.ecalToken = cms.InputTag("l1tCaloLayer1Digis")
process.simCaloStage2Layer1Digis.hcalToken = cms.InputTag("l1tCaloLayer1Digis")

#insert the anomaly trigger skunkworks 
from L1Trigger.anomalyTriggerSkunkworks.anomalyTriggerSkunkworks_cfi import *
process.anomalyTriggerSkunkworks = anomalyTriggerSkunkworks

#File service for writing portions of the analyzer out
process.TFileService = cms.Service(
    "TFileService",
    fileName = cms.string("anomalySkunkworks.root")
)

process.L1TRawToDigi_Stage2 = cms.Task(process.caloLayer1Digis, process.caloStage2Digis)
process.RawToDigi_short = cms.Sequence(process.L1TRawToDigi_Stage2)
process.p = cms.Path(process.RawToDigi_short * process.l1tCaloLayer1Digis * process.simCaloStage2Layer1Digis * process.anomalyTriggerSkunkworks)

process.schedule = cms.Schedule(process.p)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)

process.options.numberOfThreads=cms.untracked.uint32(4)
process.options.numberOfStreams=cms.untracked.uint32(0)
