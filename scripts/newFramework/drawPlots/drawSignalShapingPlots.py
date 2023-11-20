# !/usr/bin/env python3

import ROOT
import argparse
import os

from rich.console import Console
from rich.traceback import install

install()
console = Console()

def drawShapingPlots(theFile, theThresholds, destinationPath, theSample):
    theCanvas = ROOT.TCanvas("Hto2LongLviedto4b")
    
    plotTypes = ['invariantMass', 'leadingJetPt']
    plotTypes = {
        'invariantMass': {
            'x-axis': 'Invariant Mass (leading 4 jets, GeV)'
        },
        'leadingJetPt': {
            'x-axis': 'Leading jet p_{T} (GeV)'
        },

    }
    console.log(theSample)
    for plotType in plotTypes:
        theLegend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
        console.log(f'\t{plotType}')
        for index, threshold in enumerate(theThresholds):
            theHistoName = f'{theSample}_{plotType}_CICADA{int(threshold)}'
            console.log(f'\t\t{theHistoName}')
            theHisto = theFile.Get(theHistoName)

            theHisto.SetMarkerStyle(20)
            theHisto.SetMarkerColor(theThresholds[threshold]['color'])
            theHisto.SetLineColor(theThresholds[threshold]['color'])

            try:
                theHisto.Scale(1.0/theHisto.Integral())
            except ZeroDivisionError:
                pass
            
            if index == 0:
                theHisto.Draw('E1')
                theHisto.GetXaxis().SetTitle(plotTypes[plotType]['x-axis'])
                theHisto.GetYaxis().SetTitle('Fraction (normalized to 1)')
                theHisto.SetTitle('')
            else:
                theHisto.Draw('SAME E1')
            
            theLegend.AddEntry(theHisto, f'CICADA > {threshold}', 'pl')
        theLegend.Draw()

        cmsLatex = ROOT.TLatex()
        cmsLatex.SetTextSize(0.05)
        cmsLatex.SetNDC(True)
        cmsLatex.SetTextAlign(11)
        cmsLatex.DrawLatex(0.1, 0.92, "#font[61]{CMS} #font[52]{Preliminary}")

        theCanvas.SaveAs(f'{destinationPath}/{theSample}_{plotType}.png')

def main(args):
    ROOT.gStyle.SetOptStat(0)
    if args.CICADAVersion == 1:
        cicadaThresholds = {
            0.0: {
                'color': 40
            },
            3.0: {
                'color': 41
            },
            5.0: {
                'color': 42
            },
            6.0: {
                'color': 46
            },
            7.0: {
                'color': 30
            },
        }
    if args.CICADAVersion == 2:
        cicadaThresholds = {
            0.0: {
                'color': 40
            },
            8.0: {
                'color': 41
            },
            11.0: {
                'color': 42
            },
            13.0: {
                'color': 46
            },
            15.0: {
                'color': 30
            },
        }
    
    theFile = ROOT.TFile(f'/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/CICADASignalShapingCICADAv{args.CICADAVersion}.root')
    destinationPath = f'/nfs_scratch/aloeliger/anomalyPlotFiles/pngFiles/signalShapingPlotsCICADAv{args.CICADAVersion}/'
    if not os.path.isdir(destinationPath):
        os.mkdir(destinationPath)
    # Start by drawing the Hto2LongLived
    samples = [
        'Hto2LongLivedTo4b',
        'SUSYGluGlutoBBHtoBB'
    ]
    for sample in samples:
        drawShapingPlots(
            theFile,
            cicadaThresholds,
            destinationPath,
            sample
        )

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='draw the trigger object plots')
    parser.add_argument(
        '-v',
        '--CICADAVersion',
        default=1,
        type=int,
        help='Version to pull the ntuplizer from',
        choices=[1,2],
        nargs='?'
    )

    args = parser.parse_args()
    main(args)