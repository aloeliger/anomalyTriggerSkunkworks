#Another TERRIBLE script for doing some necessary plots
#But I just want this done fast, not correct programming style
#... famous last words
import ROOT
import os
import math

ROOT.gStyle.SetOptStat(0)

file2018A = ROOT.TFile(os.getenv('CMSSW_BASE')+'/src/L1Trigger/anomalyTriggerSkunkworks/l1TNtuple-ZeroBias-2018A.root')
file2018B = ROOT.TFile(os.getenv('CMSSW_BASE')+'/src/L1Trigger/anomalyTriggerSkunkworks/l1TNtuple-ZeroBias-2018B.root')
file2018C = ROOT.TFile(os.getenv('CMSSW_BASE')+'/src/L1Trigger/anomalyTriggerSkunkworks/l1TNtuple-ZeroBias-2018C.root')
file2018D = ROOT.TFile(os.getenv('CMSSW_BASE')+'/src/L1Trigger/anomalyTriggerSkunkworks/l1TNtuple-ZeroBias-2018D.root')
file2022A = ROOT.TFile(os.getenv('CMSSW_BASE')+'/src/L1Trigger/anomalyTriggerSkunkworks/l1TNtuple-ZeroBias-2022A.root')
file2022B = ROOT.TFile(os.getenv('CMSSW_BASE')+'/src/L1Trigger/anomalyTriggerSkunkworks/l1TNtuple-ZeroBias-2022B.root')
file2022C = ROOT.TFile(os.getenv('CMSSW_BASE')+'/src/L1Trigger/anomalyTriggerSkunkworks/l1TNtuple-ZeroBias-2022C.root')

#Let's just draw score distributions so we can look at them compared to each other and the model tests
################################################################

tree2018A = file2018A.L1TCaloSummaryTestNtuplizer.L1TCaloSummaryOutput
tree2018B = file2018B.L1TCaloSummaryTestNtuplizer.L1TCaloSummaryOutput
tree2018C = file2018C.L1TCaloSummaryTestNtuplizer.L1TCaloSummaryOutput
tree2018D = file2018D.L1TCaloSummaryTestNtuplizer.L1TCaloSummaryOutput
tree2022A = file2022A.L1TCaloSummaryTestNtuplizer.L1TCaloSummaryOutput
tree2022B = file2022B.L1TCaloSummaryTestNtuplizer.L1TCaloSummaryOutput
tree2022C = file2022C.L1TCaloSummaryTestNtuplizer.L1TCaloSummaryOutput

tree2018A.Draw("anomalyScore>>anomalyHist2018A(12, 0.0, 6.0)")
tree2018B.Draw("anomalyScore>>anomalyHist2018B(12, 0.0, 6.0)")
tree2018C.Draw("anomalyScore>>anomalyHist2018C(12, 0.0, 6.0)")
tree2018D.Draw("anomalyScore>>anomalyHist2018D(12, 0.0, 6.0)")
tree2022A.Draw("anomalyScore>>anomalyHist2022A(12, 0.0, 6.0)")
tree2022B.Draw("anomalyScore>>anomalyHist2022B(12, 0.0, 6.0)")
tree2022C.Draw("anomalyScore>>anomalyHist2022C(12, 0.0, 6.0)")

hist2018A = ROOT.gDirectory.Get('anomalyHist2018A').Clone()
hist2018B = ROOT.gDirectory.Get('anomalyHist2018B').Clone()
hist2018C = ROOT.gDirectory.Get('anomalyHist2018C').Clone()
hist2018D = ROOT.gDirectory.Get('anomalyHist2018D').Clone()
hist2022A = ROOT.gDirectory.Get('anomalyHist2022A').Clone()
hist2022B = ROOT.gDirectory.Get('anomalyHist2022B').Clone()
hist2022C = ROOT.gDirectory.Get('anomalyHist2022C').Clone()

theScoreCanvas = ROOT.TCanvas('theScoreCanvas','theScoreCanvas')
theScoreCanvas.Divide(1,2)

plotPad = ROOT.gPad.GetPrimitive('theScoreCanvas_1')
ratioPad = ROOT.gPad.GetPrimitive('theScoreCanvas_2')

plotPad.SetPad("pad1", "plot", 0.0, 0.4, 1.0, 1.0, 0)
ratioPad.SetPad("pad2", "ratio", 0.0, 0.0, 1.0, 0.4, 0)

plotPad.SetLogy()
plotPad.SetBottomMargin(0.0)

ratioPad.SetTopMargin(0.0)
ratioPad.SetBottomMargin(0.27)
ratioPad.SetGridy()

plotPad.cd()

hist2018A.Scale(1.0/hist2018A.Integral())
hist2018B.Scale(1.0/hist2018B.Integral())
hist2018C.Scale(1.0/hist2018C.Integral())
hist2018D.Scale(1.0/hist2018D.Integral())
hist2022A.Scale(1.0/hist2022A.Integral())
hist2022B.Scale(1.0/hist2022B.Integral())
hist2022C.Scale(1.0/hist2022C.Integral())

histAverage = hist2018A.Clone()
histAverage.Add(hist2018B)
histAverage.Add(hist2018C)
histAverage.Add(hist2018D)
histAverage.Scale(1.0/4.0)

hist2018A.SetLineColor(ROOT.kBlue)
hist2018B.SetLineColor(ROOT.kSpring)
hist2018C.SetLineColor(ROOT.kTeal)
hist2018D.SetLineColor(ROOT.kMagenta)
hist2022A.SetLineColor(ROOT.kOrange)
hist2022B.SetLineColor(ROOT.kRed)
hist2022C.SetLineColor(ROOT.kCyan)
histAverage.SetLineColor(ROOT.kBlack)

hist2018A.SetLineWidth(2)
hist2018B.SetLineWidth(2)
hist2018C.SetLineWidth(2)
hist2018D.SetLineWidth(2)
hist2022A.SetLineWidth(2)
hist2022B.SetLineWidth(2)
hist2022C.SetLineWidth(2)
histAverage.SetLineWidth(2)

hist2018A.SetMarkerStyle(20)
hist2018B.SetMarkerStyle(21)
hist2018C.SetMarkerStyle(22)
hist2018D.SetMarkerStyle(23)
hist2022A.SetMarkerStyle(24)
hist2022B.SetMarkerStyle(25)
hist2022C.SetMarkerStyle(26)
histAverage.SetMarkerStyle(27)

histAverage.Draw('pe0')
hist2018A.Draw('pe0 SAME')
hist2018B.Draw('pe0 SAME')
hist2018C.Draw('pe0 SAME')
hist2018D.Draw('pe0 SAME')
hist2022A.Draw('pe0 SAME')
#hist2022B.Draw('pe0 SAME')
#hist2022C.Draw('pe0 SAME')

histAverage.SetTitle('')
histAverage.GetXaxis().SetTitle('')
histAverage.GetYaxis().SetTitle('10^{5} Events, Normalized')
histAverage.GetYaxis().SetTitleSize(0.08)
histAverage.GetYaxis().SetTitleOffset(0.6)
histAverage.GetYaxis().SetLabelSize(0.06)
histAverage.GetYaxis().CenterTitle()


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

theLegend.AddEntry(histAverage, 'ZeroBias, 2018 Average', 'pl')
theLegend.AddEntry(hist2018A, 'ZeroBias, 2018A', 'pl')
theLegend.AddEntry(hist2018B, 'ZeroBias, 2018B', 'pl')
theLegend.AddEntry(hist2018C, 'ZeroBias, 2018C', 'pl')
theLegend.AddEntry(hist2018D, 'ZeroBias, 2018D (training set?)', 'pl')
theLegend.AddEntry(hist2022A, 'ZeroBias, 2022A', 'pl')
#theLegend.AddEntry(hist2022B, 'ZeroBias, 2022B', 'pl')
#theLegend.AddEntry(hist2022C,"ZeroBias, 2022C", 'pl')

theLegend.Draw()

ratioPad.cd()

histAverageRatio = histAverage.Clone()
histAverageRatio.Divide(histAverage)
hist2018ARatio = hist2018A.Clone()
hist2018ARatio.Divide(histAverage)
hist2018BRatio = hist2018B.Clone()
hist2018BRatio.Divide(histAverage)
hist2018CRatio = hist2018C.Clone()
hist2018CRatio.Divide(histAverage)
hist2018DRatio = hist2018D.Clone()
hist2018DRatio.Divide(histAverage)
hist2022ARatio = hist2022A.Clone()
hist2022ARatio.Divide(histAverage)
hist2022BRatio = hist2022B.Clone()
hist2022BRatio.Divide(histAverage)
hist2022CRatio = hist2022C.Clone()
hist2022CRatio.Divide(histAverage)

histAverageRatio.Draw('pe0')
hist2018ARatio.Draw('pe0 SAME')
hist2018BRatio.Draw('pe0 SAME')
hist2018CRatio.Draw('pe0 SAME')
hist2018DRatio.Draw('pe0 SAME')
hist2022ARatio.Draw('pe0 SAME')
#hist2022BRatio.Draw('pe0 SAME')
#hist2022CRatio.Draw('pe0 SAME')

histAverageRatio.SetTitle('')
histAverageRatio.GetXaxis().SetTitle('Anomaly Model MSE Score')
histAverageRatio.GetXaxis().SetTitleSize(0.1)
histAverageRatio.GetXaxis().SetLabelSize(0.1)
histAverageRatio.GetYaxis().SetTitle('Ratio to 2018 Average')
histAverageRatio.GetYaxis().SetRangeUser(0.0, 2.6)

theScoreCanvas.SaveAs('caloL1Emu_anomalyTrigger_ScoreDistribution.png')

################################################################

tree2018A.Draw("anomalyScore>>fineAnomalyHist2018A(60, 0.0, 6.0)")
tree2018B.Draw("anomalyScore>>fineAnomalyHist2018B(60, 0.0, 6.0)")
tree2018C.Draw("anomalyScore>>fineAnomalyHist2018C(60, 0.0, 6.0)")
tree2018D.Draw("anomalyScore>>fineAnomalyHist2018D(60, 0.0, 6.0)")
tree2022A.Draw("anomalyScore>>fineAnomalyHist2022A(60, 0.0, 6.0)")
tree2022B.Draw("anomalyScore>>fineAnomalyHist2022B(60, 0.0, 6.0)")
tree2022C.Draw("anomalyScore>>fineAnomalyHist2022C(60, 0.0, 6.0)")

fineHist2018A = ROOT.gDirectory.Get('fineAnomalyHist2018A').Clone()
fineHist2018B = ROOT.gDirectory.Get('fineAnomalyHist2018B').Clone()
fineHist2018C = ROOT.gDirectory.Get('fineAnomalyHist2018C').Clone()
fineHist2018D = ROOT.gDirectory.Get('fineAnomalyHist2018D').Clone()
fineHist2022A = ROOT.gDirectory.Get('fineAnomalyHist2022A').Clone()
fineHist2022B = ROOT.gDirectory.Get('fineAnomalyHist2022B').Clone()
fineHist2022C = ROOT.gDirectory.Get('fineAnomalyHist2022C').Clone()

fineHist2018A.Scale(1.0/fineHist2018A.Integral())
fineHist2018B.Scale(1.0/fineHist2018B.Integral())
fineHist2018C.Scale(1.0/fineHist2018C.Integral())
fineHist2018D.Scale(1.0/fineHist2018D.Integral())
fineHist2022A.Scale(1.0/fineHist2022A.Integral())
fineHist2022B.Scale(1.0/fineHist2022B.Integral())
fineHist2022C.Scale(1.0/fineHist2022C.Integral())

efficiencyHistogram2018A = ROOT.TH1F('efficiency2018A','efficiency2018A', 60, 0.0, 6.0)
efficiencyHistogram2018B = ROOT.TH1F('efficiency2018B','efficiency2018B', 60, 0.0, 6.0)
efficiencyHistogram2018C = ROOT.TH1F('efficiency2018C','efficiency2018C', 60, 0.0, 6.0)
efficiencyHistogram2018D = ROOT.TH1F('efficiency2018D','efficiency2018D', 60, 0.0, 6.0)
efficiencyHistogram2022A = ROOT.TH1F('efficiency2022A','efficiency2022A', 60, 0.0, 6.0)
efficiencyHistogram2022B = ROOT.TH1F('efficiency2022B','efficiency2022B', 60, 0.0, 6.0)
efficiencyHistogram2022C = ROOT.TH1F('efficiency2022C','efficiency2022C', 60, 0.0, 6.0)

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

#Integrate backwards over the bins
#this may be the only well~ish programmed thing here...
for histTuple in [(efficiencyHistogram2018A, fineHist2018A),
                  (efficiencyHistogram2018B, fineHist2018B),
                  (efficiencyHistogram2018C, fineHist2018C),
                  (efficiencyHistogram2018D, fineHist2018D),
                  (efficiencyHistogram2022A, fineHist2022A),
                  (efficiencyHistogram2022B, fineHist2022B),
                  (efficiencyHistogram2022C, fineHist2022C)]:
    for i in range(60):
        histTuple[0].SetBinContent(60-i, histTuple[1].Integral(60-i, 60))
        errSum = 0.0
        for j in range(i,60):
            errSum += histTuple[1].GetBinError(j)**2
        err = math.sqrt(errSum)
        histTuple[0].SetBinError(60-i, err)

efficiencyHistogramAverage = efficiencyHistogram2018A.Clone()
efficiencyHistogramAverage.Add(efficiencyHistogram2018B)
efficiencyHistogramAverage.Add(efficiencyHistogram2018C)
efficiencyHistogramAverage.Add(efficiencyHistogram2018D)
#efficiencyHistogramAverage.Add(efficiencyHistogram2022A)
#efficiencyHistogramAverage.Add(efficiencyHistogram2022B)
#efficiencyHistogramAverage.Add(efficiencyHistogram2022C)

efficiencyHistogramAverage.Scale(1.0/5.0)

#Scale to system rate
for x in [efficiencyHistogram2018A, 
          efficiencyHistogram2018B, 
          efficiencyHistogram2018C,
          efficiencyHistogram2018D,
          efficiencyHistogramAverage]:
    x.Scale(40.0e3)

efficiencyHistogram2018A.SetLineColor(ROOT.kBlue)
efficiencyHistogram2018B.SetLineColor(ROOT.kSpring)
efficiencyHistogram2018C.SetLineColor(ROOT.kTeal)
efficiencyHistogram2018D.SetLineColor(ROOT.kMagenta)
efficiencyHistogram2022A.SetLineColor(ROOT.kOrange)
efficiencyHistogram2022B.SetLineColor(ROOT.kRed)
efficiencyHistogram2022C.SetLineColor(ROOT.kCyan)

efficiencyHistogramAverage.SetLineColor(ROOT.kBlack)

efficiencyHistogram2018A.SetLineWidth(2)
efficiencyHistogram2018B.SetLineWidth(2)
efficiencyHistogram2018C.SetLineWidth(2)
efficiencyHistogram2018D.SetLineWidth(2)
efficiencyHistogram2022A.SetLineWidth(2)
efficiencyHistogram2022B.SetLineWidth(2)
efficiencyHistogram2022C.SetLineWidth(2)

efficiencyHistogramAverage.SetLineWidth(2)

efficiencyHistogram2018A.SetMarkerStyle(20)
efficiencyHistogram2018B.SetMarkerStyle(21)
efficiencyHistogram2018C.SetMarkerStyle(22)
efficiencyHistogram2018D.SetMarkerStyle(23)
efficiencyHistogram2022A.SetMarkerStyle(24)
efficiencyHistogram2022B.SetMarkerStyle(25)
efficiencyHistogram2022C.SetMarkerStyle(26)

efficiencyHistogramAverage.SetMarkerStyle(27)

efficiencyHistogramAverage.Draw('pe0')
efficiencyHistogram2018A.Draw('pe0 SAME')
efficiencyHistogram2018B.Draw('pe0 SAME')
efficiencyHistogram2018C.Draw('pe0 SAME')
efficiencyHistogram2018D.Draw('pe0 SAME')
#efficiencyHistogram2022A.Draw('pe0 SAME')
#efficiencyHistogram2022B.Draw('pe0 SAME')
#efficiencyHistogram2022C.Draw('pe0 SAME')

efficiencyHistogramAverage.SetTitle('')
efficiencyHistogramAverage.GetXaxis().SetTitle('')
efficiencyHistogramAverage.GetYaxis().SetTitle('Rate in kHz (Assuming 40 MHz BX Rate)')
efficiencyHistogramAverage.GetYaxis().SetTitleSize(0.05)
efficiencyHistogramAverage.GetYaxis().SetTitleOffset(0.7)
efficiencyHistogramAverage.GetYaxis().SetLabelSize(0.06)
efficiencyHistogramAverage.GetYaxis().CenterTitle()

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

theLegend.AddEntry(efficiencyHistogramAverage, 'Average of selected datasets', 'pl')
theLegend.AddEntry(efficiencyHistogram2018A, 'ZeroBias, 2018A', 'pl')
theLegend.AddEntry(efficiencyHistogram2018B, 'ZeroBias, 2018B', 'pl')
theLegend.AddEntry(efficiencyHistogram2018C, 'ZeroBias, 2018C', 'pl')
theLegend.AddEntry(efficiencyHistogram2018D, 'ZeroBias, 2018D (training set?)', 'pl')
#theLegend.AddEntry(efficiencyHistogram2022A, 'ZeroBias, 2022A, Run 352416', 'pl')

theLegend.Draw()

triggerUpperLevel = ROOT.TLine(0.0, 100.0, 6.0, 100.0)
triggerUpperLevel.SetLineColor(ROOT.kRed)
triggerUpperLevel.SetLineWidth(3)
triggerUpperLevel.Draw()

ratioPad.cd()

efficiencyHistogramAverageRatio = efficiencyHistogramAverage.Clone()
efficiencyHistogramAverageRatio.Divide(efficiencyHistogramAverage)
efficiencyHistogram2018ARatio = efficiencyHistogram2018A.Clone()
efficiencyHistogram2018ARatio.Divide(efficiencyHistogramAverage)
efficiencyHistogram2018BRatio = efficiencyHistogram2018B.Clone()
efficiencyHistogram2018BRatio.Divide(efficiencyHistogramAverage)
efficiencyHistogram2018CRatio = efficiencyHistogram2018C.Clone()
efficiencyHistogram2018CRatio.Divide(efficiencyHistogramAverage)
efficiencyHistogram2018DRatio = efficiencyHistogram2018D.Clone()
efficiencyHistogram2018DRatio.Divide(efficiencyHistogramAverage)
efficiencyHistogram2022ARatio = efficiencyHistogram2022A.Clone()
efficiencyHistogram2022ARatio.Divide(efficiencyHistogramAverage)
efficiencyHistogram2022BRatio = efficiencyHistogram2022B.Clone()
efficiencyHistogram2022BRatio.Divide(efficiencyHistogramAverage)
efficiencyHistogram2022CRatio = efficiencyHistogram2022C.Clone()
efficiencyHistogram2022CRatio.Divide(efficiencyHistogramAverage)

efficiencyHistogramAverageRatio.Draw('pe0')
efficiencyHistogram2018ARatio.Draw('pe0 SAME')
efficiencyHistogram2018BRatio.Draw('pe0 SAME')
efficiencyHistogram2018CRatio.Draw('pe0 SAME')
efficiencyHistogram2018DRatio.Draw('pe0 SAME')
#efficiencyHistogram2022ARatio.Draw('pe0 SAME')
#efficiencyHistogram2022BRatio.Draw('pe0 SAME')
#efficiencyHistogram2022CRatio.Draw('pe0 SAME')

efficiencyHistogramAverageRatio.SetTitle('')
efficiencyHistogramAverageRatio.GetXaxis().SetTitle('Anomaly Model MSE Score >')
efficiencyHistogramAverageRatio.GetXaxis().SetTitleSize(0.1)
efficiencyHistogramAverageRatio.GetXaxis().SetLabelSize(0.1)
efficiencyHistogramAverageRatio.GetYaxis().SetTitle('Ratio to Average')
efficiencyHistogramAverageRatio.GetYaxis().SetRangeUser(0.0, 2.6)

theEfficiencyCanvas.SaveAs('caloL1Emu_anomalyTrigger_EfficiencyDistribution.png')
