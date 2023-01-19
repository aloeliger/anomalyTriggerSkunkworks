import argparse

from samples.SUEPSamples import suepSample
from samples.VBFHToTauTauSample import vbfHToTauTauSample
from samples.HTo2LongLivedTo4bSample import HTo2LongLivedTo4bSample
from samples.TTSample import ttSample
from samples.GluGluToHHTo4B_node_cHHH1_sample import GluGluHTo4B_cHHH1_sample
from samples.GluGluToHHTo4B_node_cHHH5_sample import GluGluHTo4B_cHHH5_sample

from tqdm import tqdm, trange
import ROOT
from triggers.unPrescaledTriggers import *


def getAnomalyTriggerCutString(triggerGroup):
    triggerGroup = triggerGroup[0]
    if 'CICADA' in triggerGroup:
        variableName = 'anomalyScore'
        if '3kHz' in triggerGroup:
            threshold = 5.83
        elif '2kHz' in triggerGroup:
            threshold = 5.95
        elif '1kHz' in triggerGroup:
            threshold=6.20
        elif '0p5kHz' in triggerGroup:
            threshold=6.55
    
    elif 'uGT' in triggerGroup:
        variableName = 'uGTAnomalyScore'
        if '3kHz' in triggerGroup:
            threshold = 7710.76
        elif '2kHz' in triggerGroup:
            threshold = 8243.48
        elif '1kHz' in triggerGroup:
            threshold = 8811.72
        elif '0p5kHz' in triggerGroup:
            threshold = 9202.39
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
        'TT': ttSample,
        'GluGluHH4b_cHHH1': GluGluHTo4B_cHHH1_sample,
        'GluGluHH4B_cHHH5': GluGluHTo4B_cHHH5_sample,
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

    axisLabels = {
        'CICADA3kHz' : 'CICADA (3 kHz)',
        'CICADA2kHz' : 'CICADA (2 kHz)',
        'CICADA1kHz' : 'CICADA (1 kHz)',
        'CICADA0p5kHz' : 'CICADA (0.5 kHz)',
        'uGT3kHz' : 'uGT AD (3 kHz)',
        'uGT2kHz' : 'uGT AD (2 kHz)',
        'uGT1kHz' : 'uGT AD (1 kHz)',
        'uGT0p5kHz' : 'uGT AD (0.5 kHz)',
        'pureMuonTriggers': 'Pure Muon Triggers',
        'muonPlusEGTriggers': 'Muon+EG Triggers',
        'muonPlusJetMETOrHT': 'Muon+Jet/MET/HT Triggers',
        'pureEGTriggers': 'Pure EG Triggers',
        'EGPlusHTOrJet': 'EG+HT/Jet Triggers',
        'tauPlusOthers': 'Tau Plus Other Triggers',
        'pureTauTriggers': 'Pure Tau Triggers',
        'jetsPlusHTTriggers': 'Jets(+HT) Triggers',
        'HTETorMETTriggers': 'HT/ET/MET Triggers',
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
                    primaryTriggerCutString = getAnomalyTriggerCutString(triggerGroups[primaryTrigger])
                else:
                    primaryTriggerCutString = getTriggerCutString(theSample, triggerGroups[primaryTrigger])
                
                if 'CICADA' in secondaryTrigger or 'uGT' in secondaryTrigger:
                    secondaryTriggerCutString = getAnomalyTriggerCutString(triggerGroups[secondaryTrigger])
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