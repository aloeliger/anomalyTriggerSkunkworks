from .sample import sample
import os

hdfsPath = '/hdfs/store/user/aloeliger/uGTComparisons/GluGluToHHTo4B_node_cHHH1/'

GluGluHTo4B_cHHH1_sample = sample([hdfsPath + x for x in os.listdir(hdfsPath)])