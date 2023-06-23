#!/usr/bin/env python3

import ROOT
from anomalyDetection.anomalyTriggerSkunkworks.samples.EphemeralZeroBias import EphemeralZeroBiasSample
from tqdm import tqdm
import argparse

#We need to create histograms for objects

def main(args):
    objects = {
        'EGamma':{
            'tree': 'caloStage2EGammaNtuplizer/L1CaloEgammaInformation',
        },
        "Jet": {
            'tree': 'caloStage2JetNtuplizer/L1CaloJetInformation',
        },
        "Tau":{
            'tree': 'caloStage2TauNtuplizer/L1CaloTauInformation',
        },
        "EtSum":{
            'tree': 'caloStage2EtSumNtuplizer/L1CaloEtSumInformation',
        },
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
        'etVector':{
            'name': 'et',
            'nBins': 60,
            'lowBinEdge': 0.0,
            'highBinEdge': 120.0,
        },
        'mtVector':{
            'name': 'mt',
            'nBins': 60,
            'lowBinEdge': 0.0,
            'highBinEdge': 120.0,
        },
    }

    cicadaThresholds = args.thresholds

    outputFile = ROOT.TFile(f'/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/triggerObjectPlotsCICADAv{args.CICADAVersion}.root', 'RECREATE')
    # theDataframe = EphemeralZeroBiasSample.getNewDataframe(["CICADAv1ntuplizer/L1TCaloSummaryOutput"])
    for object in tqdm(objects, desc="objects"):
        hists = []
        #this will allow us to re-use the data-frame and filtering as we go down the line
        #However, we have to recycle the dataframe for each plot type
        #because of re-used filters.
        theDataframe = EphemeralZeroBiasSample.getNewDataframe(
            [
                f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
                objects[object]['tree']
            ]
        ) 
        for plotType in tqdm(histograms,desc="histograms",leave=False):
            for threshold in tqdm(cicadaThresholds,desc="CICADA thresholds", leave=False):
                thresholdString = str(threshold).replace('.', 'p')
                histoName = f'{object}_{histograms[plotType]["name"]}_CICADA{thresholdString}'
                histoModel = ROOT.RDF.TH1DModel(
                    histoName,
                    histoName,
                    histograms[plotType]['nBins'],
                    histograms[plotType]['lowBinEdge'],
                    histograms[plotType]['highBinEdge'],
                )
                # theDataframe = theDataframe.Filter(f'anomalyScore > {cicadaThreshold}')
                theHisto = theDataframe.Filter(f'anomalyScore > {threshold}').Histo1D(histoModel, plotType)
                hists.append(theHisto)
        # continue
        for hist in tqdm(hists, desc='Hist writing',leave=False):
            hist.Write()
    # exit()
    outputFile.Write()
    outputFile.Close()
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Create plots about trigger objects for certain CICADA thresholds")
    parser.add_argument(
        '-v',
        '--CICADAVersion',
        default=1,
        type=int,
        help='Version to pull the ntuplizer from',
        choices=[1,2],
        nargs='?',
    )
    parser.add_argument(
        '-t',
        '--thresholds',
        default=[0.0, 3.0, 5.0, 6.0, 7.0],
        type=float,
        nargs='*',
        help='Thresholds of CICADA plot to make',
    )

    args = parser.parse_args()

    main(args)