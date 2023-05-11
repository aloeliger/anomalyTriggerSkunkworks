from .sample import sample
import os

hdfsPath = '/hdfs/store/user/aloeliger/uGTComparisons/v_2/GluGlutoHHto4B_kl-1p00_kt-1p00_c2-3p00/'
GluGluToHHto4B_highSample = sample([hdfsPath + x for x in os.listdir(hdfsPath)])