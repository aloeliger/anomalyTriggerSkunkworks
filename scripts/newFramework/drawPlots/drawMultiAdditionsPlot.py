# !/usr/bin/env python3
import ROOT
import argparse
import os

from rich.console import Console

console = Console()

def main(args):
    ROOT.gStyle.SetOptStat(0)

    with console.status("Loading files..."):
        
        filePath = '/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/'
        
        onekHzFileName = f'{filePath}/additionPlots_1p0kHz_CICADAv{args.CICADAVersion}.root'
        threekHzFileName = f'{filePath}/additionPlots_3p0kHz_CICADAv{args.CICADAVersion}.root'
        fivekHzFileName = f'{filePath}/additionPlots_5p0kHz_CICADAv{args.CICADAVersion}.root'
        tenkHzFileName = f'{filePath}/additionPlots_10p0kHz_CICADAv{args.CICADAVersion}.root'

        onekHzFile = ROOT.TFile(onekHzFileName)
        threekHzFile = ROOT.TFile(threekHzFileName)
        fivekHzFile = ROOT.TFile(fivekHzFileName)
        tenkHzFile = ROOT.TFile(tenkHzFileName)

    with console.status("Drawing plots..."):

        triggerGraph = onekHzFile.Get('triggerGraph')
        onekHzCICADAGraph = onekHzFile.Get('triggerCICADAGraph')
        threekHzCICADAGraph = threekHzFile.Get('triggerCICADAGraph')
        fivekHzCICADAGraph = fivekHzFile.Get('triggerCICADAGraph')
        tenkHzCICADAGraph = tenkHzFile.Get('triggerCICADAGraph')

        triggerGraph.SetMarkerStyle(20)
        onekHzCICADAGraph.SetMarkerStyle(21)
        threekHzCICADAGraph.SetMarkerStyle(22)
        fivekHzCICADAGraph.SetMarkerStyle(23)
        tenkHzCICADAGraph.SetMarkerStyle(33)

        triggerGraph.SetMarkerColor(2)
        onekHzCICADAGraph.SetMarkerColor(ROOT.kGreen+3)
        threekHzCICADAGraph.SetMarkerColor(4)
        fivekHzCICADAGraph.SetMarkerColor(6)
        tenkHzCICADAGraph.SetMarkerColor(ROOT.kOrange-3)

        graphs = [
            triggerGraph,
            onekHzCICADAGraph,
            threekHzCICADAGraph,
            fivekHzCICADAGraph,
            tenkHzCICADAGraph
        ]

        for graph in graphs:
            graph.SetMarkerSize(2)
            for point in range(graph.GetN()):
                graph.SetPointY(point, graph.GetPointY(point)-0.5)
        
        finalCanvas = ROOT.TCanvas('AdditionsPlot')
        finalCanvas.SetGridy()
        finalCanvas.SetLeftMargin(0.2)
        finalCanvas.SetTopMargin(0.3)

        triggerGraph.Draw('AP')
        onekHzCICADAGraph.Draw('P')
        threekHzCICADAGraph.Draw('P')
        fivekHzCICADAGraph.Draw('P')
        tenkHzCICADAGraph.Draw('P')

        theHist = triggerGraph.GetHistogram()
        theHist.SetTitle('')
        theHist.GetXaxis().SetTitle('Acceptance')
        theHist.GetYaxis().SetNdivisions(5,0,0)

        theHist.GetYaxis().SetLabelSize(0.0)

        labelLatex = ROOT.TLatex()
        labelLatex.SetTextSize(0.025)
        labelLatex.SetTextAlign(32)
        labelLatex.SetTextFont(42)
        labelLatex.DrawLatex(0.0, 0.5, 'Hto2LongLivedTo4b')
        labelLatex.DrawLatex(0.0, 1.5, 'SUSYGluGlutoBBHtoBB')
        labelLatex.DrawLatex(0.0, 2.5, 'T#bar{T}')
        labelLatex.DrawLatex(0.0, 3.5, 'VBFHto2C')
        labelLatex.DrawLatex(0.0, 4.5, 'SUEP')

        cmsLatex = ROOT.TLatex()
        cmsLatex.SetTextSize(0.05)
        cmsLatex.SetNDC(True)
        cmsLatex.SetTextAlign(32)
        cmsLatex.DrawLatex(0.9,0.92, "#font[61]{CMS} #font[52]{Preliminary}")

        theLegend = ROOT.TLegend(0.2, 0.70, 0.9, 0.9)
        theLegend.SetBorderSize(0)
        theLegend.SetFillStyle(0)
        theLegend.SetNColumns(2)
        theLegend.AddEntry(triggerGraph, 'L1T', 'p')
        theLegend.AddEntry(onekHzCICADAGraph, 'L1T+ 1 kHz (overall) CICADA', 'p')
        theLegend.AddEntry(threekHzCICADAGraph, 'L1T+ 3 kHz (overall) CICADA', 'p')
        theLegend.AddEntry(fivekHzCICADAGraph, 'L1T+ 5 kHz (overall) CICADA', 'p')
        theLegend.AddEntry(tenkHzCICADAGraph, 'L1T+ 10 kHz (overall) CICADA', 'p')

        theLegend.Draw()

        destinationPath = f'/nfs_scratch/aloeliger/anomalyPlotFiles/pngFiles/multiAdditionsPlotsCICADAv{args.CICADAVersion}/'

        plotName = f'multiAdditionsPlotCICADAv{args.CICADAVersion}.png'
        if not os.path.isdir(destinationPath):
            os.makedirs(destinationPath, exist_ok=True)
        finalCanvas.SaveAs(f'{destinationPath}/{plotName}')

        console.print('')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Draw the additions plots for multiple rates")
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