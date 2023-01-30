import argparse

from samples.dataSamples import runASample, runBSample, runCSample, runDSample
from samples.SUEPSamples import suepSample
from samples.VBFHToTauTauSample import vbfHToTauTauSample
from samples.HTo2LongLivedTo4bSample import HTo2LongLivedTo4bSample
from samples.TTSample import ttSample
from samples.GluGluToHHTo4B_node_cHHH1_sample import GluGluHTo4B_cHHH1_sample
from samples.GluGluToHHTo4B_node_cHHH5_sample import GluGluHTo4B_cHHH5_sample
from samples.SUSYSamples import SusyGluGluToBBHToBBSample
from samples.ZToEESamples import ZToEESample

from tqdm import trange,tqdm
import ROOT
from triggers.unPrescaledTriggers import *

import json

from anomalyTriggerThresholds.thresholdHelper import thresholdHelper
import re

def getAnomalyTriggerEvents(theThresholdHelper, runSample, triggerGroup):
    triggerGroup = triggerGroup[0]
    if 'CICADA' in triggerGroup:
        trigger = 'CICADA'
        variableName = 'anomalyScore'
    elif 'uGT' in triggerGroup:
        trigger='uGT'
        variableName = 'uGTAnomalyScore'
    rateString = re.search('[0-9]+(p[0-9]+)?', triggerGroup).group(0)
    rate = rateString.replace('p', '.').replace('.0','')
    threshold = theThresholdHelper.getTriggerThreshold(trigger,rate)


    cutString = f'{variableName} >= {threshold}'
    triggeredEntries = float(runSample.chain.GetEntries(cutString))

    # try:
    #     eff = float(triggeredEntries)/float(totalEntries)
    # except ZeroDivisionError:
    #     eff = 0.0

    return triggeredEntries

def getTriggerEvents(runSample, triggerGroup):
    cutString = f'{triggerGroup[0]} == 1'
    listOfBranches = [x.GetName() for x in list(runSample.triggerBitsChain.GetListOfBranches())]
    #print(listOfBranches)
    for i in range(1,len(triggerGroup)):
        #We need to consider whether this trigger is truly present in the MC
        #TODO: synchronize MC and data trigger availability
        if triggerGroup[i] in listOfBranches:
            cutString+=f'|| {triggerGroup[i]} == 1'
        else:
            print(f'Skipping trigger {triggerGroup[i]} in current sample')
    triggeredEntries = runSample.chain.GetEntries(cutString)

    # try:
    #     eff = float(triggeredEntries)/float(totalEntries)
    # except ZeroDivisionError:
    #     eff = 0.0

    return triggeredEntries

def main(args):
    samples = {
        'RunA': runASample,
        'RunB': runBSample,
        'RunC': runCSample,
        'RunD': runDSample,
        'SUEP': suepSample,
        'VBFHTT': vbfHToTauTauSample,
        'HLongLived': HTo2LongLivedTo4bSample,
        'TT': ttSample,
        'GluGluHH4b_cHHH1': GluGluHTo4B_cHHH1_sample,
        'GluGluHH4B_cHHH5': GluGluHTo4B_cHHH5_sample,
        'SUSY': SusyGluGluToBBHToBBSample,
        'ZToEE': ZToEESample,
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
    with open(args.jsonFile, 'r') as jsonFile:
        thresholdData = json.load(jsonFile)
        
    numeratorPlots = {}
    denominatorPlots = {}

    for sampleKey in tqdm(samples):
        sample = samples[sampleKey]
        numeratorPlot = ROOT.TH1F(
            f'{sampleKey}Numerator',
            f'{sampleKey}Numerator',
            len(triggerGroups.keys()),
            0.0,
            float(len(triggerGroups.keys()))
        )
        denominatorPlot = ROOT.TH1F(
            f'{sampleKey}Denominator',
            f'{sampleKey}Denominator',
            len(triggerGroups.keys()),
            0.0,
            float(len(triggerGroups.keys()))
        )
        totalEntries = sample.GetEntries()
        for triggerGroup in tqdm(triggerGroups, leave=False):
            if 'CICADA' in triggerGroup or 'uGT' in triggerGroup:
                numeratorPlot.Fill(
                    axisLabels[triggerGroup],
                    getAnomalyTriggerEvents(theThresholdHelper, sample, triggerGroups[triggerGroup])
                )
            else:
                numeratorPlot.Fill(
                    axisLabels[triggerGroup],
                    getTriggerEvents(sample, triggerGroups[triggerGroup])
                )
            denominatorPlot.Fill(
                axisLabels[triggerGroup],
                totalEntries
            )
        #efficiencyPlots[sampleKey] = efficiencyPlot
        numeratorPlots[sampleKey] = numeratorPlot
        denominatorPlots[sampleKey] = denominatorPlot
    
    theFile = ROOT.TFile(args.theFile, 'RECREATE')
    for sampleKey in numeratorPlots:
        #efficiencyPlots[sampleKey].Write()
        numeratorPlots[sampleKey].Write()
    for sampleKey in denominatorPlots:
        denominatorPlots[sampleKey].Write()
    theFile.Write()
    theFile.Close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Do efficiency Comparisons between samples')
    
    parser.add_argument('--theFile',default='sampleFile.root',nargs='?',help='Output plot file')
    parser.add_argument('--jsonFile', default='./anomalyTriggerThresholds/triggerThresholds.json', help='Json file that defines the thresholds for anomaly triggers')

    args = parser.parse_args()

    main(args)