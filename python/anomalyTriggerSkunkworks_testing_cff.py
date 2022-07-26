#just a quick framework to test the analyzer/producer framework to make sure that 
#all the insanity I am trying to pull will actually fly inside CMSSW

import FWCore.ParameterSet.Config as cms

process = cms.Process('anomalyTriggerTesting')

process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.Geometry.GeometryExtended2016Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

#custom loads for the L1 summary setup

process.load('L1Trigger.Configuration.CaloTriggerPrimitives_cff')

process.load('EventFilter.L1TXRawToDigi.caloLayer1Stage2Digis_cfi')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.MessageLogger.cerr.FwkReport.reportEvery = 1000

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

process.options = process.options = cms.untracked.PSet(

)

#insert the anomaly trigger skunkworks 
from L1Trigger.anomalyTriggerSkunkworks.anomalyTriggerSkunkworks_cfi import *
process.anomalyTriggerSkunkworks = anomalyTriggerSkunkworks

process.L1TRawToDigi_Stage2 = cms.Task(process.caloLayer1Digis, process.caloStage2Digis)
process.RawToDigi_short = cms.Sequence(process.L1TRawToDigi_Stage2)
process.p = cms.Path(process.RawToDigi_short*process.l1tCaloLayer1Digis * process.anomalyTriggerSkunkworks)

process.schedule = cms.Schedule(process.p)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)

process.options.numberOfThreads=cms.untracked.uint32(4)
process.options.numberOfStreams=cms.untracked.uint32(0)
