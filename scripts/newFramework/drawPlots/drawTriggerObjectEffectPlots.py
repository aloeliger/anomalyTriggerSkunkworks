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

    theFile = ROOT.TFile(f'/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/triggerObjectPlotsCICADAv{args.CICADAVersion}.root')
    destinationPath = f'/nfs_scratch/aloeliger/anomalyPlotFiles/pngFiles/triggerObjectEffectsCICADAv{args.CICADAVersion}/'
    if not os.path.isdir(destinationPath):
        os.mkdir(destinationPath)
    for object in objects:
        # print(f'Object: {object}')
        for histoType in histograms:
            # print(f'histoType: {histoType}')
            theCanvas = ROOT.TCanvas(f'{object}_{histoType}')
            theCanvas.SetLogy()

            theLegend = ROOT.TLegend(0.7,0.7,0.9,0.9)
            for index, threshold in enumerate(cicadaThresholds):
                # print(f'threshold: {threshold}')
                thresholdString = str(threshold).replace('.', 'p')
                thePlot = getattr(theFile, f'{object}_{histoType}_CICADA{thresholdString}')
                
                thePlot.SetMarkerStyle(20)
                thePlot.SetMarkerColor(cicadaThresholds[threshold]['color'])
                thePlot.SetLineColor(cicadaThresholds[threshold]['color'])

                try:
                    thePlot.Scale(1.0/thePlot.Integral())
                except ZeroDivisionError:
                    pass

                if index == 0:
                    thePlot.Draw('E1')
                    thePlot.GetXaxis().SetTitle(f'{object} {histograms[histoType]["axisLabel"]}')
                    thePlot.GetYaxis().SetTitle('Fraction (normalized to 1)')
                    thePlot.SetTitle('')
                    # thePlot.GetYaxis().SetRangeUser(1e-2,1.0)
                else:
                    thePlot.Draw('SAME E1')
                theLegend.AddEntry(thePlot, f'CICADA > {threshold}', 'pl')
                # print(thePlot.Integral())
                # cumsum = 0.0
                # for binNum in range(1,thePlot.GetNbinsX()+1):
                #     content = thePlot.GetBinContent(binNum)
                #     cumsum += content
                #     print(f'binNum: {binNum}, content: {content}, cumulative: {cumsum}')
            theLegend.Draw()

            cmsLatex = ROOT.TLatex()
            cmsLatex.SetTextSize(0.05)
            cmsLatex.SetNDC(True)
            cmsLatex.SetTextAlign(11)
            cmsLatex.DrawLatex(0.1,0.92, "#font[61]{CMS} #font[52]{Preliminary}")

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
