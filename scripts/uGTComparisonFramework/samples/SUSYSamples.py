from .sample import sample
import os

hdfsPath = '/hdfs/store/user/aloeliger/uGTComparisons/SUSYGluGluToBBHToBB_NarrowWidth_M-350/'

SusyGluGluToBBHToBBSample = sample([hdfsPath+x for x in os.listdir(hdfsPath)])