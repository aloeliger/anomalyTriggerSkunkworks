#!/usr/bin/env python3

import ROOT
from tqdm import tqdm
import argparse

def main(args):
    if args.mc == True:
        outputFile = ROOT.TFile(f'/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/scoreMCPlots{args.year}CICADAv{args.CICADAVersion}.root', 'RECREATE')
    else:
        outputFile = ROOT.TFile(f'/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/scorePlots{args.year}CICADAv{args.CICADAVersion}.root', 'RECREATE')
    if args.year == '2018':
        from anomalyDetection.anomalyTriggerSkunkworks.samples.RunA import RunASample
        from anomalyDetection.anomalyTriggerSkunkworks.samples.RunB import RunBSample
        from anomalyDetection.anomalyTriggerSkunkworks.samples.RunC import RunCSample
        from anomalyDetection.anomalyTriggerSkunkworks.samples.RunD import RunDSample
        dataframes = {
            'RunA': RunASample.getNewDataframe(
                [
                    f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
                ]
            ),
            'RunB': RunBSample.getNewDataframe(
                [
                    f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
                ]
            ),
            'RunC': RunCSample.getNewDataframe(
                [
                    f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
                ]
            ),
            'RunD': RunDSample.getNewDataframe(
                [
                    f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
                ]
            ),
        }
    elif args.year == '2022':
        if args.mc:
            from anomalyDetection.anomalyTriggerSkunkworks.samples.mcSamples2022.DYto2L import DYTo2LSample
            from anomalyDetection.anomalyTriggerSkunkworks.samples.mcSamples2022.GGHTT import GGHTTSample
            from anomalyDetection.anomalyTriggerSkunkworks.samples.mcSamples2022.HTo2LongLived4b import HTo2LongLived4bSample
            from anomalyDetection.anomalyTriggerSkunkworks.samples.mcSamples2022.SUSYGGBBHtoBB import SUSYGGBBHtoBBSample
            from anomalyDetection.anomalyTriggerSkunkworks.samples.mcSamples2022.TT import TTSample
            from anomalyDetection.anomalyTriggerSkunkworks.samples.mcSamples2022.VBFHToInvisible import VBFHToInvisibleSample
            from anomalyDetection.anomalyTriggerSkunkworks.samples.mcSamples2022.VBFHTT import VBFHTTSample
            from anomalyDetection.anomalyTriggerSkunkworks.samples.mcSamples2022.ZPrimeTT import ZPrimeTTSample
            dataframes = {
                'DYTo2L': DYTo2LSample.getNewDataframe(
                    [
                      f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',  
                    ]
                ),
                'GGHTT': GGHTTSample.getNewDataframe(
                    [
                      f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',  
                    ]
                ),
                'HTo2LongLived4b': HTo2LongLived4bSample.getNewDataframe(
                    [
                      f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',  
                    ]
                ),
                'SUSYGGBBHtoBB': SUSYGGBBHtoBBSample.getNewDataframe(
                    [
                      f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',  
                    ]
                ),
                'TT': TTSample.getNewDataframe(
                    [
                      f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',  
                    ]
                ),
                'VBFHToInvisible': VBFHToInvisibleSample.getNewDataframe(
                    [
                      f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',  
                    ]
                ),
                'VBFHTT': VBFHTTSample.getNewDataframe(
                    [
                      f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',  
                    ]
                ),
                'ZPrimeTT': ZPrimeTTSample.getNewDataframe(
                    [
                      f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',  
                    ]
                ),
            }
        else:
            from anomalyDetection.anomalyTriggerSkunkworks.samples.dataSamples2022.RunB import RunBSample
            from anomalyDetection.anomalyTriggerSkunkworks.samples.dataSamples2022.RunC import RunCSample
            from anomalyDetection.anomalyTriggerSkunkworks.samples.dataSamples2022.RunD import RunDSample
            from anomalyDetection.anomalyTriggerSkunkworks.samples.dataSamples2022.RunE import RunESample
            from anomalyDetection.anomalyTriggerSkunkworks.samples.dataSamples2022.RunF import RunFSample
            from anomalyDetection.anomalyTriggerSkunkworks.samples.dataSamples2022.RunG import RunGSample
            dataframes = {
                'RunB': RunBSample.getNewDataframe(
                    [
                        f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
                    ]
                ),
                'RunC': RunCSample.getNewDataframe(
                    [
                        f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
                    ]
                ),
                'RunD': RunDSample.getNewDataframe(
                    [
                        f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
                    ]
                ),
                'RunE': RunESample.getNewDataframe(
                    [
                        f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
                    ]
                ),
                'RunF': RunFSample.getNewDataframe(
                    [
                        f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
                    ]
                ),
                'RunG': RunGSample.getNewDataframe(
                    [
                        f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
                    ]
                ),
            }

    maxes = []
    mins = []
    for run in tqdm(dataframes, desc="extremum"):
        maxes.append(
            dataframes[run].Max('anomalyScore').GetValue()
        )
        mins.append(
            dataframes[run].Min('anomalyScore').GetValue()
        )
    nBins = 100
    highGranularityBins = 1000
    scoreMax = max(maxes)
    scoreMin = min(mins)
    hists = []
    for run in tqdm(dataframes, desc="histogram booking"):
        histoName = f'{run}_score'
        histoModel = ROOT.RDF.TH1DModel(
            histoName,
            histoName,
            nBins,
            scoreMin,
            scoreMax
        )
        highGranularityHistoModel = ROOT.RDF.TH1DModel(
            histoName+'_highGranularity',
            histoName+'_highGranularity',
            highGranularityBins,
            scoreMin,
            scoreMax,
        )
        hists.append(
            dataframes[run].Histo1D(
                histoModel,
                'anomalyScore'
            )
        )
        hists.append(
            dataframes[run].Histo1D(
                highGranularityHistoModel,
                'anomalyScore'
            )
        )
    for hist in tqdm(hists, desc='histogram writing'):
        hist.Write()
    
    outputFile.Write()
    outputFile.Close()

        

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Create score plots for CICADA versions")
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
        '-y',
        '--year',
        default='2018',
        help='Year of samples to use',
        choices=['2018','2022'],
        nargs='?'
    )
    parser.add_argument(
        '--mc',
        action='store_true',
        help='Trigger the MC samples'
    )

    args = parser.parse_args()

    main(args)  