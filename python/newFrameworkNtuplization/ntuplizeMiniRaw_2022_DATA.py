import FWCore.ParameterSet.Config as cms

# from Configuration.Eras.Era_Run2_2018_cff import Run2_2018
from Configuration.Eras.Era_Run3_cff import Run3

import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing ('analysis')
options.parseArguments()

process = cms.Process("NTUPLIZE",Run3)
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

#attempt to get rid of muon shower warning
process.MessageLogger.suppressWarning = cms.untracked.vstring(
    'l1UpgradeTree',
    'l1UpgradeEmuTree',
    'l1UpgradeTfMuonShowerTree', 
    'emtfStage2Digis', 
    'l1uGTTestcrateTree', 
    'simDtTriggerPrimitiveDigis'
)

#Define out input source
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring('/store/data/Run2022G/EphemeralZeroBias1/MINIAOD/PromptReco-v1/000/362/437/00000/18960f50-c733-4369-aec0-8a9b3b57bca1.root'),
                            secondaryFileNames = cms.untracked.vstring(
                                '/store/data/Run2022G/EphemeralZeroBias1/RAW/v1/000/362/437/00000/38499c58-9b59-4302-9ba1-f314ddeac12c.root',
                                '/store/data/Run2022G/EphemeralZeroBias1/RAW/v1/000/362/437/00000/7b7c7b12-c838-4f1c-91e1-7214ad4ea0a2.root',
                                '/store/data/Run2022G/EphemeralZeroBias1/RAW/v1/000/362/437/00000/811c58d6-c794-4aa5-801c-80ddcaa182c1.root',
                                '/store/data/Run2022G/EphemeralZeroBias1/RAW/v1/000/362/437/00000/89d256d7-85bd-4563-bb41-e527b0ac9737.root',
                                '/store/data/Run2022G/EphemeralZeroBias1/RAW/v1/000/362/437/00000/93382701-4c91-4b41-b844-2288f13a4c1e.root',
                                '/store/data/Run2022G/EphemeralZeroBias1/RAW/v1/000/362/437/00000/946291e8-72ab-4c99-a809-6878e6da1cf9.root',
                                '/store/data/Run2022G/EphemeralZeroBias1/RAW/v1/000/362/437/00000/9f429629-ca52-470a-842a-604988f60e70.root',
                                '/store/data/Run2022G/EphemeralZeroBias1/RAW/v1/000/362/437/00000/9ff46ba6-7b93-4948-bb29-b1acc65e2b8f.root',
                                '/store/data/Run2022G/EphemeralZeroBias1/RAW/v1/000/362/437/00000/f92864a9-6587-4f7f-bb7b-5fd753e142aa.root',
                            )
                            #ttbar MC inputs
                            # fileNames = cms.untracked.vstring('/store/mc/Run3Summer22MiniAODv3/TT_TuneCP5_13p6TeV_powheg-pythia8/MINIAODSIM/124X_mcRun3_2022_realistic_v12-v3/2810000/030d8d9c-7ee7-425e-9686-1cb23020feda.root'),
                            # secondaryFileNames = cms.untracked.vstring(
                            #   '/store/mc/Run3Summer22DRPremix/TT_TuneCP5_13p6TeV_powheg-pythia8/GEN-SIM-RAW/124X_mcRun3_2022_realistic_v12-v3/2810001/708c1b63-19b6-468d-808e-2c4bdcd8859f.root',
                            #   '/store/mc/Run3Summer22DRPremix/TT_TuneCP5_13p6TeV_powheg-pythia8/GEN-SIM-RAW/124X_mcRun3_2022_realistic_v12-v3/2810001/e5617bda-2ef0-43e6-bf21-31b70ce34fd1.root',
                            #   '/store/mc/Run3Summer22DRPremix/TT_TuneCP5_13p6TeV_powheg-pythia8/GEN-SIM-RAW/124X_mcRun3_2022_realistic_v12-v3/2810001/78cac27f-73eb-4e54-adaa-6f53fbe3bedc.root',
                            #   '/store/mc/Run3Summer22DRPremix/TT_TuneCP5_13p6TeV_powheg-pythia8/GEN-SIM-RAW/124X_mcRun3_2022_realistic_v12-v3/2810001/8c540b01-2997-493e-9c35-8102f38c7ee9.root',
                            #   '/store/mc/Run3Summer22DRPremix/TT_TuneCP5_13p6TeV_powheg-pythia8/GEN-SIM-RAW/124X_mcRun3_2022_realistic_v12-v3/2810001/aae5621d-42db-4c19-8861-4760f52e1e7d.root',
                            #   '/store/mc/Run3Summer22DRPremix/TT_TuneCP5_13p6TeV_powheg-pythia8/GEN-SIM-RAW/124X_mcRun3_2022_realistic_v12-v3/2810001/ba6e772b-d547-4169-87bb-4eb3ce27a57c.root',
                            #   '/store/mc/Run3Summer22DRPremix/TT_TuneCP5_13p6TeV_powheg-pythia8/GEN-SIM-RAW/124X_mcRun3_2022_realistic_v12-v3/2810001/bc47deee-423e-4ccb-82e1-83373d2d5b99.root',
                            #   '/store/mc/Run3Summer22DRPremix/TT_TuneCP5_13p6TeV_powheg-pythia8/GEN-SIM-RAW/124X_mcRun3_2022_realistic_v12-v3/2810001/e5617bda-2ef0-43e6-bf21-31b70ce34fd1.root',
                            # ),
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
from L1Trigger.Configuration.customiseReEmul import L1TReEmulMCFromRAW

#call to customisation function L1TReEmulFromRAW imported from L1Trigger.Configuration.customiseReEmul
process = L1TReEmulMCFromRAW(process)

# Automatic addition of the customisation function from L1Trigger.L1TNtuples.customiseL1Ntuple
#from L1Trigger.L1TNtuples.customiseL1Ntuple import L1NtupleRAWEMU 

#call to customisation function L1NtupleRAWEMU imported from L1Trigger.L1TNtuples.customiseL1Ntuple
#process = L1NtupleRAWEMU(process)

# Automatic addition of the customisation function from L1Trigger.Configuration.customiseSettings
# from L1Trigger.Configuration.customiseSettings import L1TSettingsToCaloParams_2018_v1_3 

#call to customisation function L1TSettingsToCaloParams_2018_v1_3 imported from L1Trigger.Configuration.customiseSettings
# process = L1TSettingsToCaloParams_2018_v1_3(process)

#load up our ntuplization stuff and append it on to the end of the schedule
#process.load('L1Trigger.L1TCaloLayer1.uct2016EmulatorDigis_cfi')
process.load('L1Trigger.L1TCaloLayer1.L1TCaloSummaryCICADAv1')
process.load('L1Trigger.L1TCaloLayer1.L1TCaloSummaryCICADAv2')
#process.CaloSummaryPath = cms.Path(process.uct2016EmulatorDigis)
#process.schedule.append(process.CaloSummaryPath)

process.load('anomalyDetection.anomalyTriggerSkunkworks.uGTADEmulator_cfi')
#process.uGTEmulationPath = cms.Path(process.uGTADEmulator)
#process.schedule.append(process.uGTEmulationPath)

#get the pileup network
process.load('anomalyDetection.anomalyTriggerSkunkworks.pileupNetworkProducer_cfi')
# get the CICADAInputNetworkProducer 
# process.load('anomalyDetection.miniCICADA.CICADAInputNetworkProducer_cfi')
#get the CICADAInputNetwork Producer
# process.load('anomalyDetection.miniCICADA.CICADAFromCINProducer_cfi')
# process.load('anomalyDetection.miniCICADA.miniCICADAProducer_cfi')


process.productionTask = cms.Task(
#    process.uct2016EmulatorDigis,
    process.L1TCaloSummaryCICADAv1,
    process.L1TCaloSummaryCICADAv2,
    process.uGTADEmulator,
    process.pileupNetworkProducer,
    process.inciSNAILv0p1Producer,
    # process.CICADAInputNetworkProducerv1p0,
    # process.CICADAv1FromCINv1Producer,
    # process.CICADAv2FromCINv1Producer,
    # process.miniCICADAProducer,
    # process.miniCICADAProducerCICADAv1,
    # process.miniCICADAv1p1CICADAv1,
    # process.miniCICADAv1p1CICADAv2,
)

process.productionPath = cms.Path(process.productionTask)

process.schedule.append(process.productionPath)

# process.load('anomalyDetection.anomalyTriggerSkunkworks.L1TCaloSummaryTestNtuplizer_cfi')
# process.L1TCaloSummaryTestNtuplizer.ecalToken = cms.InputTag('simEcalTriggerPrimitiveDigis')
# process.L1TCaloSummaryTestNtuplizer.hcalToken = cms.InputTag('simHcalTriggerPrimitiveDigis')
from anomalyDetection.anomalyTriggerSkunkworks.L1TCaloSummaryTestNtuplizer_cfi import L1TCaloSummaryTestNtuplizer

process.CICADAv1ntuplizer = L1TCaloSummaryTestNtuplizer.clone(
    scoreSource = cms.InputTag("L1TCaloSummaryCICADAv1","anomalyScore"),
    ecalToken = cms.InputTag('simEcalTriggerPrimitiveDigis'),
    hcalToken = cms.InputTag('simHcalTriggerPrimitiveDigis'),
    # includePUInfo = cms.bool(True),
)

process.CICADAv2ntuplizer = L1TCaloSummaryTestNtuplizer.clone(
    scoreSource = cms.InputTag("L1TCaloSummaryCICADAv2","anomalyScore"),
    ecalToken = cms.InputTag('simEcalTriggerPrimitiveDigis'),
    hcalToken = cms.InputTag('simHcalTriggerPrimitiveDigis'),
    # includePUInfo = cms.bool(True),
)
# Custom boosted jet trigger information
from anomalyDetection.anomalyTriggerSkunkworks.boostedJetTriggerNtuplizer_cfi import boostedJetTriggerNtuplizer
process.boostedJetTriggerNtuplizer = boostedJetTriggerNtuplizer.clone(boostedJetCollection = cms.InputTag("L1TCaloSummaryCICADAv1","Boosted"))

process.load('anomalyDetection.anomalyTriggerSkunkworks.L1TTriggerBitsNtuplizer_cfi')
# process.L1TTriggerBitsNtuplizer.verboseDebug = cms.bool(True)
# process.load('anomalyDetection.anomalyTriggerSkunkworks.boostedJetTriggerNtuplizer_cfi')
process.load('anomalyDetection.anomalyTriggerSkunkworks.uGTModelNtuplizer_cfi')
process.load('anomalyDetection.anomalyTriggerSkunkworks.pileupNetworkNtuplizer_cfi')
process.load('anomalyDetection.anomalyTriggerSkunkworks.genJetInformationNtuplizer_cfi')

process.load('anomalyDetection.miniCICADA.PFcandSequence_cfi')
#process.load('anomalyDetection.miniCICADA.electronInformationAnalyzer_cfi')
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

# process.CICADAFromCINSequence = cms.Sequence(
#     process.CICADAv1FromCINv1Analyzer +
#     process.CICADAv2FromCINv1Analyzer
# )
# process.miniCICADAAnalyzerSequence = cms.Sequence(
#     process.miniCICADAAnalyzer +
#     process.miniCICADAAnalyzerCICADAv1 +
#     process.miniCICADAv1p1AnalyzerCICADAv1 +
#     process.miniCICADAv1p1AnalyzerCICADAv2
# )


process.TFileService = cms.Service(
	"TFileService",
	#fileName = cms.string("l1TNtuple-test.root")
        fileName = cms.string(options.outputFile)
)
process.NtuplePath = cms.Path(
                                # process.L1TCaloSummaryTestNtuplizer +
                                process.CICADAv1ntuplizer +
                                process.CICADAv2ntuplizer +
                                process.boostedJetTriggerNtuplizer +
                                process.L1TTriggerBitsNtuplizer +
                                # process.CICADAInputNetworkAnalyzerv1p0 +
                                # process.CICADAFromCINSequence +
                                # process.miniCICADAAnalyzerSequence +
                                process.uGTModelNtuplizer +
                                # process.PFcandSequence +
                                process.pileupNetworkNtuplizer +
                                process.inciSNAILv0p1Ntuplizer +
                                process.pileupInformationNtuplizer +
                                process.metInformationNtuplizer +
                                process.caloStage2Sequence +
                                process.objectCountSequence 
                                # process.genJetInformationNtuplizer
)
process.schedule.append(process.NtuplePath)

print("schedule:")
print(process.schedule)
print("schedule contents:")
print([x for x in process.schedule])
