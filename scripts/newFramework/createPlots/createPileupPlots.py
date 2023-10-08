# !/usr/bin/env python3

import ROOT
import argparse
import os
import time

import numpy as np
import math

from rich.console import Console

from anomalyDetection.anomalyTriggerSkunkworks.plotSettings.utilities import convertEffToRate
from anomalyDetection.anomalyTriggerSkunkworks.utilities.decorators import cache
from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.largeRunDEphemeralZeroBias import largeRunDEphemeralZeroBiasSample
from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.RunDEphemeralZeroBias0 import RunDEphemeralZeroBias0Sample

from multiprocessing import Queue, Pool

console = Console()

def getMaxAndMinScore(theFrame, ADScoreName='anomalyScore'):
    return theFrame.Max(ADScoreName).GetValue(), theFrame.Min(ADScoreName).GetValue()

@cache
def getRateForPoint(theFrame, theThreshold, anomalyScoreName = 'anomalyScore'):
    totalCount = theFrame.Count()

    filterFrame = theFrame.Filter(f'{anomalyScoreName} >= {theThreshold}')
    filterCount = filterFrame.Count()

    eff = filterCount.GetValue() / totalCount.GetValue()
    rate = convertEffToRate(eff)
    return rate

def getThresholdForRate(theFrame, theRate, minScore, maxScore, iterations=100, epsilonPercent=1e-2, anomalyScoreName = 'anomalyScore'):
    testThreshold = minScore
    testRate = 40e3

    lowerBound = minScore
    upperBound = maxScore

    for i in range(iterations):
        # If we're close enough, we're done
        if abs(testRate-theRate) < epsilonPercent*theRate:
            break
        
        # If we're below the rate, we need to loosen the cut
        # and then not go back above this
        if testRate < theRate:
            upperBound = testThreshold
            testThreshold = (lowerBound+testThreshold)/2.0
        # If we're above the rate then we need to tighten the cut
        # and then not go back below this
        else:
            lowerBound = testThreshold
            testThreshold = (upperBound+testThreshold)/2.0
        
        testRate = getRateForPoint(theFrame, testThreshold, anomalyScoreName = anomalyScoreName)
    return testThreshold

def getAverageRateForPUBin(theFrame, theThreshold, lowPU, highPU):
    PUFrame = theFrame.Filter(f"npv >= {lowPU}").Filter(f"npv < {highPU}")
    anomalyFrame = PUFrame.Filter(f"anomalyScore >= {theThreshold}")

    nEvents = anomalyFrame.Count().GetValue()
    totalEvents = PUFrame.Count().GetValue()

    eff =  nEvents / totalEvents
    rate = convertEffToRate(eff)

    error = math.sqrt(nEvents) / totalEvents
    error = convertEffToRate(error)

    return rate, error

def getListOfRunLumiPairs(theFrame):
    runLumiPairs = []

    runCol = theFrame.AsNumpy(['run'])['run']
    uniqueRuns = np.unique(runCol)
    uniqueRuns = list(uniqueRuns)

    for run in uniqueRuns:
        lumiFrame = theFrame.Filter(f'run == {run}')
        lumiCol = lumiFrame.AsNumpy(['lumi'])['lumi']
        uniqueLumis = np.unique(lumiCol)
        uniqueLumis = list(uniqueLumis)
        for lumi in uniqueLumis:
            runLumiPairs.append(
                (run, lumi,)
            )
    return runLumiPairs

def getCICADAMuRate(theFrame, run, lumi, threshold):
    runLumiFrame = theFrame.Filter(f'run == {run}').Filter(f'lumi == {lumi}')
    thresholdFrame = runLumiFrame.Filter(f'anomalyScore >= {threshold}')
    singleMuFrame = runLumiFrame.Filter(f'L1_SingleMu22 == 1.0')

    cicadaEff = thresholdFrame.Count().GetValue() / runLumiFrame.Count().GetValue()
    cicadaRate = convertEffToRate(cicadaEff)

    singleMuEff = singleMuFrame.Count().GetValue() / runLumiFrame.Count().GetValue()
    singleMuRate = convertEffToRate(singleMuEff)

    return cicadaRate, singleMuRate

# Okay, the single mu versus CICADA rate for a large dataset is taking forever,
# so the idea is going to be to farm out the run lumi pairs to a function
# and each one will put 
resultsPackage = Queue()
def multiprocessingCICADAMuRateHandle(run, lumi, threshold):
    # make a process based copy of the dataframe for thread safety
    start_time = time.perf_counter()
    processSample = largeRunDEphemeralZeroBiasSample.getNewDataframe(
        [
            f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
            'L1TTriggerBitsNtuplizer/L1TTriggerBits',
        ]        
    )
    # Filter it down,
    runLumiFrame = processSample.Filter(f'run == {run} && lumi == {lumi}')
    thresholdFrame = runLumiFrame.Filter(f'anomalyScore >= {threshold}')
    singleMuFrame = runLumiFrame.Filter(f'L1_SingleMu22 == 1.0')

    cicadaEff = thresholdFrame.Count().GetValue() / runLumiFrame.Count().GetValue()
    cicadaRate = convertEffToRate(cicadaEff)

    singleMuEff = singleMuFrame.Count().GetValue() / runLumiFrame.Count().GetValue()
    singleMuRate = convertEffToRate(singleMuEff)

    end_time = time.perf_counter()

    # console.print(cicadaRate, singleMuRate, f'In {end_time-start_time:.3f} seconds')

    resultsPackage.put(
        (cicadaRate, singleMuRate)
    )

def main(args):
    
    destinationPath = '/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/'
    if not os.path.isdir(destinationPath):
        os.makedirs(destinationPath, exist_ok=True)
    outputFile = ROOT.TFile(f'{destinationPath}/pileupPlotsCICADAv{args.CICADAVersion}.root', 'RECREATE')

    theSample = largeRunDEphemeralZeroBiasSample.getNewDataframe(
        [
            f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
            'L1TTriggerBitsNtuplizer/L1TTriggerBits',
        ]
    )
    # theSample = RunDEphemeralZeroBias0Sample.getNewDataframe(
    #         [
    #             f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
    #             'L1TTriggerBitsNtuplizer/L1TTriggerBits',
    #         ]
    # )

    # rates in kHz we want thresholds for
    desiredRates = [
        1,
        2,
        3,
        5,
        10,
    ]

    # Figure out the max and min score
    # DONE
    with console.status('Finding max and min score...'):
        maxScore, minScore = getMaxAndMinScore(theSample)
    console.log('Max and min score: Done', style='bold green')

    # Figure out where our thresholds are for given rates
    # DONE
    rateThresholds = {}
    with console.status('Finding rate thresholds...'):
        for rate in desiredRates:
            rateThresholds[rate] = getThresholdForRate(theSample, rate, minScore, maxScore)
    # console.log(rateThresholds)
    console.log('Rate thresholds: Done', style='bold green')

    # make the simplistic graph
    # DONE
    with console.status('Making simple score vertex plots...'):
        scorePUGraph = theSample.Graph(
            'npv',
            'anomalyScore'
        )
    console.log('Simple score vertex plots: Done', style='bold green')

    # I can't quite pull off what AXOL1TL did
    # instead we'll make an average rate for a given number of primary vertices
    # we'll pick a threshold, find all events with given PU, count the total and threshold passing events
    # And infer a rate from that, and plot it
    # DONE
    PUBins = [(30+(x)*5, 30+(x+1)*5) for x in range(10)]
    PURateGraphs = {}
    with console.status('Making average rate versus PU plots...'):
        for avRate in rateThresholds:

            thePURateGraph = ROOT.TGraphErrors(len(PUBins))
            nameTitle = f'PURateGraph_{avRate}'
            thePURateGraph.SetNameTitle(nameTitle,nameTitle)
            theThreshold = rateThresholds[avRate]

            for index, PUBin in enumerate(PUBins):
                cicadaRate, error = getAverageRateForPUBin(theSample, theThreshold, PUBin[0], PUBin[1])
                thePURateGraph.SetPoint(
                    index,
                    (PUBin[0]+PUBin[1])/2.0,
                    cicadaRate
                )
                thePURateGraph.SetPointError(
                    index,
                    0.0,
                    error
                )
            PURateGraphs[avRate]=thePURateGraph
    # console.log(PURateGraphs)
    console.log('average rate versus PU plots: Done', style='bold green')

    # This is a tricky one. We'll likely have to split our data up into run+lumi bites
    # Then for each, calculate a rate for a series of thresholds
    # And look at the single mu eff/rate for that
    # DONE

    CICADAvsSingleMuGraphs = {}
    with console.status('Making CICADA rate versus single mu rate...'):
        # Get a list of run lumi pairs
        runLumiPairs = getListOfRunLumiPairs(theSample)
        for rate in rateThresholds:

            workPackage = [
                [run, lumi, rateThresholds[rate]] for run, lumi in runLumiPairs
            ]
            console.log(f'There are {len(workPackage)} items in the work package')

            # console.print('Work package:')
            # console.print(workPackage)

            theCICADAvsSingleMuGraph = ROOT.TGraph(len(runLumiPairs))
            nameTitle = f'CICADAvsSingleMu_{rate}'
            theCICADAvsSingleMuGraph.SetNameTitle(nameTitle, nameTitle)

            console.log(f'Starting multiprocessing pool for rate: {rate} ...', style='bold green')
            try:
                thePool = Pool(10)
                thePool.starmap(multiprocessingCICADAMuRateHandle, workPackage)
                thePool.close()
            except:
                thePool.terminate()
            finally:
                thePool.join()
                console.log(f'Finalized multiprocessing pool for rate: {rate} ...', style='bold green')

            index = 0
            while not resultsPackage.empty():
                cicadaRate, singleMuRate = resultsPackage.get()
                theCICADAvsSingleMuGraph.SetPoint(
                    index,
                    singleMuRate,
                    cicadaRate
                )
                index+=1
            # theThreshold = rateThresholds[rate]

            # for index, runLumi in enumerate(runLumiPairs):
            #     run, lumi = runLumi[0], runLumi[1]
            #     cicadaRate, singleMuRate = getCICADAMuRate(
            #         theSample,
            #         run,
            #         lumi,
            #         theThreshold,
            #     )

            #     theCICADAvsSingleMuGraph.SetPoint(
            #         index,
            #         singleMuRate,
            #         cicadaRate,
            #     )
            CICADAvsSingleMuGraphs[rate] = theCICADAvsSingleMuGraph

    console.log('CICADA rate versus single mu rate: Done', style='bold green')

    with console.status('Writing everyhing out...'):
        scorePUGraph.SetNameTitle('scoreVsPU','scoreVsPU')
        scorePUGraph.Write()

        for rate in PURateGraphs:
            PURateGraphs[rate].Write()
        
        for rate in CICADAvsSingleMuGraphs:
            CICADAvsSingleMuGraphs[rate].Write()

        outputFile.Write()
        outputFile.Close()
    console.log('Writing everything out: Done', style='bold green')
    console.print('')
    console.print('')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a series of pileup plots for CICADA')
    parser.add_argument(
        '-v',
        '--CICADAVersion',
        default=1,
        type=int,
        help='CICADA version to pull out of the ntuplizer',
        choices = [1,2],
        nargs='?',
    )

    args = parser.parse_args()

    main(args)