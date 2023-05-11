import ROOT
import os
import argparse
import re

from anomalyDetection.anomalyTriggerSkunkworks.plotSettings.utilities import convertEffToRate

def getListOfRuns(theFile):
    theRuns = []
    keyList = [x.GetName() for x in list(theFile.GetListOfKeys())]

    for name in keyList:
        if 'Total' not in name:
            continue
        runNum = re.search('[0-9]+', name).group(0)
        theRuns.append(runNum)

    return theRuns

# def getListOfTriggers(theFile):
#     theTriggers = []
#     keyList = [x.GetName() for x in list(theFile.GetListOfKeys())]

#     for name in keyList:
#         triggerName = re.search('.*?(?>_[0-9]+)', name).group(0)
#         if triggerName not in theTriggers:
#             theTriggers.append(triggerName)
    
#     return theTriggers

def createEffPlot(triggerHisto, totalHisto):
    effPlot = triggerHisto.Clone()
    effPlot.Divide(totalHisto)

    return effPlot

def createRatePlotFromEffPlot(thePlot):
    ratePlot = thePlot.Clone()
    for theBin in range(1,thePlot.GetNbinsX()+1):
        ratePlot.SetBinContent(theBin, convertEffToRate(ratePlot.GetBinContent(theBin)))
    return ratePlot

def smoothPlotsWithRunningAverage(theHistogram, runningAveragePeriod):
    smoothedHisto = theHistogram.Clone()
    runningTotal = []
    for theBin in range(1, theHistogram.GetNbinsX()+1):
        runningTotal.append(theHistogram.GetBinContent(theBin))
        if len(runningTotal) > runningAveragePeriod:
            runningTotal.pop(0)
        runningAverage = 0.
        for value in runningTotal:
            runningAverage += value
        runningAverage = runningAverage / len(runningTotal)
        smoothedHisto.SetBinContent(theBin, runningAverage)
    return smoothedHisto

def main(args):
    ROOT.gStyle.SetOptStat(0)

    theFile = ROOT.TFile(args.theFile, 'READ')
    theRuns = getListOfRuns(theFile)
    # theTriggers = getListOfTriggers(theFile)

    triggerSettings = {
        'CICADA3kHz': (ROOT.kRed+3, 'CICADA (3 kHz)'),
        'CICADA2kHz': (ROOT.kRed, 'CICADA (2 kHz)'),
        'CICADA1kHz': (ROOT.kRed-7, 'CICADA (1 kHz)'),
        'CICADA0p5kHz': (ROOT.kRed-9, 'CICADA (0.5 kHz)'),
        'uGT3kHz': (ROOT.kBlue+3, 'uGT AD (3 kHz)'),
        'uGT2kHz': (ROOT.kBlue, 'uGT AD (2 kHz)'),
        'uGT1kHz': (ROOT.kBlue-7, 'uGT AD (1kHz)'),
        'uGT0p5kHz': (ROOT.kBlue-9, 'uGT AD (0.5 kHz)'),
        'L1_SingleMu22': (ROOT.kGreen, 'L1_SIngleMu22'),
        'L1_SingleJet180': (ROOT.kOrange, 'L1_SingleJet180'),
        'L1_DoubleIsoTau34er2p1': (ROOT.kViolet, 'L1_DoubleIsoTau34er2p1')
    }

    theTriggers = list(triggerSettings.keys())

    for runNumber in theRuns:
        totalHisto = getattr(theFile, f'Total_{runNumber}')

        #We need to create a specific canvas for each run
        #It also has to be wide enough to handle all of the lumi sections in a plot
        xWisePixels = max(800, 3*totalHisto.GetNbinsX())
        theCanvas = ROOT.TCanvas(f'Canvas_{runNumber}',f'Canvas_{runNumber}', xWisePixels, 600)
        theCanvas.SetLogy()

        theLegend = ROOT.TLegend(0.15, 0.8, 0.85, 0.9)
        theLegend.SetNColumns(3)

        plotDict = {}

        for triggerName in theTriggers:
            triggerHisto = getattr(theFile, f'{triggerName}_{runNumber}')
            effHisto = createEffPlot(triggerHisto, totalHisto)
            rateHisto = createRatePlotFromEffPlot(effHisto)
            smoothedHisto = smoothPlotsWithRunningAverage(rateHisto, args.smoothingPeriod)

            #Now we have a smoothed plot, we need to style it and draw it
            smoothedHisto.SetLineColor(triggerSettings[triggerName][0])
            smoothedHisto.SetLineWidth(2)
            theLegend.AddEntry(smoothedHisto, triggerSettings[triggerName][1], 'l') 
        
            plotDict[triggerName] = smoothedHisto
        
        firstPlot = True
        for plotName in plotDict:
            if firstPlot:
                theHist = plotDict[plotName]
                theHist.Draw('L')

                theHist.SetMaximum(28.6*10e3)
                theHist.SetMinimum(0.01)

                theHist.SetTitle('')
                theHist.GetXaxis().SetTitle('LS')

                theHist.GetYaxis().SetTitle('Rate (kHz)')

                firstPlot=False
            else:
                plotDict[plotName].Draw('SAME L')
        theLegend.Draw()

        cmsLatex = ROOT.TLatex()
        cmsLatex.SetTextSize(0.06)
        cmsLatex.SetNDC(True)
        cmsLatex.SetTextAlign(11)
        cmsLatex.DrawLatex(0.1,0.92, "#font[61]{CMS} #font[52]{Preliminary}")

        overallLatex = ROOT.TLatex()
        overallLatex.SetTextSize(0.06)
        overallLatex.SetNDC(True)
        overallLatex.SetTextAlign(31)
        overallLatex.DrawLatex(0.9, 0.92, f'Run: {runNumber}, Overall')

        theCanvas.SaveAs(f'plots/OverallRate_Run{runNumber}.png')
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Draw the smoothed rate plots')

    parser.add_argument(
        '--theFile',
        default='lumiScoreFile.root',
        nargs='?',
        help='File to draw the plots from'
    )
    parser.add_argument(
        '--smoothingPeriod',
        default=10,
        type=int,
        nargs='?'
    )

    args = parser.parse_args()
    main(args)
