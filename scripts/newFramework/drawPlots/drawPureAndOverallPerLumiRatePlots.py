# !/usr/bin/env python3
import ROOT
import os
import argparse
from drawScorePlots import convertEffToRate
import re
from drawPerLumiRatePlot import smoothPlot
from rich.console import Console

console = Console()

def makeRunPlot(run, theFile, destinationPath, CICADAVersion, drawBoostedJets = False):
    # print('run: ', run)
    # print('Associated objects:')
    listOfKeys = list(theFile.GetListOfKeys())
    listOfNames = [x.GetName() for x in listOfKeys if run in x.GetName()]
    # print(listOfNames)
    match = re.search('L1Menu_.*_v[0-9]_[0-9]_[0-9]', listOfNames[0])
    if match:
        menuName = match.group(0)
        # print(menuName)
    else:
        console.log('failed to match menu name')
        return
    CICADAName = f'CICADA_{run}_{menuName}'

    zeroBiasPlot = getattr(theFile, f'{CICADAName}_overall_ZeroBias_eventsPerLumi')

    overall5kHZPlot = getattr(theFile, f'{CICADAName}_overall_5kHz_eventsPerLumi')
    pure3kHZPlot = getattr(theFile, f'{CICADAName}_pure_3kHz_eventsPerLumi')
    singleMuPlot = getattr(theFile, f'L1_SingleMu22_{run}_{menuName}_overall_eventsPerLumi')
    singleJetPlot = getattr(theFile, f'L1_SingleJet180_{run}_{menuName}_overall_eventsPerLumi')
    singleTauPlot = getattr(theFile, f'L1_SingleTau120er2p1_{run}_{menuName}_overall_eventsPerLumi')
    boostedJetPlot = getattr(theFile, f'boostedJetTrigger_{run}_{menuName}_overall_eventsPerLumi')

    overall5kHZPlot.Divide(zeroBiasPlot) 
    pure3kHZPlot.Divide(zeroBiasPlot) 
    singleMuPlot.Divide(zeroBiasPlot) 
    singleJetPlot.Divide(zeroBiasPlot) 
    singleTauPlot.Divide(zeroBiasPlot)
    boostedJetPlot.Divide(zeroBiasPlot)

    smooth_overall5kHZPlot = smoothPlot(overall5kHZPlot, 10)
    smooth_pure3kHZPlot = smoothPlot(pure3kHZPlot, 10)
    smooth_singleMuPlot = smoothPlot(singleMuPlot, 10)
    smooth_singleJetPlot = smoothPlot(singleJetPlot, 10)
    smooth_singleTauPlot = smoothPlot(singleTauPlot, 10)
    smooth_boostedJetPlot = smoothPlot(boostedJetPlot, 10)

    smooth_overall5kHZPlot = convertEffToRate(smooth_overall5kHZPlot)
    smooth_pure3kHZPlot = convertEffToRate(smooth_pure3kHZPlot)
    smooth_singleMuPlot = convertEffToRate(smooth_singleMuPlot)
    smooth_singleJetPlot = convertEffToRate(smooth_singleJetPlot)
    smooth_singleTauPlot = convertEffToRate(smooth_singleTauPlot)
    smooth_boostedJetPlot = convertEffToRate(smooth_boostedJetPlot)

    theCanvas = ROOT.TCanvas("theCanvas","theCanvas",1400,1000)
    theCanvas.SetLogy()

    smooth_overall5kHZPlot.SetLineColor(ROOT.kRed)
    smooth_pure3kHZPlot.SetLineColor(ROOT.kBlue)
    smooth_singleMuPlot.SetLineColor(ROOT.kMagenta)
    smooth_singleJetPlot.SetLineColor(ROOT.kOrange)
    smooth_singleTauPlot.SetLineColor(ROOT.kGreen)
    smooth_boostedJetPlot.SetLineColor(ROOT.kBlack)

    smooth_overall5kHZPlot.SetLineWidth(4)
    smooth_pure3kHZPlot.SetLineWidth(4)
    smooth_singleMuPlot.SetLineWidth(4)
    smooth_singleJetPlot.SetLineWidth(4)
    smooth_singleTauPlot.SetLineWidth(4)
    smooth_boostedJetPlot.SetLineWidth(4)

    smooth_overall5kHZPlot.Draw("HIST")
    smooth_overall5kHZPlot.GetXaxis().SetTitle("Lumisections")
    smooth_overall5kHZPlot.GetYaxis().SetTitle("Rate (kHz)")
    smooth_overall5kHZPlot.GetYaxis().SetRangeUser(0.1, 100)
    smooth_overall5kHZPlot.SetTitle('')

    smooth_pure3kHZPlot.Draw("HIST SAME")
    smooth_singleMuPlot.Draw("HIST SAME")
    smooth_singleJetPlot.Draw("HIST SAME")
    smooth_singleTauPlot.Draw("HIST SAME")
    if drawBoostedJets:
        smooth_boostedJetPlot.Draw("HIST SAME")

    theLegend = ROOT.TLegend(0.1, 0.75, 0.9, 0.9)
    # theLegend.AddEntry(smooth_overall5kHZPlot, f'CICADA v{CICADAVersion} 5 kHz (overall, nominal)', 'l')
    # theLegend.AddEntry(smooth_pure3kHZPlot, f'CICADA v{CICADAVersion} 3 kHz (pure, nominal)', 'l')
    theLegend.AddEntry(smooth_overall5kHZPlot, f'CICADA 5 kHz (overall, nominal)', 'l')
    theLegend.AddEntry(smooth_pure3kHZPlot, f'CICADA 3 kHz (pure, nominal)', 'l')
    if drawBoostedJets:
        theLegend.AddEntry(smooth_boostedJetPlot, f'Boosted Jet Trigger', 'l')
    theLegend.AddEntry(smooth_singleMuPlot, f'L1 Single Mu 22', 'l')
    theLegend.AddEntry(smooth_singleJetPlot, f'L1 Single Jet 180', 'l')
    theLegend.AddEntry(smooth_singleTauPlot, f'L1 Single Tau 120')

    theLegend.SetNColumns(3)
    theLegend.SetFillStyle(0)
    theLegend.SetBorderSize(0)
    theLegend.Draw()

    cmsLatex = ROOT.TLatex()
    cmsLatex.SetTextSize(0.05)
    cmsLatex.SetNDC(True)
    cmsLatex.SetTextAlign(11)
    cmsLatex.DrawLatex(0.1,0.92, "#font[61]{CMS} #font[52]{Preliminary}")

    rightLatex = ROOT.TLatex()
    rightLatex.SetTextSize(0.05)
    rightLatex.SetNDC(True)
    rightLatex.SetTextAlign(31)
    # rightLatex.DrawLatex(0.9, 0.92, '#font[62]{Run: ' + str(run)+'}')
    rightLatex.DrawLatex(0.9, 0.92, "#font[41]{2023 (13.6 TeV)}")

    if drawBoostedJets:
        histoName = f'{destinationPath}/{run}_wBoostedJets_ratePlot.png'
    else:
        histoName = f'{destinationPath}/{run}_ratePlot.png'

    theCanvas.SaveAs(histoName)

def main(args):
    ROOT.gStyle.SetOptStat(0)
    theFile = ROOT.TFile(f'/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/perLumiPureAndOverallRatePlotsCICADAv{args.CICADAVersion}.root')
    destinationPath = f'/nfs_scratch/aloeliger/anomalyPlotFiles/pngFiles/perLumiPureAndOverallPlotsCICADAv{args.CICADAVersion}/'
    if not os.path.isdir(destinationPath):
        os.mkdir(destinationPath)
    
    listOfKeys = list(theFile.GetListOfKeys())
    listOfNames = [x.GetName() for x in listOfKeys]
    # print(listOfNames)
    listOfRuns = []
    for name in listOfNames:
        console.log(f'Processing name: {name}')
        match = re.search('(?<=_)[0-9]+(?=_)', name)
        if match:
            runNum = match.group(0)
        else:
            console.log('failed to generate a run number. Continuing')
            continue
        listOfRuns.append(runNum)

    listOfUniqueRuns = []
    for runNum in listOfRuns:
        if runNum not in listOfUniqueRuns:
            listOfUniqueRuns.append(runNum)
    # print(listOfUniqueRuns)
    console.log("Runs to consider:")
    console.print(listOfUniqueRuns)

    for run in listOfUniqueRuns:
        makeRunPlot(
            run,
            theFile,
            destinationPath,
            args.CICADAVersion,
            drawBoostedJets = args.drawBoostedJets
        )
    
    

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
        '-b',
        '--drawBoostedJets',
        action="store_true",
        help='Draw (or don\'t) the boosted jet plots'
    )

    args = parser.parse_args()

    main(args)
