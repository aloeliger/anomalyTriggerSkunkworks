# !/usr/bin/env python3

import ROOT
import argparse

from rich.console import Console
from collections import OrderedDict

console = Console()

def main(args):
    ROOT.gStyle.SetOptStat(0)

    console.rule('Loading file')

    theFilename = f'/nfs_scratch/aloeliger/anomalyPlotFiles/pileupPlots/pileupPlotsCICADAv{args.CICADAVersion}.root'
    theFile = ROOT.TFile(theFilename, 'READ')
    if theFile.IsZombie():
        console.log(f'Failed to load file (found zombie)...', style='bold red')
        exit(1)
    else:
        console.log(f'Loaded {theFilename}', style='bold green')

    console.rule('Drawing plots')

    # draw the simple score plots

    simpleScoreCanvas = ROOT.TCanvas('SimpleScoreCanvas')
    simpleScoreGraph = theFile.Get('scoreVsPU')
    simpleScoreGraph.SetMarkerStyle(7)
    simpleScoreGraph.SetMarkerColor(ROOT.kRed)
    simpleScoreGraph.Draw('AP')
    simpleScoreGraph.GetHistogram().SetTitle('')

    simpleScoreCanvas.SaveAs(f'scoreVsPU_CICADAv{args.CICADAVersion}.png')

    # draw the avg rate per lumi plot
    rateSettings = OrderedDict(
        [
            (10, ROOT.kCyan),
            (5, 28),
            (3, ROOT.kGreen),
            (2, ROOT.kBlue),
            (1, ROOT.kRed),
        ]
    )
    ratePerPUCanvas = ROOT.TCanvas('RatePerPUCanvas')
    ratePerPUCanvas.SetLogy()
    firstGraph = True
    for rate in rateSettings:
        theGraph = theFile.Get(f'PURateGraph_{rate}')
        theGraph.SetMarkerStyle(20)
        theGraph.SetLineColor(rateSettings[rate])
        theGraph.SetMarkerColor(rateSettings[rate])

        if firstGraph:
            theLegend = ROOT.TLegend(0.15,0.7,0.35,0.9)
            theGraph.Draw('ALP')
            firstGraph = False
            
            theHistogram = theGraph.GetHistogram()
            theHistogram.SetTitle('')
            theHistogram.GetXaxis().SetTitle('Number of Primary Vertices')
            theHistogram.GetYaxis().SetTitle('Average Rate (kHz)')
            theHistogram.GetYaxis().SetRangeUser(0.1, 100.0)
        else:
            theGraph.Draw('LP')
        
        theLegend.AddEntry(theGraph, f'Nominal {rate} kHz', 'lp')
    theLegend.Draw()
    ratePerPUCanvas.SaveAs(f'ratePerPU_CICADAv{args.CICADAVersion}.png')

    # draw the CICADA versus single mu rate plot
    rateVsSingleMuCanvas = ROOT.TCanvas('RateVsSingleMuCanvas')
    firstGraph = True
    for rate in rateSettings:
        theGraph = theFile.Get(f'CICADAvsSingleMu_{rate}')
        theGraph.SetMarkerStyle(7)
        theGraph.SetMarkerColor(rateSettings[rate])

        if firstGraph:
            theLegend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
            theGraph.Draw('AP')
            firstGraph = False

            theHistogram = theGraph.GetHistogram()
            theHistogram.SetTitle('')
            theHistogram.GetXaxis().SetTitle('Single Mu Rate (kHz)')
            theHistogram.GetYaxis().SetTitle('CICADA Rate (kHz)')
            theHistogram.GetXaxis().SetRangeUser(0, 45)
        else:
            theGraph.Draw('P')

        theLegend.AddEntry(theGraph, f'Nominal {rate} kHz', 'p')

    theLegend.Draw()
    rateVsSingleMuCanvas.SaveAs(f'rateVsSingleMu_CICADAv{args.CICADAVersion}.png')
    console.rule('')
    console.print('')
    console.print('')          

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Draw pileup plots from existing file")
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