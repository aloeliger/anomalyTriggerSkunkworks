# !/usr/bin/env python3

import ROOT
import argparse
import os

from rich.console import Console
from collections import OrderedDict

console = Console()

def main(args):
    ROOT.gStyle.SetOptStat(0)
    ROOT.gStyle.SetPaintTextFormat('1.3g')

    console.rule('Loading file')

    theFilename = f'/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/pileupPlotsCICADAv{args.CICADAVersion}.root'
    theFile = ROOT.TFile(theFilename, 'READ')
    if theFile.IsZombie():
        console.log(f'Failed to load file (found zombie)...', style='bold red')
        exit(1)
    else:
        console.log(f'Loaded {theFilename}', style='bold green')

    destinationPath = f'/nfs_scratch/aloeliger/anomalyPlotFiles/pngFiles/pileupPlotsCICADAv{args.CICADAVersion}/'
    os.makedirs(destinationPath, exist_ok=True)

    console.rule('Drawing plots')

    # setup the cmsLatex that goes into each of these plots
    cmsLatex = ROOT.TLatex()
    cmsLatex.SetTextSize(0.05)
    cmsLatex.SetNDC(True)
    cmsLatex.SetTextAlign(32)

    # draw the simple score plots

    simpleScoreCanvas = ROOT.TCanvas('SimpleScoreCanvas')
    simpleScoreGraph = theFile.Get('scoreVsPU')
    simpleScoreGraph.SetMarkerStyle(7)
    simpleScoreGraph.SetMarkerColor(ROOT.kRed)
    simpleScoreGraph.Draw('AP')
    simpleScoreGraph.GetHistogram().SetTitle('')

    cmsLatex.DrawLatex(0.9,0.92, "#font[61]{CMS} #font[52]{Preliminary}")

    simpleScoreCanvas.SaveAs(f'{destinationPath}/scoreVsPU_CICADAv{args.CICADAVersion}.png')

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

    cmsLatex.DrawLatex(0.9,0.92, "#font[61]{CMS} #font[52]{Preliminary}")

    ratePerPUCanvas.SaveAs(f'{destinationPath}/ratePerPU_CICADAv{args.CICADAVersion}.png')

    # draw the CICADA versus single mu rate plot
    rateVsSingleMuCanvas = ROOT.TCanvas('RateVsSingleMuCanvas')
    firstGraph = True
    rateGraphs = {}
    for rate in rateSettings:
        theGraph = theFile.Get(f'CICADAvsSingleMu_{rate}')
        theGraph.SetMarkerStyle(20)
        theGraph.SetMarkerColor(rateSettings[rate])
        # theGraph.SetMarkerSize(5)

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
        rateGraphs[rate] = theGraph

    theLegend.Draw()

    cmsLatex.DrawLatex(0.9,0.92, "#font[61]{CMS} #font[52]{Preliminary}")

    rateVsSingleMuCanvas.SaveAs(f'{destinationPath}/rateVsSingleMu_CICADAv{args.CICADAVersion}.png')

    # let's use the CICADA versus single mu rate plot to construct a
    # profile of CICADA rate versus single mu rate per nominal rate
    profileCanvas = ROOT.TCanvas("profileCanvas")
    for rate in rateGraphs:
        thePlot = ROOT.TH2D(
            f"{rate}kHzVsSingleMu",
            f"{rate}kHzVsSingleMu",
            20,
            0.0,
            25.0,
            20,
            0.0,
            70.0,
        )
        theRelevantGraph = rateGraphs[rate]
        for i in range(theRelevantGraph.GetN()):
            thePlot.Fill(
                theRelevantGraph.GetPointX(i),
                theRelevantGraph.GetPointY(i),
            )
        thePlot.Scale(1.0/thePlot.Integral())
        thePlot.Draw("COLZ TEXT")

        thePlot.GetXaxis().SetTitle('Single Mu Rate (kHz)')
        thePlot.GetYaxis().SetTitle('CICADA Rate (kHz)')
        thePlot.SetTitle("")

        cmsLatex.DrawLatex(0.9,0.92, "#font[61]{CMS} #font[52]{Preliminary}")

        rateLatex = ROOT.TLatex()
        rateLatex.SetTextSize(0.05)
        rateLatex.SetNDC(True)
        rateLatex.SetTextAlign(12)
        rateLatex.DrawLatex(0.1, 0.92, "#font[61]{"+f"Nominal {rate} kHz Overall"+"}")

        profileCanvas.SaveAs(f'{destinationPath}/{rate}kHzVsSingleMu.png')

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