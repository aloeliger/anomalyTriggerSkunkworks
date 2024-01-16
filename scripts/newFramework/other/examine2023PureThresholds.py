# !/usr/bin/env python3

import ROOT
import numpy as np
import argparse
from collections import OrderedDict

from anomalyDetection.anomalyTriggerSkunkworks.utilities.decorators import cache

from rich.console import Console, Group
from rich.text import Text
from rich.panel import Panel
from rich.traceback import install

install()

# from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.largeRunDEphemeralZeroBias import largeRunDEphemeralZeroBiasSample
# from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.RunD import RunDSample
# from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.allSmallZeroBias import allSmallZeroBiasSample
from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.RunDEphemeralZeroBias0 import RunDEphemeralZeroBias0Sample
# from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.RunAComplete import RunASample
from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.RunBComplete import RunBSample
from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.RunCComplete import RunCSample
from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.RunDComplete import RunDSample

from anomalyDetection.anomalyTriggerSkunkworks.plotSettings.utilities import convertEffToRate
from anomalyDetection.anomalyTriggerSkunkworks.triggerInfo.unprescaledTriggerBits import unprescaledBits2023

from anomalyDetection.anomalyTriggerSkunkworks.utilities.removeTraining import removeTrainingTool

def noUnprescaledBitPassesCondition(unprescaledBits):
    noPassCondition = ''
    for bit in unprescaledBits:
        noPassCondition += f'{bit} == 0 && '
    noPassCondition = noPassCondition[:-3]
    return noPassCondition

def getMaxAndMinScore(theFrame, ADScoreName='anomalyScore'):
    return theFrame.Max(ADScoreName).GetValue(), theFrame.Min(ADScoreName).GetValue()

def getPureRateForPoint(theFrame, theThreshold, unprescaledBits, menuName, anomalyScoreName = 'anomalyScore'):
    totalCount = theFrame.Count()

    unprescaledBitList = unprescaledBits[menuName]
    unprescaledBitList = [
        bit for category in unprescaledBitList for bit in unprescaledBitList[category]
    ]

    filterFrame = theFrame.Filter(noUnprescaledBitPassesCondition(unprescaledBitList) + f' && {anomalyScoreName} >= {theThreshold}')
    filterCount = filterFrame.Count()

    eff = filterCount.GetValue() / totalCount.GetValue()
    rate = convertEffToRate(eff)
    return rate

def getThresholdForRate(theFrame, theRate, minScore, maxScore, unprescaledBits, menuName, iterations=100, epsilonPercent=1e-2, anomalyScoreName = 'anomalyScore'):
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
        
        testRate = getPureRateForPoint(theFrame, testThreshold, unprescaledBits=unprescaledBits, menuName=menuName, anomalyScoreName = anomalyScoreName)
    return testThreshold

console = Console()

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

samples = {
    'RunDEZB': RunDEphemeralZeroBias0Sample.getNewDataframe(
        [
            f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
            'L1TTriggerBitsNtuplizer/L1TTriggerBits',
            'uGTModelNtuplizer/uGTModelOutput',
        ]
    ),
    # 'RunA': RunASample.getNewDataframe(
    #     [
    #         f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
    #         'L1TTriggerBitsNtuplizer/L1TTriggerBits',
    #         'uGTModelNtuplizer/uGTModelOutput',
    #     ]
    # ),
    'RunB': RunBSample.getNewDataframe(
        [
            f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
            'L1TTriggerBitsNtuplizer/L1TTriggerBits',
            'uGTModelNtuplizer/uGTModelOutput',
        ]
    ),
    'RunC': RunCSample.getNewDataframe(
        [
            f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
            'L1TTriggerBitsNtuplizer/L1TTriggerBits',
            'uGTModelNtuplizer/uGTModelOutput',
        ]
    ),
    'RunD': RunDSample.getNewDataframe(
        [
            f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
            'L1TTriggerBitsNtuplizer/L1TTriggerBits',
            'uGTModelNtuplizer/uGTModelOutput',
        ]
    ),
}

theTrainingRemovalTool = removeTrainingTool()

for sampleName in samples:
    theSample = samples[sampleName]
    console.rule(sampleName)

    console.log('Removing training...')
    theSample = theTrainingRemovalTool.removeTrainingDataFromDataframe(theSample)

    console.log('Determining menus...')
    possibleMenus = theSample.AsNumpy(['menuName'])['menuName']
    # possibleMenus = np.unique(possibleMenus)
    # console.print(possibleMenus)
    uniqueMenus = []
    console.log('Making uniques...')
    for menu in possibleMenus:
        if menu not in uniqueMenus:
            uniqueMenus.append(str(menu))
    console.print(uniqueMenus)

    console.log('Determining max and min')
    scoreMax, scoreMin = getMaxAndMinScore(theSample)

    rates = OrderedDict([
        ('10 kHz', 10.0),
        ('5 kHz', 5.0),
        ('3 kHz', 3.0),
        ('2 kHz', 2.0),
        ('1 kHz', 1.0),
        ('0p5 kHz', 0.5),]
    )

    console.log('Processing menus...')
    for menu in uniqueMenus:
        # console.log(f'Processing menu: {menu}')
        menuSample = theSample.Filter(f'menuName == "{menu}"')
        thresholds = {}
        thresholdText = []
        # console.log(f'Determining thresholds')
        for rateString in rates:
            # console.log(f'{rateString}')
            thresholds[rateString] = getThresholdForRate(
                menuSample,
                rates[rateString],
                scoreMin,
                scoreMax,
                unprescaledBits=unprescaledBits2023,
                menuName=menu,
            )
            thresholdText.append(
                Text(f'{rateString}: {thresholds[rateString]:.3f}')
            )
        console.log(f'Printing...')
        textGroup = Group(*thresholdText)
        textPanel = Panel(
            textGroup,
            title=menu
        )
        console.print(textPanel)
    console.print('')