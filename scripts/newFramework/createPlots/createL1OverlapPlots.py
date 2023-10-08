# !/usr/bin/env python3

import ROOT
import argparse
from tqdm import tqdm,trange

from collections import OrderedDict

from anomalyDetection.anomalyTriggerSkunkworks.triggerInfo.thresholds import CICADAThresholds

def createStringConditionForTriggerGroup(triggerGroup):
    theStr = ''
    for trigger in triggerGroup:
        theStr += f'{trigger} == 1 || '
    theStr = theStr[:-4]
    return theStr

def main(args):
    outputFile = ROOT.TFile(f'/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/L1OverlapCICADAv{args.CICADAVersion}.root', 'RECREATE')
    
    # 2018
    """     from anomalyDetection.anomalyTriggerSkunkworks.samples.ephemeralZeroBiasSamples2018.ephemeralZeroBiasAll2018 import EphemeralZeroBiasSample
    from anomalyDetection.anomalyTriggerSkunkworks.triggerInfo.unprescaledTriggerBits import unprescaledBits2023

    theDataframe = EphemeralZeroBiasSample.getNewDataframe(
        [
            f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
            'L1TTriggerBitsNtuplizer/L1TTriggerBits',
        ]
    )
    menus = ['L1Menu_Collisions2018_v2_0_0','L1Menu_Collisions2018_v2_1_0']
     """
    # 2023
    from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.largeRunDEphemeralZeroBias import largeRunDEphemeralZeroBiasSample
    from anomalyDetection.anomalyTriggerSkunkworks.triggerInfo.unprescaledTriggerBits import unprescaledBits2023

    theDataframe = largeRunDEphemeralZeroBiasSample.getNewDataframe(
        [
            f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
            'L1TTriggerBitsNtuplizer/L1TTriggerBits',
        ]
    )

    menus = ['L1Menu_Collisions2023_v1_2_0']

    """     if args.CICADAVersion == 1:
        rateThresholds = {
            'L1Menu_Collisions2018_v2_0_0': OrderedDict({
                '10kHz (overall)': 5.364,
                '5kHz (overall)': 5.600,
                '3kHz (overall)': 5.758,
                '2kHz (overall)': 5.880,
                '1kHz (overall)': 6.142,
                '0p5kHz (overall)': 6.474,
            }),
            'L1Menu_Collisions2018_v2_1_0': OrderedDict({
                '10kHz (overall)': 5.906,
                '5kHz (overall)': 6.037,
                '3kHz (overall)': 6.142,
                '2kHz (overall)': 6.273,
                '1kHz (overall)': 6.500,
                '0p5kHz (overall)': 6.788,
            }),
        }
    if args.CICADAVersion == 2:
        rateThresholds = {
            'L1Menu_Collisions2018_v2_0_0':OrderedDict({
                '10kHz (overall)': 9.131,
                '5kHz (overall)': 10.0128,
                '3kHz (overall)': 10.763,
                '2kHz (overall)': 11.601,
                '1kHz (overall)': 13.365,
                '0p5kHz (overall)': 15.527,
            }),
            'L1Menu_Collisions2018_v2_1_0': OrderedDict({
                '10kHz (overall)': 11.557,
                '5kHz (overall)': 12.483,
                '3kHz (overall)': 13.189,
                '2kHz (overall)': 13.983,
                '1kHz (overall)': 15.747,
                '0p5kHz (overall)': 17.820,
            }),
        } """
    if args.CICADAVersion == 1:
        rateThresholds = {
            'L1Menu_Collisions2023_v1_2_0': OrderedDict({
                '10kHz (overall)': 5.734,
                '5kHz (overall)': 5.884,
                '3kHz (overall)': 5.953,
                '2kHz (overall)': 6.047,
                '1kHz (overall)': 6.406,
                '0p5kHz (overall)': 6.922,
            })
        }
    if args.CICADAVersion == 2:
        rateThresholds = {
            'L1Menu_Collisions2023_v1_2_0': OrderedDict({
                '10kHz (overall)': 11.356,
                '5kHz (overall)': 11.983,
                '3kHz (overall)': 12.477,
                '2kHz (overall)': 13.371,
                '1kHz (overall)': 15.707,
                '0p5kHz (overall)': 18.934,
            })
        }

    overlapEvents = OrderedDict()
    allEvents = OrderedDict()
    for menu in tqdm(menus, ascii=True, dynamic_ncols=True, leave=False, desc='Menu'):
        #narrow the datafame down to the menu we want
        menuDF = theDataframe.Filter(f'menuName == \"{menu}\"')

        #first, we get a list of all the trigger conditions we want

        triggerGroupNames = [group for group in unprescaledBits2023[menu]]
        triggerConditions = OrderedDict()
        for cicadaRate in rateThresholds[menu]:
            triggerConditions[cicadaRate] = f'anomalyScore > {rateThresholds[menu][cicadaRate]}'
        for name in triggerGroupNames:
            triggerConditions[name] = createStringConditionForTriggerGroup(unprescaledBits2023[menu][name])
        # print(triggerConditions)
        # Let's create the histogram that we are going to fill with stuff
        overlapHisto = ROOT.TH2F(
            f'overlap_{menu}',
            f'overlap_{menu}',
            len(triggerConditions.keys()),
            0.0,
            float(len(triggerConditions.keys())),
            len(triggerConditions.keys()),
            0.0,
            float(len(triggerConditions.keys())),
        )

        #okay. at this point we loop on the primary trigger conditions
        for primaryTrigger in tqdm(triggerConditions, ascii=True, dynamic_ncols=True, leave=False, desc="primary trigger condition"):
            # Get a DF and an all events count
            triggerDF = menuDF.Filter(triggerConditions[primaryTrigger])
            allEvents[primaryTrigger] = triggerDF.Count()
            overlapEvents[primaryTrigger]=OrderedDict()
            # And then on the secondary trigger conditions  
            for secondaryTrigger in tqdm(triggerConditions, ascii=True, dynamic_ncols=True, leave=False, desc="Secondary trigger condition"):
                twoConditionDF = triggerDF.Filter(triggerConditions[secondaryTrigger])
                overlapEvents[primaryTrigger][secondaryTrigger] = twoConditionDF.Count()
        # We can now force the values?
        for primaryTrigger in tqdm(triggerConditions, ascii=True, dynamic_ncols=True, leave=False, desc="Write out primary"):
            allEvents[primaryTrigger] = allEvents[primaryTrigger].GetValue()
            for secondaryTrigger in tqdm(triggerConditions, ascii=True, dynamic_ncols=True, leave=False, desc="Write out secondary"):
                overlapEvents[primaryTrigger][secondaryTrigger] = overlapEvents[primaryTrigger][secondaryTrigger].GetValue()
                overlapHisto.Fill(primaryTrigger, secondaryTrigger, overlapEvents[primaryTrigger][secondaryTrigger]/allEvents[primaryTrigger])
        overlapHisto.Write()
    outputFile.Write()
    outputFile.Close()


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