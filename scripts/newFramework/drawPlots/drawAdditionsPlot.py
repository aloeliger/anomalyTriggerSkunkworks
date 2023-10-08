# !/usr/bin/env python3
import ROOT
import argparse
import os

from rich.console import Console

console = Console()

def main(args):
    ROOT.gStyle.SetOptStat(0)

    console.rule('Loading file')

    theFilename = f'/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/additionPlotsCICADAv{args.CICADAVersion}.root'
    theFile = ROOT.TFile(theFilename, 'READ')
    if theFile.IsZombie():
        console.log('Failed to load file (found zombie)...', style='bold red')
        exit(1)
    else:
        console.log(f'Loaded {theFilename}', style='bold green')
    
    console.rule('Drawing plots')

    triggerGraph = theFile.Get('triggerGraph')
    triggerCICADAGraph = theFile.Get('triggerCICADAGraph')
    if args.includeAXOL1TL:
        triggerAXOGraph = theFile.Get('triggerAXOGraph')
        triggerBothGraph = theFile.Get('triggerBothGraph')

    # trigger: red circle
    # trigger plus AXO: pink square
    # trigger plus CICADA: green triangle
    # trigger plus both: blue star

    triggerGraph.SetMarkerStyle(20)
    triggerCICADAGraph.SetMarkerStyle(22)

    triggerGraph.SetMarkerColor(2)
    triggerCICADAGraph.SetMarkerColor(3)

    if args.includeAXOL1TL:
        triggerAXOGraph.SetMarkerStyle(21)
        triggerBothGraph.SetMarkerStyle(29)

        triggerAXOGraph.SetMarkerColor(6)
        triggerBothGraph.SetMarkerColor(4)

    graphs = [triggerGraph, triggerCICADAGraph]
    if args.includeAXOL1TL:
        graphs.append(triggerAXOGraph)
        graphs.append(triggerBothGraph)

    for graph in graphs:
        graph.SetMarkerSize(2)
        for point in range(graph.GetN()):
            graph.SetPointY(point, graph.GetPointY(point)-0.5)

    finalCanvas = ROOT.TCanvas('AdditionsPlot')
    finalCanvas.SetGridy()
    finalCanvas.SetLeftMargin(0.2)

    triggerGraph.Draw('AP')
    if args.includeAXOL1TL:
        triggerAXOGraph.Draw('P')
    triggerCICADAGraph.Draw('P')
    if args.includeAXOL1TL:
        triggerBothGraph.Draw('P')

    theHist = triggerGraph.GetHistogram()
    theHist.SetTitle('')
    theHist.GetXaxis().SetTitle('Acceptance')
    # theHist.GetYaxis().SetRangeUser(0.0, 5.0)
    theHist.GetYaxis().SetNdivisions(5,0,0)

    # theHist.GetYaxis().SetBinLabel(2,'Hto2LongLivedTo4b')
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

    rateLatex = ROOT.TLatex()
    cmsLatex.SetTextSize(0.04)
    cmsLatex.SetNDC(True)
    cmsLatex.SetTextAlign(12)
    cmsLatex.SetTextFont(42)
    if args.includeAXOL1TL:
        cmsLatex.DrawLatex(0.2, 0.92, '10 kHz Overall Rate AD, Each')
    else:
        cmsLatex.DrawLatex(0.2, 0.92, '10 kHz Overall Rate AD')

    theLegend = ROOT.TLegend(0.5, 0.73, 0.9, 0.9)
    theLegend.SetBorderSize(0)
    theLegend.SetFillStyle(0)
    theLegend.SetNColumns(2)
    theLegend.AddEntry(triggerGraph, 'L1T', 'p')
    theLegend.AddEntry(triggerCICADAGraph, 'L1T+CICADA', 'p')
    if args.includeAXOL1TL:
        theLegend.AddEntry(triggerAXOGraph, 'L1T+AXOL1TL', 'p')
        theLegend.AddEntry(triggerBothGraph, 'L1T+AXOL1TL+CICADA', 'p')
    theLegend.Draw()


    destinationPath = f'/nfs_scratch/aloeliger/anomalyPlotFiles/pngFiles/additionsPlotsCICADAv{args.CICADAVersion}/'
    if args.includeAXOL1TL:
        plotName = f'additionsPlotCICADAv{args.CICADAVersion}AndAXOL1TL.png'
    else:
        plotName = f'additionsPlotCICADAv{args.CICADAVersion}.png'
    if not os.path.isdir(destinationPath):
        os.makedirs(destinationPath, exist_ok=True)
    finalCanvas.SaveAs(f'{destinationPath}/{plotName}')

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
    parser.add_argument(
        '-a',
        '--includeAXOL1TL',
        action='store_true',
        help='Use AXOL1TL in the plots'
    )

    args = parser.parse_args()

    main(args)