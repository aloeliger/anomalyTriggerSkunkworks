# !/usr/bin/env python3

import ROOT
import argparse
from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.largeRunDEphemeralZeroBias import largeRunDEphemeralZeroBiasSample
import os

from rich.console import Console

console = Console()

def drawUnrolledObjectPlots(theFile, typeOfObject, theThresholds, destinationPath, nObjects=12):
    for nObject in range(1,nObjects+1):
        theCanvas = ROOT.TCanvas(
            f'Unrolled{typeOfObject}_n{nObject}',
            f'Unrolled{typeOfObject}_n{nObject}',
        )
        theCanvas.SetLogy()
        theLegend = ROOT.TLegend(0.7,0.7,0.9,0.9)
        for index, threshold in enumerate(theThresholds):
            theHistoName = f'{typeOfObject}_n{nObject}_pt_CICADA{int(threshold)}'
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
                theHisto.GetXaxis().SetTitle(f'{typeOfObject}'+'p_{T}')
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
        cmsLatex.DrawLatex(0.1,0.92, "#font[61]{CMS} #font[52]{Preliminary}")

        theCanvas.SaveAs(f'{destinationPath}/{typeOfObject}_n{nObject}_pt.png')

def drawNthObjectPlots(theFile, typeOfObject, theThresholds, destinationPath, nObjects=3):
    for nthObject in range(1,nObjects+1):
        theCanvas = ROOT.TCanvas(
            f'{typeOfObject}_pt_object{nthObject}',
            f'{typeOfObject}_pt_object{nthObject}',
        )
        theLegend = ROOT.TLegend(0.7,0.7,0.9,0.9)
        for index, threshold in enumerate(theThresholds):
            theHistoName = f'{typeOfObject}_pt_object{nthObject}_CICADA{int(threshold)}'
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
                theHisto.GetXaxis().SetTitle(f'{typeOfObject}'+'p_{T}')
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
        cmsLatex.DrawLatex(0.1,0.92, "#font[61]{CMS} #font[52]{Preliminary}")

        theCanvas.SaveAs(f'{destinationPath}/{typeOfObject}_pt_{nthObject}.png')

def main(args):
    objects = [
        'EGamma',
        'Jet',
        'Tau'
    ]
    if args.CICADAVersion == 1:
        cicadaThresholds = {
            0.0: {
                'color': 40
            },
            7.0: {
                'color': 41
            },
            10.0: {
                'color': 42
            },
            11.0: {
                'color': 46
            },
            13.0: {
                'color': 30
            },
        }
    if args.CICADAVersion == 2:
        cicadaThresholds = {
            0.0: {
                'color': 40
            },
            7.0: {
                'color': 41
            },
            8.5: {
                'color': 42
            },
            10.5: {
                'color': 46
            },
            14.0: {
                'color': 30
            },
        }
    theFile = ROOT.TFile(f'/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/unrolledTriggerObjectPlotsCICADAv{args.CICADAVersion}.root')
    destinationPath = f'/nfs_scratch/aloeliger/anomalyPlotFiles/pngFiles/unrolledTriggerObjectPlotsCICADAv{args.CICADAVersion}/'
    if not os.path.isdir(destinationPath):
        os.mkdir(destinationPath)
    
    for typeOfObject in objects:
        drawUnrolledObjectPlots(
            theFile=theFile,
            typeOfObject=typeOfObject,
            theThresholds=cicadaThresholds,
            destinationPath=destinationPath,
        )
        
        drawNthObjectPlots(
            theFile=theFile,
            typeOfObject=typeOfObject,
            theThresholds=cicadaThresholds,
            destinationPath=destinationPath
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