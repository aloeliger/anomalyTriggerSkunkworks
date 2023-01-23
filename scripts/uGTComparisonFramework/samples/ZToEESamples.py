from .sample import sample
import os

hdfsPath = '/hdfs/store/user/aloeliger/uGTComparisons/ZToEE/'

ZToEESample = sample([hdfsPath+x for x in os.listdir(hdfsPath)])