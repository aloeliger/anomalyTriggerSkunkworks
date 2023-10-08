# !/usr/bin/env python3

import ROOT
import argparse
import numpy as np
from tqdm import tqdm, trange
import os

def main(args):
    ROOT.gStyle.SetOptStat(0)
    theFile = ROOT.TFile(f'/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/L1OverlapCICADAv{args.CICADAVersion}.root')
    destinationPath = f'/nfs_scratch/aloeliger/anomalyPlotFiles/pngFiles/L1OverlapCICADAv{args.CICADAVersion}/'

    if not os.path.isdir(destinationPath):
        os.mkdir(destinationPath)

    menus = ['L1Menu_Collisions2023_v1_2_0']
    
    ROOT.gStyle.SetPaintTextFormat('1.2g')

    remappedBinNames = {
        '10kHz (overall)':'CICADA 10 kHz (overall)',
        '5kHz (overall)':'CICADA 5 kHz (overall)',
        '3kHz (overall)':'CICADA 3 kHz (overall)',
        '2kHz (overall)':'CICADA 2 kHz (overall)',
        '1kHz (overall)':'CICADA 1 kHz (overall)',
        '0p5kHz (overall)':'CICADA 0.5 kHz (overall)',
        'Muon': 'Muon triggers',
        'MuonEG': 'Muon + EG triggers',
        'MuonJetOrSum': 'Muon + Jet or Sum triggers',
        'EG': 'EG triggers',
        'EGJetOrSum': 'EG + Jet Or Sum triggers',
        'EGTau': 'EG + Tau triggers',
        'Tau': 'Tau triggers',
        'MuonTau': 'Muon + Tau triggers',
        'TauJetOrSum': 'Tau + Jet or Sum triggers',
        'Jet': 'Jet (only) triggers',
        'JetOrSum': 'Jet + Sum triggers',
        'Sum': 'Sum (only) triggers'
    }

    for menu in tqdm(menus, ascii=True, dynamic_ncols=True, desc='menu'):
        theHist = getattr(theFile, f'overlap_{menu}')

        # rename the bins
        for i in range(1, theHist.GetXaxis().GetNbins()):
            theHist.GetXaxis().SetBinLabel(i, remappedBinNames[theHist.GetXaxis().GetBinLabel(i)])
        for i in range(1, theHist.GetYaxis().GetNbins()):
            theHist.GetYaxis().SetBinLabel(i, remappedBinNames[theHist.GetYaxis().GetBinLabel(i)])

        theCanvas = ROOT.TCanvas(f'{menu}_overlap')
        theCanvas.SetBottomMargin(0.32)
        theCanvas.SetLeftMargin(0.23)
        theCanvas.SetGridx()
        theCanvas.SetGridy()

        theHist.Draw('COLZ TEXT')
        theHist.GetXaxis().SetTitle('Primary Trigger Group')
        theHist.GetXaxis().SetTitleOffset(5.0)
        theHist.GetXaxis().CenterTitle()
        theHist.LabelsOption('v', 'X')
        theHist.GetYaxis().SetTitle('Overlap with Trigger Group')
        theHist.GetYaxis().CenterTitle()
        # theHist.GetYaxis().SetTitleOffset(1.)
        theHist.SetTitle('')

        cmsLatex = ROOT.TLatex()
        cmsLatex.SetTextSize(0.04)
        cmsLatex.SetNDC(True)
        cmsLatex.SetTextAlign(11)
        cmsLatex.DrawLatex(0.17,0.92, "#font[61]{CMS} #font[52]{Preliminary}")

        menuLatex = ROOT.TLatex()
        menuLatex.SetTextSize(0.04)
        menuLatex.SetNDC(True)
        menuLatex.SetTextAlign(31)
        menuLatex.DrawLatex(0.9,0.92, '#font[41]{'+menu+'}')

        theCanvas.SaveAs(f'{destinationPath}/L1Overlap_{menu}.png')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Create stability rate plots for CICADA versions")
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