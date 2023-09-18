# !/usr/bin/env python3

import ROOT
import argparse
import os

def main(args):
    ROOT.gStyle.SetOptStat(0)
    ROOT.gStyle.SetPalette(ROOT.kTemperatureMap)
    theFile = ROOT.TFile(f'/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/calorimeterImagesCICADAv{args.CICADAVersion}.root')
    
    destinationPath = f'/nfs_scratch/aloeliger/anomalyPlotFiles/pngFiles/averageCalorimeterImages/'
    if not os.path.isdir(destinationPath):
        os.mkdir(destinationPath)

    histSettings = [
        ("ZeroBias","Zero Bias"),
        ("GT3", "CICADA > 3"),
        ("GT5", "CICADA > 5"),
        ("GT6", "CICADA > 6"),
    ]

    for histSetting in histSettings:
        theCanvas = ROOT.TCanvas('theCanvas')
        theCanvas.SetRightMargin(0.17)

        theHist = getattr(theFile, histSetting[0])

        theHist.Scale(1.0/theHist.GetEntries())

        theHist.Draw("COLZ")
        theHist.GetXaxis().SetTitle('iPhi')
        theHist.GetYaxis().SetTitle('iEta')
        theHist.GetZaxis().SetTitle('Average Energy (GeV)')
        theHist.GetZaxis().SetTitleOffset(1.3)
        theHist.GetZaxis().CenterTitle()
        theHist.GetZaxis().SetRangeUser(0.0, 0.05)

        theHist.SetTitle("")

        cmsLatex = ROOT.TLatex()
        cmsLatex.SetTextSize(0.05)
        cmsLatex.SetNDC(True)
        cmsLatex.SetTextAlign(11)
        cmsLatex.DrawLatex(0.1,0.92, "#font[61]{CMS} #font[52]{Preliminary}")

        labelLatex = ROOT.TLatex()
        labelLatex.SetTextSize(0.05)
        labelLatex.SetNDC(True)
        labelLatex.SetTextAlign(31)
        labelLatex.DrawLatex(0.83, 0.92, "#font[52]{"+f'{histSetting[1]}'+"}")

        theCanvas.SaveAs(f'{destinationPath}/CalorimeterImage_{histSetting[0]}.png')

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