# !/usr/bin/env python3

import ROOT
import argparse
import os
from anomalyDetection.anomalyTriggerSkunkworks.plotSettings.utilities import convertRateToEff

from rich.console import Console
from rich.traceback import install

console = Console()
install()

def main(args):
    ROOT.gStyle.SetOptStat(0)

    console.rule('Loading file')
    fileName = f'/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/ROCAndHTCICADAv{args.CICADAVersion}.root'
    theFile = ROOT.TFile(fileName, 'READ')
    if theFile.IsZombie():
        console.log(f'Failed to load file (found zombie)...', style='bold red')
        exit(1)
    else:
        console.log(f'Loaded {fileName}', style='bold green')

    console.rule('Drawing plots')

    signals = [
        'Hto2LongLivedTo4b',
        'SUSYGluGlutoBBHtoBB',
        'TT',
        'VBFHto2C',
        'SUEP'        
    ]

    rateEffs = {
        '10 kHz Overall': convertRateToEff(10.0),
        '5 kHz Overall': convertRateToEff(5.0),
        '3 kHz Overall': convertRateToEff(3.0),
        '2 kHz Overall': convertRateToEff(2.0),
        '1 kHz Overall': convertRateToEff(1.0),
    }

    lineColors = {
        '10 kHz Overall': 40,
        '5 kHz Overall': 30,
        '3 kHz Overall': 42,
        '2 kHz Overall': 46,
        '1 kHz Overall': 28,           
    }

    destinationPath = f'/nfs_scratch/aloeliger/anomalyPlotFiles/pngFiles/rocPlusHTCurvesCICADAv{args.CICADAVersion}/'
    os.makedirs(destinationPath, exist_ok=True)

    for signal in signals:
        CICADAName = f'{signal}_CICADA_ROC'
        HTName = f'{signal}_HT_ROC'

        cicadaGraph = theFile.Get(CICADAName)
        htGraph = theFile.Get(HTName)

        theCanvas = ROOT.TCanvas('canvas')

        cicadaGraph.Draw('ALP')
        htGraph.Draw('LP')

        cicadaGraph.SetLineColor(ROOT.kRed)
        cicadaGraph.SetLineWidth(2)
        cicadaGraph.SetMarkerStyle(20)
        cicadaGraph.SetMarkerColor(ROOT.kRed)

        htGraph.SetLineColor(ROOT.kBlack)
        htGraph.SetMarkerStyle(20)
        htGraph.SetMarkerColor(ROOT.kBlack)

        theHist = cicadaGraph.GetHistogram()

        theHist.GetXaxis().SetTitle('Background Acceptance')
        theHist.GetYaxis().SetRangeUser(0.0, 1.0)
        theHist.GetYaxis().SetTitle('Signal Acceptance')

        lines = {}
        for index, rate in enumerate(rateEffs):
            rateLine = ROOT.TLine(
                rateEffs[rate],
                0.0,
                rateEffs[rate],
                1.0
            )
            rateLine.SetLineColor(lineColors[rate])
            rateLine.SetLineWidth(2)
            rateLine.SetLineStyle(9)
            rateLine.Draw()

            lines[rate] = rateLine

        cicadaGraph.SetTitle('')

        theLegend = ROOT.TLegend (0.4, 0.75, 0.9, 0.9)
        theLegend.SetNColumns(3)
        for rate in lines:
            theLegend.AddEntry(lines[rate], rate, 'l')
        theLegend.AddEntry(cicadaGraph, 'CICADA ROC', 'l')
        theLegend.AddEntry(htGraph, 'HT ROC', 'l')
        theLegend.Draw()

        cmsLatex = ROOT.TLatex()
        cmsLatex.SetTextSize(0.04)
        cmsLatex.SetNDC(True)
        cmsLatex.SetTextAlign(11)
        cmsLatex.DrawLatex(0.1,0.92, "#font[61]{CMS} #font[52]{Preliminary}")

        signalLatex = ROOT.TLatex()
        signalLatex.SetTextSize(0.04)
        signalLatex.SetNDC(True)
        signalLatex.SetTextAlign(31)
        signalLatex.DrawLatex(0.9,0.92, "#font[61]{"+signal+"}")

        theCanvas.SaveAs(f'{destinationPath}/{signal}_CICADAv{args.CICADAVersion}.png')
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