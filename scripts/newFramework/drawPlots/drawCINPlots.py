#!/usr/bin/env python3

import ROOT
import os
import argparse

def main(args):
    ROOT.gStyle.SetOptStat(0)

    plotTypes = [
        'CIN',
        'Calorimeter',
        'Error'
    ]
    runs = [
        'RunA',
        'RunB',
        'RunC',
        'RunD',
    ]

    theFile = ROOT.TFile('/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/CICADAInputNetworkPlots.root')
    destinationPath = '/nfs_scratch/aloeliger/anomalyPlotFiles/pngFiles/CICADAInputNetworkPlots/'
    if not os.path.isdir(destinationPath):
        os.mkdir(destinationPath)
    for plotType in plotTypes:
        if plotType == 'Error':
            ROOT.gStyle.SetPalette(ROOT.kBlackBody)
        else:
            ROOT.gStyle.SetPalette(ROOT.kLightTemperature)
        for run in runs:
            for i in range(5):
                theCanvas = ROOT.TCanvas('theCanvas')
                plotName = f'{plotType}_{run}_{i}'
                thePlot = getattr(theFile, plotName)

                thePlot.Draw('COLZ')
                thePlot.GetXaxis().SetTitle('iPhi')
                thePlot.GetYaxis().SetTitle('iEta')
                if plotType == 'Error':
                    thePlot.GetZaxis().SetRangeUser(-10.0,10.0)
                theCanvas.SaveAs(f'{destinationPath}/{plotName}.png')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Draw CICADAInputNetwork plots")
    
    args = parser.parse_args()
    main(args)