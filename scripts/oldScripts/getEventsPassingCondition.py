#!/usr/bin/env python3

import ROOT
import argparse
import os
import random

def main(args):
    
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

    caloSummaryChain.AddFriend(upgradeChain)
    caloSummaryChain.AddFriend(l1BitsChain)

    newTree = caloSummaryChain.CopyTree(args.selections)

    print('-'*52)
    print('|{:^16s}|{:^16s}|{:^16s}|'.format('Run', 'Lumi', 'Evt'))
    print('-'*52)
    for i in range(newTree.GetEntries()):
        newTree.GetEntry(i)
        print('|{:^16}|{:^16}|{:^16}|'.format(newTree.run, newTree.lumi, newTree.evt))
        print('-'*52)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Print Run, Luminosity, and Event No of events passing certain conditions')
    parser.add_argument('--selections',
                        nargs='?',
                        default='',
                        help='Selections for events')
    parser.add_argument('--fractionToAccept',
                        nargs='?',
                        default=0.01,
                        type=float,
                        help='Fraction of files to use. Using all files can cause incredibly long file read times')

    args = parser.parse_args()

    main(args)
