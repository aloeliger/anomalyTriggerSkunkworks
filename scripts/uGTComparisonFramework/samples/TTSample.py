from .sample import sample
import os

hdfsPath = '/hdfs/store/user/aloeliger/uGTComparisons/v_2/TT/'

ttSample = sample([hdfsPath + x for x in os.listdir(hdfsPath)])