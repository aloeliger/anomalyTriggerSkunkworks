import CRABClient
from CRABClient.UserUtilities import config
import os

config = config()

config.General.requestName = 'CICADA_EphemeralZeroBias3_Feb2023'
config.General.workArea = 'crabWorkArea'
config.General.transferOutputs = True

config.JobType.pluginname = 'Analysis'
config.JobType.psetName = f'{os.environ["CMSSW_BASE"]}/src/L1Trigger/anomalyTriggerSkunkworks/python/emulateCompleteL1_withMini_cff.py'
config.JobType.maxMemoryMB = 4000

config.Data.inputDataset = '/EphemeralZeroBias3/Run2018D-PromptReco-v2/MINIAOD'
config.Data.secondaryInputDataset = '/EphemeralZeroBias3/Run2018D-v1/RAW'
config.Data.inputDBS = 'global'
config.Data.splitting = 'Automatic'
config.Data.lumiMask = 'https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions18/13TeV/Legacy_2018/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.txt'
config.Data.publication = False
config.Data.outputDatasetTag = 'CICADA_EphemeralZeroBias3_Feb2023'

config.Site.storageSite = 'T2_US_Wisconsin'