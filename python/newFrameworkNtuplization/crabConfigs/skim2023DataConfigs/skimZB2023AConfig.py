from CRABClient.UserUtilities import config
import os
import datetime

config = config()
todaysDate = datetime.date.today().strftime('%d%b%Y')

config.General.requestName = f'CICADASkim_2023RunA_ZB_{todaysDate}'
config.General.workArea = 'crabWorkArea'
config.General.transferOutputs = True

config.JobType.pluginname = 'Analysis'
config.JobType.psetName = f'{os.environ["CMSSW_BASE"]}/src/anomalyDetection/anomalyTriggerSkunkworks/python/newFrameworkNtuplization/skim2023.py'
config.JobType.maxMemoryMB = 4000

config.Data.inputDataset = '/ZeroBias/Run2023A-PromptReco-v1/MINIAOD'
config.Data.secondaryInputDataset = '/ZeroBias/Run2023A-v1/RAW'
config.Data.inputDBS = 'global'
config.Data.splitting = 'Automatic'
config.Data.totalUnits = 300000
config.Data.publication = False
config.Data.outputDatasetTag = f'CICADASkim_2023RunA_ZB_{todaysDate}'

config.Site.storageSite = 'T2_US_Wisconsin'