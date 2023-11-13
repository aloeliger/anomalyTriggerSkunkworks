from CRABClient.UserUtilities import config
import os
import datetime

config = config()
todaysDate = datetime.date.today().strftime('%d%b%Y')

config.General.requestName = f'CICADASkimNtuplization_2023RunD_ZB_{todaysDate}'
config.General.workArea = 'crabWorkArea'
config.General.transferOutputs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = f'{os.environ["CMSSW_BASE"]}/src/anomalyDetection/anomalyTriggerSkunkworks/python/newFrameworkNtuplization/ntuplizeSkim_2023_DATA.py'
config.JobType.maxMemoryMB = 4000
cicadaPath = f'{os.environ["CMSSW_BASE"]}/src/anomalyDetection/CICADA'
if os.path.isdir(cicadaPath):
    config.JobType.inputFiles=[cicadaPath]

config.Data.inputDataset = '/ZeroBias/Run2023D-PromptReco-v1/MINIAOD'
config.Data.secondaryInputDataset = '/ZeroBias/Run2023D-v1/RAW'
config.Data.inputDBS = 'global'
config.Data.splitting = 'Automatic'
# config.Data.unitsPerJob = 240
# config.Data.lumiMask = 'https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions18/13TeV/Legacy_2018/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt'
config.Data.publication = False
config.Data.outputDatasetTag = f'CICADASkimNtuplization_2023RunD_ZB_{todaysDate}'

config.Site.storageSite = 'T2_US_Wisconsin'