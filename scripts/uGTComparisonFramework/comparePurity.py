import argparse
from samples.dataSamples import runASample, runBSample, runCSample, runDSample
from tqdm import trange, tqdm
import math
import ROOT
import re
from triggers.unPrescaledTriggers import *
from anomalyTriggerThresholds.thresholdHelper import thresholdHelper

def createOverlapFractionDict(triggerCounts, triggerOverlaps):
    overlapFractionDict = {}
    for triggerGroup in triggerOverlaps:
        try:
            overlapFractionDict[triggerGroup] = float(triggerOverlaps[triggerGroup])/float(triggerCounts)
        except ZeroDivisionError:
            overlapFractionDict[triggerGroup] = 0.0
    return overlapFractionDict

def anomalyTriggerGroupFires(theThresholdHelper, runSample, anomalyTriggerGroup):
    triggerGroupFires = False
    if 'CICADA' in anomalyTriggerGroup[0]:
        trigger = 'CICADA'
        varToCheck = runSample.chain.anomalyScore
    elif 'uGT' in anomalyTriggerGroup[0]:
        trigger = 'uGT'
        varToCheck = runSample.chain.uGTAnomalyScore
    rateString = re.search('[0-9]+(p[0-9]+)?', anomalyTriggerGroup[0]).group(0)
    rate = rateString.replace('p', '.').replace('.0', '')
    threshold = theThresholdHelper.getTriggerThreshold(trigger,rate)

    triggerGroupFires = (varToCheck >= threshold)
    
    return triggerGroupFires

def triggerGroupFires(runSample, triggerGroup):
    triggerGroupFires = False

    for trigger in triggerGroup:
        try:
            fired = getattr(runSample.chain, trigger)
            if fired:
                triggerGroupFires = True
                break
        except:
            pass

    return triggerGroupFires

def main(args):
    ROOT.gStyle.SetOptStat(0)
    runs = {
        'RunA': runASample,
        'RunB': runBSample,
        'RunC': runCSample,
        'RunD': runDSample,
    }
    theThresholdHelper = thresholdHelper()

    triggerGroups = {
        'CICADA3kHz' : ['CICADA3kHz'],
        'CICADA2kHz' : ['CICADA2kHz'],
        'CICADA1kHz' : ['CICADA1kHz'],
        'CICADA0p5kHz' : ['CICADA0p5kHz'],
        'uGT3kHz' : ['uGT3kHz'],
        'uGT2kHz' : ['uGT2kHz'],
        'uGT1kHz' : ['uGT1kHz'],
        'uGT0p5kHz' : ['uGT0p5kHz'],
        'pureMuonTriggers': pureMuonTriggers,
        'muonPlusEGTriggers': muonPlusEGTriggers,
        'muonPlusJetMETOrHT': muonPlusJetMETOrHT,
        'pureEGTriggers': pureEGTriggers,
        'EGPlusHTOrJet': EGPlusHTOrJet,
        'tauPlusOthers': tauPlusOthers,
        'pureTauTriggers': pureTauTriggers,
        'jetsPlusHTTriggers': jetsPlusHTTriggers,
        'HTETorMETTriggers': HTETorMETTriggers,
    }

    triggerCounts = {}
    triggerOverlaps = {}
    triggerAnyOverlaps = {}

    print('Setting up count and overlap maps...')
    for triggerGroup in triggerGroups:
        triggerCounts[triggerGroup] = 0
        triggerOverlaps[triggerGroup] = {}
        if 'CICADA' in triggerGroup or 'uGT' in triggerGroup:
            triggerAnyOverlaps[triggerGroup] = 0
        for differentTriggerGroup in triggerGroups:
            if differentTriggerGroup == triggerGroup:
                continue
            triggerOverlaps[triggerGroup][differentTriggerGroup] = 0

    print('Looping runs...')
    for runName in runs:
        runSample = runs[runName]
        #print(f'{runName} entries...')
        chainSize = runSample.GetEntries()
        argumentEvents = 0.0
        if args.events < 0:
            argumentEvents = chainSize
        else:
            argumentEvents = args.events
        entriesToProcess = int(min(chainSize, argumentEvents))
        #entriesToProcess = runSample.GetEntries()
        #entriesToProcess = int(25e3)
        #entriesToProcess = 100
        for i in trange(entriesToProcess):
            runSample.GetEntry(i)

            for triggerGroup in triggerGroups:
                if 'CICADA' in triggerGroup or 'uGT' in triggerGroup:
                    anyOverlap = False
                    if anomalyTriggerGroupFires(theThresholdHelper, runSample, triggerGroups[triggerGroup]):
                        triggerCounts[triggerGroup] += 1
                        for differentTriggerGroup in triggerGroups:
                            if differentTriggerGroup == triggerGroup:
                                continue
                            if 'CICADA' in differentTriggerGroup or 'uGT' in differentTriggerGroup:
                                if anomalyTriggerGroupFires(theThresholdHelper, runSample, triggerGroups[differentTriggerGroup]):
                                    triggerOverlaps[triggerGroup][differentTriggerGroup] += 1
                            else:
                                if triggerGroupFires(runSample, triggerGroups[differentTriggerGroup]):
                                    triggerOverlaps[triggerGroup][differentTriggerGroup] += 1 
                                    anyOverlap = True
                        if anyOverlap:
                            triggerAnyOverlaps[triggerGroup] += 1          
                else:
                    if triggerGroupFires(runSample, triggerGroups[triggerGroup]):
                        triggerCounts[triggerGroup] += 1
                        for differentTriggerGroup in triggerGroups:
                            if differentTriggerGroup == triggerGroup:
                                continue
                            if 'CICADA' in differentTriggerGroup or 'uGT' in differentTriggerGroup:
                                if anomalyTriggerGroupFires(theThresholdHelper, runSample, triggerGroups[differentTriggerGroup]):
                                    triggerOverlaps[triggerGroup][differentTriggerGroup] += 1
                            else:
                                if triggerGroupFires(runSample, triggerGroups[differentTriggerGroup]):
                                    triggerOverlaps[triggerGroup][differentTriggerGroup] += 1   
    #let's just double check at this point that whatever we have makes sense
    # for triggerGroup in triggerCounts:
    #     print(f'{triggerGroup}: {triggerCounts[triggerGroup]}')
    # print(triggerCounts)
    # print(triggerOverlaps)
    #How do we represent this information that we have gotten?
    axisLabels = {
        'CICADA3kHz' : 'CICADA (3 kHz)',
        'CICADA2kHz' : 'CICADA (2 kHz)',
        'CICADA1kHz' : 'CICADA (1 kHz)',
        'CICADA0p5kHz' : 'CICADA (0.5 kHz)',
        'uGT3kHz' : 'uGT AD (3 kHz)',
        'uGT2kHz' : 'uGT AD (2 kHz)',
        'uGT1kHz' : 'uGT AD (1 kHz)',
        'uGT0p5kHz' : 'uGT AD (0.5 kHz)',
        'pureMuonTriggers': 'Pure Muon Triggers (~9 kHz)',
        'muonPlusEGTriggers': 'Muon + EG Triggers (~2.5 kHz)',
        'muonPlusJetMETOrHT': 'Muon+Jet/MET/HT Triggers (~1.5 kHz)',
        'pureEGTriggers': 'Pure EG Triggers (~15 kHz)',
        'EGPlusHTOrJet': 'EG+HT/Jet Triggers (~6 kHz)',
        'tauPlusOthers': 'Tau Plus Other Triggers (5 kHz)',
        'pureTauTriggers': 'Pure Tau Triggers (~7 kHz)',
        'jetsPlusHTTriggers': 'Jets(+HT) Triggers (~4 kHz)',
        'HTETorMETTriggers': 'HT/ET/MET Triggers (~2 kHz)',
    }
    
    plotSetup = {}
    for triggerGroup in axisLabels:
        plotSetup[triggerGroup] = {}
        currentBin = 1
        for differentTriggerGroup in axisLabels:
            if differentTriggerGroup==triggerGroup:
                continue
            plotSetup[triggerGroup][differentTriggerGroup] = (currentBin, differentTriggerGroup, axisLabels[differentTriggerGroup])
            currentBin += 1

    #Okay. Now we're going to go through each possible trigger group, and create the plots
    overlapPlots = {}
    for triggerGroup in triggerOverlaps:
        theOverlapPlot = ROOT.TH1F(
            f'{triggerGroup}',
            f'{triggerGroup}',
            len(triggerOverlaps.keys())-1,
            0.0,
            float(len(triggerOverlaps.keys())-1)
        )
        theCountPlot = ROOT.TH1F(
            f'{triggerGroup}Counts',
            f'{triggerGroup}Counts',
            len(triggerOverlaps.keys())-1,
            0.0,
            float(len(triggerOverlaps.keys())-1)
        )
        for differentTriggerGroup in plotSetup[triggerGroup]:
            groupTuple = plotSetup[triggerGroup][differentTriggerGroup]
            theOverlapPlot.Fill(groupTuple[2], triggerOverlaps[triggerGroup][groupTuple[1]])
            theCountPlot.Fill(groupTuple[2],triggerCounts[triggerGroup])
        theOverlapPlot.Divide(theCountPlot)
        overlapPlots[triggerGroup] = theOverlapPlot

    #make the any overlap plot
    theOverlapPlot = ROOT.TH1F(
        'anyOverlap',
        'anyOverlap',
        len(triggerAnyOverlaps.keys()),
        0.0,
        float(len(triggerAnyOverlaps.keys()))
    )
    countPlot = ROOT.TH1F(
        'counts',
        'counts',
        len(triggerAnyOverlaps.keys()),
        0.0,
        float(len(triggerAnyOverlaps.keys()))
    )
    for triggerGroup in triggerAnyOverlaps:
        theOverlapPlot.Fill(axisLabels[triggerGroup], triggerAnyOverlaps[triggerGroup])
        countPlot.Fill(axisLabels[triggerGroup],triggerCounts[triggerGroup])
    theOverlapPlot.Divide(countPlot)
    #We're done here. Write things out, and we can draw/style this in another script
    theFile = ROOT.TFile(args.theFile, 'RECREATE')
    for triggerGroup in overlapPlots:
        overlapPlots[triggerGroup].Write()
    theOverlapPlot.Write()
    theFile.Write()
    theFile.Close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Create plots used for purity comparison drawing')

    parser.add_argument('--theFile', default='purityFile.root', nargs='?', help='Output plot file')
    parser.add_argument('--events', type=float, default=1.5e6, nargs='?', help='Maximum number of events to consider (as a float). Defaults to all events in a particular chain' )

    args = parser.parse_args()

    main(args)