#!/usr/bin/env python3

import ROOT
# from tqdm import tqdm
import argparse
from rich.progress import track
from rich.console import Console
from rich.traceback import install

console = Console()
install()

def main(args):
    
    outputFile = ROOT.TFile(f'/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/scorePlotsCICADAv{args.CICADAVersion}.root', 'RECREATE')
    # 2018 setup
    """ from anomalyDetection.anomalyTriggerSkunkworks.samples.RunA import RunASample
    from anomalyDetection.anomalyTriggerSkunkworks.samples.RunB import RunBSample
    from anomalyDetection.anomalyTriggerSkunkworks.samples.RunC import RunCSample
    from anomalyDetection.anomalyTriggerSkunkworks.samples.RunD import RunDSample """
    # 2023 setup
    # Run A seems... incorrect
    # from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.RunA import RunASample
    from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.RunBComplete import RunBSample
    from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.RunCComplete import RunCSample
    from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.RunDComplete import RunDSample

    dataframes = {
        # 'RunA': RunASample.getNewDataframe(
        #     [
        #         f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
        #     ]
        # ),
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

    # console.log('Removing training from samples...')

    maxes = []
    mins = []
    for run in track(dataframes, description="Finding Extrememum..."):
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

    # Pull any training data out before histograms are made
    from anomalyDetection.anomalyTriggerSkunkworks.utilities.removeTraining import removeTrainingTool
    theTrainingRemovalTool = removeTrainingTool()
    for run in track(dataframes, description='Removing traning from samples...'):
        dataframes[run] = theTrainingRemovalTool.removeTrainingDataFromDataframe(dataframes[run])

    for run in track(dataframes, description="Histogram booking.."):
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
    for hist in track(hists, description='Histogram writing...'):
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

    args = parser.parse_args()

    main(args)  