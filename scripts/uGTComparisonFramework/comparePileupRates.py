#This should be a quick thing to determine what our threshold's rates are across a series of PU bins
#

import argparse
from samples.pileupSamples import pileupSample
from tqdm import trange
import ROOT
from anomalyTriggerThresholds.thresholdHelper import thresholdHelper
import math

def main(args):
    theThresholdHelper = thresholdHelper()
    rateThresholds = [
        "0.5",
        "1",
        "2",
        "3"
    ]
    triggers = [
        "CICADA",
        "uGT" #now AXOL1TL
    ]

    maxPU = 120.0
    minPU = 0.0
    PUperBin = 5.0
    puBins = math.ceil((maxPU-minPU)/PUperBin)

    entriesToProcess = pileupSample.GetEntries()

    infoStorage = {}

    for trigger in triggers:
        infoStorage[trigger] = {}
        for rateThreshold in rateThresholds:
            numeratorHisto = ROOT.TH1F(
                f'{trigger}_{rateThreshold}_num',
                f'{trigger}_{rateThreshold}_num',
                puBins,
                minPU,
                maxPU
            )
            denominatorHisto = ROOT.TH1F(
                f'{trigger}_{rateThreshold}_denom',
                f'{trigger}_{rateThreshold}_denom',
                puBins,
                minPU,
                maxPU
            )
            theThreshold = theThresholdHelper.getTriggerThreshold(trigger, rateThreshold)
            #yikes
            infoStorage[trigger][rateThreshold] = (theThreshold, numeratorHisto, denominatorHisto)
    #At least it only loops the chain once...
    for i in trange(entriesToProcess):
        pileupSample.GetEntry(i)
        for trigger in infoStorage:
            if trigger == 'CICADA':
                triggerVar = pileupSample.chain.precompiledModelAnomalyScore
            elif trigger == 'uGT':
                triggerVar = pileupSample.chain.uGTAnomalyScore
            
            for rateThreshold in infoStorage[trigger]:
                packedInfo = infoStorage[trigger][rateThreshold]
                packedInfo[2].Fill(pileupSample.chain.npv)
                if triggerVar > packedInfo[0]:
                    packedInfo[1].Fill(pileupSample.chain.npv)

    theFile = ROOT.TFile(args.theFile, 'RECREATE')
    for trigger in infoStorage:
        for rateThreshold in infoStorage[trigger]:
            infoStorage[trigger][rateThreshold][1].Write()
            infoStorage[trigger][rateThreshold][2].Write()
    theFile.Write()
    theFile.Close()
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get pileup information')

    parser.add_argument(
        '--theFile',
        default='pileupRates.root',
        nargs='?',
        help='Output plot file'
    )

    args = parser.parse_args()
    main(args)