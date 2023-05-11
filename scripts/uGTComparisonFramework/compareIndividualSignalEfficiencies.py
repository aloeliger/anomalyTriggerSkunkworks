import argparse

from samples.SUEPSamples import suepSample
from samples.VBFHToTauTauSample import vbfHToTauTauSample
from samples.HTo2LongLivedTo4bSample import HTo2LongLivedTo4bSample
from samples.TTSample import ttSample
from samples.GluGluToHHTo4B_highSamples import GluGluToHHto4B_highSample
from samples.GluGluToHHTo4B_lowSamples import GluGluToHHto4B_lowSample
from samples.SUSYSamples import SusyGluGluToBBHToBBSample
from samples.DYLLSamples import DYLLSample

from tqdm import tqdm, trange
import ROOT
from triggers.unPrescaledTriggers import *

from anomalyTriggerThresholds.thresholdHelper import thresholdHelper
import re


def getAnomalyTriggerCutString(theThresholdHelper, triggerGroup):
    triggerGroup = triggerGroup[0]
    if 'CICADA' in triggerGroup:
        trigger = 'CICADA'
        variableName = 'anomalyScore'
    elif 'uGT' in triggerGroup:
        trigger = 'uGT'
        variableName = 'uGTAnomalyScore'

    rateString = re.search('[0-9]+(p[0-9]+)?', triggerGroup).group(0)
    rate = rateString.replace('p', '.').replace('.0','')
    threshold = theThresholdHelper.getTriggerThreshold(trigger,rate)

    cutString = f'{variableName} >= {threshold}'
    return cutString

def getTriggerCutString(runSample, triggerGroup):
    cutString = f'{triggerGroup[0]} == 1'
    listOfBranches = [x.GetName() for x in list(runSample.triggerBitsChain.GetListOfBranches())]
    #print(listOfBranches)
    for i in range(1,len(triggerGroup)):
        #We need to consider whether this trigger is truly present in the MC
        #TODO: synchronize MC and data trigger availability
        if triggerGroup[i] in listOfBranches:
            cutString+=f'|| {triggerGroup[i]} == 1'
        else:
            #print(f'Skipping trigger {triggerGroup[i]} in current sample')
            pass
    return cutString

def main(args):
    samples = {
        'SUEP': suepSample,
        'VBFHTT': vbfHToTauTauSample,
        'HLongLived': HTo2LongLivedTo4bSample,
        # #'TT': ttSample, #This is sort of too big to do this kind of analysis on.
        'GluGluToHHto4B_highSample': GluGluToHHto4B_highSample,
        'GluGluToHHto4B_lowSample': GluGluToHHto4B_lowSample,
        'SUSY': SusyGluGluToBBHToBBSample,
        'DYLLSample': DYLLSample,
    }
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

    theThresholdHelper = thresholdHelper()

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

    plots = {}

    for sampleKey in tqdm(samples, desc='Sample'):
        theSample = samples[sampleKey]
        for i in trange(len(triggerGroups.keys()), leave=False, desc='Primary Trigger'): #primary trigger
            for j in trange(i+1, len(triggerGroups.keys()), leave=False, desc='Secondary Trigger'): #secondary trigger
                primaryTrigger = list(triggerGroups.keys())[i]
                secondaryTrigger = list(triggerGroups.keys())[j]
                
                if 'CICADA' in primaryTrigger and 'CICADA' in secondaryTrigger:
                    continue
                if 'uGT' in primaryTrigger and 'uGT' in secondaryTrigger:
                    continue
                
                plotName = f'{primaryTrigger}_{secondaryTrigger}_{sampleKey}'
                thePlot = ROOT.TH1F(
                    plotName,
                    plotName,
                    4,
                    0.0,
                    4.0,
                )

                if 'CICADA' in primaryTrigger or 'uGT' in primaryTrigger:
                    primaryTriggerCutString = getAnomalyTriggerCutString(theThresholdHelper, triggerGroups[primaryTrigger])
                else:
                    primaryTriggerCutString = getTriggerCutString(theSample, triggerGroups[primaryTrigger])
                
                if 'CICADA' in secondaryTrigger or 'uGT' in secondaryTrigger:
                    secondaryTriggerCutString = getAnomalyTriggerCutString(theThresholdHelper, triggerGroups[secondaryTrigger])
                else:
                    secondaryTriggerCutString = getTriggerCutString(theSample, triggerGroups[secondaryTrigger])
                

                onlyPrimaryTriggerEvents = theSample.chain.GetEntries(primaryTriggerCutString+' && !('+secondaryTriggerCutString+')')
                onlySecondaryTriggerEvents = theSample.chain.GetEntries('!('+primaryTriggerCutString+') && '+secondaryTriggerCutString)
                bothTriggerEvents = theSample.chain.GetEntries(primaryTriggerCutString+' && '+secondaryTriggerCutString)
                neitherTriggerEvents = theSample.chain.GetEntries('!('+primaryTriggerCutString+') && !('+secondaryTriggerCutString+')')
                
                thePlot.Fill(f'Only {axisLabels[primaryTrigger]}', onlyPrimaryTriggerEvents)
                thePlot.Fill(f'Only {axisLabels[secondaryTrigger]}', onlySecondaryTriggerEvents)
                thePlot.Fill(f'Both Triggers', bothTriggerEvents)
                thePlot.Fill(f'Neither Trigger', neitherTriggerEvents)

                plots[plotName] = thePlot
    theFile = ROOT.TFile(args.theFile, 'RECREATE')
    for plot in plots:
        plots[plot].Write()
    theFile.Write()
    theFile.Close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Look at individual signals, and groups of triggers')

    parser.add_argument('--theFile', default='individualSignalEfficiencyFile.root',nargs='?',help='Output plot file')

    args = parser.parse_args()

    main(args)