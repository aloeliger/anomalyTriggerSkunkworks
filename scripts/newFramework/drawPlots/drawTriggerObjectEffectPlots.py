#!/usr/bin/env python3

import ROOT
import os
import argparse

def main(args):
    ROOT.gStyle.SetOptStat(0)

    objects = [
        'EGamma',
        'Jet',
        'Tau',
        'EtSum',
    ]
    histograms = {
        'nObjects':{
            'axisLabel': 'nObjects',
        },
        'pt':{
            'axisLabel': 'p_{T}',
        },
        'eta':{
            'axisLabel': '#eta',
        },
        'phi':{
            'axisLabel': '#phi',
        },
        'et':{
            'axisLabel': 'E_{T}',
        },
        'mt':{
            'axisLabel': 'm_{T}'
        },
    }
    # cicadaThresholds = [0.0, 3.0, 5.0, 6.0, 7.0]
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
            3.0: {
                'color': 41
            },
            5.0: {
                'color': 42
            },
            8.0: {
                'color': 46
            },
            9.0: {
                'color': 30
            },
            10.0: {
                'color': 12
            },
        }

    theFile = ROOT.TFile(f'/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/triggerObjectPlotsCICADAv{args.CICADAVersion}.root')
    destinationPath = f'/nfs_scratch/aloeliger/anomalyPlotFiles/pngFiles/triggerObjectEffectsCICADAv{args.CICADAVersion}/'
    if not os.path.isdir(destinationPath):
        os.mkdir(destinationPath)
    for object in objects:
        for histoType in histograms:
            theCanvas = ROOT.TCanvas(f'{object}_{histoType}')
            theCanvas.SetLogy()

            theLegend = ROOT.TLegend(0.7,0.7,0.9,0.9)
            for index, threshold in enumerate(cicadaThresholds):
                thresholdString = str(threshold).replace('.', 'p')
                thePlot = getattr(theFile, f'{object}_{histoType}_CICADA{thresholdString}')
                
                thePlot.SetMarkerStyle(20)
                thePlot.SetMarkerColor(cicadaThresholds[threshold]['color'])
                thePlot.SetLineColor(cicadaThresholds[threshold]['color'])

                thePlot.Scale(1.0/thePlot.Integral())

                if index == 0:
                    thePlot.Draw('E1')
                    thePlot.GetXaxis().SetTitle(f'{object} {histograms[histoType]["axisLabel"]}')
                    thePlot.GetYaxis().SetTitle('Fraction (normalized to 1)')
                    thePlot.SetTitle('')
                    # thePlot.GetYaxis().SetRangeUser(1e-2,1.0)
                else:
                    thePlot.Draw('SAME E1')
                theLegend.AddEntry(thePlot, f'CICADA > {threshold}', 'pl')
            theLegend.Draw()
            theCanvas.SaveAs(f'{destinationPath}/{object}_{histoType}.png')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Draw the trigger object plots")
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