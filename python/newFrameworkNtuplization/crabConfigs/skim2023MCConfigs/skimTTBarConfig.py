from CRABClient.UserUtilities import config
import os
import datetime

config = config()
todaysDate = datetime.date.today().strftime('%d%b%Y')

config.General.requestName = f'CICADASkim_2023_TTBar_{todaysDate}'
config.General.workArea = 'crabWorkArea'
config.General.transferOutputs = True

config.JobType.pluginname = 'Analysis'
config.JobType.psetName = f'{os.environ["CMSSW_BASE"]}/src/anomalyDetection/anomalyTriggerSkunkworks/python/newFrameworkNtuplization/skim2023.py'
config.JobType.maxMemoryMB = 4000

config.Data.inputDataset = '/TT_TuneCP5_13p6TeV_powheg-pythia8/Run3Winter23MiniAOD-126X_mcRun3_2023_forPU65_v1-v2/MINIAODSIM'
config.Data.secondaryInputDataset = '/TT_TuneCP5_13p6TeV_powheg-pythia8/Run3Winter23Digi-126X_mcRun3_2023_forPU65_v1-v2/GEN-SIM-RAW'
config.Data.inputDBS = 'global'
config.Data.splitting = 'Automatic'
config.Data.totalUnits = 100000
config.Data.publication = False
config.Data.outputDatasetTag = f'CICADASkim_2023_TTBar_{todaysDate}'

config.Site.storageSite = 'T2_US_Wisconsin'