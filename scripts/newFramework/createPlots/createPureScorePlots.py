#!/usr/bin/env python3

import ROOT
from tqdm import tqdm
import argparse
import numpy as np

from tqdm import tqdm,trange
from prettytable import PrettyTable


def getUniqueMenuNames(df):
    menuNames = df.AsNumpy(['menuName'])['menuName']
    uniqueMenuNames = []
    for name in menuNames:
        if name not in uniqueMenuNames:
            uniqueMenuNames.append(name)
    # print(uniqueMenuNames)
    return uniqueMenuNames


def getStringForNoBitPass(bitDict, excludedCats=[]):
    theString = ''
    for group in bitDict:
        if group in excludedCats:
            continue
        for bit in bitDict[group]:
            theString += f'{bit} == 0 && '
    theString = theString[:-4]
    return theString


def main(args):
    #make the output file
    outputFile = ROOT.TFile(f'/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/pureScorePlots{args.year}CICADAv{args.CICADAVersion}.root', 'RECREATE')
    #Get the sample
    #for right now this is just going to be EphemeralZeroBias

    # 2018 setup
    # from anomalyDetection.anomalyTriggerSkunkworks.triggerInfo.unprescaledTriggerBits import unprescaledBits2018

    # 2023 setup
    from anomalyDetection.anomalyTriggerSkunkworks.triggerInfo.unprescaledTriggerBits import unprescaledBits2023

    # 2018 setup
    """ from anomalyDetection.anomalyTriggerSkunkworks.samples.ephemeralZeroBiasSamples2018.ephemeralZeroBiasAll2018 import EphemeralZeroBiasSample
    from anomalyDetection.anomalyTriggerSkunkworks.samples.dataSamples2018.RunA import RunASample
    from anomalyDetection.anomalyTriggerSkunkworks.samples.dataSamples2018.RunC import RunCSample
    from anomalyDetection.anomalyTriggerSkunkworks.samples.dataSamples2018.RunD import RunDSample """
    
    # 2023 setup
    from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.largeRunDEphemeralZeroBias import largeRunDEphemeralZeroBiasSample

    # 2018 setup
    """ dataframes = {
        'EphemeralZeroBias': EphemeralZeroBiasSample.getNewDataframe(
            [
                f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
                'L1TTriggerBitsNtuplizer/L1TTriggerBits',
            ]
        ),
    } """
    # 2023 
    dataframes = {
        'EphemeralZeroBias': largeRunDEphemeralZeroBiasSample.getNewDataframe(
            [
                f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
                'L1TTriggerBitsNtuplizer/L1TTriggerBits',
            ]
        )
    }

    maxes = []
    mins = []
    for run in tqdm(dataframes, desc="extremum", ascii=True, dynamic_ncols=True):
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
    # scoreMax = 8.0
    # scoreMin = 0.0
    alldataFrames = []
    hists = []

    #for each DF we will make certain plots
    for run in tqdm(dataframes, ascii=True, dynamic_ncols=True, desc='plot booking'):
        # print('dataframe')
        df = dataframes[run]

        #Figure out available menus
        # print(df.GetColumnNames())
        # print('unique menus')
        menuNames = df.AsNumpy(['menuName'])['menuName']
        uniqueMenuNames = []
        for name in menuNames:
            if name not in uniqueMenuNames:
                uniqueMenuNames.append(name)
        # print(run)
        # print(uniqueMenuNames)
        # continue

        #Figure out unprescaled bits per menu
        # We should probably have this sorted out beforehand?
        # print('unmatched menus')
        unmatchedMenus = []
        for menuName in uniqueMenuNames:
            if not menuName in unprescaledBits2023:
                print(f"Failed to find prescales for {menuName} in unprescaled bits file. Please add it")
                unmatchedMenus.append(menuName)
                uniqueMenuNames.remove(menuName)
        #Make unprescaled score plots per menu
        # print('general plots')
        scoreModel = ROOT.RDF.TH1DModel(
            f'{run}_score',
            f'{run}_score',
            nBins,
            scoreMin,
            scoreMax,
        )
        hists.append(
            df.Histo1D(
                scoreModel,
                'anomalyScore',
            )
        )
        highGranularityScoreModel = ROOT.RDF.TH1DModel(
            f'{run}_score_highGranularity',
            f'{run}_score_highGranularity',
            highGranularityBins,
            scoreMin,
            scoreMax,
        )
        hists.append(
            df.Histo1D(
                highGranularityScoreModel,
                'anomalyScore'
            )
        )
        # print('per menu plots')
        for menu in uniqueMenuNames:
            menuDF =  df.Filter(f'menuName == \"{menu}\"')
            # print('general plots')
            menuScoreModel = ROOT.RDF.TH1DModel(
                f'{run}_{menu}_score',
                f'{run}_{menu}_score',
                nBins,
                scoreMin,
                scoreMax,
            )
            hgMenuScoreModel = ROOT.RDF.TH1DModel(
                f'{run}_{menu}_score_highGranularity',
                f'{run}_{menu}_score_highGranularity',
                highGranularityBins,
                scoreMin,
                scoreMax,
            )
            hists.append(
                menuDF.Histo1D(
                    menuScoreModel,
                    'anomalyScore',
                )
            )
            hists.append(
                menuDF.Histo1D(
                    hgMenuScoreModel,
                    'anomalyScore'
                )
            )
            alldataFrames.append(menuDF)

            # print('pure plots')
            pureRateScoreModel = ROOT.RDF.TH1DModel(
                f'{run}_{menu}_pureScore',
                f'{run}_{menu}_pureScore',
                nBins,
                scoreMin,
                scoreMax,
            )
            pureRateMinusMuonScoreModel = ROOT.RDF.TH1DModel(
                f'{run}_{menu}_pureScoreMinusMuon',
                f'{run}_{menu}_pureScoreMinusMuon',
                nBins,
                scoreMin,
                scoreMax,
            )
            hgPureRateScoreModel = ROOT.RDF.TH1DModel(
                f'{run}_{menu}_pureScore_highGranularity',
                f'{run}_{menu}_pureScore_highGranularity',
                highGranularityBins,
                scoreMin,
                scoreMax,
            )
            hgPureRateMinusMuonScoreModel = ROOT.RDF.TH1DModel(
                f'{run}_{menu}_pureScoreMinusMuon_highGranularity',
                f'{run}_{menu}_pureScoreMinusMuon_highGranularity',    
                highGranularityBins,
                scoreMin,
                scoreMax,
            )

            noUnprescaledBitPasses = getStringForNoBitPass(unprescaledBits2023[menu])
            noUnprescaledBitPassesMinusMuons = getStringForNoBitPass(
                unprescaledBits2023[menu],
                excludedCats=[
                    'Muon',
                    'MuonEG',
                    'MuonJetOrSum',
                    'MuonTau',
                ]
            )

            pureDF = menuDF.Filter(noUnprescaledBitPasses)
            pureDFMinusMuons = menuDF.Filter(noUnprescaledBitPassesMinusMuons)

            hists.append(
                pureDF.Histo1D(
                    pureRateScoreModel,
                    'anomalyScore'
                )
            )
            hists.append(
                pureDFMinusMuons.Histo1D(
                    pureRateMinusMuonScoreModel,
                    'anomalyScore'
                )
            )
            hists.append(
                pureDF.Histo1D(
                    hgPureRateScoreModel,
                    'anomalyScore'
                )
            )
            hists.append(
                pureDFMinusMuons.Histo1D(
                    hgPureRateMinusMuonScoreModel,
                    'anomalyScore'
                )
            )
            alldataFrames.append(pureDF)
            alldataFrames.append(pureDFMinusMuons)
    for hist in tqdm(hists, ascii=True, dynamic_ncols=True):
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

    args = parser.parse_args()

    main(args)  