from CRABClient.UserUtilities import config
import os
import datetime

config = config()
todaysDate = datetime.date.today().strftime('%d%b%Y')

config.General.requestName = f'CICADA_2022EZB5_{todaysDate}'
config.General.workArea = 'crabWorkArea'
config.General.transferOutputs = True

config.JobType.pluginname = 'Analysis'
config.JobType.psetName = f'{os.environ["CMSSW_BASE"]}/src/anomalyDetection/anomalyTriggerSkunkworks/python/newFrameworkNtuplization/ntuplizeMiniRaw_2022_DATA.py'
config.JobType.maxMemoryMB = 4000
cicadaPath = f'{os.environ["CMSSW_BASE"]}/src/anomalyDetection/CICADA'
if os.path.isdir(cicadaPath):
    config.JobType.inputFiles=[cicadaPath]

config.Data.inputDataset = '/EphemeralZeroBias5/Run2022G-PromptReco-v1/MINIAOD'
config.Data.secondaryInputDataset = '/EphemeralZeroBias5/Run2022G-v1/RAW'
config.Data.inputDBS = 'global'
config.Data.splitting = 'Automatic'
config.Data.unitsPerJob = 240
# config.Data.lumiMask = 'https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions18/13TeV/Legacy_2018/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt'
config.Data.publication = False
config.Data.outputDatasetTag = f'CICADA_2022EphemeralZeroBias5_{todaysDate}'

config.Site.storageSite = 'T2_US_Wisconsin'
