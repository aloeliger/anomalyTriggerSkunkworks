# !/usr/bin/env python3

import ROOT
import argparse
import numpy as np
# from tqdm import tqdm,trange
from rich.progress import Progress, track
import math
import time

from createPureScorePlots import getStringForNoBitPass

uniqueLumiMapping = {}
def getCachedUniqueLumiMapping(run):
    if run in uniqueLumiMapping.keys():
        return uniqueLumiMapping[run]
    else:
        return None

def createRateThresholdPlotForRun(dataframe, name, run, rate, rateThreshold):
    runDataframe = dataframe.Filter(f'run == {run}')
    if getCachedUniqueLumiMapping(run) != None:
        uniqueLumis = getCachedUniqueLumiMapping(run)
    else:
        lumiCol = runDataframe.AsNumpy(['lumi'])['lumi']
        uniqueLumis = list(np.unique(lumiCol))
        uniqueLumis.sort()
        uniqueLumiMapping[run] = uniqueLumis

    thresholdDF = runDataframe.Filter(f'anomalyScore >= {rateThreshold}')
    maxLumi = uniqueLumis[len(uniqueLumis)-1]
    minLumi = uniqueLumis[0]
    nLumis = maxLumi-minLumi

    perLumiModel = ROOT.RDF.TH1DModel(
        f'{name}_{rate}_eventsPerLumi',
        f'{name}_{rate}_eventsPerLumi',
        int(nLumis),
        float(minLumi),
        float(maxLumi+1)
    )
    theHist = thresholdDF.Histo1D(
        perLumiModel,
        'lumi'
    )
    return theHist

def createBitPlotForRun(dataframe, name, run):
    runDataframe = dataframe.Filter(f'run == {run}')
    if getCachedUniqueLumiMapping(run) != None:
        uniqueLumis = getCachedUniqueLumiMapping(run)
    else:
        lumiCol = runDataframe.AsNumpy(['lumi'])['lumi']
        uniqueLumis = list(np.unique(lumiCol))
        uniqueLumis.sort()
        uniqueLumiMapping[run] = uniqueLumis

    maxLumi = uniqueLumis[len(uniqueLumis)-1]
    minLumi = uniqueLumis[0]
    nLumis = maxLumi-minLumi

    perLumiModel = ROOT.RDF.TH1DModel(
        f'{name}_eventsPerLumi',
        f'{name}_eventsPerLumi',
        int(nLumis),
        float(minLumi),
        float(maxLumi+1),
    )
    theHist = runDataframe.Histo1D(
        perLumiModel,
        'lumi'
    )
    return theHist

def main(args):
    outputFile = ROOT.TFile(f'/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/perLumiPureAndOverallRatePlotsCICADAv{args.CICADAVersion}.root', 'RECREATE')
    
    # 2018 setup
    """ from anomalyDetection.anomalyTriggerSkunkworks.samples.ephemeralZeroBiasSamples2018.ephemeralZeroBiasAll2018 import EphemeralZeroBiasSample
    from anomalyDetection.anomalyTriggerSkunkworks.triggerInfo.unprescaledTriggerBits import unprescaledBits2018 """
    
    from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.largeRunDEphemeralZeroBias import largeRunDEphemeralZeroBiasSample as EphemeralZeroBiasSample
    from anomalyDetection.anomalyTriggerSkunkworks.triggerInfo.unprescaledTriggerBits import unprescaledBits2023

    theDataframe = EphemeralZeroBiasSample.getNewDataframe(
        [
            f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
            'L1TTriggerBitsNtuplizer/L1TTriggerBits',
            'boostedJetTriggerNtuplizer/boostedJetTrigger',
        ]
    )

    # 2018 setup
    """ if args.CICADAVersion == 1:
        rateThresholds = {
            'L1Menu_Collisions2018_v2_0_0':{
                'overall':{
                    'ZeroBias': 0.0,
                    '10kHz': 5.364,
                    '5kHz': 5.600,
                    '3kHz': 5.758,
                    '2kHz': 5.880,
                    '1kHz': 6.142,
                    '0p5kHz': 6.474,
                },
                'pure':{
                    'ZeroBias': 0.0,
                    '10kHz': 5.269,
                    '5kHz': 5.470,
                    '3kHz': 5.600,
                    '2kHz': 5.688,
                    '1kHz': 5.819,
                    '0p5kHz': 5.941,
                },
            },
            'L1Menu_Collisions2018_v2_1_0':{
                'overall':{physics
                    'ZeroBias': 0.0,
                    '10kHz': 5.906,
                    '5kHz': 6.037,
                    '3kHz': 6.142,
                    '2kHz': 6.273,
                    '1kHz': 6.500,
                    '0p5kHz': 6.788,
                },
                'pure':{
                    'ZeroBias': 0.0,
                    '10kHz': 5.863,
                    '5kHz': 5.959,
                    '3kHz': 6.020,
                    '2kHz': 6.064,
                    '1kHz': 6.177,
                    '0p5kHz': 6.273,
                },
            }
        }
    if args.CICADAVersion == 2:
        rateThresholds = {
            'L1Menu_Collisions2018_v2_0_0':{
                'overall':{
                    'ZeroBias':0.0,
                    '10kHz': 9.131,
                    '5kHz': 10.0128,
                    '3kHz': 10.763,
                    '2kHz': 11.601,
                    '1kHz': 13.365,
                    '0p5kHz': 15.527,
                },
                'pure':{
                    'ZeroBias':0.0,
                    '10kHz': 8.777,
                    '5kHz': 9.395,
                    '3kHz': 9.881,
                    '2kHz': 10.277,
                    '1kHz': 10.939,
                    '0p5kHz': 11.601,
                },
            },
            'L1Menu_Collisions2018_v2_1_0':{
                'overall':{
                    'ZeroBias':0.0,
                    '10kHz': 11.557,physics
                    '5kHz': 12.483,
                    '3kHz': 13.189,
                    '2kHz': 13.983,
                    '1kHz': 15.747,
                    '0p5kHz': 17.820,
                },
                'pure':{
                    'ZeroBias':0.0,
                    '10kHz': 11.204,
                    '5kHz': 11.865,
                    '3kHz': 12.395,
                    '2kHz': 12.792,
                    '1kHz': 13.497,
                    '0p5kHz': 14.336,
                },
            }
        } """
    if args.CICADAVersion == 1:
        rateThresholds = {
            'L1Menu_Collisions2023_v1_2_0':{
                'overall':{
                    'ZeroBias': 0.0,
                    "10kHz": 5.734,
                    "5kHz": 5.884,
                    "3kHz": 5.953,
                    "2kHz": 6.047,
                    "1kHz": 6.406,
                    "0p5kHz": 6.922,
                },
                'pure':{
                    'ZeroBias': 0.0,
                    "10kHz": 5.781,
                    "5kHz": 5.859,
                    "3kHz": 5.922,
                    "2kHz": 5.983,
                    "1kHz": 6.016,
                    "0p5kHz": 6.109,
                },
            },
        }
    if args.CICADAVersion == 2:
        rateThresholds = {
            'L1Menu_Collisions2023_v1_2_0':{
                'overall':{
                    'ZeroBias':0.0,
                    "10kHz": 11.356,
                    "5kHz": 11.983,
                    "3kHz": 12.477,
                    "2kHz": 13.371,
                    "1kHz": 15.707,
                    "0p5kHz": 18.934,
                },
                'pure':{
                    'ZeroBias':0.0,
                    '10kHz': 11.555,
                    '5kHz': 11.947,
                    '3kHz': 12.252,
                    '2kHz': 13.528,
                    '1kHz': 13.277,
                    '0p5kHz': 14.012,
                },
            },
        }
    usefulUnprescaledBits = [
        'L1_SingleMu22',
        'L1_SingleTau120er2p1',
        'L1_SingleJet180',
    ]
    #Let's just abuse the fact that we know what the menus are
    # 2018 setup
    # menus = ['L1Menu_Collisions2018_v2_0_0','L1Menu_Collisions2018_v2_1_0']
    menus = ['L1Menu_Collisions2023_v1_2_0']
    # storage so we don't lose any pieces
    dataframes = []
    hists = []

    with Progress(transient=True) as progress:
        task1 = progress.add_task("[red]Menus...",total=len(menus))
        for menu in menus:
            menuDF = theDataframe.Filter(f'menuName == \"{menu}\"')
            dataframes.append(menuDF)

            runCol = menuDF.AsNumpy(['run'])['run']
            uniqueRuns = np.unique(runCol)
            uniqueRuns = list(uniqueRuns)
 
            # we now need to make a DF that has the boosted jet information we want available
            # normal trigger would be pt 120.0
            # but we suspect there is a factor of 3/2 in the pt for some reason
            # so the trigger here is defined as 180.0
            boostedJetTriggerDerivationFunction = """
                for(int i = 0; i < numberOfJets; ++i){
                    if(jetPts.at(i) > 180.0){
                        return 1.0;
                    }
                }
                return 0.0;
            """
            menuDF = menuDF.Define(
                "boostedJetTriggerFires",
                boostedJetTriggerDerivationFunction,
            )

            noUnprescaledBitCondition = getStringForNoBitPass(unprescaledBits2023[menu])
            pureMenuDF = menuDF.Filter(noUnprescaledBitCondition)
            dataframes.append(pureMenuDF)

            #first, let's handle
            task2 = progress.add_task("[green]Runs...",total=len(uniqueRuns))
            # for run in tqdm(uniqueRuns, ascii=True, dynamic_ncols=True, leave=False, desc="Booking Anomaly Hists"):
            for run in uniqueRuns:
                task3 = progress.add_task("[cyan]Pure Vs Overall...", total=2)
                # for pureOrOverall in tqdm(['pure','overall'], ascii=True, dynamic_ncols=True, leave=False, desc='Pure or Overall?'):
                for pureOrOverall in ['pure','overall']:
                    # make the CICADA plots
                    task4 = progress.add_task("[magenta]Rate...", total=len(rateThresholds[menu][pureOrOverall].keys()))
                    # for rate in tqdm(rateThresholds[menu][pureOrOverall], ascii=True, dynamic_ncols=True, leave=False, desc="rates"):
                    for rate in rateThresholds[menu][pureOrOverall]:
                        threshold = rateThresholds[menu][pureOrOverall][rate]
                        histoRunName = f'CICADA_{run}_{menu}_{pureOrOverall}'
                        if pureOrOverall == 'pure':
                            hists.append(
                                createRateThresholdPlotForRun(
                                    dataframe = pureMenuDF,
                                    name = histoRunName,
                                    run = run,
                                    rate = rate,
                                    rateThreshold = threshold
                                )
                            )
                        elif pureOrOverall == 'overall':
                            hists.append(
                                createRateThresholdPlotForRun(
                                    dataframe = menuDF,
                                    name = histoRunName,
                                    run = run,
                                    rate = rate,
                                    rateThreshold = threshold
                                )
                            )
                        progress.update(task4, advance=1)
                    # While we're here, let's try to make pure or overall plots 
                    # for our l1 bits
                    task4 = progress.add_task("[magenta]Unprescaled Bits...",total=len(usefulUnprescaledBits))
                    # for bit in tqdm(usefulUnprescaledBits, ascii=True, dynamic_ncols=True, leave=False, desc='L1 Bits'):
                    for bit in usefulUnprescaledBits:
                        if pureOrOverall == 'pure':
                            condition = getStringForNoBitPass(unprescaledBits2023[menu])
                            condition.replace(f'{bit} == 0', f'{bit} == 1')
                        elif pureOrOverall == 'overall':
                            condition = f'{bit}==1'
                        bitDF = menuDF.Filter(condition)
                        dataframes.append(bitDF)
                        histoRunName = f'{bit}_{run}_{menu}_{pureOrOverall}'
                        hists.append(
                            createBitPlotForRun(
                                dataframe=bitDF,
                                name=histoRunName,
                                run=run,
                            )
                        )
                        progress.update(task4, advance=1)
                    #now, the other thing we need to do is make a boosted jet algorithm dataframe
                    if pureOrOverall == 'pure':
                        pureBoostedDF = pureMenuDF.Filter('boostedJetTriggerFires == 1.0')
                        histoName = f'boostedJetTrigger_{run}_{menu}_{pureOrOverall}'
                        hists.append(
                            createBitPlotForRun(
                                dataframe=pureBoostedDF,
                                name=histoName,
                                run = run,
                            )
                        )
                    elif pureOrOverall == 'overall':
                        boostedDF = menuDF.Filter('boostedJetTriggerFires == 1.0')
                        histoName = f'boostedJetTrigger_{run}_{menu}_{pureOrOverall}'
                        hists.append(
                            createBitPlotForRun(
                                dataframe=boostedDF,
                                name=histoName,
                                run = run,
                            )
                        )
                    progress.update(task3, advance=1)
                progress.update(task2, advance=1)
            progress.update(task1, advance=1)

    for hist in track(hists, description='Writing hists...', transient=True):
        hist.Write()
    outputFile.Write()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Create stability rate plots for CICADA versions")
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