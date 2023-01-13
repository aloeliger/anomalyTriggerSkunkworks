from .sample import sample
import os

SUEPPath = '/hdfs/store/user/aloeliger/anomalyTriggerMCSubmission/SUEP_HLT/'

suepSample = sample([SUEPPath+x for x in os.listdir(SUEPPath)])