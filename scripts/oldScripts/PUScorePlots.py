#PU plots
from anomalyDetection.anomalyTriggerSkunkworks.plotSettings.PUScoreSettings import makeTreeTuples
import ROOT
import os
import math
import argparse


ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetPaintTextFormat('1.2f')

treeTuples = makeTreeTuples()

nXbins = 20
nYbins = 10
PUScoreHistograms = []
rowNormalHistograms = []
columnNormalHistograms = []
for i in range(len(treeTuples)):
    variableExpression = "npv:anomalyScore>>"
    histName = "PUScore"+treeTuples[i][0]
    individualPUCanvas = ROOT.TCanvas('PUCanvas'+treeTuples[i][0],'PUCanvas'+treeTuples[i][0])
    treeTuples[i][2].Draw(variableExpression+histName+"("+str(nXbins)+",0.0,10.0, "+str(nYbins)+",1,51)")
    PUHist = ROOT.gDirectory.Get(histName).Clone()
    PUHist.SetTitle('')
    PUHist.GetYaxis().SetTitle("Primary Vertices")
    PUHist.GetXaxis().SetTitle("Anomaly Score")
    rowNormalHist = PUHist.Clone()
    columnNormalHist = PUHist.Clone()
    PUHist.Scale(1.0/PUHist.Integral())
    #Let's row normalize
    for j in range(1,1+nYbins):
        rowSum = 0.0
        for k in range(1,1+nXbins):
            rowSum += rowNormalHist.GetBinContent(k, j)
            
        for k in range(1,1+nXbins):
            binContent = rowNormalHist.GetBinContent(k, j)
            try:
                rowNormalHist.SetBinContent(k, j, binContent/rowSum)
            except ZeroDivisionError:
                continue
    for j in range(1,1+nXbins):
        columnSum = 0.0
        for k in range(1,1+nYbins):
            columnSum += columnNormalHist.GetBinContent(j, k)
        for k in range(1, 1+nYbins):
            binContent = columnNormalHist.GetBinContent(j, k)
            try:
                columnNormalHist.SetBinContent(j,k, binContent/columnSum)
            except ZeroDivisionError:
                continue
    PUHist.Draw("COLZ TEXT")
    cmsLatex = ROOT.TLatex()
    cmsLatex.SetTextSize(0.06)
    cmsLatex.SetNDC(True)
    cmsLatex.SetTextFont(61)
    cmsLatex.SetTextAlign(11)
    cmsLatex.DrawLatex(0.1,0.92,"CMS")
    cmsLatex.SetTextFont(52)
    cmsLatex.DrawLatex(0.1+0.08,0.92,"Preliminary")
    individualPUCanvas.SaveAs('PUvsScore_'+treeTuples[i][0]+'.png')
    
    individualRowNormalCanvas = ROOT.TCanvas('rowNormalPU'+treeTuples[i][0], 'rowNormalPU'+treeTuples[i][0])
    rowNormalHist.Draw("COLZ TEXT")
    rowNormalHist.GetXaxis().SetTitle("Anomaly Score (Row Normalized)")
    cmsLatex = ROOT.TLatex()
    cmsLatex.SetTextSize(0.06)
    cmsLatex.SetNDC(True)
    cmsLatex.SetTextFont(61)
    cmsLatex.SetTextAlign(11)
    cmsLatex.DrawLatex(0.1,0.92,"CMS")
    cmsLatex.SetTextFont(52)
    cmsLatex.DrawLatex(0.1+0.08,0.92,"Preliminary")
    individualRowNormalCanvas.SaveAs("rowNormalPUvsScore_"+treeTuples[i][0]+'.png')

    individualColumnNormalCanvas = ROOT.TCanvas('columnNormalPU'+treeTuples[i][0], 'columnNormalPU'+treeTuples[i][0])
    columnNormalHist.Draw("COLZ TEXT")
    columnNormalHist.GetXaxis().SetTitle("Anomaly Score (Column Normalized)")
    cmsLatex = ROOT.TLatex()
    cmsLatex.SetTextSize(0.06)
    cmsLatex.SetNDC(True)
    cmsLatex.SetTextFont(61)
    cmsLatex.SetTextAlign(11)
    cmsLatex.DrawLatex(0.1,0.92,"CMS")
    cmsLatex.SetTextFont(52)
    cmsLatex.DrawLatex(0.1+0.08,0.92,"Preliminary")
    individualColumnNormalCanvas.SaveAs("columnNormalPUvsScore_"+treeTuples[i][0]+'.png')
    
    PUScoreHistograms.append(PUHist)
    rowNormalHistograms.append(rowNormalHist)
    columnNormalHistograms.append(columnNormalHist)

averagePUCanvas = ROOT.TCanvas('averagePUCanvas','averagePUCanvas')

averagePUScore = PUScoreHistograms[0].Clone()
for i in range(1, len(PUScoreHistograms)):
    averagePUScore.Add(PUScoreHistograms[i])
averagePUScore.Scale(1.0/averagePUScore.Integral())

averagePUScore.Draw('COLZ TEXT')
cmsLatex = ROOT.TLatex()
cmsLatex.SetTextSize(0.06)
cmsLatex.SetNDC(True)
cmsLatex.SetTextFont(61)
cmsLatex.SetTextAlign(11)
cmsLatex.DrawLatex(0.1,0.92,"CMS")
cmsLatex.SetTextFont(52)
cmsLatex.DrawLatex(0.1+0.08,0.92,"Preliminary")

averagePUCanvas.SaveAs('PUvsScore_average.png')
