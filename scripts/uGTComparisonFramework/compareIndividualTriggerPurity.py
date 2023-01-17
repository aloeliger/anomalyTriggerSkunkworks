import argparse
from samples.dataSamples import runASample, runBSample, runCSample, runDSample
from tqdm import tqdm
import ROOT
from triggers.unPrescaledTriggers import *

def main(args):
    ROOT.gStyle.SetOptStat(0)
    runs = {
        'RunA': runASample,
        'RunB': runBSample,
        'RunC': runCSample,
        'RunD': runDSample,
    }

    anomalyTriggers = [
        'CICADA3kHz',
        'CICADA2kHz',
        'CICADA1kHz',
        'CICADA0p5kHz',
        'uGT3kHz',
        'uGT2kHz',
        'uGT1kHz',
        'uGT0p5kHz'
    ]

    triggerGroups = {
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

    overlapPlots = []
    for anomalyTrigger in tqdm(anomalyTriggers, desc='Anomaly Triggers'):
        for triggerGroup in tqdm(triggerGroups, leave=False, desc='UnPrescaled Trigger Groups'):
            for triggerName in tqdm(triggerGroups[triggerGroup], leave=False, desc='UnPrescaled Triggers'):
                overlapPlot = ROOT.TH2F(
                    f'{anomalyTrigger}_{triggerName}_overlap',
                    f'{anomalyTrigger}_{triggerName}_overlap',
                    2,
                    0.0,
                    2.0,
                    2,
                    0.0,
                    2.0,
                )
                #There are four categories we need to consider,
                #Across four different runs
                if 'CICADA' in anomalyTrigger:
                    anomalyVariable = 'anomalyScore'
                    if '3kHz' in anomalyTrigger:
                        threshold = 5.83
                    elif '2kHz' in anomalyTrigger:
                        threshold = 5.95
                    elif '1kHz' in anomalyTrigger:
                        threshold = 6.20
                    elif '0p5kHz' in anomalyTrigger:
                        threshold = 6.55
                elif 'uGT' in anomalyTrigger:
                    anomalyVariable = 'uGTAnomalyScore'
                    if '3kHz' in anomalyTrigger:
                        threshold = 7710.76
                    elif '2kHz' in anomalyTrigger:
                        threshold = 8243.48
                    elif '1kHz' in anomalyTrigger:
                        threshold = 8811.72
                    elif '0p5kHz' in anomalyTrigger:
                        threshold = 9202.39
                anomalyPasses = f'{anomalyVariable} >= {threshold}'
                anomalyFails = f'{anomalyVariable} < {threshold}'
                triggerPasses = f'{triggerName} == 1'
                triggerFails = f'{triggerName} == 0'
                #We'll organize this with the trigger (anomaly) on the X (Y) axis
                for run in tqdm(runs, leave=False, desc='Run Event Calculation'):
                    overlapPlot.Fill('pass','pass', runs[run].chain.GetEntries(f'{anomalyPasses} && {triggerPasses}'))
                    overlapPlot.Fill('pass','fail', runs[run].chain.GetEntries(f'{anomalyFails} && {triggerPasses}'))
                    overlapPlot.Fill('fail','pass', runs[run].chain.GetEntries(f'{anomalyPasses} && {triggerFails}'))
                    overlapPlot.Fill('fail','fail', runs[run].chain.GetEntries(f'{anomalyFails} && {triggerFails}'))
                overlapPlots.append(overlapPlot)
    theFile = ROOT.TFile(args.theFile, 'RECREATE')
    for plot in overlapPlots:
        plot.Write()
    theFile.Write()
    theFile.Close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script for checking the overlap of individual triggers with anomaly triggers')
    
    parser.add_argument('--theFile', default='individualPurityFile.root', nargs='?', help='Ouptut plot file')
    
    args = parser.parse_args()

    main(args)