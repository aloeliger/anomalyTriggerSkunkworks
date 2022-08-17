import FWCore.ParameterSet.Config as cms
import re
import json

process = cms.Process("L1TCaloSummaryTest")

from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing()
options.register('numEvents',10000, VarParsing.multiplicity.singleton, VarParsing.varType.int, 'Number of Events to Process')
options.register('loadFile','', VarParsing.multiplicity.singleton, VarParsing.varType.string, 'JSON file to take a list of files from')
options.register('campaignRE','.*',VarParsing.multiplicity.singleton, VarParsing.varType.string, 'Regular expression to define which campaigns to pull from')
options.register('datasetRE','.*',VarParsing.multiplicity.singleton, VarParsing.varType.string, 'Regular expression to define which datasets to pull from')
options.register('outputFile', 'ntuplize.root', VarParsing.multiplicity.singleton, VarParsing.varType.string, 'File to store results in')

options.parseArguments()

#load the input file and prepare a 
with open(options.loadFile) as jsonInputFile:
    jsonFileList = json.load(jsonInputFile)

try:
    campaignPattern = re.compile(options.campaignRE)
except Exception as err:
    print('failed to generate campaign RE')
    print(err)
    exit(1)

try:
    datasetPattern = re.compile(options.datasetRE)
except Exception as err:
    print('failed to generate dataset RE')
    print(err)
    exit(1)

finalFileList = []

for campaign in jsonFileList:
    if not campaignPattern.search(campaign):
        continue
    for dataset in jsonFileList[campaign]:
        if not datasetPattern.search(dataset):
            continue
        for fileName in jsonFileList[campaign][dataset]:
            finalFileList.append(fileName)
finalFileList = tuple(finalFileList)

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

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.numEvents) )

process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
                                finalFileList
                            ),
                            skipBadFiles=cms.untracked.bool(True),
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
	fileName = cms.string(options.outputFile)
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

