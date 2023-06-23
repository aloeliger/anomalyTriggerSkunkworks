#!/usr/bin/env python3

import ROOT
import argparse
import os
import prettytable
import math

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
    print(f'Info for run: {run}')
    theTable = prettytable.PrettyTable()
    theTable.field_names = ["nominal rate", "bin no", "rate (plot content)", "low threshold", "high threshold"]
    theTable.add_rows(
        [
            [5.0, *findBinForRate(ratePlot, 5.0)],
            [3.0, *findBinForRate(ratePlot, 3.0)],
            [2.0, *findBinForRate(ratePlot, 2.0)],
            [1.0, *findBinForRate(ratePlot, 1.0)],
            [0.5, *findBinForRate(ratePlot, 0.5)],
        ]
    )
    print(theTable)

def rateEffPlot(runs, scorePlots, destinationPath, args):
    theCanvas = ROOT.TCanvas('highGranularityCanvas')
    theCanvas.SetLogy()
    theLegend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)

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
        theLegend.AddEntry(ratePlot, f'Run {run [3]}', 'pl')
    theLegend.Draw()
    theCanvas.SaveAs(f'{destinationPath}/ratePlotCICADAv{args.CICADAVersion}.png')

def basicScorePlot(runs, scorePlots, destinationPath, args):
    theCanvas = ROOT.TCanvas('theCanvas')
    theCanvas.SetLogy()
    theLegend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)

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
        theLegend.AddEntry(thePlot, f'Run {run[3]}', 'pl')
    theLegend.Draw()
    theCanvas.SaveAs(f'{destinationPath}/scorePlotCICADAv{args.CICADAVersion}.png')

def main(args):
    ROOT.gStyle.SetOptStat(0)
    runs = {
        'RunA': 41,
        'RunB': 42,
        'RunC': 46,
        'RunD': 30,
    }

    theFile = ROOT.TFile(f'/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/scorePlotsCICADAv{args.CICADAVersion}.root')
    destinationPath = f'/nfs_scratch/aloeliger/anomalyPlotFiles/pngFiles/scorePlotsCICADAv{args.CICADAVersion}/'
    if not os.path.isdir(destinationPath):
        os.mkdir(destinationPath)

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

    args = parser.parse_args()

    main(args)