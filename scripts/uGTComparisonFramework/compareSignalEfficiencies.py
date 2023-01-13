import argparse
from samples.dataSamples import runASample, runBSample, runCSample, runDSample
from samples.SUEPSamples import suepSample
from tqdm import trange,tqdm
import ROOT
from triggers.unPrescaledTriggers import *

def getAnomalyTriggerEfficiency(runSample, triggerGroup, totalEntries):
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
    triggeredEntries = float(runSample.chain.GetEntries(cutString))

    try:
        eff = float(triggeredEntries)/float(totalEntries)
    except ZeroDivisionError:
        eff = 0.0

    return eff

def getTriggerEfficiency(runSample, triggerGroup, totalEntries):
    cutString = f'{triggerGroup[0]} == 1'
    for i in range(1,len(triggerGroup)):
        cutString+=f'|| {triggerGroup[i]} == 1'
    triggeredEntries = runSample.chain.GetEntries(cutString)

    try:
        eff = float(triggeredEntries)/float(totalEntries)
    except ZeroDivisionError:
        eff = 0.0

    return eff

def main(args):
    samples = {
        'RunA': (runASample, 'Run A'),
        'RunB': (runBSample, 'Run B'),
        'RunC': (runCSample, 'Run C'),
        'RunD': (runDSample, 'Run D'),
        'SUEP': (suepSample, 'SUEP')
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
    efficiencyPlots = {}

    for sampleKey in tqdm(samples):
        sample = samples[sampleKey][0]
        efficiencyPlot = ROOT.TH1F(
            f'{sampleKey}Efficiencies',
            f'{sampleKey}Efficiencies',
            len(triggerGroups.keys()),
            0.0,
            float(len(triggerGroups.keys()))
        )
        totalEntries = sample.GetEntries()
        for triggerGroup in tqdm(triggerGroups, leave=False):
            if 'CICADA' in triggerGroup or 'uGT' in triggerGroup:
                efficiencyPlot.Fill(
                    samples[sampleKey][1],
                    getAnomalyTriggerEfficiency(sample, triggerGroups[triggerGroup], totalEntries)
                )
            else:
                efficiencyPlot.Fill(
                    samples[sampleKey][1],
                    getTriggerEfficiency(sample, triggerGroups[triggerGroup], totalEntries)
                )
        efficiencyPlots[sampleKey] = efficiencyPlot
    
    theFile = ROOT.TFile(args.theFile, 'RECREATE')
    for sampleKey in efficiencyPlots:
        efficiencyPlots[sampleKey].Write()
    theFile.Write()
    theFile.Close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Do efficiency Comparisons between samples')
    
    parser.add_argument('--theFile',default='sampleFile.root',nargs='?',help='Output plot file')
    
    args = parser.parse_args()

    main(args)