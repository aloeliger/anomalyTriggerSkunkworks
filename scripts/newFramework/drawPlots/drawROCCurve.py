# !/usr/bin/env python3

import ROOT
import argparse
import itertools
from rich.console import Console
from rich.table import Table

console = Console()

def main(args):
    console.rule('Loading file')

    ROOT.gStyle.SetOptStat(0)

    fileName = f'/nfs_scratch/aloeliger/anomalyPlotFiles/rocCurves/rocCurveFileCICADAv{args.CICADAVersion}.root'
    theFile = ROOT.TFile(fileName, 'READ')
    if theFile.IsZombie():
        console.log(f'Failed to load file (found zombie)...', style='bold red')
        exit(1)
    else:
        console.log(f'Loaded {fileName}', style='bold green')
    
    console.rule('Drawing plots')

    backgrounds = [
        'RunCEphemeralZeroBias',
        'RunDEphemeralZeroBias',
        'ZeroBiasPlusRunCEphemeralZeroBias'
    ]
    signals = [
        'Hto2LongLivedTo4b',
        'SUSYGluGlutoBBHtoBB',
        'TT',
        'VBFHto2C',
        'SUEP'
    ]

    backgroundSignalCombinations = itertools.product(
        backgrounds,
        signals
    )
    backgroundSignalCombinations = list(backgroundSignalCombinations)

    spreadTypes = [
        'CompleteSpread',
        'FreqSpread',
    ]

    rateEffs = {
        '10 kHz': 0.00034405405,
        '5 kHz': 0.00017202702,
        '3 kHZ': 0.00010321621,
        '2 kHz': 0.00006881081,
        '1 kHz': 0.0000344054,
    }

    for spreadType in spreadTypes:
        for combination in backgroundSignalCombinations:
            histoName = f'{combination[0]}_{combination[1]}_{spreadType}_ROC'
            with console.status(histoName):
                theGraph = theFile.Get(histoName)
                # inspect(theGraph)
                canvasName = histoName + '_canvas'
                theCanvas = ROOT.TCanvas(canvasName)

                # theCanvas.SetLogx()
                # theCanvas.SetLogy()

                theGraph.Draw('ALP')

                theGraph.SetLineColor(ROOT.kRed)
                theGraph.SetLineWidth(2)
                theGraph.SetMarkerStyle(20)
                theGraph.SetMarkerColor(ROOT.kRed)

                theHist = theGraph.GetHistogram()

                # theHist.GetXaxis().SetRangeUser(1e-4, 1e-1)
                if spreadType == 'CompleteSpread':
                    theHist.GetXaxis().SetRangeUser(0.0, 1.0)
                theHist.GetXaxis().SetTitle('Background Acceptance')

                theHist.GetYaxis().SetRangeUser(0.0, 1.0)
                theHist.GetYaxis().SetTitle('Signal Acceptance')

                if spreadType == 'FreqSpread':
                    lines = []
                    texts = []
                    for index, rate in enumerate(rateEffs):
                        rateLine = ROOT.TLine(
                            rateEffs[rate],
                            0.0,
                            rateEffs[rate],
                            1.0
                        )
                        rateLine.SetLineColor(ROOT.kBlue)
                        rateLine.SetLineWidth(2)
                        rateLine.Draw()

                        rateText = ROOT.TLatex(rateEffs[rate], 0.9-index*0.1, f'{rate}')
                        rateText.Draw()

                        lines.append(rateLine)
                        texts.append(rateText)

                theGraph.SetTitle('')
                theCanvas.SaveAs(histoName+f'_CICADAv{args.CICADAVersion}.png')

    console.rule('AUCs')

    theTable = Table(title_style='underline', expand=True)

    theTable.add_column("Background", style='bold red', justify='center')
    theTable.add_column("Signal", style='bold green', justify='center')
    theTable.add_column('AUC', style='black on white', justify='right')

    previousSection = ''
    for combination in backgroundSignalCombinations:
        if combination[0] != previousSection:
            theTable.add_section()
            previousSection = combination[0]
        histoName = f'{combination[0]}_{combination[1]}_CompleteSpread_ROC'
        with console.status(histoName):
            theGraph = theFile.Get(histoName)
            theAUC = 0.0
            for i in range(1,101):
                theAUC += theGraph.GetPointY(i)*(1.0/100.0)

            theTable.add_row(f"{combination[0]}", f"{combination[1]}", f'{theAUC:.3g}')
    console.print(theTable)

    console.print('')
    console.print('')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Draw ROC curve plots from existing file")
    parser.add_argument(
        '-v',
        '--CICADAVersion',
        default=1,
        type=int,
        help='CICADA version to draw',
        choices = [1, 2],
        nargs='?',
    )

    args = parser.parse_args()

    main(args)