import argparse
import ROOT
from anomalyTriggerThresholds.thresholdHelper import thresholdHelper

from anomalyDetection.anomalyTriggerSkunkworks.plotSettings.utilities import convertEffToRate

def convertBinToRates(theHistogram, theBinNumber):
    hist = theHistogram.Clone()
    eff = theHistogram.GetBinContent(theBinNumber)
    rate = convertEffToRate(eff)
    try:
        rateScaling = rate/eff
    except ZeroDivisionError:
        rateScaling = 0
    currentErr = theHistogram.GetBinError(theBinNumber)
    newBinError = currentErr * rateScaling    

    hist.SetBinContent(theBinNumber, rate)
    hist.SetBinError(theBinNumber, newBinError)

    return hist

def convertHistogramToRates(theHistogram):
    hist = theHistogram.Clone()
    numberOfBins = theHistogram.GetNbinsX()
    for i in range(1,numberOfBins+1):
        hist = convertBinToRates(hist, i)
    return hist

def main(args):
    ROOT.gStyle.SetOptStat(0)
    theFile = ROOT.TFile(args.theFile)

    triggers = ('CICADA', 'uGT')
    rates = ('0.5', '1', '2', '3')

    finalPlots = {}

    for trigger in triggers:
        finalPlots[trigger] = {}
        for rate in rates:
            numeratorPlotName = f'{trigger}_{rate}_num'
            denominatorPlotName = f'{trigger}_{rate}_denom'
            thePlot = getattr(theFile, numeratorPlotName).Clone()
            denominatorPlot = getattr(theFile, denominatorPlotName).Clone()
            
            thePlot.Divide(denominatorPlot)

            theCanvas = ROOT.TCanvas(f'{trigger}_{rate}')
            theCanvas.SetLogy()
            theCanvas.SetGridx()

            thePlot = convertHistogramToRates(thePlot)
            errorHisto = thePlot.Clone()

            thePlot.SetLineColor(ROOT.kRed)
            thePlot.SetLineWidth(2)

            errorHisto.SetFillColor(ROOT.kGray)
            errorHisto.SetFillStyle(3244)
            errorHisto.Draw('E2')
            errorHisto.GetXaxis().SetNdivisions(errorHisto.GetNbinsX())
            thePlot.Draw('SAME HIST')

            errorHisto.GetYaxis().SetTitle('Overall Rate (kHz)')
            errorHisto.GetXaxis().SetTitle('Number of Primary Vertices')
            errorHisto.SetTitle('')

            cmsLatex = ROOT.TLatex()
            cmsLatex.SetTextSize(0.06)
            cmsLatex.SetNDC(True)
            cmsLatex.SetTextAlign(11)
            cmsLatex.DrawLatex(0.1,0.92, "#font[61]{CMS} #font[52]{Preliminary}")

            nominalLatex  = ROOT.TLatex()
            nominalLatex.SetTextSize(0.06)
            nominalLatex.SetNDC(True)
            nominalLatex.SetTextAlign(31)
            nominalLatex.DrawLatex(0.9,0.92, '#font[72]{'+f'{trigger}'+'}'+' #font[42]{'+f'{rate} kHz, Nominal'+'}')

            theCanvas.SaveAs(f'{trigger}_{rate}_PURate.png')
            finalPlots[trigger][rate] = thePlot

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Draw pileup rate information')

    parser.add_argument(
        '--theFile',
        default='pileupRates.root',
        nargs='?',
        help='File to draw plots out of'
    )

    args = parser.parse_args()
    main(args)
