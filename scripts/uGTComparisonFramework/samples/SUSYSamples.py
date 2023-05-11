from .sample import sample
import os

hdfsPath = '/hdfs/store/user/aloeliger/uGTComparisons/v_2/SUSYGluGluToBBHToBB_NarrowWidth_M-120/'

SusyGluGluToBBHToBBSample = sample([hdfsPath+x for x in os.listdir(hdfsPath)])