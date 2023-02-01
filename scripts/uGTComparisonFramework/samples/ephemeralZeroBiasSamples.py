from .sample import sample
import os

hdfsPath = '/hdfs/store/user/aloeliger/L1TriggerBitTest/allv7/'

ephemeralZeroBiasSample = sample([hdfsPath+'/'+x for x in os.listdir(hdfsPath)])
#ephemeralZeroBiasSample = sample([hdfsPath+'/'+x for x in os.listdir(hdfsPath)][:10])