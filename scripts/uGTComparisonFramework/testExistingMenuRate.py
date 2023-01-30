import argparse
from samples.dataSamples import runASample,runBSample,runCSample,runDSample
from triggers.unPrescaledTriggers import *

from tqdm import trange, tqdm
import math
import ROOT

from prettytable import PrettyTable

from compareSignalEfficiencies import getAnomalyTriggerEvents, getTriggerEvents
from drawFrequencyStability import convertEffToRate

def main(args):
    ROOT.gStyle.SetOptStat(0)
    runs = {
        'RunA': runASample,
        'RunB': runBSample,
        'RunC': runCSample,
        'RunD': runDSample,
    }

    runNames = {
        'RunA': 'Run A',
        'RunB': 'Run B',
        'RunC': 'Run C',
        'RunD': 'Run D',
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

    fieldNames = {
        'CICADA3kHz' : 'CICADA (3 kHz)',
        'CICADA2kHz' : 'CICADA (2 kHz)',
        'CICADA1kHz' : 'CICADA (1 kHz)',
        'CICADA0p5kHz' : 'CICADA (0.5 kHz)',
        'uGT3kHz' : 'uGT AD (3 kHz)',
        'uGT2kHz' : 'uGT AD (2 kHz)',
        'uGT1kHz' : 'uGT AD (1 kHz)',
        'uGT0p5kHz' : 'uGT AD (0.5 kHz)',
        'pureMuonTriggers': 'Pure Muon Triggers',
        'muonPlusEGTriggers': 'Muon Plus EG Triggers',
        'muonPlusJetMETOrHT': 'Muon Plus Jet/MET/HT Trigger',
        'pureEGTriggers': 'Pure EG Triggers',
        'EGPlusHTOrJet': 'EG Plus HT/Jet Triggers',
        'tauPlusOthers': 'Tau Plus Other Object Triggers',
        'pureTauTriggers': 'Pure Tau Triggers',
        'jetsPlusHTTriggers': 'Jets (Plus HT) Triggers',
        'HTETorMETTriggers': 'HT/ET/MET Triggers',
    }

    rates =  {}

    for run in tqdm(runs, desc='Runs'):
        rates[run] = {}
        theSample = runs[run]
        totalEntries = theSample.GetEntries()
        for triggerGroup in tqdm(triggerGroups, leave=False, desc='Trigger Group'):
            if 'CICADA' in triggerGroup or 'uGT' in triggerGroup:
                rates[run][triggerGroup] = convertEffToRate(getAnomalyTriggerEvents(theSample, triggerGroups[triggerGroup]) / float(totalEntries))
            else:
                rates[run][triggerGroup] = convertEffToRate(getTriggerEvents(theSample, triggerGroups[triggerGroup]) / float(totalEntries))
    theTable = PrettyTable()

    theTable.field_names = ['Trigger/Run (kHz):'] + list(runNames.values())
    for triggerGroup in triggerGroups:
        tableRow = []
        tableRow.append(fieldNames[triggerGroup])
        for run in ('RunA','RunB','RunC','RunD'):
            tableRow.append(f'{rates[run][triggerGroup]:3.2g} kHz')
        #tableRow.append(f'{rates["RunA"][triggerGroup]:3.2g} kHz')
        theTable.add_row(tableRow)
    
    print(theTable)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Look at the overall rates for existing unprescaled menu triggers')

    args = parser.parse_args()

    main(args)