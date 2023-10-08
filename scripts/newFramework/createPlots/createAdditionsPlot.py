# !/usr/bin/env python3
import ROOT
import argparse
import os

from rich.console import Console
from rich.text import Text
from rich.console import Group
from rich.panel import Panel

from collections import OrderedDict

from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.Hto2LongLivedTo4b import Hto2LongLivedTo4bSample
from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.SUSYGluGlutoBBHtoBB import SUSYGluGlutoBBHtoBBSample
from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.TT import TTSample
from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.VBFHto2C import VBFHto2CSample
from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.SUEP import SUEPSample

from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.largeRunDEphemeralZeroBias import largeRunDEphemeralZeroBiasSample
# from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.RunDEphemeralZeroBias0 import RunDEphemeralZeroBias0Sample

from anomalyDetection.anomalyTriggerSkunkworks.triggerInfo.unprescaledTriggerBits import unprescaledBits2023

from createPileupPlots import getMaxAndMinScore, getThresholdForRate

console = Console()

def noUnprescaledBitPassesCondition(unprescaledBits):
    noPassCondition = ''
    for bit in unprescaledBits:
        noPassCondition += f'{bit} == 0 && '
    noPassCondition = noPassCondition[:-3]
    return noPassCondition

def anUnprescaledBitPassesCondition(unprescaledBits):
    passCondition = ''
    for bit in unprescaledBits:
        passCondition += f'{bit} == 1 || '
    passCondition = passCondition[:-3]
    return passCondition

def main(args):
    destinationPath='/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/'
    if not os.path.isdir(destinationPath):
        os.makedirs(destinationPath, exist_ok=True)
    outputFile = ROOT.TFile(f'{destinationPath}/additionPlotsCICADAv{args.CICADAVersion}.root', 'RECREATE')

    theSamples = OrderedDict()
    theSamples['Hto2LongLivedTo4b'] =  Hto2LongLivedTo4bSample.getNewDataframe(
        [
            f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
            'L1TTriggerBitsNtuplizer/L1TTriggerBits',
            'uGTModelNtuplizer/uGTModelOutput',
        ]
    )
    theSamples['SUSYGluGlutoBBHtoBB'] = SUSYGluGlutoBBHtoBBSample.getNewDataframe(
        [
            f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
            'L1TTriggerBitsNtuplizer/L1TTriggerBits',
            'uGTModelNtuplizer/uGTModelOutput',
        ]
    )
    theSamples['TT'] =  TTSample.getNewDataframe(
        [
            f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
            'L1TTriggerBitsNtuplizer/L1TTriggerBits',
            'uGTModelNtuplizer/uGTModelOutput',
        ]
    )
    theSamples['VBFHto2C'] = VBFHto2CSample.getNewDataframe(
        [
            f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
            'L1TTriggerBitsNtuplizer/L1TTriggerBits',
            'uGTModelNtuplizer/uGTModelOutput',
        ]
    )
    theSamples['SUEP'] = SUEPSample.getNewDataframe(
        [
            f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
            'L1TTriggerBitsNtuplizer/L1TTriggerBits',
            'uGTModelNtuplizer/uGTModelOutput',
        ]
    )
    

    mcBits = unprescaledBits2023['L1Menu_Collisions2022_v1_4_0']
    mcBits = [
        bit for category in mcBits for bit in mcBits[category]
    ]

    dataSample = largeRunDEphemeralZeroBiasSample.getNewDataframe(
                [
                    f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
                    'L1TTriggerBitsNtuplizer/L1TTriggerBits',
                    'uGTModelNtuplizer/uGTModelOutput',
                ]
            )

    with console.status('Figuring out CICADA thresholds...'):
        cicada_maxScore, cicada_minScore = getMaxAndMinScore(dataSample, ADScoreName='anomalyScore')
        cicada_tenkHzThreshold = getThresholdForRate(
            dataSample,
            10.0,
            cicada_minScore,
            cicada_maxScore,
            anomalyScoreName = 'anomalyScore'
        )
    with console.status('Figuring out AXOL1TL thresholds...'):
        axo_maxScore, axo_minScore = getMaxAndMinScore(dataSample, ADScoreName='uGTAnomalyScore')
        axo_tenkHzThreshold = getThresholdForRate(
            dataSample,
            10.0,
            axo_minScore,
            axo_maxScore,
            anomalyScoreName = 'uGTAnomalyScore'
        )
    console.print(f'10 kHz: CICADA Threshold: {cicada_tenkHzThreshold:.3f}, AX0L1TL: {axo_tenkHzThreshold:.2f}')
    
    nSamples = len(theSamples.keys())

    triggerGraph = ROOT.TGraph(nSamples)
    triggerCICADAGraph = ROOT.TGraph(nSamples)
    triggerAXOGraph = ROOT.TGraph(nSamples)
    triggerBothGraph = ROOT.TGraph(nSamples)

    for sampleIndex, sampleName in enumerate(theSamples):
        sample = theSamples[sampleName]

        # total info

        totalEvents = sample.Count().GetValue()

        # un-caught events

        noTriggerSample = sample.Filter(noUnprescaledBitPassesCondition(mcBits))
        unTriggeredEvents = noTriggerSample.Count().GetValue()
        unCaughtFraction = unTriggeredEvents / totalEvents

        #  reclaimed information

        cicadaReclaimedSample = noTriggerSample.Filter(f'anomalyScore >= {cicada_tenkHzThreshold}')
        axoReclaimedSample = noTriggerSample.Filter(f'uGTAnomalyScore >= {axo_tenkHzThreshold}')
        bothReclaimedSample = noTriggerSample.Filter(f'anomalyScore >= {cicada_tenkHzThreshold} || uGTAnomalyScore >= {axo_tenkHzThreshold}')

        cicadaReclaimedEvents = cicadaReclaimedSample.Count().GetValue()
        axoReclaimedEvents = axoReclaimedSample.Count().GetValue()
        bothReclaimedEvents = bothReclaimedSample.Count().GetValue()

        cicadaFracReclaimed = cicadaReclaimedEvents / unTriggeredEvents
        axoFracReclaimed = axoReclaimedEvents / unTriggeredEvents
        bothFracReclaimed = bothReclaimedEvents / unTriggeredEvents

        # Total Catch information

        triggerCaughtSample = sample.Filter(anUnprescaledBitPassesCondition(mcBits))
        triggerCICADACaughtSample = sample.Filter(f'{anUnprescaledBitPassesCondition(mcBits)} || anomalyScore >= {cicada_tenkHzThreshold}')
        triggerAXOCaughtSample = sample.Filter(f'{anUnprescaledBitPassesCondition(mcBits)} || uGTAnomalyScore >= {axo_tenkHzThreshold}')
        triggerBothCaughtSample = sample.Filter(f'{anUnprescaledBitPassesCondition(mcBits)} || anomalyScore >= {cicada_tenkHzThreshold} || uGTAnomalyScore >= {axo_tenkHzThreshold}')

        triggerCaughtEvents = triggerCaughtSample.Count().GetValue()
        triggerCICADACaughtEvents = triggerCICADACaughtSample.Count().GetValue()
        triggerAXOCaughtEvents = triggerAXOCaughtSample.Count().GetValue()
        triggerBothCaughtEvents = triggerBothCaughtSample.Count().GetValue()

        triggerCaughtFrac = triggerCaughtEvents / totalEvents
        triggerCICADACaughtFrac = triggerCICADACaughtEvents / totalEvents
        triggerAXOCaughtFrac = triggerAXOCaughtEvents / totalEvents
        triggerBothCaughtFrac = triggerBothCaughtEvents / totalEvents

        # Text assembly
        topLine = Text.assemble(
            ('Total Events:', 'underline white'),
            f' {totalEvents} ',
            ('Uncaught events:', 'underline white'),
            f' {unTriggeredEvents} ',
            ('Percent uncaught:', 'underline red'),
            (f' {unCaughtFraction:.2%}', 'Bold red')
        )
        secondLine = Text.assemble(
            ('Percent of uncaught reclaimed by CICADA:', 'underline green'),
            (f' {cicadaFracReclaimed:.2%} ', 'bold green'),
            ('Percent of uncaught reclaimed by AXOL1TL:', 'underline green'),
            (f' {axoFracReclaimed:.2%} ', 'bold green'),
            ('Percent of uncaught reclaimed by both (OR):', 'underline cyan'),
            (f' {bothFracReclaimed:.2%} ', 'bold cyan'),
        )
        thirdLine = Text.assemble(
            ('Total events caught by the trigger:', 'underline white'),
            (f' {triggerCaughtEvents} ', 'bold white'),
            ('Total percent caught by the trigger:', 'underline white'),
            (f' {triggerCaughtFrac:.2%} ', 'bold white'),
        )
        fourthLine = Text.assemble(
            ('Total events caught by the trigger + CICADA:', 'underline green'),
            (f' {triggerCICADACaughtEvents} ', 'bold green'),
            ('Total percent caught by the trigger + CICADA:', 'underline green'),
            (f' {triggerCICADACaughtFrac:.2%} ', 'bold green')
        )
        fifthLine = Text.assemble(
            ('Total events caught by the trigger + AXOL1TL:', 'underline green'),
            (f' {triggerAXOCaughtEvents} ', 'bold green'),
            ('Total percent caught by the trigger + AXOL1TL:', 'underline green'),
            (f' {triggerAXOCaughtFrac:.2%} ', 'bold green')
        )
        sixthLine = Text.assemble(
            ('Total events caught by the trigger + CICADA + AXOL1TL', 'underline cyan'),
            (f' {triggerBothCaughtEvents} ', 'bold cyan'),
            ('Total percent caught by the trigger + CICADA + AXOL1TL', 'underline cyan'),
            (f' {triggerBothCaughtFrac:.2%} ', 'bold cyan')
        )
        textGroup = Group(
            topLine,
            secondLine,
            thirdLine,
            fourthLine,
            fifthLine,
            sixthLine,
        )
        textPanel = Panel(
            textGroup,
            title=sampleName,
            subtitle='10 kHz AD'
        )
        console.print(textPanel)

        triggerGraph.SetPoint(
            sampleIndex,
            triggerCaughtFrac,
            float(sampleIndex+1),
        )
        triggerCICADAGraph.SetPoint(
            sampleIndex,
            triggerCICADACaughtFrac,
            float(sampleIndex+1),
        )
        triggerAXOGraph.SetPoint(
            sampleIndex,
            triggerAXOCaughtFrac,
            float(sampleIndex+1),
        )
        triggerBothGraph.SetPoint(
            sampleIndex,
            triggerBothCaughtFrac,
            float(sampleIndex+1),
        )

    console.print('')

    triggerGraph.SetNameTitle(
        'triggerGraph',
        'triggerGraph',
    )
    triggerCICADAGraph.SetNameTitle(
        'triggerCICADAGraph',
        'triggerCICADAGraph',
    )
    triggerAXOGraph.SetNameTitle(
        'triggerAXOGraph',
        'triggerAXOGraph',
    )
    triggerBothGraph.SetNameTitle(
        'triggerBothGraph',
        'triggerBothGraph',
    )

    triggerGraph.Write()
    triggerCICADAGraph.Write()
    triggerAXOGraph.Write()
    triggerBothGraph.Write()

    outputFile.Write()
    outputFile.Close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a series of pileup plots for AD')
    parser.add_argument(
        '-v',
        '--CICADAVersion',
        default=1,
        type=int,
        help='AD version to pull out of the ntuplizer',
        choices = [1,2],
        nargs='?',
    )

    args = parser.parse_args()

    main(args)