import ROOT
import os
import math

def makeTreeTuples():
    years = (
        '2018A',
        '2018B',
        '2018C',
        '2018D',
             #'2022A',
             #'2022B',
             #'2022C'
    )
    legendEntries = [
        'ZeroBias 2018A',
        'ZeroBias 2018B',
        'ZeroBias 2018C',
        'ZeroBias 2018D',
    #    'ZeroBias 2022A',
    #    'ZeroBias 2022B',
    #    'ZeroBias 2022C',
    ]
    colors = [
        ROOT.kBlue,
        ROOT.kRed,
        ROOT.kGreen,
        ROOT.kMagenta,
    ]

    location = os.getenv("CMSSW_BASE")+'/src/anomalyDetection/anomalyTriggerSkunkworks/data/pileupNtuples/'

    files = []
    trees = []

    for year in years:
        theFile = ROOT.TFile(location+'l1TNtuple-ZeroBias-'+year+'.root')
        files.append(theFile)
        trees.append(theFile.L1TCaloSummaryTestNtuplizer.L1TCaloSummaryOutput)

    treeTuples = list(zip(years, files, trees, legendEntries, colors))
    return treeTuples
