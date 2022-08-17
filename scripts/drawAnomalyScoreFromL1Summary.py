print('startup...')

print('import ROOT...')
import ROOT
print('import os...')
import os

#Just going to do this quickly and poorly. This doesn't have to be a dedicated tool. Just a
#Proof of concept. If this becomes necessary later, it can adapted into something real
ROOT.gStyle.SetOptStat(0)

print('loading files...')
file2018A = ROOT.TFile(os.getenv('CMSSW_BASE')+'/src/L1Trigger/anomalyTriggerSkunkworks/l1TNtuple-ZeroBias-2018A.root')
file2018D = ROOT.TFile(os.getenv('CMSSW_BASE')+'/src/L1Trigger/anomalyTriggerSkunkworks/l1TNtuple-ZeroBias-2018D.root')
file2022CEphemeral = ROOT.TFile(os.getenv('CMSSW_BASE')+'/src/L1Trigger/anomalyTriggerSkunkworks/l1TNtuple-EphemeralZeroBias0-2022C.root')
file2022C = ROOT.TFile(os.getenv('CMSSW_BASE')+'/src/L1Trigger/anomalyTriggerSkunkworks/l1TNtuple-ZeroBias-2022C.root')

print('loading trees...')
tree2018A = file2018A.L1TCaloSummaryTestNtuplizer.L1TCaloSummaryOutput
tree2018D = file2018D.L1TCaloSummaryTestNtuplizer.L1TCaloSummaryOutput
tree2022CEphemeral = file2022CEphemeral.L1TCaloSummaryTestNtuplizer.L1TCaloSummaryOutput
tree2022C = file2022CEphemeral.L1TCaloSummaryTestNtuplizer.L1TCaloSummaryOutput

print('drawing histograms...')
tree2018A.Draw("anomalyScore>>anomalyHist2018A(20, 0.0, 10.0)")
tree2018D.Draw("anomalyScore>>anomalyHist2018D(20, 0.0, 10.0)")
tree2022CEphemeral.Draw("anomalyScore>>anomalyHist2022CEphemeral(20, 0.0, 10.0)")
tree2022C.Draw("anomalyScore>>anomalyHist2022C(20, 0.0, 10.0)")

print('retrieving histograms...')
hist2018A = ROOT.gDirectory.Get('anomalyHist2018A').Clone()
hist2018D = ROOT.gDirectory.Get('anomalyHist2018D').Clone()
hist2022CEphemeral = ROOT.gDirectory.Get('anomalyHist2022CEphemeral').Clone()
hist2022C = ROOT.gDirectory.Get('anomalyHist2022C').Clone()

print('setting up the canvas...')
theCanvas = ROOT.TCanvas("theCanvas", "theCanvas")
theCanvas.SetLogy()

hist2018A.Scale(1.0/hist2018A.Integral())
hist2018D.Scale(1.0/hist2018D.Integral())
hist2022CEphemeral.Scale(1.0/hist2022CEphemeral.Integral())
hist2022C.Scale(1.0/hist2022C.Integral())

hist2018A.SetLineColor(ROOT.kAzure-2)
hist2018D.SetLineColor(ROOT.kGreen+3)
hist2022CEphemeral.SetLineColor(ROOT.kRed+1)
hist2022C.SetLineColor(ROOT.kViolet)

hist2018A.SetTitle('')
hist2018A.GetXaxis().SetTitle('Quantized Student Model MSE Score')
hist2018A.GetYaxis().SetTitle('1E4 Events, Normalized to 1.')

hist2018A.Draw("e0")
hist2018D.Draw("e0 SAME")
hist2022CEphemeral.Draw("e0 SAME")
hist2022C.Draw("e0 SAME")

cmsLatex = ROOT.TLatex()
cmsLatex.SetTextSize(0.06)
cmsLatex.SetNDC(True)
cmsLatex.SetTextFont(61)
cmsLatex.SetTextAlign(11)
cmsLatex.DrawLatex(0.1,0.92,"CMS")
cmsLatex.SetTextFont(52)
cmsLatex.DrawLatex(0.1+0.08,0.92,"Preliminary")

cmsLatex.SetTextAlign(31)
cmsLatex.SetTextFont(42)

cmsLatex.Draw()

theLegend = ROOT.TLegend(0.5,0.61,0.9,0.9)
theLegend.AddEntry(hist2018A, 'ZeroBias, 2018A, Run 315252', 'l')
theLegend.AddEntry(hist2018D, 'ZeroBias, 2018D, Run 323940 (training set?)', 'l')
theLegend.AddEntry(hist2022CEphemeral,"EphemeralZeroBias, 2022C, Run 335862", 'l')
theLegend.AddEntry(hist2022C,"ZeroBias, 2022C, Run 335862", 'l')

theLegend.Draw()

print('saving the canvas...')
theCanvas.SaveAs("caloL1Emu_anomalyTrigger.png")
