from CRABClient.UserUtilities import config
import os
import datetime

config = config()
todaysDate = datetime.date.today().strftime('%d%b%Y')

config.General.requestName = f'CICADASkim_2023_HToLongLivedTo4b_{todaysDate}'
config.General.workArea = 'crabWorkArea'
config.General.transferOutputs = True

config.JobType.pluginname = 'Analysis'
config.JobType.psetName = f'{os.environ["CMSSW_BASE"]}/src/anomalyDetection/anomalyTriggerSkunkworks/python/newFrameworkNtuplization/skim2023.py'
config.JobType.maxMemoryMB = 4000

config.Data.inputDataset = '/Hto2LongLivedto4b_MH-125_MFF-25_CTau-1500mm_TuneCP5_13p6TeV_pythia8/Run3Winter23MiniAOD-RnD_126X_mcRun3_2023_forPU65_v1-v2/MINIAODSIM'
config.Data.secondaryInputDataset = '/Hto2LongLivedto4b_MH-125_MFF-25_CTau-1500mm_TuneCP5_13p6TeV_pythia8/Run3Winter23Digi-RnD_126X_mcRun3_2023_forPU65_v1-v2/GEN-SIM-RAW'
config.Data.inputDBS = 'global'
config.Data.splitting = 'Automatic'
config.Data.totalUnits = 40000 #max of the whole dataset
config.Data.publication = False
config.Data.outputDatasetTag = f'CICADASkim_2023_HToLongLivedTo4b_{todaysDate}'

config.Site.storageSite = 'T2_US_Wisconsin'