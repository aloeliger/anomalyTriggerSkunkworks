import ROOT
from prettytable import PrettyTable
import argparse
from collections import OrderedDict

from anomalyDetection.anomalyTriggerSkunkworks.plotSettings.utilities import getListOfUniqueEntries, convertEffToRate
from tqdm import trange

from HighEffSingleRunPureRatePlot import *

def smoothRates(listOfRates:list[float], smoothingPeriod:int):
    smoothedRates = []
    for i in range(len(listOfRates)):
        lowIndex = max(0,i-smoothingPeriod+1)
        smoothValues = listOfRates[lowIndex:i+1]
        smoothedRate = sum(smoothValues)/len(smoothValues)
        smoothedRates.append(smoothedRate)
    return smoothedRates

def main(args):
    #Let's get some files
    overallFile = ROOT.TFile(args.overallFile)
    pureFile = ROOT.TFile(args.overallFile)

    uniqueOverallLumis = getListOfUniqueEntries(overallFile.L1TCaloSummaryOutput, 'lumi')
    uniquePureLumis = getListOfUniqueEntries(pureFile.L1TCaloSummaryOutput, 'lumi')

    uniqueOverallLumis.sort()
    uniquePureLumis.sort()

    if not uniqueOverallLumis == uniquePureLumis:
        onlyInOverall = list (x for x in uniqueOverallLumis if x not in uniquePureLumis)
        onlyInPure = list(x for x in uniquePureLumis if x not in uniqueOverallLumis)

        print("Lumi sections only in the overall tree: ",onlyInOverall)
        print("Lumi sections only in the pure tree: ",onlyInPure)
    
    lumis = list(x for x in uniqueOverallLumis if x in uniquePureLumis)

    overallTree = overallFile.L1TCaloSummaryOutput
    overallTree.AddFriend(overallFile.L1TTriggerBits)
    overallTree.AddFriend(overallFile.boostedJetTrigger)

    pureTree = pureFile.L1TCaloSummaryOutput
    pureTree.AddFriend(pureFile.L1TTriggerBits)
    pureTree.AddFriend(pureFile.boostedJetTrigger)

    #Just a bunch of data to print to screen later
    overallEventsInLumi = []
    pureEventsInLumi = []

    modes = ('overall', 'pure')
    triggers = ('None','AD3', 'AD6', 'AD6p5', 'AD7', 'boosted', 'boostedFlag')
    infoTypes = ('EventsInLumi', 'Eff', 'Rate')
    triggerConditions = {
        'None': '',
        'AD3': ' && anomalyScore > 3.0',
        'AD6': ' && anomalyScore > 6.0',
        'AD6p5': ' && anomalyScore > 6.5',
        'AD7': ' && anomalyScore > 7.0',
        'boosted': ' && jetPts > 120',
        'boostedFlag': ' && triggerFires == 1.0'
    }

    infoLists = OrderedDict()

    pureHigherThanOverall = {}    

    for mode in modes:
        infoLists[mode] = OrderedDict()
        for trigger in triggers:
            infoLists[mode][trigger] = OrderedDict()
            for infoType in infoTypes:
                infoLists[mode][trigger][infoType] = []

    for trigger in triggers:
        pureHigherThanOverall[trigger] = []

    for i in trange(len(lumis), desc="Lumis"):

        for trigger in triggers:
            infoLists['overall'][trigger]['EventsInLumi'].append( overallTree.GetEntries(f'lumi=={lumis[i]} {triggerConditions[trigger]}') )
            infoLists['pure'][trigger]['EventsInLumi'].append( overallTree.GetEntries(f'lumi=={lumis[i]} {triggerConditions[trigger]} && '+noUnprescaledBitPasses()) )
            pureHigherThanOverall[trigger].append( infoLists['pure'][trigger]['EventsInLumi'] > infoLists['pure'][trigger]['EventsInLumi'])
            for mode in modes:
                infoLists[mode][trigger]['Eff'].append( infoLists[mode][trigger]['EventsInLumi'][i]/infoLists[mode]['None']['EventsInLumi'][i] )
                infoLists[mode][trigger]['Rate'].append( convertEffToRate(infoLists[mode][trigger]['Eff'][i]) )

    for trigger in triggers:
        output = PrettyTable()
        print(f'\n{trigger:}\n')
        output.field_names = ['Lumi', 'Overall Events', 'Pure Events', 'Overall Eff', 'Pure Eff', 'Overall Rate', 'Pure Rate', 'Pure > Overall?', 'Smoothed Overall Rate', 'Smoothed Pure Rate', 'Smoothed Pure > Overall?']
        
        pureSmoothRates = smoothRates(infoLists['pure'][trigger]['Rate'], args.smoothedPeriod)
        overallSmoothRates = smoothRates(infoLists['overall'][trigger]['Rate'], args.smoothedPeriod)

        for i in range(len(lumis)):
            output.add_row(
                [
                    lumis[i],
                    infoLists['overall'][trigger]['EventsInLumi'][i],
                    infoLists['pure'][trigger]['EventsInLumi'][i],
                    infoLists['overall'][trigger]['Eff'][i],
                    infoLists['pure'][trigger]['Eff'][i],
                    infoLists['overall'][trigger]['Rate'][i],
                    infoLists['pure'][trigger]['Rate'][i],
                    '\u001b[31m'+str(pureHigherThanOverall[trigger][i])+'\u001b[0m' if pureHigherThanOverall[trigger][i] else '\u001b[32m'+str(pureHigherThanOverall[trigger][i])+'\u001b[0m',
                    overallSmoothRates[i],
                    pureSmoothRates[i],
                    '\u001b[31mTrue\u001b[0m' if pureSmoothRates[i] > overallSmoothRates[i] else '\u001b[32mFalse\u001b[0m'
                ]
            )
        print(output)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Check the issue with pure rates out doing overall rates")
    parser.add_argument(
        '--overallFile',
        nargs='?',
        required=True,
        help='ROOT file containing information for the overall rates'
    )
    parser.add_argument(
        '--pureFile',
        nargs='?',
        required = True,
        help='ROOT file containing information about the pure rates'
    )
    parser.add_argument(
        '--smoothedPeriod',
        nargs='?',
        required = True,
        type=int,
        help='NUmber of iterations to smooth the rate over'
    )

    args = parser.parse_args()

    main(args)