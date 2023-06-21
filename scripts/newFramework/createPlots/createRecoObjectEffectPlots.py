# !/usr/bin/env python3

import ROOT
from anomalyDetection.anomalyTriggerSkunkworks.samples.EphemeralZeroBias import EphemeralZeroBiasSample
import numpy as np
from tqdm import tqdm

def main():
    objects = {
        'Electron':{
            'tree': 'electronCounter/objectInfo',
        },
        'Jet':{
            'tree': 'jetCounter/objectInfo',
        },
        'FatJet':{
            'tree': 'fatJetCounter/objectInfo',
        },
        'Muon':{
            'tree': 'muonCounter/objectInfo',
        },
        'Photon':{
            'tree': 'photonCounter/objectInfo',
        },
        'Tau':{
            'tree': 'tauCounter/objectInfo',
        },
        'BoostedTau':{
            'tree': 'boostedTauCounter/objectInfo',
        }
    }
    histograms = {
        'nObjects':{
            'name': 'nObjects',
            'nBins': 13,
            'lowBinEdge': 0,
            'highBinEdge': 13,
        },
        'ptVector':{
            'name': 'pt',
            'nBins': 60,
            'lowBinEdge': 0.0,
            'highBinEdge': 120,
        },
        'etaVector':{
            'name': 'eta',
            'nBins': 40,
            'lowBinEdge': -5.0,
            'highBinEdge': 5.0,
        },
        'phiVector':{
            'name': 'phi',
            'nBins': 40,
            'lowBinEdge': -3.14,
            'highBinEdge': 3.14,
        },
    }

    cicadaThresholds = [0.0, 3.0, 5.0, 6.0, 7.0]

    outputFile = ROOT.TFile('/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/recoObjectPlots.root', 'RECREATE')

    for object in tqdm(objects, desc="objects"):
        hists = []
        theDataframe = EphemeralZeroBiasSample.getNewDataframe(
            [
                'CICADAv1ntuplizer/L1TCaloSummaryOutput',
                objects[object]['tree']     
            ]
        )
        for plotType in tqdm(histograms, desc="histograms", leave=False):
            for threshold in tqdm(cicadaThresholds, desc="CICADA thresholds", leave=False):
                thresholdString = str(threshold).replace('.','p')
                histoName = f'{object}_{histograms[plotType]["name"]}_CICADA{thresholdString}'
                histoModel = ROOT.RDF.TH1DModel(
                    histoName,
                    histoName,
                    histograms[plotType]['nBins'],
                    histograms[plotType]['lowBinEdge'],
                    histograms[plotType]['highBinEdge'],
                )
                theHisto = theDataframe.Filter(f'anomalyScore > {threshold}').Histo1D(histoModel, plotType)
                hists.append(theHisto)
        for hist in tqdm(hists, desc='Hist writing', leave=False):
            hist.Write()
    outputFile.Write()
    outputFile.Close()

if __name__ == '__main__':
    main()