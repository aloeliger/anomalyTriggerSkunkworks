import argparse
import ROOT
import math

from anomalyDetection.anomalyTriggerSkunkworks.plotSettings.utilities import convertEffToRate
from drawFrequencyStability import getThresholdForRate

def createRatePlot(scorePlot):
    integralPlot = scorePlot.Clone()
    integralPlot.Scale(1.0/integralPlot.Integral())

    nBins = scorePlot.GetNbinsX()

    ratePlot = ROOT.TH1F(
        scorePlot.GetName()+'_Rate',
        scorePlot.GetTitle()+'_Rate',
        nBins,
        scorePlot.GetXaxis().GetXmin(),
        scorePlot.GetXaxis().GetXmax(),
    )
    for i in range(1,nBins+1):
        ratePlot.SetBinContent(i, convertEffToRate(integralPlot.Integral(i, nBins)))

    return ratePlot

def main(args):
    theFile = ROOT.TFile(args.theFile)
    ROOT.gStyle.SetOptStat(0)

    plots = (
        'CaloScore',
        'uGTScore'
    )
    maxPU = 120.0
    minPU = 0.0
    PUperBin = 5.0
    puBins = math.ceil((maxPU-minPU)/PUperBin)

    rates = (
        0.5,
        1,
        2,
        3,
    )

    histos = {}
    for plotType in plots:
        histos[plotType] = {}
        for rate in rates:
            rateString = str(rate)
            rateString.replace('.','p')
            histos[plotType][rate] = ROOT.TH1F(
                f'PU_{plotType}_{rateString}_thresholds',
                f'PU_{plotType}_{rateString}_thresholds',
                puBins,
                minPU,
                maxPU,
            )

    for plotType in plots:
        for i in range(puBins):
            plotName = f'{plotType}_PU_{i*int(PUperBin)}_{(i+1)*int(PUperBin)}'
            thePlot = getattr(theFile, plotName)

            theRatePlot = createRatePlot(thePlot)

            for rate in rates:
                theThreshold = getThresholdForRate(theRatePlot, rate)
                histos[plotType][rate].Fill(i*PUperBin, theThreshold)
    #Let's make a big plot of all this junk.
    for plotType in plots:
        theCanvas = ROOT.TCanvas(f'{plotType}_canvas')
        axisMax = 0
        for rate in rates:
            axisMax = max(axisMax, histos[plotType][rate].GetMaximum())
        histos[plotType][0.5].SetLineColor(40)
        histos[plotType][1].SetLineColor(30)
        histos[plotType][2].SetLineColor(41)
        histos[plotType][3].SetLineColor(46)

        histos[plotType][0.5].Draw('HIST')
        histos[plotType][1].Draw('SAME HIST')
        histos[plotType][2].Draw('SAME HIST')
        histos[plotType][3].Draw('SAME HIST')

        histos[plotType][0.5].GetXaxis().SetTitle('npv')
        histos[plotType][0.5].GetYaxis().SetTitle('Threshold')
        histos[plotType][0.5].SetTitle('')
        histos[plotType][0.5].SetMaximum(axisMax*1.2)

        cmsLatex = ROOT.TLatex()
        cmsLatex.SetTextSize(0.06)
        cmsLatex.SetNDC(True)
        cmsLatex.SetTextAlign(11)
        cmsLatex.DrawLatex(0.1,0.92, "#font[61]{CMS} #font[52]{Preliminary}")

        algoLatex = ROOT.TLatex()
        algoLatex.SetTextSize(0.06)
        algoLatex.SetNDC(True)
        algoLatex.SetTextAlign(31)
        if plotType == 'CaloScore':
            algoString = 'CICADA'
        elif plotType == 'uGTScore':
            algoString = 'AXOL1TL'
        algoLatex.DrawLatex(0.9, 0.92, '#font[72]{'+f'{algoString}'+'}')

        theLegend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
        theLegend.AddEntry(histos[plotType][0.5], '0.5 kHz', 'l')
        theLegend.AddEntry(histos[plotType][1], '1 kHz', 'l')
        theLegend.AddEntry(histos[plotType][2], '2 kHz', 'l')
        theLegend.AddEntry(histos[plotType][3], '3 kHz', 'l')
        theLegend.Draw()

        theCanvas.SaveAs(f'{plotType}_thresholds.png')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Draw PU threshold plots')

    parser.add_argument(
        '--theFile',
        nargs='?',
        default='pileupThresholds.root',
        help='File to create plots from'
    )

    args = parser.parse_args()
    main(args)
