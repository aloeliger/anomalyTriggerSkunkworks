#!/usr/bin/env python3

import ROOT
import argparse
from anomalyDetection.anomalyTriggerSkunkworks.samples.RunA import RunASample
from anomalyDetection.anomalyTriggerSkunkworks.samples.RunB import RunBSample
from anomalyDetection.anomalyTriggerSkunkworks.samples.RunC import RunCSample
from anomalyDetection.anomalyTriggerSkunkworks.samples.RunD import RunDSample
from tqdm import tqdm
import copy

def main(args):
    outputFile = ROOT.TFile(f'/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/approximationPlotsCICADAv{args.CICADAVersion}.root', 'RECREATE')
    runs = {
        'RunA': RunASample,
        'RunB': RunBSample,
        'RunC': RunCSample,
        'RunD': RunDSample,
    }
    
    if args.CICADAVersion == 1:
        baseCICADATree = 'CICADAv1ntuplizer/L1TCaloSummaryOutput'
        treeTypes = {
            'miniCICADAv1p0': 'miniCICADAAnalyzerCICADAv1/miniCICADAScoreTree',
            'miniCICADAv1p1': 'miniCICADAv1p1AnalyzerCICADAv1/miniCICADAScoreTree',
            'CICADAPlusCIN': 'CICADAv1FromCINv1Analyzer/CICADAPlusCIN'
        }
        scoreBins = 40
        scoreMin = 0.0
        scoreMax = 7.0
    elif args.CICADAVersion == 2:
        baseCICADATree = 'CICADAv2ntuplizer/L1TCaloSummaryOutput'
        treeTypes = {
            'miniCICADAv1p0': 'miniCICADAAnalyzer/miniCICADAScoreTree',
            'miniCICADAv1p1': 'miniCICADAv1p1AnalyzerCICADAv2/miniCICADAScoreTree',
            'CICADAPlusCIN': 'CICADAv2FromCINv1Analyzer/CICADAPlusCIN'
        }
        scoreBins = 40
        scoreMin = 0.0
        scoreMax = 15.0
    # Have to do this crazy junk to avoid overlap of samples
    # and to keep it all in memory to avoid the garbage cleaner destroying me
    samples = {}

    dataframes = {}
    for run in tqdm(runs, desc='Defining samples and frames: runs', leave=False):
        samples[run] = {}
        dataframes[run] = {}
        samples[run]['CICADA'] = copy.deepcopy(runs[run])
        dataframes[run]['CICADA'] = samples[run]['CICADA'].getNewDataframe([baseCICADATree])
        for treeType in tqdm(treeTypes, desc='Defining samples and frames: tree types', leave=False):
            samples[run][treeType] = copy.deepcopy(runs[run])
            dataframes[run][treeType] = samples[run][treeType].getNewDataframe(
                [
                    baseCICADATree,
                    treeTypes[treeType]
                ]
            )
    scoreColumns = {
        'CICADA': 'anomalyScore',
        'miniCICADAv1p0': 'miniCICADAScore',
        'miniCICADAv1p1': 'miniCICADAScore',
        'CICADAPlusCIN': 'CICADAPlusCINScore',
    }
    
    for run in tqdm(dataframes,desc='Defining columns: runs', leave=False):
        for frameType in tqdm(dataframes[run], desc='Defining columns: frame types', leave=False):
            if frameType == 'CICADA':
                continue
            scoreColumn = scoreColumns[frameType]
            dataframes[run][frameType] = dataframes[run][frameType].Define("scoreError",f'{scoreColumn}-anomalyScore')
            dataframes[run][frameType] = dataframes[run][frameType].Define("absScoreError",f'abs({scoreColumn}-anomalyScore)')

    hists = []
    for run in tqdm(
        dataframes,
        desc='Booking Hists: runs',
        leave=False
    ):
        for frameType in tqdm(
            dataframes[run],
            desc='Booking Hists: frame types',
            leave=False
        ):
            scoreColumn = scoreColumns[frameType]
            scoreName = f'{run}_{frameType}_score'
            scoreModel = ROOT.RDF.TH1DModel(
                scoreName,
                scoreName,
                scoreBins,
                scoreMin,
                scoreMax
            )
            if frameType == 'CICADA':
                pass
            else:
                errorModel = ROOT.RDF.TH1DModel(
                    f'{scoreName}_error',
                    f'{scoreName}_error',
                    scoreBins,
                    scoreMin,
                    scoreMax
                )
                absErrorModel = ROOT.RDF.TH1DModel(
                    f'{scoreName}_abserror',
                    f'{scoreName}_abserror',
                    scoreBins,
                    scoreMin,
                    scoreMax
                )
                hists.append(
                    dataframes[run][frameType].Histo1D(
                        errorModel,
                        'anomalyScore',
                        'scoreError'
                    )
                )
                hists.append(
                    dataframes[run][frameType].Histo1D(
                        absErrorModel,
                        'anomalyScore',
                        'absScoreError',
                    )
                )
            hists.append(
                dataframes[run][frameType].Histo1D(
                    scoreModel,
                    scoreColumn
                )
            )
    for hist in tqdm(hists, desc='Writing hists', leave=False):
        hist.Write()
    outputFile.Write()
    outputFile.Close

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='make plots of the CICADA approximation methods')
    parser.add_argument(
        '-v',
        '--CICADAVersion',
        default=1,
        type=int,
        help='Version of CICADA to compare approximators for',
        choices=[1, 2],
        nargs='?',
    )

    args = parser.parse_args()

    main(args)