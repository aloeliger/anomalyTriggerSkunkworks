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
                            fileNames = cms.untracked.vstring('/store/mc/Run3Winter23MiniAOD/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/MINIAODSIM/RnD_126X_mcRun3_2023_forPU65_v1-v2/2540000/173d48ef-56c6-45eb-876a-76ccb2e10ca2.root'),
                            secondaryFileNames = cms.untracked.vstring(
                                '/store/mc/Run3Winter23Digi/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/RnD_126X_mcRun3_2023_forPU65_v1-v2/40001/28e3b2b8-aae8-4e6e-913a-9cfd475fd454.root',
                                '/store/mc/Run3Winter23Digi/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/RnD_126X_mcRun3_2023_forPU65_v1-v2/40001/69a22394-d1d9-4e1b-ba4d-d05ff1e42768.root',
                                '/store/mc/Run3Winter23Digi/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/RnD_126X_mcRun3_2023_forPU65_v1-v2/40002/487f67f2-9f8e-4934-9ca8-fcca9faeac0a.root',
                                '/store/mc/Run3Winter23Digi/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/RnD_126X_mcRun3_2023_forPU65_v1-v2/40002/4c9f4f45-fa2e-42b7-8b2b-a510c4e65cbb.root',
                                '/store/mc/Run3Winter23Digi/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/RnD_126X_mcRun3_2023_forPU65_v1-v2/40001/07422941-48bb-4539-89cd-ea5546079119.root',
                                '/store/mc/Run3Winter23Digi/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/RnD_126X_mcRun3_2023_forPU65_v1-v2/40002/81fb92ce-6840-4611-af9e-8ab037a01df5.root',
                                '/store/mc/Run3Winter23Digi/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/RnD_126X_mcRun3_2023_forPU65_v1-v2/40002/8bbd395e-e070-4df8-9852-c75711206a2d.root',
                                '/store/mc/Run3Winter23Digi/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/RnD_126X_mcRun3_2023_forPU65_v1-v2/40002/e5c377a7-8672-428c-aea4-867903bf7102.root',
                                '/store/mc/Run3Winter23Digi/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/RnD_126X_mcRun3_2023_forPU65_v1-v2/40001/502f7a3a-001b-4dc1-a410-028a390f4f9d.root',
                                '/store/mc/Run3Winter23Digi/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/RnD_126X_mcRun3_2023_forPU65_v1-v2/40002/14693673-c1ec-4ebe-af87-10a23ff4b6ff.root',
                                '/store/mc/Run3Winter23Digi/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/RnD_126X_mcRun3_2023_forPU65_v1-v2/40002/37eb20f4-5e2f-41ac-8347-2e5ae001b7cf.root',
                                '/store/mc/Run3Winter23Digi/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/RnD_126X_mcRun3_2023_forPU65_v1-v2/40002/79adbfa6-4048-43a6-b4b5-897a0d6abe8d.root',
                                '/store/mc/Run3Winter23Digi/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/RnD_126X_mcRun3_2023_forPU65_v1-v2/40001/53b65b45-0889-4e2e-9e49-508c8838dd91.root',
                                '/store/mc/Run3Winter23Digi/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/RnD_126X_mcRun3_2023_forPU65_v1-v2/40002/3aa35426-4b87-452f-9841-5df4abb4fe6c.root',
                                '/store/mc/Run3Winter23Digi/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/RnD_126X_mcRun3_2023_forPU65_v1-v2/40002/765e68f1-e193-4174-8e64-67c782f06f76.root',
                                '/store/mc/Run3Winter23Digi/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/RnD_126X_mcRun3_2023_forPU65_v1-v2/40002/c902d25f-f6b5-4dda-9586-bc34ac324920.root',
                                '/store/mc/Run3Winter23Digi/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/RnD_126X_mcRun3_2023_forPU65_v1-v2/40001/c09ac36a-592e-4385-83a7-1d41f9e3d144.root',
                                '/store/mc/Run3Winter23Digi/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/RnD_126X_mcRun3_2023_forPU65_v1-v2/40002/22c2f2cc-9260-429b-8291-96563d65a41a.root',
                                '/store/mc/Run3Winter23Digi/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/RnD_126X_mcRun3_2023_forPU65_v1-v2/40002/a4af11dd-5115-4d99-bdf3-dbecc84a05c9.root',
                                '/store/mc/Run3Winter23Digi/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/RnD_126X_mcRun3_2023_forPU65_v1-v2/40002/c7d9e81f-8d76-41eb-9bec-15860f815222.root',
                                '/store/mc/Run3Winter23Digi/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/RnD_126X_mcRun3_2023_forPU65_v1-v2/40002/34c9e59c-5404-40c0-942e-5e39d4d25d41.root',
                                '/store/mc/Run3Winter23Digi/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/RnD_126X_mcRun3_2023_forPU65_v1-v2/40002/87339dce-16e3-4972-b301-e7dffafab0cc.root',
                                '/store/mc/Run3Winter23Digi/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/RnD_126X_mcRun3_2023_forPU65_v1-v2/40002/9384a22f-1d72-4f72-94d6-11d32f6450c7.root',
                                '/store/mc/Run3Winter23Digi/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/RnD_126X_mcRun3_2023_forPU65_v1-v2/40002/efbd8596-a5cd-4347-99af-55ef96ac7772.root',
                                '/store/mc/Run3Winter23Digi/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8/GEN-SIM-RAW/RnD_126X_mcRun3_2023_forPU65_v1-v2/40002/f21366bb-8a1a-4311-9b08-274b5c09a627.root',
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
process.GlobalTag = GlobalTag(process.GlobalTag, '126X_mcRun3_2023_forPU65_v1', '')

process.raw2digi_step = cms.Path(process.RawToDigi)
process.schedule = cms.Schedule(process.raw2digi_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

from L1Trigger.Configuration.customiseReEmul import L1TReEmulMCFromRAW

#call to customisation function L1TReEmulFromRAW imported from L1Trigger.Configuration.customiseReEmul
process = L1TReEmulMCFromRAW(process)

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

