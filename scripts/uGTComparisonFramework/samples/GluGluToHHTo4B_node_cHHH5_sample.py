from .sample import sample
import os

hdfsPath = '/hdfs/store/user/aloeliger/uGTComparisons/GluGluToHHTo4B_node_cHHH5/'

GluGluHTo4B_cHHH5_sample = sample([hdfsPath + x for x in os.listdir(hdfsPath)])