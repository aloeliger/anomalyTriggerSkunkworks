#let's recreate the original score and efficiency distribution plots
#let's attempt to do this vaguely right this time
from L1Trigger.anomalyTriggerSkunkworks.plotSettings.PUScoreSettings import makeTreeTuples
import ROOT
import os
import math

ROOT.gStyle.SetOptStat(0)

treeTuples = makeTreeTuples()

ratePlots = []
for i in range(len(treeTuples)):
    variable = 'anomalyScore>>'
    histName = 'fineAnomalyHist'+treeTuples[i][0]
    treeTuples[i][2].Draw(variable+histName+'(50, 0.0, 10.0)')
    theHist = ROOT.gDirectory.Get(histName).Clone()    
    theHist.Scale(1.0/theHist.Integral())
    efficiencyHistName = 'efficiency'+treeTuples[i][0]
    theEfficiencyHist = ROOT.TH1F(efficiencyHistName, 
                                  efficiencyHistName,
                                  50, 0.0, 10.0)
    for j in range(50):
        theEfficiencyHist.SetBinContent(50-j, theHist.Integral(50-j, 50))
        errSum = 0.0
        for k in range(i,50):
            errSum += theHist.GetBinError(k)**2
        err = math.sqrt(errSum)
        theEfficiencyHist.SetBinError(50-j,err)
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
rateAverage.Scale(40.0e3)
for hist in ratePlots:
    hist.Scale(40.0e3)
    
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

cmsLatex = ROOT.TLatex()
cmsLatex.SetTextSize(0.06)
cmsLatex.SetNDC(True)
cmsLatex.SetTextFont(61)
cmsLatex.SetTextAlign(11)
cmsLatex.DrawLatex(0.1,0.92,"CMS")
cmsLatex.SetTextFont(52)
cmsLatex.DrawLatex(0.1+0.06,0.92,"Simulation")
cmsLatex.DrawLatex(0.1+0.18,0.92,"Preliminary")

theLegend = ROOT.TLegend(0.5, 0.61, 0.9, 0.9)

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

theEfficiencyCanvas.SaveAs('caloL1Emu_anomalyTrigger_EfficiencyDistribution.png')
