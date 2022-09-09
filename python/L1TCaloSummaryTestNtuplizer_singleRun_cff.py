import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2018_cff import Run2_2018

process = cms.Process("L1TCaloSummaryTest", Run2_2018)

from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing()
options.register('numEvents', 10000, VarParsing.multiplicity.singleton, VarParsing.varType.int, 'Number of Events to Process')
options.register('inputFiles','', VarParsing.multiplicity.singleton, VarParsing.varType.string, 'File to load and run. Can be local if prefixed with file:')
options.register('outputFile', 'out.root', VarParsing.multiplicity.singleton, VarParsing.varType.string, 'File to write the output to.')
options.register('useECALLUT',True, VarParsing.multiplicity.singleton, VarParsing.varType.bool, 'enable or disable usage of the ECAL LUTs at the simCaloStage2Layer1Digis (CaloL1 Emulation) side')
options.register('useHCALLUT',True, VarParsing.multiplicity.singleton, VarParsing.varType.bool, 'enable or disable usage of the HCAL LUTs at the simCaloStage2Layer1Digis (CaloL1 Emulation) side')
options.register('useCalib',True, VarParsing.multiplicity.singleton, VarParsing.varType.bool, 'enable or disable the Calibrations at the simCaloStage2Layer1Digis (CaloL1 Emulation) side')
options.register('useLSB',True, VarParsing.multiplicity.singleton, VarParsing.varType.bool, 'ebable or disable the LSB at the simCaloStage2Layer1Digis (CaloL1 Emulation) side')

options.parseArguments()

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
#process.GlobalTag = GlobalTag(process.GlobalTag, '112X_dataRun2_v7', '')
process.GlobalTag = GlobalTag(process.GlobalTag, '120X_dataRun2_v2', '')

process.load('L1Trigger.Configuration.CaloTriggerPrimitives_cff')

process.load('EventFilter.L1TXRawToDigi.caloLayer1Stage2Digis_cfi')

process.load('L1Trigger.L1TCaloLayer1.simCaloStage2Layer1Digis_cfi')
process.simCaloStage2Layer1Digis.ecalToken = cms.InputTag("l1tCaloLayer1Digis")
process.simCaloStage2Layer1Digis.hcalToken = cms.InputTag("l1tCaloLayer1Digis")
process.simCaloStage2Layer1Digis.useECALLUT = options.useECALLUT
process.simCaloStage2Layer1Digis.useHCALLUT = options.useHCALLUT
process.simCaloStage2Layer1Digis.useHFLUT = options.useHCALLUT
process.simCaloStage2Layer1Digis.useCalib = options.useCalib
process.simCaloStage2Layer1Digis.useLSB = options.useLSB

process.load('L1Trigger.L1TCaloLayer1.uct2016EmulatorDigis_cfi')

process.load("L1Trigger.Run3Ntuplizer.l1BoostedJetStudies_cfi")

process.load("L1Trigger.anomalyTriggerSkunkworks.L1TCaloSummaryTestNtuplizer_cfi")
process.L1TCaloSummaryTestNtuplizer.verboseDebug = cms.bool(True)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.numEvents) )

process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
                                options.inputFiles,
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
	#fileName = cms.string("l1TNtuple-test.root")
        fileName = cms.string(options.outputFile)
)

process.L1TRawToDigi_Stage2 = cms.Task(process.caloLayer1Digis, process.caloStage2Digis)
process.RawToDigi_short = cms.Sequence(process.L1TRawToDigi_Stage2)
process.p = cms.Path(process.RawToDigi_short * 
                     process.l1tCaloLayer1Digis *
                     process.simCaloStage2Layer1Digis * 
                     process.uct2016EmulatorDigis * 
                     #process.l1NtupleProducer
                     process.L1TCaloSummaryTestNtuplizer)
#Output
process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string("l1TFullEvent.root"),
    outputCommands = cms.untracked.vstring('keep *')
)

process.e = cms.EndPath(process.out)

process.schedule = cms.Schedule(process.p,process.e)
#process.schedule = cms.Schedule(process.p)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)

# Multi-threading
process.options.numberOfThreads=cms.untracked.uint32(8)
process.options.numberOfStreams=cms.untracked.uint32(0)

