import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_2023_cff import Run3_2023

import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing ('analysis')
options.register('secondaryFiles',
                 [],
                 VarParsing.VarParsing.multiplicity.list,
                VarParsing.VarParsing.varType.string,
                "Secondary files to use in SUEP skimming"
)
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

# process.MessageLogger = cms.Service(
#     "MessageLogger",
#     destinations = cms.untracked.vstring("cerr", "cout"),
#     cerr = cms.untracked.PSet(
#         threshold = cms.untracked.string('DEBUG')
#     ),
#     cout = cms.untracked.PSet(
#         threshold = cms.untracked.string('DEBUG')
#     )
# )
# process.MessageLogger.cerr.FwkReport.reportEvery = 10000

#attempt to get rid of muon shower warning
process.MessageLogger.suppressWarning = cms.untracked.vstring(
    'l1UpgradeTree',
    'l1UpgradeEmuTree',
    'l1UpgradeTfMuonShowerTree', 
    'emtfStage2Digis', 
    'l1uGTTestcrateTree', 
    'simDtTriggerPrimitiveDigis',
    'simEmtfDigis'
)

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(options.inputFiles),

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
process.GlobalTag = GlobalTag(process.GlobalTag, '130X_dataRun3_Prompt_v4', '')

process.raw2digi_step = cms.Path(process.RawToDigi)
process.endjob_step = cms.EndPath(process.endOfProcess)
# event setup contents
# process.escontent = cms.EDAnalyzer(
#     "PrintEventSetupContent",
#     compact=cms.untracked.bool(True),
#     printProviders=cms.untracked.bool(True),
# )
# process.endjob_step = cms.EndPath(process.escontent+process.endOfProcess)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step, process.endjob_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads = 1
process.options.numberOfStreams = 1
process.options.numberOfConcurrentLuminosityBlocks = 1
process.options.eventSetup.numberOfConcurrentIOVs = 1
if hasattr(process, 'DQMStore'): process.DQMStore.assertLegacySafe=cms.untracked.bool(False)
# Automatic addition of the customisation function from L1Trigger.Configuration.customiseReEmul
from L1Trigger.Configuration.customiseReEmul import L1TReEmulFromRAW

#call to customisation function L1TReEmulFromRAW imported from L1Trigger.Configuration.customiseReEmul
process = L1TReEmulFromRAW(process)

# Automatic addition of the customisation function from L1Trigger.L1TNtuples.customiseL1Ntuple
from L1Trigger.L1TNtuples.customiseL1Ntuple import L1NtupleRAWEMU 

#call to customisation function L1NtupleRAWEMU imported from L1Trigger.L1TNtuples.customiseL1Ntuple
process = L1NtupleRAWEMU(process)
process.l1ntupleraw.remove(process.l1uGTTestcrateTree)

# Automatic addition of the customisation function from L1Trigger.Configuration.customiseSettings
# from L1Trigger.Configuration.customiseSettings import L1TSettingsToCaloParams_2018_v1_3 

#call to customisation function L1TSettingsToCaloParams_2018_v1_3 imported from L1Trigger.Configuration.customiseSettings
# process = L1TSettingsToCaloParams_2018_v1_3(process)

#load up our ntuplization stuff and append it on to the end of the schedule
process.load('L1Trigger.L1TCaloLayer1.L1TCaloSummaryCICADAv1p1')
process.load('L1Trigger.L1TCaloLayer1.L1TCaloSummaryCICADAv2p1')

#get the pileup network

process.productionTask = cms.Task(
    process.L1TCaloSummaryCICADAv1,
    process.L1TCaloSummaryCICADAv2,
)
process.productionPath = cms.Path(process.productionTask)

process.schedule.append(process.productionPath)

# process.load('anomalyDetection.anomalyTriggerSkunkworks.L1TCaloSummaryTestNtuplizer_cfi')
from anomalyDetection.anomalyTriggerSkunkworks.L1TCaloSummaryTestNtuplizer_cfi import L1TCaloSummaryTestNtuplizer

process.CICADAv1ntuplizer = L1TCaloSummaryTestNtuplizer.clone(
    scoreSource = cms.InputTag("L1TCaloSummaryCICADAv1","anomalyScore"),
    ecalToken = cms.InputTag('simEcalTriggerPrimitiveDigis'),
    hcalToken = cms.InputTag('simHcalTriggerPrimitiveDigis'),
    includePUInfo = cms.bool(True),
)

process.CICADAv2ntuplizer = L1TCaloSummaryTestNtuplizer.clone(
    scoreSource = cms.InputTag("L1TCaloSummaryCICADAv2","anomalyScore"),
    ecalToken = cms.InputTag('simEcalTriggerPrimitiveDigis'),
    hcalToken = cms.InputTag('simHcalTriggerPrimitiveDigis'),
    includePUInfo = cms.bool(True),
)
# Custom boosted jet trigger information
from anomalyDetection.anomalyTriggerSkunkworks.boostedJetTriggerNtuplizer_cfi import boostedJetTriggerNtuplizer
process.boostedJetTriggerNtuplizer = boostedJetTriggerNtuplizer.clone(boostedJetCollection = cms.InputTag("L1TCaloSummaryCICADAv1","Boosted"))

process.load('anomalyDetection.anomalyTriggerSkunkworks.L1TTriggerBitsNtuplizer_cfi')
# process.L1TTriggerBitsNtuplizer.verboseDebug = cms.bool(True)
# process.load('anomalyDetection.anomalyTriggerSkunkworks.boostedJetTriggerNtuplizer_cfi')
process.load('anomalyDetection.anomalyTriggerSkunkworks.uGTModelNtuplizer_cfi')
# process.load('anomalyDetection.anomalyTriggerSkunkworks.pileupNetworkNtuplizer_cfi')
process.load('anomalyDetection.anomalyTriggerSkunkworks.genJetInformationNtuplizer_cfi')

process.load('anomalyDetection.miniCICADA.PFcandSequence_cfi')
process.load('anomalyDetection.miniCICADA.pileupInformationNtuplizer_cfi')
process.load('anomalyDetection.miniCICADA.metInformationNtuplizer_cfi')
process.load('anomalyDetection.miniCICADA.caloStage2EGammaNtuplizer_cfi')
process.load('anomalyDetection.miniCICADA.caloStage2JetNtuplizer_cfi')
process.load('anomalyDetection.miniCICADA.caloStage2TauNtuplizer_cfi')
process.load('anomalyDetection.miniCICADA.caloStage2EtSumNtuplizer_cfi')
process.load('anomalyDetection.miniCICADA.slimmedObjectCounter_cfi')
process.load('anomalyDetection.miniCICADA.CICADAInputNetworkAnalyzer_cfi')
process.load('anomalyDetection.miniCICADA.CICADAFromCINAnalyzer_cfi')
process.load('anomalyDetection.miniCICADA.miniCICADAAnalyzer_cfi')


process.caloStage2Sequence = cms.Sequence(
                                process.caloStage2EGammaNtuplizer + 
                                process.caloStage2JetNtuplizer + 
                                process.caloStage2TauNtuplizer +
                                process.caloStage2EtSumNtuplizer
)




process.TFileService = cms.Service(
	"TFileService",
	#fileName = cms.string("l1TNtuple-test.root")
        fileName = cms.string(options.outputFile)
)
process.NtuplePath = cms.Path(
                                process.CICADAv1ntuplizer +
                                process.CICADAv2ntuplizer +
                                process.boostedJetTriggerNtuplizer +
                                process.L1TTriggerBitsNtuplizer +
                                # process.pileupNetworkNtuplizer +
                                process.pileupInformationNtuplizer +
                                process.metInformationNtuplizer +
                                process.caloStage2Sequence +
                                process.objectCountSequence 
)
process.schedule.append(process.NtuplePath)

print("schedule:")
print(process.schedule)
print("schedule contents:")
print([x for x in process.schedule])
