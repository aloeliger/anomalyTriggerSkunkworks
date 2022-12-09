#!/usr/bin/env python3

import ROOT
import argparse
import random
import os
from tqdm import trange

def main(args):
    ROOT.gROOT.SetBatch(True)

    filePath = '/hdfs/store/user/aloeliger/L1TriggerBitTest/allv6/'
    
    caloSummaryChain = ROOT.TChain('L1TCaloSummaryTestNtuplizer/L1TCaloSummaryOutput')
    upgradeChain = ROOT.TChain('l1UpgradeEmuTree/L1UpgradeTree')
    eventChain = ROOT.TChain('l1EventTree/L1EventTree')
    boostedTriggerChain = ROOT.TChain('boostedJetTriggerNtuplizer/boostedJetTrigger')

    random.seed(1234)
    for name in os.listdir(filePath):
        accept = random.random()
        if accept <= args.fractionToAccept:
            caloSummaryChain.Add(filePath+name)
            upgradeChain.Add(filePath+name)
            eventChain.Add(filePath+name)
            boostedTriggerChain.Add(filePath+name)
            
    caloSummaryChain.AddFriend(upgradeChain)
    caloSummaryChain.AddFriend(eventChain)
    caloSummaryChain.AddFriend(boostedTriggerChain)

    #Okay, what we need is a list of variables we want to do correlations with
    #to start out with, we can just do the number of objects in the event to test
    listOfVars = [
        'nEGs',
        'nTaus',
        'nJets',
        'nMuons',
    ]
    varBoundaries = {
        'nEGs': (12, 0.0, 13.0),
        'nTaus': (12, 0.0, 13.0),
        'nJets': (12, 0.0, 13.0),
        'nMuons': (12, 0.0, 13.0),
    }
    histograms = {}
    for var in listOfVars:
        histograms[var] = ROOT.TH2F(
            f'{var}Correlation',
            f'{var}Correlation',
            varBoundaries[var][0],
            varBoundaries[var][1],
            varBoundaries[var][2],
            20,
            0.0,
            7.0,
        )
    #for some of these, there doesn't exist a good way to do them...
    #We just have to do it by hand
    objects = ('eg', 'tau', 'jet', 'muon')
    maxEtHistograms = {}
    minEtHistograms = {}
    avgEtHistograms = {}
    for obj in objects:
        maxEtHistograms[obj] = ROOT.TH2F(
            f'{obj}MaxEtCorrelation',
            f'{obj}MaxEtCorrelation',
            40,
            0.0,
            80.0,
            20,
            0.0,
            7.0
        )
        minEtHistograms[obj] = ROOT.TH2F(
            f'{obj}MinEtCorrelation',
            f'{obj}MinEtCorrelation',
            40,
            0.0,
            80.0,
            20,
            0.0,
            7.0
        )
        avgEtHistograms[obj] = ROOT.TH2F(
            f'{obj}AvgEtCorrelation',
            f'{obj}AvgEtCorrelation',
            40,
            0.0,
            80.0,
            20,
            0.0,
            7.0
        )
    PUHistogram = ROOT.TH2F(
        'PUCorrelation',
        'PUCorrelation',
        50,
        0.0,
        100.0,
        20,
        0.0,
        7.0
    )
    maxBoostedJetPtHistogram = ROOT.TH2F(
        'maxBoostedJetPtCorrelation',
        'maxBoostedJetPtCorrelation',
        50,
        0.0,
        200.0,
        20,
        0.0,
        7.0,
    )
    minBoostedJetPtHistogram = ROOT.TH2F(
        'minBoostedJetPtCorrelation',
        'minBoostedJetPtCorrelation',
        50,
        0.0,
        200.0,
        20,
        0.0,
        7.0,
    )
    avgBoostedJetPtHistogram = ROOT.TH2F(
        'avgBoostedJetPtCorrelation',
        'avgBoostedJetPtCorrelation',
        50,
        0.0,
        200.0,
        20,
        0.0,
        7.0,
    )
    nBoostedJetsHistogram = ROOT.TH2F(
        'nBoostedJetCorrelation',
        'nBoostedJetCorrelation',
        13,
        0.0,
        13.0,
        20,
        0.0,
        7.0,
    )
    for i in trange(caloSummaryChain.GetEntries(), desc='Filling Plots'):
        caloSummaryChain.GetEntry(i)
        for var in listOfVars:
            histograms[var].Fill(getattr(caloSummaryChain.L1Upgrade, var), caloSummaryChain.anomalyScore)
        for obj in objects:
            numName = f'n{obj[0].upper()}{obj[1:]}s' if obj != 'eg' else f'nEGs'
            numObject = getattr(caloSummaryChain.L1Upgrade, numName)
            if numObject == 0:
                continue
            maxEtHistograms[obj].Fill(getattr(caloSummaryChain.L1Upgrade, f'{obj}Et')[0], caloSummaryChain.anomalyScore)
            minEtHistograms[obj].Fill(getattr(caloSummaryChain.L1Upgrade, f'{obj}Et')[numObject-1], caloSummaryChain.anomalyScore)
            avgPt = 0.0
            for j in range(numObject):
                avgPt += getattr(caloSummaryChain.L1Upgrade, f'{obj}Et')[j] / numObject
            avgEtHistograms[obj].Fill(avgPt, caloSummaryChain.anomalyScore)
        PUHistogram.Fill(caloSummaryChain.Event.nPV, caloSummaryChain.anomalyScore)
        
        nBoostedJetsHistogram.Fill(caloSummaryChain.numberOfJets, caloSummaryChain.anomalyScore)
        if caloSummaryChain.numberOfJets != 0:
            maxBoostedJetPtHistogram.Fill(max(caloSummaryChain.jetPts), caloSummaryChain.anomalyScore)
            minBoostedJetPtHistogram.Fill(min(caloSummaryChain.jetPts), caloSummaryChain.anomalyScore)
            avgBoostedJetPtHistogram.Fill(sum(caloSummaryChain.jetPts)/caloSummaryChain.numberOfJets, caloSummaryChain.anomalyScore)
        
    theFile = ROOT.TFile('correlationOutput.root', 'RECREATE')
    for key in histograms:
        histograms[key].Write()
    for dictionary in (maxEtHistograms, minEtHistograms, avgEtHistograms):
        for key in dictionary:
            dictionary[key].Write()
    PUHistogram.Write()
    maxBoostedJetPtHistogram.Write()
    minBoostedJetPtHistogram.Write()
    avgBoostedJetPtHistogram.Write()
    nBoostedJetsHistogram.Write()

    theFile.Write()
    theFile.Close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='script for checking the correlation of anomalyScore against L1 variables')
    parser.add_argument(
        '--fractionToAccept',
        nargs='?',
        default=0.01,
        type=float,
        help='Fraction of files to use. Using all files can cause very long file load times'
    )
    
    args = parser.parse_args()

    main(args)
