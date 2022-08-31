#let's recreate the original score and efficiency distribution plots
#let's attempt to do this vaguely right this time
from L1Trigger.anomalyTriggerSkunkworks.plotSettings.PUScoreSettings import makeTreeTuples
import ROOT
import os
import math

ROOT.gStyle.SetOptStat(0)

treeTuples = makeTreeTuples()

anomalyScoreHistograms = []

for i in range(len(treeTuples)):
    variable = 'anomalyScore>>'
    histName = 'anomalyHist'+treeTuples[i][0]
    treeTuples[i][2].Draw(variable+histName+'(20,0.0,10.0)')
    theHist = ROOT.gDirectory.Get(histName).Clone()
    theHist.Scale(1.0/theHist.Integral())
    theHist.SetLineColor(treeTuples[i][4])
    theHist.SetLineWidth(2)
    theHist.SetMarkerStyle(20+i)
    anomalyScoreHistograms.append( theHist )

averageAnomalyScoreHistogram = anomalyScoreHistograms[0].Clone()
for i in range(1,len(anomalyScoreHistograms)):
    averageAnomalyScoreHistogram.Add(anomalyScoreHistograms[i])
averageAnomalyScoreHistogram.Scale(1.0/averageAnomalyScoreHistogram.Integral())
averageAnomalyScoreHistogram.SetMarkerStyle(8)
averageAnomalyScoreHistogram.SetLineColor(ROOT.kBlack)

theScoreCanvas = ROOT.TCanvas('theScoreCanvas','theScoreCanvase')
theScoreCanvas.Divide(1,2)

plotPad = ROOT.gPad.GetPrimitive('theScoreCanvas_1')
ratioPad = ROOT.gPad.GetPrimitive('theScoreCanvas_2')

plotPad.SetLogy()
plotPad.SetBottomMargin(0.0)

ratioPad.SetTopMargin(0.0)
ratioPad.SetBottomMargin(0.27)
ratioPad.SetGridy()

plotPad.cd()

averageAnomalyScoreHistogram.Draw('pe0')
for hist in anomalyScoreHistograms:
    hist.Draw('pe0 SAME')

averageAnomalyScoreHistogram.SetTitle('')
averageAnomalyScoreHistogram.GetXaxis().SetTitle('')
averageAnomalyScoreHistogram.GetYaxis().SetTitle('10^{5} Events, Normalized')
averageAnomalyScoreHistogram.GetYaxis().SetTitleSize(0.08)
averageAnomalyScoreHistogram.GetYaxis().SetTitleOffset(0.6)
averageAnomalyScoreHistogram.GetYaxis().SetLabelSize(0.06)
averageAnomalyScoreHistogram.GetYaxis().CenterTitle()


cmsLatex = ROOT.TLatex()
cmsLatex.SetTextSize(0.06)
cmsLatex.SetNDC(True)
cmsLatex.SetTextFont(61)
cmsLatex.SetTextAlign(11)
cmsLatex.DrawLatex(0.1,0.92,"CMS")
cmsLatex.SetTextFont(52)
cmsLatex.DrawLatex(0.1+0.06,0.92,"Preliminary")
#cmsLatex.DrawLatex(0.1+0.18,0.92,"Preliminary")

theLegend = ROOT.TLegend(0.65, 0.61, 0.9, 0.9)

theLegend.AddEntry(averageAnomalyScoreHistogram, 'ZeroBias 2018 Average', 'pl')
for i in range(len(anomalyScoreHistograms)):
    theLegend.AddEntry(anomalyScoreHistograms[i], treeTuples[i][3], 'pl')

theLegend.Draw()

ratioPad.cd()

ratioHists = []
averageAnomalyScoreRatio = averageAnomalyScoreHistogram.Clone()
averageAnomalyScoreRatio.Divide(averageAnomalyScoreHistogram)
for i in range(len(anomalyScoreHistograms)):
    ratioHist = anomalyScoreHistograms[i].Clone()
    ratioHist.Divide(averageAnomalyScoreHistogram)
    ratioHists.append(ratioHist)

averageAnomalyScoreRatio.Draw('pe0')
for hist in ratioHists:
    hist.Draw('pe0 SAME')

averageAnomalyScoreRatio.SetTitle('')
averageAnomalyScoreRatio.GetXaxis().SetTitle('Anomaly Model MSE Score')
averageAnomalyScoreRatio.GetXaxis().SetTitleSize(0.1)
averageAnomalyScoreRatio.GetXaxis().SetLabelSize(0.1)
averageAnomalyScoreRatio.GetYaxis().SetTitle('Ratio to 2018 Average')
averageAnomalyScoreRatio.GetYaxis().SetRangeUser(0.0, 2.6)

theScoreCanvas.SaveAs('caloL1Emu_anomalyTrigger_ScoreDistribution.png')
