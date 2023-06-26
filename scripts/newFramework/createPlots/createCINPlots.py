#!/usr/bin/env python3

import ROOT
import argparse
from anomalyDetection.anomalyTriggerSkunkworks.samples.RunA import RunASample
from anomalyDetection.anomalyTriggerSkunkworks.samples.RunB import RunBSample
from anomalyDetection.anomalyTriggerSkunkworks.samples.RunC import RunCSample
from anomalyDetection.anomalyTriggerSkunkworks.samples.RunD import RunDSample
from tqdm import tqdm, trange

def makeCalorimeterImage(array, name):
    theHist = ROOT.TH2F(
        name,
        name,
        18,
        0.0, 
        18.0,
        14,
        0.0,
        14.0,
    )
    for iPhi in range(18):
        for iEta in range(14):
            theHist.SetBinContent(iPhi+1, iEta+1, array[iPhi][iEta])
    return theHist

def translateCICADAInputNetwork(theChain):
    output = []
    for i in range(18):
        row = []
        for j in range(14):
            index = i*14+j
            row.append(theChain.CICADAInputNetworkPrediction[index])
        output.append(row)
    return output

def translateCICADAInput(theChain):
    output = []
    for i in range(18):
        row = []
        for j in range(14):
            index = i*14+j
            row.append(theChain.modelInput[index])
        output.append(row)
    return output

def main(args):
    outputFile = ROOT.TFile(f'/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/CICADAInputNetworkPlots.root','RECREATE')
    chains = {
        'RunA': RunASample.getNewChain(
            [
                'CICADAv1ntuplizer/L1TCaloSummaryOutput',
                'CICADAInputNetworkAnalyzerv1p0/CICADAInputNetworkTree',
            ]
        ),
        'RunB': RunBSample.getNewChain(
            [
                'CICADAv1ntuplizer/L1TCaloSummaryOutput',
                'CICADAInputNetworkAnalyzerv1p0/CICADAInputNetworkTree',
            ]
        ),
        'RunC': RunCSample.getNewChain(
            [
                'CICADAv1ntuplizer/L1TCaloSummaryOutput',
                'CICADAInputNetworkAnalyzerv1p0/CICADAInputNetworkTree',
            ]
        ),
        'RunD': RunDSample.getNewChain(
            [
                'CICADAv1ntuplizer/L1TCaloSummaryOutput',
                'CICADAInputNetworkAnalyzerv1p0/CICADAInputNetworkTree',
            ]
        ),
    }
    for run in tqdm(chains):
        for i in trange(5, leave=False):
            chains[run].GetEntry(i)
            modelInput = translateCICADAInput(chains[run])
            CINPrediction = translateCICADAInputNetwork(chains[run])

            predictionHist = makeCalorimeterImage(
                array=CINPrediction,
                name=f'CIN_{run}_{i}'
            )
            calorimeterHist = makeCalorimeterImage(
                array=modelInput,
                name=f'Calorimeter_{run}_{i}',
            )

            errorHist = predictionHist.Clone()
            errorHist.SetNameTitle(f'Error_{run}_{i}', f'Error_{run}_{i}')

            errorHist.Add(calorimeterHist,-1.0)

            predictionHist.Write()
            calorimeterHist.Write()
            errorHist.Write()
    outputFile.Write()
    outputFile.Close()
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Make plots about the accuracy of the CICADAInputNetwork')

    args = parser.parse_args()
    main(args)