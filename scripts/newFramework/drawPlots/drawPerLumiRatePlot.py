# !/usr/bin/env python3
import ROOT
import os
import argparse
import statistics
import math
from drawScorePlots import convertEffToRate
from tqdm import tqdm
import re

def addInQuadrature(iterable):
    sum = 0.0
    for x in iterable:
        sum += x**2
    sum = math.sqrt(sum)
    return sum

def smoothPlot(thePlot, smoothingWindow:int = 5):
    smoothPlot = thePlot.Clone()
    smoothPlot.SetNameTitle(thePlot.GetName()+"_smooth", thePlot.GetTitle()+"_smooth")
    nBins = thePlot.GetNbinsX()
    for i in range(1, nBins+1):
        if i - smoothingWindow >= 0:
            actualSmoothingWindow = smoothingWindow
        else:
            actualSmoothingWindow = i
        binNumsForAverage = [bin for bin in range((i-actualSmoothingWindow)+1,i+1)]
        binsForAverage = [thePlot.GetBinContent(bin) for bin in binNumsForAverage]
        binErrors = [thePlot.GetBinError(bin) for bin in binNumsForAverage]
        binAvg = statistics.mean(binsForAverage)
        binErr = addInQuadrature(binErrors)
        smoothPlot.SetBinContent(i, binAvg)
        smoothPlot.SetBinError(i, binErr)
    return smoothPlot

def makeRunPlot(run, theFile, destinationPath, CICADAVersion):
    zeroBiasPlot = getattr(theFile, f'{run}_ZeroBias_eventsPerLumi')
    overall0p5kHZPlot = getattr(theFile, f'{run}_0p5kHz_eventsPerLumi')
    overall1kHZPlot = getattr(theFile, f'{run}_1kHz_eventsPerLumi')
    overall2kHZPlot = getattr(theFile, f'{run}_2kHz_eventsPerLumi')
    overall3kHZPlot = getattr(theFile, f'{run}_3kHz_eventsPerLumi')
    overall5kHZPlot = getattr(theFile, f'{run}_5kHz_eventsPerLumi')

    overall0p5kHZPlot.Divide(zeroBiasPlot)
    overall1kHZPlot.Divide(zeroBiasPlot)
    overall2kHZPlot.Divide(zeroBiasPlot)
    overall3kHZPlot.Divide(zeroBiasPlot)
    overall5kHZPlot.Divide(zeroBiasPlot)

    smooth0p5kHZPlot = smoothPlot(overall0p5kHZPlot, 10)
    smooth1kHZPlot = smoothPlot(overall1kHZPlot, 10)
    smooth2kHZPlot = smoothPlot(overall2kHZPlot, 10)
    smooth3kHZPlot = smoothPlot(overall3kHZPlot, 10)
    smooth5kHZPlot = smoothPlot(overall5kHZPlot, 10)

    smooth0p5kHZPlot = convertEffToRate(smooth0p5kHZPlot)
    smooth1kHZPlot = convertEffToRate(smooth1kHZPlot)
    smooth2kHZPlot = convertEffToRate(smooth2kHZPlot)
    smooth3kHZPlot = convertEffToRate(smooth3kHZPlot)
    smooth5kHZPlot = convertEffToRate(smooth5kHZPlot)

    theCanvas = ROOT.TCanvas("theCanvas")
    theCanvas.SetLogy()

    smooth5kHZPlot.SetLineColor(40)
    smooth3kHZPlot.SetLineColor(30)
    smooth2kHZPlot.SetLineColor(41)
    smooth1kHZPlot.SetLineColor(42)
    smooth0p5kHZPlot.SetLineColor(46)

    smooth5kHZPlot.SetLineWidth(3)
    smooth3kHZPlot.SetLineWidth(3)
    smooth2kHZPlot.SetLineWidth(3)
    smooth1kHZPlot.SetLineWidth(3)
    smooth0p5kHZPlot.SetLineWidth(3)

    smooth5kHZPlot.Draw("HIST")
    smooth5kHZPlot.GetXaxis().SetTitle("Lumi")
    smooth5kHZPlot.GetYaxis().SetTitle("Rate (kHZ)")
    smooth5kHZPlot.GetYaxis().SetRangeUser(0.1, 100)
    smooth5kHZPlot.SetTitle('')

    smooth3kHZPlot.Draw('HIST SAME')
    smooth2kHZPlot.Draw('HIST SAME')
    smooth1kHZPlot.Draw('HIST SAME')
    smooth0p5kHZPlot.Draw('HIST SAME')

    theLegend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
    theLegend.AddEntry(smooth0p5kHZPlot, f'CICADA v{CICADAVersion} 0.5 kHZ (nominal)', 'l')
    theLegend.AddEntry(smooth1kHZPlot, f'CICADA v{CICADAVersion} 1 kHZ (nominal)', 'l')
    theLegend.AddEntry(smooth2kHZPlot, f'CICADA v{CICADAVersion} 2 kHZ (nominal)', 'l')
    theLegend.AddEntry(smooth3kHZPlot, f'CICADA v{CICADAVersion} 3 kHZ (nominal)', 'l')
    theLegend.AddEntry(smooth5kHZPlot, f'CICADA v{CICADAVersion} 5 kHZ (nominal)', 'l')

    theLegend.Draw()

    runLatex = ROOT.TLatex()
    runLatex.SetTextSize(0.05)
    runLatex.SetNDC(True)
    runLatex.SetTextAlign(31)
    runLatex.DrawLatex(0.9, 0.92, '#font[62]{Run: ' + str(run)+'}')

    theCanvas.SaveAs(f'{destinationPath}/{run}_ratePlot.png')

def main(args):
    ROOT.gStyle.SetOptStat(0)
    theFile = ROOT.TFile(f'/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/perLumiRatePlotsCICADAv{args.CICADAVersion}.root')
    destinationPath = f'/nfs_scratch/aloeliger/anomalyPlotFiles/pngFiles/perLumiScorePlotsCICADAv{args.CICADAVersion}/'
    if not os.path.isdir(destinationPath):
        os.mkdir(destinationPath)

    listOfKeys = list(theFile.GetListOfKeys())
    listOfNames = [x.GetName() for x in listOfKeys]
    # print(listOfNames)
    listOfRuns = []
    for name in listOfNames:
        match = re.search('^[0-9]+(?=_)', name)
        if match:
            runNum = match.group(0)
        else:
            print('failed to generate a run number. Continuing')
            continue
        listOfRuns.append(runNum)

    listOfUniqueRuns = []
    for runNum in listOfRuns:
        if runNum not in listOfUniqueRuns:
            listOfUniqueRuns.append(runNum)

    for run in listOfUniqueRuns:
        makeRunPlot(
            run,
            theFile,
            destinationPath,
            args.CICADAVersion,
        )

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