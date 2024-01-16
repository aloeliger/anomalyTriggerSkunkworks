# !/usr/bin/env python3

import ROOT
import argparse
import os
from anomalyDetection.anomalyTriggerSkunkworks.utilities.decorators import cache

from rich.console import Console
from rich.traceback import install

from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.RunDEphemeralZeroBias0 import RunDEphemeralZeroBias0Sample

from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.Hto2LongLivedTo4b import Hto2LongLivedTo4bSample
from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.SUSYGluGlutoBBHtoBB import SUSYGluGlutoBBHtoBBSample
from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.TT import TTSample
from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.VBFHto2C import VBFHto2CSample
from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.SUEP import SUEPSample

install()
console = Console()

def getFrameMinMax(backgroundFrame, signalFrame, variable):
    backgroundMin = backgroundFrame.Min(variable)
    signalMin = signalFrame.Min(variable)

    backgroundMax = backgroundFrame.Max(variable)
    signalMax = signalFrame.Max(variable)

    overallMax = max(
        backgroundMax.GetValue(),
        signalMax.GetValue()
    )

    overallMin = min(
        backgroundMin.GetValue(),
        signalMin.GetValue()
    )

    return overallMin, overallMax

@cache
def getEffsForPoint(signalSample, backgroundSample, variable, threshold):
    totalBackgroundCount = backgroundSample.Count()
    totalSignalCount = signalSample.Count()

    bfFrame = backgroundSample.Filter(f'{variable} >= {threshold}')
    sfFrame = signalSample.Filter(f'{variable} >= {threshold}')

    bfCount = bfFrame.Count()
    # sfCount = sfFrame.Count()
    sfCount = sfFrame.Sum('pileupWeight')

    backgroundEff = bfCount.GetValue() / totalBackgroundCount.GetValue()
    signalEff = sfCount.GetValue() / totalSignalCount.GetValue()

    return (backgroundEff, signalEff)

@cache
def getSignalEffForBackgroundEff(eff, signalSample, backgroundSample, rocVariable, variableMax, variableMin, iterations=100, epsilonPercent = 1e-2):
    threshold = variableMin
    testEff = 1.0
    effPair = (1.0, 1.0)

    lowerBound = variableMin
    upperBound = variableMax

    for i in range(iterations):
        # check if we're close enough
        if abs(testEff-eff) < epsilonPercent*eff:
            break
        # if the test eff is less than the required eff, then we hav ecut too high, and need to relax the cut
        if testEff < eff:
            upperBound = threshold
            threshold = (lowerBound+threshold)/2
        # if the test eff is greater than the required eff, then we need to tighten the cut
        else:
            lowerBound = threshold
            threshold = (upperBound+threshold)/2
        effPair = getEffsForPoint(signalSample, backgroundSample, rocVariable, threshold)
        testEff = effPair[0]
    
    return effPair

def createROCData(signalSample, backgroundSample, desiredEffs, rocVariable):
    # get variable min/max
    variableMin, variableMax = getFrameMinMax(backgroundSample, signalSample, variable=rocVariable)
    effPoints = []

    for eff in desiredEffs:
        effPoints.append(
            getSignalEffForBackgroundEff(
                eff,
                signalSample,
                backgroundSample,
                rocVariable,
                variableMax,
                variableMin
            )
        )

    return effPoints
    
def makeROCCurveFromData(effPoints, nameTitle):
    nPoints = len(effPoints)
    rocGraph = ROOT.TGraph(nPoints)
    for i, point in enumerate(effPoints):
        rocGraph.SetPoint(i, point[0], point[1])
    rocGraph.SetNameTitle(
        nameTitle,
        nameTitle,
    )
    return rocGraph


def main(args):
    destinationPath = '/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/'
    if not os.path.isdir(destinationPath):
        os.makedires(destinationPath, exist_ok=True)

    backgroundDataframe = RunDEphemeralZeroBias0Sample.getNewDataframe(
        [
            f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
            'caloStage2EtSumNtuplizer/L1CaloEtSumInformation', #the sum will be the sum with type == 1
        ]
    )

    signalDataframes = {
        'Hto2LongLivedTo4b': Hto2LongLivedTo4bSample.getNewDataframe(
            [
                f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
                'caloStage2EtSumNtuplizer/L1CaloEtSumInformation', #the sum will be the sum with type == 1
                'pileupWeightDirectory/pileupWeightTree',
            ]
        ),
        'SUSYGluGlutoBBHtoBB': SUSYGluGlutoBBHtoBBSample.getNewDataframe(
            [
                f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
                'caloStage2EtSumNtuplizer/L1CaloEtSumInformation', #the sum will be the sum with type == 1
                'pileupWeightDirectory/pileupWeightTree',
            ]
        ),
        'TT': TTSample.getNewDataframe(
            [
                f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
                'caloStage2EtSumNtuplizer/L1CaloEtSumInformation', #the sum will be the sum with type == 1
                'pileupWeightDirectory/pileupWeightTree',
            ]
        ),
        'VBFHto2C': VBFHto2CSample.getNewDataframe(
            [
                f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
                'caloStage2EtSumNtuplizer/L1CaloEtSumInformation', #the sum will be the sum with type == 1
                'pileupWeightDirectory/pileupWeightTree',
            ]
        ),
        'SUEP': SUEPSample.getNewDataframe(
            [
                f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
                'caloStage2EtSumNtuplizer/L1CaloEtSumInformation', #the sum will be the sum with type == 1
                'pileupWeightDirectory/pileupWeightTree',
            ]
        ),
    }

    freqEffsSpread = [i*((1e-3-1e-5)/100.0)+1e-5 for i in range(101)]

    with console.status(status='Figuring out effs',spinner='bouncingBall'):
        # make the HT more readily available
        console.log('Booking HT Derivation...')
        HTDerivationFunction =             """
            for(int i = 0; i < typeVector.size(); ++i){
                if(typeVector.at(i) == 1){
                    return ptVector.at(i);
                }
            }
            return 0.0;
            """
        backgroundDataframe = backgroundDataframe.Define(
            "HT",
            HTDerivationFunction
        )
        for sample in signalDataframes:
            signalDataframes[sample] = signalDataframes[sample].Define(
                "HT",
                HTDerivationFunction
            )
        


        console.log('Looping over samples for roc points...')
        graphs = []
        for sample in signalDataframes:
            theSample = signalDataframes[sample]
            console.log(f'{sample}...')

            # figure out the ROC data for CICADA

            CICADARocPoints = createROCData(theSample, backgroundDataframe, freqEffsSpread, rocVariable = 'anomalyScore')
            CICADARocGraph = makeROCCurveFromData(
                CICADARocPoints,
                f'{sample}_CICADA_ROC'
            )

            graphs.append(CICADARocGraph)
            # figure out the ROC data for HT thresholds

            HTRocPoints = createROCData(theSample, backgroundDataframe, freqEffsSpread, rocVariable = 'HT')
            HTRocGraph = makeROCCurveFromData(
                HTRocPoints,
                f'{sample}_HT_ROC'
            )
            
            graphs.append(HTRocGraph)

    outputFile = ROOT.TFile(f'{destinationPath}/ROCAndHTCICADAv{args.CICADAVersion}.root', 'RECREATE')
    for graph in graphs:
        graph.Write()
    outputFile.Write()
    outputFile.Close()

    console.log('Done!', style='bold green')

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