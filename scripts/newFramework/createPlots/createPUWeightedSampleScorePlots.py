# !/usr/bin/env python3
import ROOT
import argparse

from rich.console import Console
from rich.traceback import install
from rich.progress import track

from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.allZeroBias import allZeroBiasSample
from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.Hto2LongLivedTo4b import Hto2LongLivedTo4bSample
from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.SUSYGluGlutoBBHtoBB import SUSYGluGlutoBBHtoBBSample
from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.TT import TTSample
from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.VBFHto2C import VBFHto2CSample
from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.SUEP import SUEPSample

console = Console()
install(show_locals=True)

def main(args):
    outputFile = ROOT.TFile(f'/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/sampleScorePlotsCICADAv{args.CICADAVersion}.root','RECREATE')
    dataframes={
        "ZeroBias": allZeroBiasSample.getNewDataframe(
            [
                f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
            ]
        ),
        "LLP": Hto2LongLivedTo4bSample.getNewDataframe(
            [
                f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
                'pileupWeightDirectory/pileupWeightTree',
            ]
        ),
        "SUS": SUSYGluGlutoBBHtoBBSample.getNewDataframe(
            [
                f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
                'pileupWeightDirectory/pileupWeightTree',            
            ]
        ),
        "TT": TTSample.getNewDataframe(
            [
                f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
                'pileupWeightDirectory/pileupWeightTree',
            ]
        ),
        "VBF": VBFHto2CSample.getNewDataframe(
            [
                f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
                'pileupWeightDirectory/pileupWeightTree',
            ]
        ),
        "SUEP": SUEPSample.getNewDataframe(
            [
                f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
                'pileupWeightDirectory/pileupWeightTree',            
            ]
        )
    }

    maxes = []
    mins = []
    for sampleName in track(dataframes, description="Generating extremum..."):
        maxes.append(
            dataframes[sampleName].Max('anomalyScore')
        )
        mins.append(
            dataframes[sampleName].Min('anomalyScore')
        )
    with console.status("Getting actual values..."):
        maxes = [x.GetValue() for x in maxes]
        mins = [x.GetValue() for x in mins]
    
    nBins = 100
    absoluteMax = max(maxes)
    absoluteMin = min(mins)
    hists = []

    for sampleName in dataframes:
        histoName = f'{sampleName}_score'
        histoNameNoPU = f'{sampleName}_noPUWeight_score'
        histoModel = ROOT.RDF.TH1DModel(
            histoName,
            histoName,
            nBins,
            absoluteMin,
            absoluteMax,
        )
        histoModelNoPU = ROOT.RDF.TH1DModel(
            histoNameNoPU,
            histoNameNoPU,
            nBins,
            absoluteMin,
            absoluteMax,
        )

        if sampleName == 'ZeroBias':
            hists.append(
                dataframes[sampleName].Histo1D(
                    histoModel,
                    'anomalyScore'
                )
            )
        else:
            hists.append(
                dataframes[sampleName].Histo1D(
                    histoModel,
                    'anomalyScore',
                    'pileupWeight'
                )
            )
            hists.append(
                dataframes[sampleName].Histo1D(
                    histoModelNoPU,
                    'anomalyScore'
                )
            )

    for hist in track(hists, description='Histogram writing...'):
        hist.Write()
    outputFile.Write()
    outputFile.Close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create PU weighted data versus samples plots for CICADA versions')
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