# !/usr/bin/env python3

import ROOT
import argparse
import os

def createRatioPlot(denom, num):
    denomPlot = denom.Clone()
    ratioPlot = num.Clone()
    ratioPlot.Divide(denomPlot)

    return ratioPlot

def createScorePlots(theFile, run, CICADAVersion, destinationPath):
    CICADAScorePlot = getattr(theFile, f'{run}_CICADA_score').Clone()
    miniCICADAv1Plot = getattr(theFile, f'{run}_miniCICADAv1p0_score').Clone()
    miniCICADAv1p1Plot = getattr(theFile, f'{run}_miniCICADAv1p1_score').Clone()
    CICADAPlusCINPlot = getattr(theFile, f'{run}_CICADAPlusCIN_score').Clone()

    CICADAScorePlot.Scale(1.0/CICADAScorePlot.Integral())
    miniCICADAv1Plot.Scale(1.0/miniCICADAv1Plot.Integral())
    miniCICADAv1p1Plot.Scale(1.0/miniCICADAv1p1Plot.Integral())
    CICADAPlusCINPlot.Scale(1.0/CICADAPlusCINPlot.Integral())

    theCanvas = ROOT.TCanvas(f'{run}_score_canvas')

    theCanvas.cd()
    plotPad = ROOT.TPad('plotPad', 'plotPad', 0.0, 0.3, 1.0, 1.0)
    plotPad.SetBottomMargin(0.0)
    plotPad.Draw()
    theCanvas.cd()
    ratioPad = ROOT.TPad('ratioPad', 'ratioPad', 0.0, 0.0, 1.0, 0.3)
    ratioPad.SetTopMargin(0.0)
    ratioPad.SetBottomMargin(0.25)
    ratioPad.Draw()
    # theCanvas.ls()
    # plotPad.ls()
    # ratioPad.ls()
    #theCanvas.Divide(3,3)
    #theCanvas.ls()
    # exit()

    plotPad.cd()
    plotPad.SetLogy()

    CICADAScorePlot.SetMarkerStyle(20)
    CICADAScorePlot.Draw('E1')
    CICADAScorePlot.SetTitle('')
    CICADAScorePlot.GetXaxis().SetTitle('')
    CICADAScorePlot.GetYaxis().SetTitle('Fraction Events')

    miniCICADAv1Plot.SetMarkerStyle(20)
    miniCICADAv1Plot.SetMarkerColor(41)
    miniCICADAv1Plot.SetLineColor(41)
    miniCICADAv1Plot.Draw('E1 SAME')

    miniCICADAv1p1Plot.SetMarkerStyle(20)
    miniCICADAv1p1Plot.SetMarkerColor(42)
    miniCICADAv1p1Plot.SetLineColor(42)
    miniCICADAv1p1Plot.Draw('E1 SAME')

    CICADAPlusCINPlot.SetMarkerStyle(20)
    CICADAPlusCINPlot.SetMarkerColor(46)
    CICADAPlusCINPlot.SetLineColor(46)
    CICADAPlusCINPlot.Draw('E1 SAME')

    theLegend = ROOT.TLegend(0.7,0.7,0.9,0.9)
    theLegend.AddEntry(CICADAScorePlot, f'CICADA v{CICADAVersion}', 'lp')
    theLegend.AddEntry(miniCICADAv1Plot, 'miniCICADA v1', 'lp')
    theLegend.AddEntry(miniCICADAv1p1Plot, 'miniCICADA v1.1', 'lp')
    theLegend.AddEntry(CICADAPlusCINPlot, 'CICADA + CIN v1', 'lp')
    theLegend.Draw()

    runLatex = ROOT.TLatex()
    runLatex.SetTextSize(0.05)
    runLatex.SetNDC(True)
    runLatex.SetTextAlign(31)
    runLatex.DrawLatex(0.9, 0.92, '#font[62]{Run ' + run[3]+'}')

    plotPad.Update()

    ratioPad.cd()
    ratioPad.SetGridy()

    miniCICADAv1Ratio = createRatioPlot(denom=CICADAScorePlot, num=miniCICADAv1Plot)
    miniCICADAv1p1Ratio = createRatioPlot(denom=CICADAScorePlot, num=miniCICADAv1p1Plot)
    CICADAPlusCINRatio = createRatioPlot(denom=CICADAScorePlot, num=CICADAPlusCINPlot)

    miniCICADAv1Ratio.SetTitle('')
    miniCICADAv1Ratio.Draw('E1')
    miniCICADAv1Ratio.GetXaxis().SetTitle('Score')
    miniCICADAv1Ratio.GetXaxis().SetTitleSize(0.1)
    miniCICADAv1Ratio.GetXaxis().SetLabelSize(0.1)
    miniCICADAv1Ratio.GetXaxis().SetTitleOffset(0.8)
    miniCICADAv1Ratio.GetYaxis().SetTitle('Ratio to CICADA')
    miniCICADAv1Ratio.GetYaxis().SetTitleSize(0.1)
    miniCICADAv1Ratio.GetYaxis().SetTitleOffset(0.25)
    miniCICADAv1Ratio.GetYaxis().SetLabelSize(0.1)
    miniCICADAv1Ratio.GetYaxis().CenterTitle()
    miniCICADAv1Ratio.GetYaxis().SetRangeUser(-0.5,5)

    miniCICADAv1p1Ratio.Draw('E1 SAME')
    CICADAPlusCINRatio.Draw('E1 SAME')

    ratioPad.Update()

    # theCanvas.cd()
    theCanvas.SaveAs(f'{destinationPath}/{run}_CICADAv{CICADAVersion}_scorePlot.png')

def main(args):
    ROOT.gStyle.SetOptStat(0)
    theFile = ROOT.TFile(f'/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/approximationPlotsCICADAv{args.CICADAVersion}.root')
    destinationPath = f'/nfs_scratch/aloeliger/anomalyPlotFiles/pngFiles/approximationPlotsCICADAv{args.CICADAVersion}'
    if not os.path.isdir(destinationPath):
        os.mkdir(destinationPath)
    
    runs = [
        'RunA',
        'RunB',
        'RunC',
        'RunD',
    ]

    # First, let's draw the bare score comparisons
    for run in runs:
        createScorePlots(
            theFile,
            run,
            args.CICADAVersion,
            destinationPath,
        )
    # Then we can draw the bare error comparisons
    # Then the absolute error comparisons

    theFile.Close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Draw score plots for CICADA versions")
    parser.add_argument(
        '-v',
        '--CICADAVersion',
        default=1,
        type=int,
        help = 'CICADA version',
        choices = [1,2],
        nargs='?'
    )

    args = parser.parse_args()

    main(args)