# !/usr/bin/env python3

import ROOT
import argparse
from anomalyDetection.anomalyTriggerSkunkworks.samples.ephemeralZeroBiasSamples2018.ephemeralZeroBiasAll2018 import EphemeralZeroBiasSample
from tqdm import tqdm, trange

def translateModelInput(theChain):
    # calorimeterDeposits[18][14]
    # 18 in iPhi, 14 in iEta
    # It is stored in 18 14 order, but as one index
    calorimeterDeposits = []
    for i in range(18):
        theRow = []
        for j in range(14):
            theDeposit = theChain.modelInput [14*i + j]
            theRow.append(theDeposit)
        calorimeterDeposits.append(theRow)
    return calorimeterDeposits

def fillCaloImage(theHistogram, theDeposits):
    for i in range(18):
        for j in range(14):
            theHistogram.Fill(
                float(i),
                float(j),
                theDeposits[i][j]
            )
    return theHistogram

def main(args):
    outputFile = ROOT.TFile(f'/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/calorimeterImagesCICADAv{args.CICADAVersion}.root', 'RECREATE')

    conditions = [
        'anomalyScore > 0.0',
        'anomalyScore > 3.0',
        'anomalyScore > 5.0',
        'anomalyScore > 6.0',
    ]
    conditionNames = {
        'anomalyScore > 0.0': 'ZeroBias',
        'anomalyScore > 3.0': 'GT3',
        'anomalyScore > 5.0': 'GT5',
        'anomalyScore > 6.0': 'GT6',
    }

    for condition in tqdm(conditions, ascii=True, dynamic_ncols=True, leave=False, desc='Conditions'):
        theChain = EphemeralZeroBiasSample.getNewChain(
            [
                f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',            
            ]
        )
        theChain = theChain.CopyTree(condition)

        theHisto = ROOT.TH2D(
            conditionNames[condition],
            conditionNames[condition],
            18,
            0.0,
            18.0,
            14,
            0.0,
            14.0
        )

        nEntries = min(int(1e6), theChain.GetEntries())

        for entryNum in trange(nEntries, ascii=True, dynamic_ncols=True, leave=False, desc='Entries'):
            theChain.GetEntry(entryNum)

            caloDeposits = translateModelInput(theChain)

            theHisto = fillCaloImage(theHisto, caloDeposits)
        theHisto.Write()
    outputFile.Write()
    outputFile.Close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Create plots showing the ")
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