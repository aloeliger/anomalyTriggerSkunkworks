import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_2023_cff import Run3_2023

import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing('analysis')
options.parseArguments()

process = cms.Process("SKIM", Run3_2023)
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

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/028f5a12-7c59-4616-92d9-8773d09a4931.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/0330a763-90c5-47cf-a936-72c8643fface.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/04dd004d-1e5a-4563-b67d-1b14f1ed1626.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/0654cd4c-4839-4b62-bc2d-e5edb86f8834.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/099c02b9-dcb5-4233-bec1-bc043abca394.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/0d51dac0-b287-42b0-ac8d-6dee0feb41c2.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/0d7e346f-fa8d-4a0d-a90c-3a329b8f2cb6.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/0ef22190-f646-41ff-b3d7-7c7aeb70ab4a.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/0f9902a9-2b11-4055-8083-cda695df8443.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/10cd5be5-af84-4f04-88b1-aeb431ec4c09.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/10f3f1fb-8ec5-449e-8c1b-fc21e9a1f226.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/173ff1bd-5ec6-453d-833d-e05cc408c24c.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/18576144-88f4-4a10-83b3-38f7d0f23125.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/195235f4-4e53-411c-990e-72aae31f3619.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/1a1fe85a-9214-4dff-8b2b-600f2296d716.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/1a43c591-d8b4-4afd-936a-d631b48d8141.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/1bfc403d-0ca4-4050-8961-0c48d2b3e2bc.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/1e16f9b7-5016-4320-896a-4d2b91b9f540.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/208c5bd2-ee3a-4665-8a06-18b56716e7d0.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/2374081d-79b8-45aa-b85e-d245a66dca27.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/24a27897-97b4-49c5-99a4-2e0d7558d7a5.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/24f1a0f5-3cc3-41a9-9ecf-6faed5f0e297.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/293c662c-a001-4655-9e81-d6d5d1e03bb0.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/29cc3cab-942b-4594-bddc-eab9b3a5db65.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/2a39f25e-1caa-4785-9af7-85b9fa755b15.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/2acb69f6-4d9f-43d8-aa6d-3d04199bf1e1.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/2ea2a548-a2c9-4477-9f52-a457bdcfb471.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/312eb38b-0085-4190-959b-50c81d72a090.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/331f3ed0-0316-459f-9a00-d7b698a773b1.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/3335c99e-47e9-4c17-9b49-2dcf594fe361.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/33b739f6-50f0-4110-9f52-2b05047c446c.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/33e97118-2b01-499c-ac75-f03817efa7e4.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/344e2ee3-df87-44f9-9e2e-2ed7d59c9b18.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/351b2e33-8001-4e79-8df8-f8fe3f01056b.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/35291adf-e1d8-4785-934c-2ad6472c4f9d.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/363b7ba3-f180-44e6-b3e2-1a91d8f4f35a.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/379b8cdf-33b1-4fa1-8435-a4257392af29.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/37c1100f-9ec9-408b-b020-9e00c5198511.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/3865ce8d-c891-4d6b-9f2f-b91146523e5d.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/38b7e821-da9c-42e7-8f5d-371cafdc7bb7.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/396b991c-47fd-4528-a1e4-84adf31eaf81.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/3a210ac2-8a5a-4306-8196-c211da5a8935.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/3b4465b9-15be-42a2-aff5-b75c81cf7316.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/3de86433-da4f-4a42-ad15-5008cff0cc41.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/3ea3d150-e60e-4dcc-9853-8575e703e348.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/41dc7fd2-4b22-4d40-8af0-ba49ab6683a9.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/42276298-0058-44bb-bf0e-6bbd53fd3c1f.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/422e3dc7-9df1-4c6b-9b6f-ae3d56eb96e0.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/44331353-f727-4a61-a5f2-b4466c9e015f.root",
                                "/store/data/Run2023D/EphemeralZeroBias4/RAW/v1/000/369/870/00000/44e4cfe9-4d18-4ead-8308-0ec90a99268b.root",
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

process.schedule = cms.Schedule()

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '130X_dataRun3_Prompt_v4', '')

process.raw2digi_step = cms.Path(process.RawToDigi)
process.schedule.append(process.raw2digi_step)

# Automatic addition of the customisation function from L1Trigger.Configuration.customiseReEmul
from L1Trigger.Configuration.customiseReEmul import L1TReEmulFromRAW

#call to customisation function L1TReEmulFromRAW imported from L1Trigger.Configuration.customiseReEmul
process = L1TReEmulFromRAW(process)

process.load('L1Trigger.L1TCaloLayer1.L1TCaloSummaryCICADAv1p1')
process.load('L1Trigger.L1TCaloLayer1.L1TCaloSummaryCICADAv2p1')
process.load('anomalyDetection.anomalyTriggerSkunkworks.HLT.cicadaFilter_cfi')
process.productionTask = cms.Task(
    process.L1TCaloSummaryCICADAv1,
    process.L1TCaloSummaryCICADAv2,
)
process.CICADAPath = cms.Path(process.cicadaFilter, process.productionTask)
process.schedule.append(process.CICADAPath)


process.skimOutput = cms.OutputModule(
    'PoolOutputModule',
    fileName = cms.untracked.string(options.outputFile),
    outputCommands=cms.untracked.vstring(
        "drop *",
        "keep *_*_*_HLT",
        "keep *_*_*_LHC"
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('CICADAPath')
    )
)

process.skimStep = cms.EndPath(
    process.skimOutput
)
process.schedule.append(process.skimStep)

print("schedule:")
print(process.schedule)
print("schedule contents:")
print([x for x in process.schedule])
