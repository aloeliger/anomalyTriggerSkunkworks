import FWCore.ParameterSet.Config as cms

# from Configuration.Eras.Era_Run2_2018_cff import Run2_2018
from Configuration.Eras.Era_Run3_2023_cff import Run3_2023

import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing ('analysis')
options.parseArguments()

process = cms.Process("NTUPLIZE",Run3_2023)
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents)
)
process.MessageLogger.cerr.FwkReport.reportEvery = 10000

process.MessageLogger.suppressWarning = cms.untracked.vstring(
    'emtfStage2Digis', 
    'l1uGTTestcrateTree', 
    'simDtTriggerPrimitiveDigis',
    'simCscTriggerPrimitiveDigisRun3'
)

#Define out input source
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring('/store/data/Run2023C/ZeroBias/MINIAOD/PromptReco-v1/000/367/094/00000/cd8692ec-e37f-456b-8d3a-c6f854a2b83a.root'),
                            secondaryFileNames = cms.untracked.vstring(
                                "/store/data/Run2023C/ZeroBias/RAW/v1/000/367/094/00000/60dd6298-7ebf-4219-8da6-816915e8a1f8.root",
                                "/store/data/Run2023C/ZeroBias/RAW/v1/000/367/094/00000/ddf586ed-b482-400e-94f9-dc8cd3547122.root",
                             )
)

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run3_data', '')

process.raw2digi_step = cms.Path(process.RawToDigi)
process.schedule = cms.Schedule(process.raw2digi_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

from L1Trigger.Configuration.customiseReEmul import L1TReEmulFromRAW

#call to customisation function L1TReEmulFromRAW imported from L1Trigger.Configuration.customiseReEmul
process = L1TReEmulFromRAW(process)


process.skimOutput = cms.OutputModule(
    'PoolOutputModule',
    fileName = cms.untracked.string(options.outputFile),
    outputCommands = cms.untracked.vstring(
        'keep *',
        'drop *_*_*_NTUPLIZE',
        'keep *_simCaloStage2Layer1Digis_*_*',
        'drop *_*_*_LHC',
        'drop *_*_*_HLT',
    ),
)

process.skimStep = cms.EndPath(
    process.skimOutput
)

process.schedule.append(process.skimStep)

print(process.schedule)

