import FWCore.ParameterSet.Config as cms
import subprocess 

from Configuration.Eras.Era_Run2_2018_cff import Run2_2018

import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing ('analysis')
options.parseArguments()

process = cms.Process("L1TCaloSummaryTest", Run2_2018)
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

process.load('L1Trigger.anomalyTriggerSkunkworks.L1TTriggerBitsNtuplizer_cfi')

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.MessageLogger.cerr.FwkReport.reportEvery = 10000

#We're going to get a bit fancy here
#We need to match the input miniAOD up to it's raw counterpart
#but simply doing this exhaustively will load a lot of unnecessary files, and is getting
#jobs held on clusters
#So we're going to look for counterpart files, in place, and load only what is necessary
#for each miniAOD file.
#our first step is figuring out the run, and lumi of the file we're trying to use
#Assumes we run this config one miniAOD file at a time
print("***************************************")
theInputFile = str(options.inputFiles[0])
print('Input file: ', theInputFile)
runDASCommand=  ['dasgoclient --query="run file=%s"' % theInputFile]
print(runDASCommand)
lumiDASCommand = ['dasgoclient --query="lumi file=%s"' % theInputFile]
print(lumiDASCommand)
runProcess = subprocess.Popen(runDASCommand,
                              stdout = subprocess.PIPE,
                              stderr = subprocess.PIPE,
                              shell=True)
lumiProcess = subprocess.Popen(lumiDASCommand,
                               stdout = subprocess.PIPE,
                               stderr = subprocess.PIPE,
                               shell=True)
runOut, runErr = runProcess.communicate()
lumiOut, lumiErr = lumiProcess.communicate()

runCode = runProcess.wait()
if runCode != 0:
    raise RuntimeError("Failed to find the proper run for the given MiniAOD file!")
lumiCode = lumiProcess.wait()
if lumiCode != 0:
    raise RuntimeError("Failed to find the proper lumi for the given MiniAOD file!")

runOut = runOut.decode().strip()#we probably only have one run, this should work for now
lumiOut= lumiOut.decode().strip().split('\n') #we will likely have a list of lumis

print(runOut)
print(lumiOut)

rawFiles = []
for lumi in lumiOut:
    rawFileDASCommand = ['dasgoclient --query="file dataset=/EphemeralZeroBias1/Run2018D-v1/RAW run=%s lumi=%s"' % (runOut, lumi)]
    rawProcess = subprocess.Popen(rawFileDASCommand,
                                  stdout = subprocess.PIPE,
                                  stderr = subprocess.PIPE,
                                  shell=True)
    rawOut, rawErr = rawProcess.communicate()
    rawCode = rawProcess.wait()
    if rawCode != 0:
        raise RuntimeError("Could not find appropriate file for the requested MiniAOD")
    
    listOfFiles = rawOut.decode().strip().split('\n')
    rawFiles = rawFiles + listOfFiles
    print("Raw files for lumi: ", lumi, ": ",listOfFiles)
print("List of files to go alongside, ",rawFiles)
print("***********************************************")

secondaryFiles = cms.untracked.vstring(tuple(rawFiles))


process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(options.inputFiles),
                            secondaryFileNames = secondaryFiles
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
                     #process.L1TCaloSummaryTestNtuplizer *
                     process.L1TTriggerBitsNtuplizer
)

process.schedule = cms.Schedule(process.p)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)

# Multi-threading
process.options.numberOfThreads=cms.untracked.uint32(1)
process.options.numberOfStreams=cms.untracked.uint32(1)
