# !/usr/bin/env python3
import ROOT
from anomalyDetection.anomalyTriggerSkunkworks.samples.EphemeralZeroBias import EphemeralZeroBiasSample
import argparse
import numpy as np
import time
import math
from tqdm import tqdm, trange

def createPlotForThreshold(theDataframe, run, rate, threshold, lumis):
    thresholdDF = theDataframe.Filter(f'anomalyScore >= {threshold}')

    maxLumi = lumis[len(lumis)-1]
    minLumi = lumis[0]
    nLumis = maxLumi-minLumi

    # print(nLumis)
    # print(minLumi)
    # print(maxLumi)

    dummyVersusLumiModel = ROOT.RDF.TH1DModel(
        f'{run}_{rate}_eventsPerLumi',
        f'{run}_{rate}_eventsPerLumi',
        int(nLumis),
        float(minLumi),
        float(maxLumi+1),
    )

    theHist = thresholdDF.Histo1D(
        dummyVersusLumiModel,
        'lumi',
    )
    return theHist


def createLumiCountPlot(theDataframe, run, rateThresholds):
    runDataframe = theDataframe.Filter(f'run == {run}')
    lumiCol = runDataframe.AsNumpy(['lumi'])['lumi']
    uniqueLumis = np.unique(lumiCol)
    uniqueLumis = list(uniqueLumis)
    uniqueLumis.sort()

    hists = []
    # print(f'Creating plots for run {run}...')
    # startTime = time.perf_counter()
    for rateThreshold in rateThresholds:
        hists.append(
            createPlotForThreshold(
                runDataframe,
                run,
                rateThreshold,
                rateThresholds[rateThreshold],
                uniqueLumis
            )
        )
    # endTime = time.perf_counter()
    # print(f'Done in {endTime-startTime:.2f} seconds')
    return hists


def main(args):
    outputFile = ROOT.TFile(f'/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/perLumiRatePlotsCICADAv{args.CICADAVersion}.root','RECREATE')
    theDataframe = EphemeralZeroBiasSample.getNewDataframe(
        [
            f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
        ]
    )

    if args.CICADAVersion == 1:
        rateThresholds = {
            'ZeroBias': 0.0,
            '5kHz': 5.783,
            '3kHz': 5.895,
            '2kHz': 5.988,
            '1kHz': 6.221,
            '0p5kHz': 6.520,
        }
    elif args.CICADAVersion == 2:
        rateThresholds = {
            'ZeroBias': 0.0,
            '5kHz': 10.630,
            '3kHz': 11.336,
            '2kHz': 11.953,
            '1kHz': 13.365,
            '0p5kHz': 15.570,
        }

    # print(theDataframe.GetColumnNames())
    print('Getting unique runs...')
    startTime = time.perf_counter()
    runCol = theDataframe.AsNumpy(['run'])['run']
    endTime = time.perf_counter()
    print(f'Runs gotten in {endTime-startTime:.2f} seconds')
    # print(runCol)
    uniqueRuns = np.unique(runCol)
    print(uniqueRuns)
    uniqueRuns = list(uniqueRuns)

    # Dummy column for summing?
    # theDataframe.Define('counter',"1")

    hists = []
    for run in tqdm(uniqueRuns, leave=False, desc="Booking Hists"):
        hists+= createLumiCountPlot(
                theDataframe,
                run,
                rateThresholds,
            )
    
    for hist in tqdm(hists,desc="writing hists", leave=False):
        hist.Write()
    outputFile.Write()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Create stability rate plots for CICADA versions")
    parser.add_argument(
        '-v',
        '--CICADAVersion',
        default=1,
        type=int,
        help='Version to pull the ntuplizer from',
        choices=[1,2],
        nargs='?',
    )

    args = parser.parse_args()

    main(args)  