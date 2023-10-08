# !/usr/bin/env python3

import ROOT
import argparse
import os
import itertools
import math
from anomalyDetection.anomalyTriggerSkunkworks.utilities.decorators import cache

from rich.console import Console
from rich.text import Text
from rich.table import Table
from rich.progress import track
from rich.columns import Columns


from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.RunCEphemeralZeroBias0 import RunCEphemeralZeroBias0Sample
from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.RunDEphemeralZeroBias0 import RunDEphemeralZeroBias0Sample
from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.ZeroBiasPlusRunCEphemeralZeroBias import ZeroBiasPlusRunCEZBSample

from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.Hto2LongLivedTo4b import Hto2LongLivedTo4bSample
from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.SUSYGluGlutoBBHtoBB import SUSYGluGlutoBBHtoBBSample
from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.TT import TTSample
from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.VBFHto2C import VBFHto2CSample
from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.SUEP import SUEPSample


console = Console()

def getFramesMinMax(backgroundFrame, signalFrame):
    overallMin = min(
        backgroundFrame.Min('anomalyScore').GetValue(),
        signalFrame.Min('anomalyScore').GetValue(),
    )
    overallMax = max(
        backgroundFrame.Max('anomalyScore').GetValue(),
        signalFrame.Max('anomalyScore').GetValue()
    )

    return overallMin, overallMax

@cache
def getEffsForPoint(backgroundFrame, signalFrame, threshold):
    totalBackgroundCount = backgroundFrame.Count().GetValue()
    totalSignalCount = signalFrame.Count().GetValue()

    bfFrame = backgroundFrame.Filter(f'anomalyScore >= {threshold}')
    sfFrame = signalFrame.Filter(f'anomalyScore >= {threshold}')

    backgroundEff = bfFrame.Count().GetValue() / totalBackgroundCount
    signalEff = sfFrame.Count().GetValue() / totalSignalCount

    return (backgroundEff, signalEff)

# find the eff pair for a specified background efficiency
# will binary search a number of iterations or until an epsilon is reached
@cache
def getEffsForDesiredBackgroundEff(eff, backgroundFrame, signalFrame, scoreMax, scoreMin, iterations=100, epsilonPercent = 1e-2):
    # console.log(f'eff: {eff}', style='underline cyan')
    testThreshold = scoreMin
    testEff = 1.0
    effPair = (1.0, 1.0)

    lowerBound = scoreMin
    upperBound = scoreMax

    recentEffs = []

    for i in range(iterations):
        # check if we're close enough
        if abs(testEff-eff) < epsilonPercent*eff:
            break
        # if the test eff is less than the required eff, then we have cut too high
        # we need to relax the cut
        # and then not go back above this
        if testEff < eff:
            upperBound = testThreshold
            testThreshold = (lowerBound+testThreshold)/2.0
        # if the test eff is greater the required eff, then we need to tighten the cut
        # Then we need to not go back below this
        else:
            lowerBound = testThreshold
            testThreshold = (upperBound+testThreshold)/2.0
        # update what the eff is at the new test threshold
        effPair = getEffsForPoint(backgroundFrame, signalFrame, testThreshold)
        testEff = effPair[0]

    return effPair
    

def makeROCCurveFromData(effPoints):
    nPoints = len(effPoints)
    rocGraph = ROOT.TGraph(nPoints)
    for i, point in enumerate(effPoints):
        rocGraph.SetPoint(i+1, point[0], point[1])
    return rocGraph
        

def createROCDataFromFrame(backgroundFrame, signalFrame, desiredEffs):
    # First we need to find the max and minimum of our available score
    scoreMin, scoreMax = getFramesMinMax(backgroundFrame, signalFrame)
    effPoints = []

    for eff in track(desiredEffs, description='Making ROC...', transient=True):
        effPoints.append(
            getEffsForDesiredBackgroundEff(
                eff,
                backgroundFrame,
                signalFrame,
                scoreMax,
                scoreMin,
            )
        )

    effTable = Table(title='eff points')
    effTable.add_column('Background', style='bold red')
    effTable.add_column('Signal', style='bold green')
    
    for point in effPoints:
        effTable.add_row(f'{point[0]:.3g}', f'{point[1]:.3g}')
    console.print(effTable, justify='center')

    return effPoints

def main(args):
    destinationPath = '/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/'
    if not os.path.isdir(destinationPath):
        os.makedirs(destinationPath, exist_ok=True)
    outputFile = ROOT.TFile(f'{destinationPath}/rocCurveFileCICADAv{args.CICADAVersion}.root','RECREATE')

    backgroundDataframes = {
        'RunCEphemeralZeroBias': RunCEphemeralZeroBias0Sample.getNewDataframe(
            [
                f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
            ]
        ),
        'RunDEphemeralZeroBias': RunDEphemeralZeroBias0Sample.getNewDataframe(
            [
                f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
            ]
        ),
        'ZeroBiasPlusRunCEphemeralZeroBias': ZeroBiasPlusRunCEZBSample.getNewDataframe(
            [
                f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
            ]
        ),        
    }

    signalDataframes = {
        'Hto2LongLivedTo4b': Hto2LongLivedTo4bSample.getNewDataframe(
            [
                f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
            ]
        ),
        'SUSYGluGlutoBBHtoBB': SUSYGluGlutoBBHtoBBSample.getNewDataframe(
            [
                f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
            ]
        ),
        'TT': TTSample.getNewDataframe(
            [
                f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
            ]
        ),
        'VBFHto2C': VBFHto2CSample.getNewDataframe(
            [
                f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
            ]
        ),
        'SUEP': SUEPSample.getNewDataframe(
            [
                f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
            ]
        ),
    }

    backgroundSignalCombinations = itertools.product(
        list(backgroundDataframes.keys()),
        list(signalDataframes.keys())
    )
    backgroundSignalCombinations = list(backgroundSignalCombinations)

    backgroundEffSpread = {
        'CompleteSpread': [i*(1.0/100.0) for i in range(101)],
        'FreqSpread': [i*((1e-3-1e-5)/100.0)+1e-5 for i in range(101)]
    }

    # print(backgroundSignalCombinations)
    console.rule('ROC Processing')
    for spreadType in backgroundEffSpread:
        console.log(f"{spreadType}", justify='center', style='underline bold white on blue')
        theSpread = backgroundEffSpread[spreadType]
        spreadString = [f'{x:.3g}' for x in theSpread]
        console.print(Columns(spreadString, equal=True, expand=True))
        for backgroundSignalCombination in backgroundSignalCombinations:
            infoText = Text("Processing Pair:", style="bold green")
            backgroundText = Text(backgroundSignalCombination[0], style='underline', justify='left', overflow='ellipsis')
            sampleText = Text(backgroundSignalCombination[1], style='underline', justify='right', overflow='ellipsis')
            console.log(
                infoText,
                backgroundText,
                sampleText,
            )
            effData = createROCDataFromFrame(
                backgroundDataframes[backgroundSignalCombination[0]],
                signalDataframes[backgroundSignalCombination[1]],
                theSpread,
            )

            rocGraph = makeROCCurveFromData(effData)

            nameTitle = f'{backgroundSignalCombination[0]}_{backgroundSignalCombination[1]}_{spreadType}_ROC'
            rocGraph.SetNameTitle(
                nameTitle,
                nameTitle
            )

            rocGraph.Write()
    console.rule("Done ROC Processing")
    console.print('')
    console.print('')

    outputFile.Write()
    outputFile.Close()
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create ROC curve plots for a series of possible signal/background scenarios')
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