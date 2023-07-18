# !/usr/bin/env python3
import ROOT
import os
import argparse
from drawScorePlots import convertEffToRate
import re
from drawPerLumiRatePlot import smoothPlot

def makeRunPlot(run, theFile, destinationPath, CICADAVersion):
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
        print('failed to match menu name')
        return
    CICADAName = f'CICADA_{run}_{menuName}'

    zeroBiasPlot = getattr(theFile, f'{CICADAName}_overall_ZeroBias_eventsPerLumi')

    # overall0p5kHZPlot = getattr(theFile, f'{CICADAName}_overall_0p5kHz_eventsPerLumi')
    # overall1kHZPlot = getattr(theFile, f'{CICADAName}_overall_1kHz_eventsPerLumi')
    # overall2kHZPlot = getattr(theFile, f'{CICADAName}_overall_2kHz_eventsPerLumi')
    # overall3kHZPlot = getattr(theFile, f'{CICADAName}_overall_3kHz_eventsPerLumi')
    overall5kHZPlot = getattr(theFile, f'{CICADAName}_overall_5kHz_eventsPerLumi')
    # overall10kHZPlot = getattr(theFile, f'{CICADAName}_overall_10kHz_eventsPerLumi')
    # pure0p5kHZPlot = getattr(theFile, f'{CICADAName}_pure_0p5kHz_eventsPerLumi')
    # pure1kHZPlot = getattr(theFile, f'{CICADAName}_pure_1kHz_eventsPerLumi')
    # pure2kHZPlot = getattr(theFile, f'{CICADAName}_pure_2kHz_eventsPerLumi')
    pure3kHZPlot = getattr(theFile, f'{CICADAName}_pure_3kHz_eventsPerLumi')
    # pure5kHZPlot = getattr(theFile, f'{CICADAName}_pure_5kHz_eventsPerLumi')
    # pure10kHZPlot = getattr(theFile, f'{CICADAName}_pure_10kHz_eventsPerLumi')
    singleMuPlot = getattr(theFile, f'L1_SingleMu22_{run}_{menuName}_overall_eventsPerLumi')
    singleJetPlot = getattr(theFile, f'L1_SingleJet180_{run}_{menuName}_overall_eventsPerLumi')
    singleTauPlot = getattr(theFile, f'L1_SingleTau120er2p1_{run}_{menuName}_overall_eventsPerLumi')

    # overall0p5kHZPlot.Divide(zeroBiasPlot) 
    # overall1kHZPlot.Divide(zeroBiasPlot) 
    # overall2kHZPlot.Divide(zeroBiasPlot) 
    # overall3kHZPlot.Divide(zeroBiasPlot) 
    overall5kHZPlot.Divide(zeroBiasPlot) 
    # overall10kHZPlot.Divide(zeroBiasPlot) 
    # pure0p5kHZPlot.Divide(zeroBiasPlot) 
    # pure1kHZPlot.Divide(zeroBiasPlot) 
    # pure2kHZPlot.Divide(zeroBiasPlot) 
    pure3kHZPlot.Divide(zeroBiasPlot) 
    # pure5kHZPlot.Divide(zeroBiasPlot) 
    # pure10kHZPlot.Divide(zeroBiasPlot) 
    singleMuPlot.Divide(zeroBiasPlot) 
    singleJetPlot.Divide(zeroBiasPlot) 
    singleTauPlot.Divide(zeroBiasPlot) 

    # smooth_overall0p5kHZPlot = smoothPlot(overall0p5kHZPlot, 10)
    # smooth_overall1kHZPlot = smoothPlot(overall1kHZPlot, 10)
    # smooth_overall2kHZPlot = smoothPlot(overall2kHZPlot, 10)
    # smooth_overall3kHZPlot = smoothPlot(overall3kHZPlot, 10)
    smooth_overall5kHZPlot = smoothPlot(overall5kHZPlot, 10)
    # smooth_overall10kHZPlot = smoothPlot(overall10kHZPlot, 10)
    # smooth_pure0p5kHZPlot = smoothPlot(pure0p5kHZPlot, 10)
    # smooth_pure1kHZPlot = smoothPlot(pure1kHZPlot, 10)
    # smooth_pure2kHZPlot = smoothPlot(pure2kHZPlot, 10)
    smooth_pure3kHZPlot = smoothPlot(pure3kHZPlot, 10)
    # smooth_pure5kHZPlot = smoothPlot(pure5kHZPlot, 10)
    # smooth_pure10kHZPlot = smoothPlot(pure10kHZPlot, 10)
    smooth_singleMuPlot = smoothPlot(singleMuPlot, 10)
    smooth_singleJetPlot = smoothPlot(singleJetPlot, 10)
    smooth_singleTauPlot = smoothPlot(singleTauPlot, 10)

    # smooth_overall0p5kHZPlot = convertEffToRate(smooth_overall0p5kHZPlot)
    # smooth_overall1kHZPlot = convertEffToRate(smooth_overall1kHZPlot)
    # smooth_overall2kHZPlot = convertEffToRate(smooth_overall2kHZPlot)
    # smooth_overall3kHZPlot = convertEffToRate(smooth_overall3kHZPlot)
    smooth_overall5kHZPlot = convertEffToRate(smooth_overall5kHZPlot)
    # smooth_overall10kHZPlot = convertEffToRate(smooth_overall10kHZPlot)
    # smooth_pure0p5kHZPlot = convertEffToRate(smooth_pure0p5kHZPlot)
    # smooth_pure1kHZPlot = convertEffToRate(smooth_pure1kHZPlot)
    # smooth_pure2kHZPlot = convertEffToRate(smooth_pure2kHZPlot)
    smooth_pure3kHZPlot = convertEffToRate(smooth_pure3kHZPlot)
    # smooth_pure5kHZPlot = convertEffToRate(smooth_pure5kHZPlot)
    # smooth_pure10kHZPlot = convertEffToRate(smooth_pure10kHZPlot)
    smooth_singleMuPlot = convertEffToRate(smooth_singleMuPlot)
    smooth_singleJetPlot = convertEffToRate(smooth_singleJetPlot)
    smooth_singleTauPlot = convertEffToRate(smooth_singleTauPlot)

    theCanvas = ROOT.TCanvas("theCanvas")
    theCanvas.SetLogy()

    # smooth_overall0p5kHZPlot.SetLineColor(ROOT.kRed)
    # smooth_overall1kHZPlot.SetLineColor(ROOT.kRed-3)
    # smooth_overall2kHZPlot.SetLineColor(ROOT.kRed+3)
    # smooth_overall3kHZPlot.SetLineColor(ROOT.kRed-2)
    # smooth_overall5kHZPlot.SetLineColor(ROOT.kRed-6)
    smooth_overall5kHZPlot.SetLineColor(ROOT.kRed)
    # smooth_overall10kHZPlot.SetLineColor(ROOT.kRed-9)
    # smooth_pure0p5kHZPlot.SetLineColor(ROOT.kBlue)
    # smooth_pure1kHZPlot.SetLineColor(ROOT.kBlue-3)
    # smooth_pure2kHZPlot.SetLineColor(ROOT.kBlue+3)
    # smooth_pure3kHZPlot.SetLineColor(ROOT.kBlue-2)
    smooth_pure3kHZPlot.SetLineColor(ROOT.kBlue)
    # smooth_pure5kHZPlot.SetLineColor(ROOT.kBlue-6)
    # smooth_pure10kHZPlot.SetLineColor(ROOT.kBlue-9)
    smooth_singleMuPlot.SetLineColor(ROOT.kMagenta)
    smooth_singleJetPlot.SetLineColor(ROOT.kOrange)
    smooth_singleTauPlot.SetLineColor(ROOT.kGreen)

    # smooth_overall0p5kHZPlot.SetLineWidth(2)
    # smooth_overall1kHZPlot.SetLineWidth(2)
    # smooth_overall2kHZPlot.SetLineWidth(2)
    # smooth_overall3kHZPlot.SetLineWidth(2)
    smooth_overall5kHZPlot.SetLineWidth(2)
    # smooth_overall10kHZPlot.SetLineWidth(2)
    # smooth_pure0p5kHZPlot.SetLineWidth(2)
    # smooth_pure1kHZPlot.SetLineWidth(2)
    # smooth_pure2kHZPlot.SetLineWidth(2)
    smooth_pure3kHZPlot.SetLineWidth(2)
    # smooth_pure5kHZPlot.SetLineWidth(2)
    # smooth_pure10kHZPlot.SetLineWidth(2)
    smooth_singleMuPlot.SetLineWidth(2)
    smooth_singleJetPlot.SetLineWidth(2)
    smooth_singleTauPlot.SetLineWidth(2)

    smooth_overall5kHZPlot.Draw("HIST")
    smooth_overall5kHZPlot.GetXaxis().SetTitle("Lumi")
    smooth_overall5kHZPlot.GetYaxis().SetTitle("Rate (kHz)")
    smooth_overall5kHZPlot.GetYaxis().SetRangeUser(0.1, 100)
    smooth_overall5kHZPlot.SetTitle('')

    # smooth_overall0p5kHZPlot.Draw("HIST SAME")
    # smooth_overall1kHZPlot.Draw("HIST SAME")
    # smooth_overall2kHZPlot.Draw("HIST SAME")
    # smooth_overall3kHZPlot.Draw("HIST SAME")
    # smooth_overall10kHZPlot.Draw("HIST SAME")
    # smooth_pure0p5kHZPlot.Draw("HIST SAME")
    # smooth_pure1kHZPlot.Draw("HIST SAME")
    # smooth_pure2kHZPlot.Draw("HIST SAME")
    smooth_pure3kHZPlot.Draw("HIST SAME")
    # smooth_pure5kHZPlot.Draw("HIST SAME")
    # smooth_pure10kHZPlot.Draw("HIST SAME")
    smooth_singleMuPlot.Draw("HIST SAME")
    smooth_singleJetPlot.Draw("HIST SAME")
    smooth_singleTauPlot.Draw("HIST SAME")

    theLegend = ROOT.TLegend(0.1, 0.7, 0.9, 0.9)
    # theLegend.AddEntry(smooth_overall0p5kHZPlot, f'CICADA v{CICADAVersion} 0.5 kHz (overall, nominal)', 'l')
    # theLegend.AddEntry(smooth_overall1kHZPlot, f'CICADA v{CICADAVersion} 1 kHz (overall, nominal)', 'l')
    # theLegend.AddEntry(smooth_overall2kHZPlot, f'CICADA v{CICADAVersion} 2 kHz (overall, nominal)', 'l')
    # theLegend.AddEntry(smooth_overall3kHZPlot, f'CICADA v{CICADAVersion} 3 kHz (overall, nominal)', 'l')
    theLegend.AddEntry(smooth_overall5kHZPlot, f'CICADA v{CICADAVersion} 5 kHz (overall, nominal)', 'l')
    # theLegend.AddEntry(smooth_overall10kHZPlot, f'CICADA v{CICADAVersion} 10 kHz (overall, nominal)', 'l')
    # theLegend.AddEntry(smooth_pure0p5kHZPlot, f'CICADA v{CICADAVersion} 0.5 kHz (pure, nominal)', 'l')
    # theLegend.AddEntry(smooth_pure1kHZPlot, f'CICADA v{CICADAVersion} 1 kHz (pure, nominal)', 'l')
    # theLegend.AddEntry(smooth_pure2kHZPlot, f'CICADA v{CICADAVersion} 2 kHz (pure, nominal)', 'l')
    theLegend.AddEntry(smooth_pure3kHZPlot, f'CICADA v{CICADAVersion} 3 kHz (pure, nominal)', 'l')
    # theLegend.AddEntry(smooth_pure5kHZPlot, f'CICADA v{CICADAVersion} 5 kHz (pure, nominal)', 'l')
    # theLegend.AddEntry(smooth_pure10kHZPlot, f'CICADA v{CICADAVersion} 10 kHz (pure, nominal)', 'l')
    theLegend.AddEntry(smooth_singleMuPlot, f'L1 Single Mu 22', 'l')
    theLegend.AddEntry(smooth_singleJetPlot, f'L1 Single Jet 180', 'l')
    theLegend.AddEntry(smooth_singleTauPlot, f'L1 Single Tau 120')

    theLegend.SetNColumns(3)
    theLegend.Draw()

    cmsLatex = ROOT.TLatex()
    cmsLatex.SetTextSize(0.05)
    cmsLatex.SetNDC(True)
    cmsLatex.SetTextAlign(11)
    cmsLatex.DrawLatex(0.1,0.92, "#font[61]{CMS} #font[52]{Preliminary}")

    runLatex = ROOT.TLatex()
    runLatex.SetTextSize(0.05)
    runLatex.SetNDC(True)
    runLatex.SetTextAlign(31)
    runLatex.DrawLatex(0.9, 0.92, '#font[62]{Run: ' + str(run)+'}')

    theCanvas.SaveAs(f'{destinationPath}/{run}_ratePlot.png')

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
        match = re.search('(?<=_)[0-9]+(?=_)', name)
        if match:
            runNum = match.group(0)
        else:
            print('failed to generate a run number. Continuing')
            continue
        listOfRuns.append(runNum)

    listOfUniqueRuns = []
    for runNum in listOfRuns:
        if runNum not in listOfUniqueRuns:
            listOfUniqueRuns.append(runNum)
    # print(listOfUniqueRuns)

    for run in listOfUniqueRuns:
        makeRunPlot(
            run,
            theFile,
            destinationPath,
            args.CICADAVersion
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

    args = parser.parse_args()

    main(args)