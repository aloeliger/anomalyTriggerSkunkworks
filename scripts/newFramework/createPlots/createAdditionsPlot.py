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
    rateString = str(args.rate).replace('.','p')
    outputFile = ROOT.TFile(f'{destinationPath}/additionPlots_{rateString}kHz_CICADAv{args.CICADAVersion}.root', 'RECREATE')

    theSamples = OrderedDict()
    theSamples['Hto2LongLivedTo4b'] =  Hto2LongLivedTo4bSample.getNewDataframe(
        [
            f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
            'L1TTriggerBitsNtuplizer/L1TTriggerBits',
            'uGTModelNtuplizer/uGTModelOutput',
            'pileupWeightDirectory/pileupWeightTree',
        ]
    )
    theSamples['SUSYGluGlutoBBHtoBB'] = SUSYGluGlutoBBHtoBBSample.getNewDataframe(
        [
            f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
            'L1TTriggerBitsNtuplizer/L1TTriggerBits',
            'uGTModelNtuplizer/uGTModelOutput',
            'pileupWeightDirectory/pileupWeightTree',
        ]
    )
    theSamples['TT'] =  TTSample.getNewDataframe(
        [
            f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
            'L1TTriggerBitsNtuplizer/L1TTriggerBits',
            'uGTModelNtuplizer/uGTModelOutput',
            'pileupWeightDirectory/pileupWeightTree',
        ]
    )
    theSamples['VBFHto2C'] = VBFHto2CSample.getNewDataframe(
        [
            f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
            'L1TTriggerBitsNtuplizer/L1TTriggerBits',
            'uGTModelNtuplizer/uGTModelOutput',
            'pileupWeightDirectory/pileupWeightTree',
        ]
    )
    theSamples['SUEP'] = SUEPSample.getNewDataframe(
        [
            f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
            'L1TTriggerBitsNtuplizer/L1TTriggerBits',
            'uGTModelNtuplizer/uGTModelOutput',
            'pileupWeightDirectory/pileupWeightTree',
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
        cicada_rateThreshold = getThresholdForRate(
            dataSample,
            args.rate,
            cicada_minScore,
            cicada_maxScore,
            anomalyScoreName = 'anomalyScore'
        )
    with console.status('Figuring out AXOL1TL thresholds...'):
        axo_maxScore, axo_minScore = getMaxAndMinScore(dataSample, ADScoreName='uGTAnomalyScore')
        axo_rateThreshold = getThresholdForRate(
            dataSample,
            args.rate,
            axo_minScore,
            axo_maxScore,
            anomalyScoreName = 'uGTAnomalyScore'
        )
    console.print(f'{args.rate} kHz: CICADA Threshold: {cicada_rateThreshold:.3f}, AX0L1TL: {axo_rateThreshold:.2f}')
    
    nSamples = len(theSamples.keys())

    triggerGraph = ROOT.TGraph(nSamples)
    triggerCICADAGraph = ROOT.TGraph(nSamples)
    triggerAXOGraph = ROOT.TGraph(nSamples)
    triggerBothGraph = ROOT.TGraph(nSamples)

    for sampleIndex, sampleName in enumerate(theSamples):
        sample = theSamples[sampleName]

        # total info

        # totalEvents = sample.Count().GetValue()
        totalEvents = sample.Sum('pileupWeight').GetValue()

        # un-caught events

        noTriggerSample = sample.Filter(noUnprescaledBitPassesCondition(mcBits))
        # unTriggeredEvents = noTriggerSample.Count().GetValue()
        unTriggeredEvents = noTriggerSample.Sum('pileupWeight').GetValue()
        unCaughtFraction = unTriggeredEvents / totalEvents

        #  reclaimed information

        cicadaReclaimedSample = noTriggerSample.Filter(f'anomalyScore >= {cicada_rateThreshold}')
        axoReclaimedSample = noTriggerSample.Filter(f'uGTAnomalyScore >= {axo_rateThreshold}')
        bothReclaimedSample = noTriggerSample.Filter(f'anomalyScore >= {cicada_rateThreshold} || uGTAnomalyScore >= {axo_rateThreshold}')

        # cicadaReclaimedEvents = cicadaReclaimedSample.Count().GetValue()
        # axoReclaimedEvents = axoReclaimedSample.Count().GetValue()
        # bothReclaimedEvents = bothReclaimedSample.Count().GetValue()
        cicadaReclaimedEvents = cicadaReclaimedSample.Sum("pileupWeight").GetValue()
        axoReclaimedEvents = axoReclaimedSample.Sum("pileupWeight").GetValue()
        bothReclaimedEvents = bothReclaimedSample.Sum("pileupWeight").GetValue()

        cicadaFracReclaimed = cicadaReclaimedEvents / unTriggeredEvents
        axoFracReclaimed = axoReclaimedEvents / unTriggeredEvents
        bothFracReclaimed = bothReclaimedEvents / unTriggeredEvents

        # Total Catch information

        triggerCaughtSample = sample.Filter(anUnprescaledBitPassesCondition(mcBits))
        triggerCICADACaughtSample = sample.Filter(f'{anUnprescaledBitPassesCondition(mcBits)} || anomalyScore >= {cicada_rateThreshold}')
        triggerAXOCaughtSample = sample.Filter(f'{anUnprescaledBitPassesCondition(mcBits)} || uGTAnomalyScore >= {axo_rateThreshold}')
        triggerBothCaughtSample = sample.Filter(f'{anUnprescaledBitPassesCondition(mcBits)} || anomalyScore >= {cicada_rateThreshold} || uGTAnomalyScore >= {axo_rateThreshold}')

        # triggerCaughtEvents = triggerCaughtSample.Count().GetValue()
        # triggerCICADACaughtEvents = triggerCICADACaughtSample.Count().GetValue()
        # triggerAXOCaughtEvents = triggerAXOCaughtSample.Count().GetValue()
        # triggerBothCaughtEvents = triggerBothCaughtSample.Count().GetValue()
        triggerCaughtEvents = triggerCaughtSample.Sum("pileupWeight").GetValue()
        triggerCICADACaughtEvents = triggerCICADACaughtSample.Sum("pileupWeight").GetValue()
        triggerAXOCaughtEvents = triggerAXOCaughtSample.Sum("pileupWeight").GetValue()
        triggerBothCaughtEvents = triggerBothCaughtSample.Sum("pileupWeight").GetValue()

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
            subtitle=f'{rateString} kHz AD'
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
    parser.add_argument(
        '-r',
        '--rate',
        default=10.0,
        type=float,
        help='Nominal overall rate to make the plot for',
        nargs='?'
    )

    args = parser.parse_args()

    main(args)