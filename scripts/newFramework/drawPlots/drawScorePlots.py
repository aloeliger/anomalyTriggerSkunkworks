#!/usr/bin/env python3

import ROOT
import argparse
import os
# import prettytable
import math

from rich.console import Console
from rich.table import Table
from rich.traceback import install

console = Console()
install()

def createEffPlot(scorePlot):
    theEffPlot = ROOT.TH1D(
        scorePlot.GetName()+'_rate',
        scorePlot.GetTitle()+'_rate',
        scorePlot.GetNbinsX(),
        scorePlot.GetXaxis().GetXmin(),
        scorePlot.GetXaxis().GetXmax()
    )
    totalIntegral = float(scorePlot.Integral())
    for integralLeftBin in range(1, scorePlot.GetNbinsX()+1):
        integratedEvents = float(scorePlot.Integral(integralLeftBin, scorePlot.GetNbinsX()))
        uncertainty = math.sqrt(integratedEvents)

        integratedEvents = integratedEvents/totalIntegral
        uncertainty = uncertainty/totalIntegral

        theEffPlot.SetBinContent(integralLeftBin, integratedEvents)
        theEffPlot.SetBinError(integralLeftBin, uncertainty)
    return theEffPlot

def convertEffToRate(effPlot):
    #https://indico.cern.ch/event/1060362/contributions/4455928/attachments/2286702/3886636/RatesAndPrescales_L1MenuTutorial2021.pdf#page=2
    #converts a fraction acceptance of zero-bias to a rate
    effPlot.Scale(2544.0 * 11245e-3)
    return effPlot

#scroll from highest rate down to lowest
#find the first bin that is lower than or equal to the desired rate
#we can find the bin, and it's left and right edge.
#and report back the bin content, left and right edge,
#and try to come up with what we expect the thresholds to be
def findBinForRate(ratePlot, rate):
    totalBins = ratePlot.GetNbinsX()

    binContent = None
    binLeftEdge = None
    binRightEdge = None
    currentBin = None

    for bin in range(1,totalBins+1):
        binContent = ratePlot.GetBinContent(bin)
        binLeftEdge = ratePlot.GetXaxis().GetBinLowEdge(bin)
        binRightEdge = ratePlot.GetXaxis().GetBinUpEdge(bin)
        currentBin = bin
        if binContent <= rate:
            break
    
    return currentBin, binContent, binLeftEdge, binRightEdge

def printRateThresholds(ratePlot, run):
    console.log(f'Info for run: {run}')

    theTable = Table(title=run)
    theTable.add_column("Nominal rate", style='cyan', justify='center')
    theTable.add_column("Bin No.", style='cyan', justify='center')
    theTable.add_column("Rate (plot content)", style='underline white', justify='right')
    theTable.add_column('Low threshold', style='green', justify='right')
    theTable.add_column('High threshold', style='green', justify='right')
    
    theTable.add_row('10.0', *[str(x) for x in findBinForRate(ratePlot, 10.0)])
    theTable.add_row('5.0', *[str(x) for x in findBinForRate(ratePlot, 5.0)])
    theTable.add_row('3.0', *[str(x) for x in findBinForRate(ratePlot, 3.0)])
    theTable.add_row('2.0', *[str(x) for x in findBinForRate(ratePlot, 2.0)])
    theTable.add_row('1.0', *[str(x) for x in findBinForRate(ratePlot, 1.0)])
    theTable.add_row('0.5', *[str(x) for x in findBinForRate(ratePlot, 0.5)])

    console.print(theTable)

def rateEffPlot(runs, scorePlots, destinationPath, args):
    theCanvas = ROOT.TCanvas('highGranularityCanvas')
    theCanvas.SetLogy()
    theLegend = ROOT.TLegend(0.5, 0.7, 0.9, 0.9)

    ratePlots = []

    for index, run in enumerate(runs):
        #let's get the high granularity plots
        thePlot = scorePlots[run]
        effPlot = createEffPlot(thePlot)
        ratePlot = convertEffToRate(effPlot.Clone())
        ratePlots.append(ratePlot)
        printRateThresholds(ratePlot, run)

        ratePlot.SetMarkerStyle(6)
        ratePlot.SetMarkerColor(runs[run])
        ratePlot.SetLineColor(runs[run])

        if index == 0:
            ratePlot.Draw('E1 X0')
            ratePlot.GetXaxis().SetTitle(f'CICADA v{args.CICADAVersion} score')
            ratePlot.GetYaxis().SetTitle('Rate (kHZ)')
            ratePlot.SetTitle('')
        else:
            ratePlot.Draw('SAME E1 X0')
        
        _, _, five_kHz_threshold, _ = findBinForRate(ratePlot, 5.0)

        theLegend.AddEntry(ratePlot, f'{run}, 5 kHz Threshold: {five_kHz_threshold:1.2f}', 'pl')
    theLegend.Draw()
    
    cmsLatex = ROOT.TLatex()
    cmsLatex.SetTextSize(0.04)
    cmsLatex.SetNDC(True)
    cmsLatex.SetTextAlign(11)
    cmsLatex.DrawLatex(0.1,0.92, "#font[61]{CMS} #font[52]{Preliminary}")

    theCanvas.SaveAs(f'{destinationPath}/ratePlotCICADAv{args.CICADAVersion}.png')

def basicScorePlot(runs, scorePlots, destinationPath, args):
    theCanvas = ROOT.TCanvas('theCanvas')
    theCanvas.SetLogy()
    theLegend = ROOT.TLegend(0.5, 0.7, 0.9, 0.9)

    for index, run in enumerate(runs):
        thePlot = scorePlots[run]

        thePlot.SetMarkerStyle(20)
        thePlot.SetMarkerColor(runs[run])
        thePlot.SetLineColor(runs[run])

        thePlot.Scale(1.0/thePlot.Integral())

        if index == 0:
            thePlot.Draw('E1 X0')
            thePlot.GetXaxis().SetTitle(f'CICADA v{args.CICADAVersion} score')
            thePlot.GetYaxis().SetTitle('Fraction (normalized to 1)')
            thePlot.SetTitle('')
        else:
            thePlot.Draw('SAME E1 X0')

        theMean = thePlot.GetMean()
        stdDev = thePlot.GetStdDev()

        theLegend.AddEntry(thePlot, f'{run}, Mean: {theMean:1.2f}, StdDev: {stdDev:1.2f}', 'pl')
    theLegend.Draw()

    cmsLatex = ROOT.TLatex()
    cmsLatex.SetTextSize(0.04)
    cmsLatex.SetNDC(True)
    cmsLatex.SetTextAlign(11)
    cmsLatex.DrawLatex(0.1,0.92, "#font[61]{CMS} #font[52]{Preliminary}")

    theCanvas.SaveAs(f'{destinationPath}/scorePlotCICADAv{args.CICADAVersion}.png')

def main(args):
    ROOT.gStyle.SetOptStat(0)
    """ if args.mc:
        theFile = ROOT.TFile(f'/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/scoreMCPlots{args.year}CICADAv{args.CICADAVersion}.root')
        destinationPath = f'/nfs_scratch/aloeliger/anomalyPlotFiles/pngFiles/scoreMCPlots{args.year}CICADAv{args.CICADAVersion}/'
    else:
        theFile = ROOT.TFile(f'/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/scorePlots{args.year}CICADAv{args.CICADAVersion}.root')
        destinationPath = f'/nfs_scratch/aloeliger/anomalyPlotFiles/pngFiles/scorePlots{args.year}CICADAv{args.CICADAVersion}/' """
    theFile = ROOT.TFile(f'/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/scorePlotsCICADAv{args.CICADAVersion}.root')
    destinationPath = f'/nfs_scratch/aloeliger/anomalyPlotFiles/pngFiles/scorePlotsCICADAv{args.CICADAVersion}/'
    if not os.path.isdir(destinationPath):
        os.mkdir(destinationPath)

    if args.year == '2018':
        runs = {
            'RunA': 41,
            'RunB': 42,
            'RunC': 46,
            'RunD': 30,
        }
        scorePlots = {
            'RunA': theFile.RunA_score,
            'RunB': theFile.RunB_score,
            'RunC': theFile.RunC_score,
            'RunD': theFile.RunD_score,
        }
        hgScorePlots = {
            'RunA': theFile.RunA_score_highGranularity,
            'RunB': theFile.RunB_score_highGranularity,
            'RunC': theFile.RunC_score_highGranularity,
            'RunD': theFile.RunD_score_highGranularity,
        }
    if args.year == '2022':
        if args.mc:
            runs = {
                'DYTo2L':40,
                'GGHTT':42,
                'HTo2LongLived4b':46,
                'SUSYGGBBHtoBB':30,
                'TT':33,
                'VBFHToInvisible':28,
                'VBFHTT':6,
                'ZPrimeTT':2,
            }
            scorePlots = {
                'DYTo2L':theFile.DYTo2L_score,
                'GGHTT':theFile.DYTo2L_score,
                'HTo2LongLived4b':theFile.HTo2LongLived4b_score,
                'SUSYGGBBHtoBB':theFile.SUSYGGBBHtoBB_score,
                'TT':theFile.TT_score,
                'VBFHToInvisible':theFile.VBFHToInvisible_score,
                'VBFHTT':theFile.VBFHTT_score,
                'ZPrimeTT':theFile.ZPrimeTT_score,
            }
            hgScorePlots = {
                'DYTo2L':theFile.DYTo2L_score_highGranularity,
                'GGHTT':theFile.DYTo2L_score_highGranularity,
                'HTo2LongLived4b':theFile.HTo2LongLived4b_score_highGranularity,
                'SUSYGGBBHtoBB':theFile.SUSYGGBBHtoBB_score_highGranularity,
                'TT':theFile.TT_score_highGranularity,
                'VBFHToInvisible':theFile.VBFHToInvisible_score_highGranularity,
                'VBFHTT':theFile.VBFHTT_score_highGranularity,
                'ZPrimeTT':theFile.ZPrimeTT_score_highGranularity,
            }
    if args.year == '2023':
        runs = {
            # 'RunA': 41,
            'RunB': 42,
            'RunC': 46,
            'RunD': 30,
        }
        scorePlots = {
            # 'RunA': theFile.RunA_score,
            'RunB': theFile.RunB_score,
            'RunC': theFile.RunC_score,
            'RunD': theFile.RunD_score,
        }
        hgScorePlots = {
            # 'RunA': theFile.RunA_score_highGranularity,
            'RunB': theFile.RunB_score_highGranularity,
            'RunC': theFile.RunC_score_highGranularity,
            'RunD': theFile.RunD_score_highGranularity,
        }
    
    basicScorePlot(
        runs=runs,
        scorePlots=scorePlots,
        destinationPath=destinationPath,
        args=args
    )
    rateEffPlot(
        runs=runs,
        scorePlots=hgScorePlots,
        destinationPath=destinationPath,
        args=args
    )
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
    parser.add_argument(
        '-y',
        '--year',
        default='2023',
        help='Year of samples to use',
        choices=['2018','2022','2023'],
        nargs='?'
    )
    parser.add_argument(
        '--mc',
        action='store_true',
        help='Trigger the MC samples'
    )

    args = parser.parse_args()

    main(args)