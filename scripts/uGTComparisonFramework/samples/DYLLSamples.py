from .sample import sample
import os

hdfsPath = '/hdfs/store/user/aloeliger/uGTComparisons/v_2/DYTo2L_MLL-4to50/'

DYLLSample = sample([hdfsPath+x for x in os.listdir(hdfsPath)])