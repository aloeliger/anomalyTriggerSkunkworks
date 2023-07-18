#!/usr/bin/env python3

import ROOT
import argparse
import os
import prettytable
import math
from array import array

from drawScorePlots import createEffPlot, convertEffToRate, printRateThresholds

def getListOfAllRates(ratePlot):
    theList = []
    nBins = ratePlot.GetNbinsX()
    for i in range(1,nBins+1):
        theList.append(ratePlot.GetBinContent(i))
    return theList

def main(args):
    ROOT.gStyle.SetOptStat(0)

    theFile = ROOT.TFile(f'/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/pureScorePlots{args.year}CICADAv{args.CICADAVersion}.root')
    destinationPath = f'/nfs_scratch/aloeliger/anomalyPlotFiles/pngFiles/pureScorePlots{args.year}CICADAv{args.CICADAVersion}/'
    if not os.path.isdir(destinationPath):
        os.mkdir(destinationPath)
    
    runs = ['EphemeralZeroBias']
    menus = {
        'EphemeralZeroBias': ['L1Menu_Collisions2018_v2_0_0', 'L1Menu_Collisions2018_v2_1_0']
    }
    menuColors = {
        'L1Menu_Collisions2018_v2_0_0': {
            'overall': ROOT.kBlue,
            'pure': 30,
            'pureMinusMuon': 40
        },
        'L1Menu_Collisions2018_v2_1_0':{
            'overall': ROOT.kGreen,
            'pure': 42,
            'pureMinusMuon': 9
        }
    }

    plots = []

    for run in runs:
        #Let's do one set of canvases per run
        #one for scores
        #one for rates
        scoreCanvas = ROOT.TCanvas(f'{run}_score_canvas')
        scoreCanvas.SetLogy()
        scoreLegend = ROOT.TLegend(0.4,0.7,1.0,1.0)
        scoreLegend.SetTextSize(0.0225)

        rateCanvas = ROOT.TCanvas(f'{run}_rate_canvas')
        rateCanvas.SetLogy()
        rateLegend = ROOT.TLegend(0.4,0.7,1.0,1.0)
        rateLegend.SetTextSize(0.0225)

        #First thing's first, let's grab the overall score plots
        scorePlot = getattr(theFile, f'{run}_score')
        hgScorePlot = getattr(theFile, f'{run}_score_highGranularity')
        #We'll style it, 
        scorePlot.SetLineColor(ROOT.kRed)
        scorePlot.SetMarkerColor(ROOT.kRed)
        scorePlot.SetMarkerStyle(20)
        scorePlot.Scale(1.0/scorePlot.Integral())

        scoreCanvas.cd()
        scorePlot.Draw('E1 X0')
        scorePlot.GetXaxis().SetTitle(f'CICADA v{args.CICADAVersion} score')
        scorePlot.GetYaxis().SetTitle('Fraction (normalized to 1)')
        scorePlot.GetYaxis().SetRangeUser(scorePlot.GetMinimum()+1e-7, scorePlot.GetMaximum()*10)
        scorePlot.SetTitle('')

        scoreLegend.AddEntry(scorePlot, f'{run} score', 'pl')
        plots.append(scorePlot)

        #and make a rate plot from the high granularity version
        effPlot = createEffPlot(hgScorePlot)
        ratePlot = convertEffToRate(effPlot.Clone())
        ratePlot.SetMarkerStyle(6)
        ratePlot.SetMarkerColor(ROOT.kRed)
        ratePlot.SetLineColor(ROOT.kRed)

        rateCanvas.cd()
        ratePlot.Draw('E1 X0')
        ratePlot.GetXaxis().SetTitle(f'CICADA v{args.CICADAVersion} score')
        ratePlot.GetYaxis().SetTitle('Rate (KHz)')
        ratePlot.GetYaxis().SetRangeUser(0.1, ratePlot.GetMaximum()*10)
        ratePlot.SetTitle('')

        rateLegend.AddEntry(ratePlot, f'{run} rate', 'pl')
        plots.append(ratePlot)

        printRateThresholds(ratePlot, run=f'{run}')

        for menu in menus[run]:
            #Then we can grab the per menu plots, these can have score made
            menuScorePlot = getattr(theFile, f'{run}_{menu}_score')
            hgMenuScorePlot = getattr(theFile, f'{run}_{menu}_score_highGranularity')

            menuScorePlot.SetLineColor(menuColors[menu]['overall'])
            menuScorePlot.SetMarkerColor(menuColors[menu]['overall'])
            menuScorePlot.SetMarkerStyle(20)
            menuScorePlot.Scale(1.0/menuScorePlot.Integral())

            scoreCanvas.cd()
            menuScorePlot.Draw('E1 X0 SAME')

            scoreLegend.AddEntry(menuScorePlot, f'{run} {menu} score', 'pl')
            plots.append(menuScorePlot)

            #and rate plots
            menuEffPlot = createEffPlot(hgMenuScorePlot)
            menuRatePlot = convertEffToRate(menuEffPlot.Clone())
            menuRatePlot.SetMarkerStyle(6)
            menuRatePlot.SetMarkerColor(menuColors[menu]['overall'])
            menuRatePlot.SetLineColor(menuColors[menu]['overall'])


            rateCanvas.cd()
            menuRatePlot.Draw('E1 X0 SAME')

            rateLegend.AddEntry(menuRatePlot, f'{run} {menu} Rate', 'pl')
            plots.append(menuRatePlot)
            printRateThresholds(menuRatePlot, run=f'{run} {menu}')

            #Then per menu we can grab the pure score plots and we can make rate plots from these

            pureScorePlot = getattr(theFile, f'{run}_{menu}_pureScore')
            hgPureScorePlot = getattr(theFile, f'{run}_{menu}_pureScore_highGranularity')

            pureScorePlot.SetLineColor(menuColors[menu]['pure'])
            pureScorePlot.SetMarkerColor(menuColors[menu]['pure'])
            pureScorePlot.SetMarkerStyle(20)
            pureScorePlot.Scale(1.0/pureScorePlot.Integral())

            scoreCanvas.cd()
            pureScorePlot.Draw('E1 X0 SAME')

            scoreLegend.AddEntry(pureScorePlot, f'{run} {menu} Pure Score', 'pl')
            plots.append(pureScorePlot)

            pureEffPlot = createEffPlot(hgPureScorePlot)
            pureRatePlot = convertEffToRate(pureEffPlot)
            pureRatePlot.SetMarkerStyle(6)
            pureRatePlot.SetMarkerColor(menuColors[menu]['pure'])
            pureRatePlot.SetLineColor(menuColors[menu]['pure'])
            
            rateCanvas.cd()
            pureRatePlot.Draw('E1 X0 SAME')

            rateLegend.AddEntry(pureRatePlot, f'{run} {menu} Pure Rate', 'pl')
            plots.append(pureRatePlot)

            printRateThresholds(pureRatePlot, f'{run} {menu} Pure')

            #then repeat for pure minus muons

            # pureScoreMinusMuonPlot = getattr(theFile, f'{run}_{menu}_pureScoreMinusMuon')
            # hgPureScorePlot = getattr(theFile, f'{run}_{menu}_pureScoreMinusMuon_highGranularity')

            # pureScoreMinusMuonPlot.SetLineColor(menuColors[menu]['pureMinusMuon'])
            # pureScoreMinusMuonPlot.SetMarkerColor(menuColors[menu]['pureMinusMuon'])
            # pureScoreMinusMuonPlot.SetMarkerStyle(20)
            # pureScoreMinusMuonPlot.Scale(1.0/pureScoreMinusMuonPlot.Integral())

            # scoreCanvas.cd()
            # pureScoreMinusMuonPlot.Draw('E1 X0 SAME')

            # scoreLegend.AddEntry(pureScoreMinusMuonPlot, f'{run} {menu} pure (not counting muon) score', 'pl')
            # plots.append(pureScoreMinusMuonPlot)

            # pureMinusMuonEffPlot = createEffPlot(hgPureScorePlot)
            # pureMinusMuonRatePlot = convertEffToRate(pureMinusMuonEffPlot)
            # pureMinusMuonRatePlot.SetMarkerStyle(6)
            # pureMinusMuonRatePlot.SetMarkerColor(menuColors[menu]['pureMinusMuon'])
            # pureMinusMuonRatePlot.SetLineColor(menuColors[menu]['pureMinusMuon'])
            
            # rateCanvas.cd()
            # pureMinusMuonRatePlot.Draw('E1 X0 SAME')

            # rateLegend.AddEntry(pureMinusMuonRatePlot, f'{run} {menu} pure (not counting)', 'pl')
            # plots.append(pureMinusMuonRatePlot)
            #Then we can try to make a graph of the pure rate for the overall rate
            menuRates = array('d', getListOfAllRates(menuRatePlot))
            pureRates = array('d', getListOfAllRates(pureRatePlot))
            pureVsOverallCurve = ROOT.TGraph(len(menuRates), menuRates, pureRates)
            pureVsOverallCurve.SetTitle(f";CICADA Overall Rate; CICADA Pure Rate")
            pureVsOverallCurve.SetMarkerStyle(7)
            pureVsOverallCurve.SetMarkerColor(ROOT.kRed)
            pureVsOverallCurve.SetLineColor(ROOT.kRed)
            pureVsOverallCanvas = ROOT.TCanvas(f'{run}_{menu}_p_Vs_o')
            pureVsOverallCurve.Draw("A P C")
            pureVsOverallCurve.GetHistogram().GetXaxis().SetRangeUser(0,15)
            pureVsOverallCurve.GetHistogram().GetYaxis().SetRangeUser(0,10)
            cmsLatex = ROOT.TLatex()
            cmsLatex.SetTextSize(0.06)
            cmsLatex.SetNDC(True)
            cmsLatex.SetTextAlign(11)
            cmsLatex.DrawLatex(0.1,0.92, "#font[61]{CMS} #font[52]{Preliminary}")
            menuLatex = ROOT.TLatex()
            menuLatex.SetTextSize(0.04)
            menuLatex.SetNDC(True)
            menuLatex.SetTextAlign(31)
            menuLatex.DrawLatex(0.9, 0.92, "#font[52]{"+menu+"}")
            pureVsOverallCanvas.SaveAs(f'{destinationPath}/{run}_{menu}_p_vs_o.png')

        #then we can draw the canvas for all of these things
        #and let's also report some stats
        scoreCanvas.cd()
        scoreLegend.Draw()
        cmsLatex = ROOT.TLatex()
        cmsLatex.SetTextSize(0.06)
        cmsLatex.SetNDC(True)
        cmsLatex.SetTextAlign(11)
        cmsLatex.DrawLatex(0.1,0.92, "#font[61]{CMS} #font[52]{Preliminary}")

        rateCanvas.cd()
        rateLegend.Draw()
        cmsLatex = ROOT.TLatex()
        cmsLatex.SetTextSize(0.06)
        cmsLatex.SetNDC(True)
        cmsLatex.SetTextAlign(11)
        cmsLatex.DrawLatex(0.1,0.92, "#font[61]{CMS} #font[52]{Preliminary}")

        scoreCanvas.SaveAs(f'{destinationPath}/pureScorePlotCICADAv{args.CICADAVersion}_{run}.png')
        rateCanvas.SaveAs(f'{destinationPath}/pureRatePlotCICADAv{args.CICADAVersion}_{run}.png')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Draw score plots for CICADA versions")
    parser.add_argument(
        '-v',
        '--CICADAVersion',
        default=1,
        type=int,
        help = 'CICADA version',
        choices = [1,2],
        nargs='?'
    )
    parser.add_argument(
        '-y',
        '--year',
        default='2018',
        help='Year of samples to use',
        choices=['2018','2022'],
        nargs='?'
    )

    args = parser.parse_args()

    main(args)