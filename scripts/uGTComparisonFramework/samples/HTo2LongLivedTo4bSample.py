from .sample import sample
import os

hdfsPath = '/hdfs/store/user/aloeliger/uGTComparisons/v_2/HTo2LongLivedTo4b/'

HTo2LongLivedTo4bSample = sample([hdfsPath+x for x in os.listdir(hdfsPath)])