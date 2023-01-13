from .sample import sample
import os

hdfsPath = '/hdfs/store/user/aloeliger/uGTComparisons/'
runAPath = hdfsPath+'RunA/'
runBPath = hdfsPath+'RunB/'
runCPath = hdfsPath+'RunC/'
runDPath = hdfsPath+'RunD/'

runASample = sample([runAPath+'/'+ x for x in os.listdir(runAPath)])
runBSample = sample([runBPath+'/'+ x for x in os.listdir(runBPath)])
runCSample = sample([runCPath+'/'+ x for x in os.listdir(runCPath)])
runDSample = sample([runDPath+'/'+ x for x in os.listdir(runDPath)])