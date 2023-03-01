import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2018_cff import Run2_2018

import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing ('analysis')
options.parseArguments()

process = cms.Process("USERTEST",Run2_2018)
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

#we're just testing if we can get the full emulation sequence up and running on 
# a raw file. THen we have to go through and decipher what trigger bits are what.
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents)
)
process.MessageLogger.cerr.FwkReport.reportEvery = 10000

#attempt to get rid of muon shower warning
process.MessageLogger.suppressWarning = cms.untracked.vstring('l1UpgradeTree','l1UpgradeEmuTree','l1UpgradeTfMuonShowerTree', 'emtfStage2Digis', 'l1uGTTestcrateTree')

#Define out input source
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring('/store/data/Run2018D/EphemeralZeroBias1/MINIAOD/PromptReco-v2/000/320/569/00000/020CE671-3C96-E811-B611-FA163EF7B7E3.root'),
                            secondaryFileNames = cms.untracked.vstring(
                                '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/041811F3-6F94-E811-B723-FA163EDA3EDC.root',
                                '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/10B6E814-6D94-E811-9E53-02163E01A16E.root',
                                '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/14B6680E-6D94-E811-9C87-FA163E44D80B.root',
                                '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/20F59A7D-7194-E811-B65A-02163E0164F8.root',
                                '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/48BBDCB6-7194-E811-84CE-FA163EC7FEDF.root',
                                '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/5A76C334-6D94-E811-BE3C-FA163E943C2A.root',
                                '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/5ED16976-7194-E811-9AF5-FA163E8BC3ED.root',
                                '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/68CAC802-7494-E811-B11D-FA163E581BC1.root',
                                '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/86361D76-7294-E811-B762-FA163E337D5D.root',
                                '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/AC24EE4A-6D94-E811-8956-02163E00BCAD.root',
                                '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/B87ECA12-6D94-E811-A3E1-FA163E959DBF.root',
                                '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/C60DDE19-6A94-E811-85D4-FA163E298876.root',
                                '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/DA76F2DC-7494-E811-A646-FA163E3FE3C5.root',
                                '/store/data/Run2018D/EphemeralZeroBias1/RAW/v1/000/320/569/00000/DC0BF10F-7094-E811-B67A-FA163EF670D6.root',
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
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(1),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(1),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, '120X_dataRun2_v2', '')
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.endjob_step = cms.EndPath(process.endOfProcess)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step, process.endjob_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
#from L1Trigger.L1TGlobal.uGTADEmulator_cfi import uGTADEmulator
#uGTEmulationPath = cms.Path(uGTADEmulator)
#process.schedule.append(uGTEmulationPath)
#Setup FWK for multithreaded
if hasattr(process, 'DQMStore'): process.DQMStore.assertLegacySafe=cms.untracked.bool(False)

# customisation of the process.

# Automatic addition of the customisation function from L1Trigger.Configuration.customiseReEmul
from L1Trigger.Configuration.customiseReEmul import L1TReEmulFromRAW 

#call to customisation function L1TReEmulFromRAW imported from L1Trigger.Configuration.customiseReEmul
process = L1TReEmulFromRAW(process)

# Automatic addition of the customisation function from L1Trigger.L1TNtuples.customiseL1Ntuple
from L1Trigger.L1TNtuples.customiseL1Ntuple import L1NtupleRAWEMU 

#call to customisation function L1NtupleRAWEMU imported from L1Trigger.L1TNtuples.customiseL1Ntuple
process = L1NtupleRAWEMU(process)

# Automatic addition of the customisation function from L1Trigger.Configuration.customiseSettings
from L1Trigger.Configuration.customiseSettings import L1TSettingsToCaloParams_2018_v1_3 

#call to customisation function L1TSettingsToCaloParams_2018_v1_3 imported from L1Trigger.Configuration.customiseSettings
process = L1TSettingsToCaloParams_2018_v1_3(process)

#load up our ntuplization stuff and append it on to the end of the schedule
process.load('L1Trigger.L1TCaloLayer1.uct2016EmulatorDigis_cfi')
# process.CaloSummaryPath = cms.Path(process.uct2016EmulatorDigis)
# process.schedule.append(process.CaloSummaryPath)

process.load('L1Trigger.anomalyTriggerSkunkworks.uGTADEmulator_cfi')
# process.uGTEmulationPath = cms.Path(process.uGTADEmulator)
# process.schedule.append(process.uGTEmulationPath)

process.load('L1Trigger.anomalyTriggerSkunkworks.pileupNetworkProducer_cfi')

process.productionTask = cms.Task(
    process.uct2016EmulatorDigis,
    process.uGTADEmulator,
    process.pileupNetworkProducer,
)
process.productionPath = cms.Path(process.productionTask)

process.schedule.append(process.productionPath)

process.load('L1Trigger.anomalyTriggerSkunkworks.L1TCaloSummaryTestNtuplizer_cfi')
process.L1TCaloSummaryTestNtuplizer.ecalToken = cms.InputTag('simEcalTriggerPrimitiveDigis')
process.L1TCaloSummaryTestNtuplizer.hcalToken = cms.InputTag('simHcalTriggerPrimitiveDigis')
process.L1TCaloSummaryTestNtuplizer.includePUInfo = cms.bool(True)

process.load('L1Trigger.anomalyTriggerSkunkworks.L1TTriggerBitsNtuplizer_cfi')
process.L1TTriggerBitsNtuplizer.verboseDebug= cms.bool(False)

process.load('L1Trigger.anomalyTriggerSkunkworks.boostedJetTriggerNtuplizer_cfi')

process.load('L1Trigger.anomalyTriggerSkunkworks.uGTModelNtuplizer_cfi')

process.load('L1Trigger.anomalyTriggerSkunkworks.pileupNetworkNtuplizer_cfi')


process.TFileService = cms.Service(
	"TFileService",
	#fileName = cms.string("l1TNtuple-test.root")
        fileName = cms.string(options.outputFile)
)
process.NtuplePath = cms.Path(
                                process.L1TCaloSummaryTestNtuplizer +
                                process.L1TTriggerBitsNtuplizer +
                                process.boostedJetTriggerNtuplizer +
                                process.uGTModelNtuplizer +
                                process.pileupNetworkNtuplizer
                              )
process.schedule.append(process.NtuplePath)


print(process.schedule)
print("**************************************************")
print([x for x in process.schedule])

#Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
