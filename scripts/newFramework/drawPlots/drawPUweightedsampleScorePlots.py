# !/usr/bin/env python3
import ROOT
import argparse
import os

from rich.console import Console
from rich.traceback import install
from rich.progress import track

console = Console()
install(show_locals=True)

def main(args):
    ROOT.gStyle.SetOptStat(0)
    theFile = ROOT.TFile(f'/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/sampleScorePlotsCICADAv{args.CICADAVersion}.root')
    destinationPath = f'/nfs_scratch/aloeliger/anomalyPlotFiles/pngFiles/sampleScorePlotsCICADAv{args.CICADAVersion}/'
    if not os.path.isdir(destinationPath):
        os.mkdir(destinationPath)
    plots = {
        'ZeroBias_score':{
            'color':ROOT.kBlack,
            'name': 'Zero Bias',
        },
        'LLP_score':{
            'color': ROOT.kRed - 3,
            'name': 'H to Long Lived to 4b',
        },
        'SUS_score': {
            'color': ROOT.kBlue - 7,
            'name': 'SUS Glu Glu to BBH to BB',
        },
        'TT_score': {
            'color': ROOT.kGreen - 3,
            'name': 't#bar{t}',
        },
        'VBF_score': {
            'color': ROOT.kCyan - 3,
            'name': 'VBF H to 2 C',
        },
        'SUEP_score': {
            'color': ROOT.kViolet,
            'name': 'SUEP',
        }
    }

    theCanvas = ROOT.TCanvas('theCanvas', 'theCanvas')
    theCanvas.SetLogy()

    theLegend = ROOT.TLegend(0.5, 0.69, 0.9, 0.89)
    theLegend.SetBorderSize(0)
    # theLegend.SetLineWidth(2)
    for index, plotName in enumerate(plots):
        thePlot = theFile.Get(plotName)

        thePlot.SetMarkerStyle(20)
        # thePlot.SetMarkerSize(2)
        thePlot.SetMarkerColor(plots[plotName]['color'])
        thePlot.SetLineColor(plots[plotName]['color'])
        # thePlot.SetLineWidth(2)

        thePlot.Scale(1.0/thePlot.Integral())

        if index == 0:
            thePlot.Draw('E1 X0')
            thePlot.GetXaxis().SetTitle('CICADA score')
            thePlot.GetYaxis().SetTitle('Fraction (normalized to 1)')
            thePlot.SetTitle('')
        else:
            thePlot.Draw('SAME E1 X0')
        theLegend.AddEntry(thePlot, f'{plots[plotName]["name"]}', 'pl')
    theLegend.Draw()

    cmsLatex = ROOT.TLatex()
    cmsLatex.SetTextSize(0.04)
    cmsLatex.SetNDC(True)
    cmsLatex.SetTextAlign(11)
    cmsLatex.DrawLatex(0.1,0.92, "#font[61]{CMS} #font[52]{Preliminary}")

    yearEnergyLabel = ROOT.TLatex()
    yearEnergyLabel.SetTextSize(0.04)
    yearEnergyLabel.SetNDC(True)
    yearEnergyLabel.SetTextAlign(31)
    yearEnergyLabel.DrawLatex(0.9, 0.92, "#font[42]{2023 (13.6 TeV)}")

    theCanvas.SaveAs(f'{destinationPath}/sampleScorePlotCICADAv{args.CICADAVersion}.png')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create PU weighted data versus samples plots for CICADA versions')
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