#!/usr/bin/env python3

import ROOT
import argparse
import os
from tqdm import trange
import random
import re

def printOverallStats(theTree, totalEvents, allSelectionTriggers, args):
    anomalyTriggers = theTree.GetEntries(f'anomalyScore > {args.anomalyThreshold}')
    anomalyTriggerPercentage = anomalyTriggers/totalEvents

    allSelectionPercentage = allSelectionTriggers/totalEvents
    allOverAnomaly = allSelectionTriggers/anomalyTriggers
    #call it 50 characters wide
    #totalEvents = theTree.GetEntries()
    print('-'*50)
    print('|{:^23s}||{:^23}|'.format('Entries',theTree.GetEntries()))
    print('-'*75)
    print('|{:^23s}||{:^23}||{:^23.10%}|'.format('Anomaly Triggers', anomalyTriggers, anomalyTriggerPercentage))
    print('-'*100)
    #selectionString = f'anomalyScore > {args.anomalyThreshold}'
    #if args.otherSelections != '':
    #    selectionString += f' && {args.otherSelections}'
    #allSelectionTriggers = theTree.GetEntries(selectionString)
    print('|{:^23s}||{:^23}||{:^23.10%}||{:^23.10%}|'.format('All Selections', allSelectionTriggers, allSelectionPercentage, allOverAnomaly))
    print('-'*125)

def printOverlapInformation(theTree, L1Bit, totalEvents, allSelectionTriggers, args):
    selectionString = f'anomalyScore > {args.anomalyThreshold}'
    if args.otherSelections != '':
        selectionString += f' && {args.otherSelections}'
    
    #print('-'*75)
    L1BitAccepts = theTree.GetEntries(f'{L1Bit} > 0')
    overlapEvents = theTree.GetEntries(selectionString+' && '+f'{L1Bit} > 0')

    print('|{:^73s}||{:^23}||{:^23.10%}|'.format(L1Bit, L1BitAccepts, L1BitAccepts/totalEvents))
    print('-'*125)
    print('|{:^73s}||{:^23}||{:^23.10%}|'.format('Overlap', overlapEvents, overlapEvents/allSelectionTriggers))
    print('-'*125)

def main(args):
    #let's get the files and make the three we want to see
    
    ROOT.gROOT.SetBatch(True)
    
    caloSummaryChain = ROOT.TChain('L1TCaloSummaryTestNtuplizer/L1TCaloSummaryOutput')
    upgradeChain = ROOT.TChain('l1UpgradeEmuTree/L1UpgradeTree')
    l1BitsChain = ROOT.TChain('L1TTriggerBitsNtuplizer/L1TTriggerBits')

    filePath = '/hdfs/store/user/aloeliger/L1TriggerBitTest/allv5/'

    random.seed(1234)

    for name in os.listdir(filePath):
        accept = random.random()
        if accept <= args.fractionToAccept:
            caloSummaryChain.Add(filePath+name)
            upgradeChain.Add(filePath+name)
            l1BitsChain.Add(filePath+name)
        
    #We should get all the names of the bits being stored here.
    names = [x.GetName() for x in list(l1BitsChain.GetListOfBranches()) if 'L1' in x.GetName()]
    
    caloSummaryChain.AddFriend(upgradeChain)
    caloSummaryChain.AddFriend(l1BitsChain)

    totalEvents = caloSummaryChain.GetEntries()
    
    selectionString = f'anomalyScore > {args.anomalyThreshold}'
    if args.otherSelections != '':
        selectionString += f' && {args.otherSelections}'
    allSelectionTriggers = caloSummaryChain.GetEntries(selectionString)

    printOverallStats(caloSummaryChain, totalEvents, allSelectionTriggers, args)
    print('|{:^123}|'.format('Anomaly Overlaps With L1'))
    print('-'*125)

    for name in names:
        if not re.search(args.overlapRE, name):
            continue
        printOverlapInformation(caloSummaryChain, name, totalEvents, allSelectionTriggers, args)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Examine the overlap of specified Anomaly Thresholds versus L1 trigger Bits')
    parser.add_argument('--anomalyThreshold',
                        required=True,
                        nargs='?',
                        help='threshold to simulate an anomaly trigger firing')
    parser.add_argument('--otherSelections',
                        nargs='?',
                        default='',
                        help='Other selections for regions of the anomaly trigger to check')
    parser.add_argument('--fractionToAccept',
                        nargs='?',
                        default=0.01,
                        type=float,
                        help='Fraction of files to use. Using all files can cause incredibly long file read times')
    parser.add_argument('--overlapRE',
                        nargs='?',
                        default='.*',
                        help='regular expression to for L1 bit names to check overlap against. Defaults to all bits')

    args = parser.parse_args()

    main(args)
