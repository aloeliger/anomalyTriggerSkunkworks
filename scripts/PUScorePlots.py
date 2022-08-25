#let's recreate the original score and efficiency distribution plots
#let's attempt to do this vaguely right this time
import ROOT
import os
import math

ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetPaintTextFormat('1.2f')

years = (
    #'2018A',
    #'2018B',
    '2018C',
    '2018D',
         #'2022A',
         #'2022B',
         #'2022C'
)
legendEntries = [
    #'ZeroBias 2018A',
    #'ZeroBias 2018B',
    'ZeroBias 2018C',
    'ZeroBias 2018D',
#    'ZeroBias 2022A',
#    'ZeroBias 2022B',
#    'ZeroBias 2022C',
]
colors = [
    ROOT.kBlue,
    ROOT.kRed,
    #ROOT.kGreen,
    #ROOT.kMagenta,
]

location = os.getenv("CMSSW_BASE")+'/src/L1Trigger/anomalyTriggerSkunkworks/data/pileupNtuples/'

files = []
trees = []

for year in years:
    theFile = ROOT.TFile(location+'l1TNtuple-ZeroBias-'+year+'.root')
    files.append(theFile)
    trees.append(theFile.L1TCaloSummaryTestNtuplizer.L1TCaloSummaryOutput)

treeTuples = list(zip(years, files, trees, legendEntries, colors))

anomalyScoreHistograms = []

for i in range(len(treeTuples)):
    variable = 'anomalyScore>>'
    histName = 'anomalyHist'+treeTuples[i][0]
    treeTuples[i][2].Draw(variable+histName+'(12,0.0,6.0)')
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
cmsLatex.DrawLatex(0.1+0.06,0.92,"Simulation")
cmsLatex.DrawLatex(0.1+0.18,0.92,"Preliminary")

theLegend = ROOT.TLegend(0.5, 0.61, 0.9, 0.9)

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

################### RATE/EFFICIENCY PLOTS #############################

ratePlots = []
for i in range(len(treeTuples)):
    variable = 'anomalyScore>>'
    histName = 'fineAnomalyHist'+treeTuples[i][0]
    treeTuples[i][2].Draw(variable+histName+'(60, 0.0, 6.0)')
    theHist = ROOT.gDirectory.Get(histName).Clone()    
    theHist.Scale(1.0/theHist.Integral())
    efficiencyHistName = 'efficiency'+treeTuples[i][0]
    theEfficiencyHist = ROOT.TH1F(efficiencyHistName, 
                                  efficiencyHistName,
                                  60, 0.0, 6.0)
    for j in range(60):
        theEfficiencyHist.SetBinContent(60-j, theHist.Integral(60-j, 60))
        errSum = 0.0
        for k in range(i,60):
            errSum += theHist.GetBinError(k)**2
        err = math.sqrt(errSum)
        theEfficiencyHist.SetBinError(60-j,err)
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

triggerUpperLevel = ROOT.TLine(0.0, 100.0, 6.0, 100.0)
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

##################### PU Plot #################################

PUScoreHistograms = []
rowNormalHistograms = []
for i in range(len(treeTuples)):
    variableExpression = "npv:anomalyScore>>"
    histName = "PUScore"+treeTuples[i][0]
    individualPUCanvas = ROOT.TCanvas('PUCanvas'+treeTuples[i][0],'PUCanvas'+treeTuples[i][0])
    treeTuples[i][2].Draw(variableExpression+histName+"(24,0.0,6.0, 10,1,51)")
    PUHist = ROOT.gDirectory.Get(histName).Clone()
    PUHist.GetYaxis().SetTitle("Primary Vertices")
    PUHist.GetXaxis().SetTitle("Anomaly Score")
    rowNormalHist = PUHist.Clone()
    PUHist.Scale(1.0/PUHist.Integral())
    #Let's row normalize
    for j in range(1,11):
        rowSum = 0.0
        for k in range(1,25):
            rowSum += rowNormalHist.GetBinContent(k, j)
            
        for k in range(1,25):
            binContent = rowNormalHist.GetBinContent(k, j)
            try:
                rowNormalHist.SetBinContent(k, j, binContent/rowSum)
            except ZeroDivisionError:
                continue
            
    PUHist.Draw("COLZ TEXT")
    individualPUCanvas.SaveAs('PUvsScore_'+treeTuples[i][0]+'.png')
    
    individualRowNormalCanvas = ROOT.TCanvas('rowNormalPU'+treeTuples[i][0], 'rowNormalPU'+treeTuples[i][0])
    rowNormalHist.Draw("COLZ TEXT")
    rowNormalHist.GetXaxis().SetTitle("Anomaly Score (Row Normalized)")
    individualRowNormalCanvas.SaveAs("rowNormalPUvsScore_"+treeTuples[i][0]+'.png')
    
    PUScoreHistograms.append(PUHist)
    rowNormalHistograms.append(rowNormalHist)

averagePUCanvas = ROOT.TCanvas('averagePUCanvas','averagePUCanvas')

averagePUScore = PUScoreHistograms[0].Clone()
for i in range(1, len(PUScoreHistograms)):
    averagePUScore.Add(PUScoreHistograms[i])
averagePUScore.Scale(1.0/averagePUScore.Integral())

averagePUScore.Draw('COLZ TEXT')

averagePUCanvas.SaveAs('PUvsScore_average.png')
