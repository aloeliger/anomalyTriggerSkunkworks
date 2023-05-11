from .sample import sample
import os

hdfsPath = '/hdfs/store/user/aloeliger/uGTComparisons/v_2/GluGlutoHHto4B_kl-0p00_kt-1p00_c2-0p00/'
GluGluToHHto4B_lowSample = sample([hdfsPath + x for x in os.listdir(hdfsPath)])