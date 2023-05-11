#let's recreate the original score and efficiency distribution plots
#let's attempt to do this vaguely right this time
from anomalyDetection.anomalyTriggerSkunkworks.plotSettings.PUScoreSettings import makeTreeTuples
import ROOT
import os
import math
import argparse

parser = argparse.ArgumentParser(description = 'Create rate/efficiency plots for given series of weightings')
parser.add_argument('--condition',
                    nargs='?',
                    help='conditions to put on the tree before drawing any plots',
                    default='')
parser.add_argument('--binLabel',
                    nargs='?',
                    help='LaTeX label to put on the bin after drawing')
parser.add_argument('--nBins',
                    nargs='?',
                    help='Number of bins to calculate the efficiency plot on',
                    type = int,
                    default=50)
parser.add_argument('--fileExtension',
                    nargs='?',
                    help='String to append to the filename to differentiate it')
#L1 Group method
#Frac events accepted compared to zero bias * zeroBias rate
#zero bias rate = nBunches * LHC Frequency
#               = 2544     * 11245.6e-3 kHz
#               = 28607 kHz = 28.607e3 kHz
parser.add_argument('--zeroThresholdTriggerRate',
                    nargs='?',
                    help='Assumed rate if the triggering threshold is zero in kHz. Defaults to LHC BX rate (40MHz = 40e3 kHZ)',
                    type = float,
                    default=40.0e3)

args=parser.parse_args()

ROOT.gStyle.SetOptStat(0)

treeTuples = makeTreeTuples()

ratePlots = []
nBins = args.nBins
for i in range(len(treeTuples)):
    variable = 'anomalyScore>>'
    histName = 'fineAnomalyHist'+treeTuples[i][0]
    treeTuples[i][2].Draw(variable+histName+'('+str(nBins)+', 0.0, 10.0)', args.condition)
    theHist = ROOT.gDirectory.Get(histName).Clone()    
    theHist.Scale(1.0/theHist.Integral())
    efficiencyHistName = 'efficiency'+treeTuples[i][0]
    theEfficiencyHist = ROOT.TH1F(efficiencyHistName, 
                                  efficiencyHistName,
                                  nBins, 0.0, 10.0)
    for j in range(nBins):
        theEfficiencyHist.SetBinContent(nBins-j, theHist.Integral(nBins-j, nBins))
        errSum = 0.0
        for k in range(i,nBins):
            errSum += theHist.GetBinError(k)**2
        err = math.sqrt(errSum)
        theEfficiencyHist.SetBinError(nBins-j,err)
    theEfficiencyHist.SetLineColor(treeTuples[i][4])
    theEfficiencyHist.SetLineWidth(2)
    theEfficiencyHist.SetMarkerStyle(20+i)
    ratePlots.append(theEfficiencyHist)

rateAverage = ratePlots[0].Clone()
for i in range(1,len(ratePlots)):
    rateAverage.Add(ratePlots[i])
rateAverage.Scale(1.0/float(len(ratePlots)))
rateAverage.SetMarkerStyle(8)
rateAverage.SetLineColor(ROOT.kBlack)

#Scale to the system rate
rateAverage.Scale(args.zeroThresholdTriggerRate)
for hist in ratePlots:
    hist.Scale(args.zeroThresholdTriggerRate)
    
theEfficiencyCanvas = ROOT.TCanvas('theEfficiencyCanvas','theEfficiencyCanvas')
theEfficiencyCanvas.Divide(1,2)

plotPad = ROOT.gPad.GetPrimitive('theEfficiencyCanvas_1')
ratioPad = ROOT.gPad.GetPrimitive('theEfficiencyCanvas_2')

plotPad.SetPad("pad1", "plot", 0.0, 0.4, 1.0, 1.0, 0)
ratioPad.SetPad("pad2", "ratio", 0.0, 0.0, 1.0, 0.4, 0)

plotPad.SetLogy()
plotPad.SetBottomMargin(0.0)

ratioPad.SetTopMargin(0.0)
ratioPad.SetBottomMargin(0.27)
ratioPad.SetGridy()

plotPad.cd()

rateAverage.Draw('pe0')
for hist in ratePlots:
    hist.Draw('pe0 SAME')

rateAverage.SetTitle('')
rateAverage.GetXaxis().SetTitle('')
rateAverage.GetYaxis().SetTitle('Rate in kHz (Assuming 40 MHz BX Rate)')
rateAverage.GetYaxis().SetTitleSize(0.05)
rateAverage.GetYaxis().SetTitleOffset(0.7)
rateAverage.GetYaxis().SetLabelSize(0.06)
rateAverage.GetYaxis().CenterTitle()
rateAverage.SetMaximum(50e3)
rateAverage.SetMinimum(1)

cmsLatex = ROOT.TLatex()
cmsLatex.SetTextSize(0.06)
cmsLatex.SetNDC(True)
cmsLatex.SetTextFont(61)
cmsLatex.SetTextAlign(11)
cmsLatex.DrawLatex(0.1,0.92,"CMS")
cmsLatex.SetTextFont(52)
cmsLatex.DrawLatex(0.1+0.06,0.92,"Preliminary")
#cmsLatex.DrawLatex(0.1+0.18,0.92,"Preliminary")

if args.binLabel != None:
    binLabel = ROOT.TLatex()
    binLabel.SetNDC(True)
    binLabel.SetTextFont(52)
    binLabel.SetTextAlign(11)
    binLabel.DrawLatex(0.5,0.92,args.binLabel)

theLegend = ROOT.TLegend(0.65, 0.61, 0.9, 0.9)

theLegend.AddEntry(rateAverage, 'Average of Datasets', 'pl')
for i in range(len(ratePlots)):
    theLegend.AddEntry(ratePlots[i], treeTuples[i][3], 'pl')

theLegend.Draw()

triggerUpperLevel = ROOT.TLine(0.0, 100.0, 10.0, 100.0)
triggerUpperLevel.SetLineColor(ROOT.kRed)
triggerUpperLevel.SetLineWidth(3)
triggerUpperLevel.Draw()

ratioPad.cd()

rateRatioPlots = []
averageRateRatio = rateAverage.Clone()
averageRateRatio.Divide(rateAverage)
averageRateRatio.Draw('pe0')
for hist in ratePlots:
    rateRatio = hist.Clone()
    rateRatio.Divide(rateAverage)
    rateRatioPlots.append( rateRatio )
    rateRatio.Draw('pe0 SAME')

averageRateRatio.SetTitle('')
averageRateRatio.GetXaxis().SetTitle('Anomaly Model MSE Score >')
averageRateRatio.GetXaxis().SetTitleSize(0.1)
averageRateRatio.GetXaxis().SetLabelSize(0.1)
averageRateRatio.GetYaxis().SetTitle('Ratio to Average')
averageRateRatio.GetYaxis().SetRangeUser(0.0, 2.6)

fileName = 'caloL1Emu_anomalyTrigger_EfficiencyDistribution.png' if args.fileExtension==None else 'caloL1Emu_anomalyTrigger_EfficiencyDistribution_'+args.fileExtension+'.png'

theEfficiencyCanvas.SaveAs(fileName)
