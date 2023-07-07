from CRABClient.UserUtilities import config
import os
import datetime

config = config()
todaysDate = datetime.date.today().strftime('%d%b%Y')

config.General.requestName = f'CICADA_2022_H2LongLived_{todaysDate}'
config.General.workArea = 'crabWorkArea'
config.General.transferOutputs = True

config.JobType.pluginname = 'Analysis'
config.JobType.psetName = f'{os.environ["CMSSW_BASE"]}/src/anomalyDetection/anomalyTriggerSkunkworks/python/newFrameworkNtuplization/ntuplizeMiniRaw_2022_MC.py'
config.JobType.maxMemoryMB = 4000
cicadaPath = f'{os.environ["CMSSW_BASE"]}/src/anomalyDetection/CICADA'
if os.path.isdir(cicadaPath):
    config.JobType.inputFiles=[cicadaPath]

config.Data.inputDataset = '/HTo2LongLivedTo4b_MH-125_MFF-50_CTau-3000mm_TuneCP5_13p6TeV_pythia8/Run3Summer22MiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM'
config.Data.secondaryInputDataset = '/HTo2LongLivedTo4b_MH-125_MFF-50_CTau-3000mm_TuneCP5_13p6TeV_pythia8/Run3Summer22DRPremix-124X_mcRun3_2022_realistic_v12-v2/GEN-SIM-RAW'
config.Data.inputDBS = 'global'
config.Data.splitting = 'Automatic'
config.Data.unitsPerJob = 240
# config.Data.lumiMask = 'https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions18/13TeV/Legacy_2018/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt'
config.Data.publication = False
config.Data.outputDatasetTag = f'CICADA_2022_H2LongLived_{todaysDate}'

config.Site.storageSite = 'T2_US_Wisconsin'
