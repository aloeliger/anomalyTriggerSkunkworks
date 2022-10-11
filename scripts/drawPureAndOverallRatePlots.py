import ROOT
import os
import argparse
import re

from L1Trigger.anomalyTriggerSkunkworks.plotSettings.utilities import  convertEffToRate

def convertHistFromEffToRate(theHistogram):
    theNewHistogram = theHistogram.Clone()
    for theBin in range(1, theHistogram.GetNbinsX()+1):
        theNewHistogram.SetBinContent(theBin, convertEffToRate(theHistogram.GetBinContent(theBin)))
    return theNewHistogram

def convertDictFromEffToRate(theDict):
    theNewDict = {}
    for pureOrOverall in theDict:
        theNewDict[pureOrOverall] = {}
        for histType in theDict[pureOrOverall]:
            theNewDict[pureOrOverall][histType] = convertHistFromEffToRate(theDict[pureOrOverall][histType])
    return theNewDict
    
def smoothPlotsWithRunningAverage(theHistogram, runningAveragePeriod):
    theNewHistogram = theHistogram.Clone()
    runningTotal = []
    for theBin in range(1, theHistogram.GetNbinsX()+1):
        runningTotal.append(theHistogram.GetBinContent(theBin))
        if len(runningTotal) > runningAveragePeriod:
            runningTotal.pop(0)
        runningAverage = 0.
        for value in runningTotal:
            runningAverage += value
        runningAverage = runningAverage / len(runningTotal)
        theNewHistogram.SetBinContent(theBin, runningAverage)
    return theNewHistogram

def smoothDictWithRunningAverage(theDict, runningAveragePeriod):
    theNewDict = {}
    for pureOrOverall in theDict:
        theNewDict[pureOrOverall] = {}
        for histType in theDict[pureOrOverall]:
            theNewDict[pureOrOverall][histType] = smoothPlotsWithRunningAverage(theDict[pureOrOverall][histType], runningAveragePeriod)
    return theNewDict

def createRatePlotForAllBits(histograms, pureOrOverall, runNumber, settings):
    #xWisePixels = max(800, 3*singleMuonHist.GetNbinsX())
    #I don't like this
    xWisePixels = max(800, 3*histograms[pureOrOverall]['singleMuon'].GetNbinsX())
    theCanvas = ROOT.TCanvas('theCanvas','theCanvas',xWisePixels, 600)
    theCanvas.SetLogy()

    theLegend = ROOT.TLegend(0.15,0.8,0.85,0.9)
    theLegend.SetNColumns(3)

    for histType in histograms[pureOrOverall]:
        histograms[pureOrOverall][histType].SetLineColor(settings['lineColor'][histType])
        histograms[pureOrOverall][histType].SetLineWidth(2)
        theLegend.AddEntry(histograms[pureOrOverall][histType], settings['legendEntry'][histType])
        
    firstPlot = True
    for histType in histograms[pureOrOverall]:
        if firstPlot:
            theHist = histograms[pureOrOverall][histType]
            theHist.Draw('L')

            theHist.SetMaximum(28.6*10e3)
            theHist.SetMinimum(0.01)

            theHist.SetTitle('')
            theHist.GetXaxis().SetTitle('LS')

            theHist.GetYaxis().SetTitle('Rate (kHz)')

            firstPlot = False
        else:
            histograms[pureOrOverall][histType].Draw('SAME L')

    theLegend.Draw()

    cmsLatex = ROOT.TLatex()
    cmsLatex.SetTextSize(0.06)
    cmsLatex.SetNDC(True)
    cmsLatex.SetTextFont(61)
    cmsLatex.SetTextAlign(11)
    cmsLatex.DrawLatex(0.1, 0.91, "CMS")
    cmsLatex.SetTextFont(52)
    cmsLatex.DrawLatex(0.1+0.025+0.1, 0.91, "Preliminary")

    runLatex = ROOT.TLatex()
    runLatex.SetTextSize(0.06)
    runLatex.SetNDC(True)
    runLatex.SetTextFont(41)
    cmsLatex.SetTextAlign(11)
    runLatex.DrawLatex(0.65, 0.91, 'Run: '+runNumber)

    if pureOrOverall == 'pure':
        theCanvas.SaveAs('PureRate_Run'+runNumber+'.png')
    else:
        theCanvas.SaveAs('OverallRate_Run'+runNumber+'.png')

def createDiffPlotForHistType(histograms, histType, triggerName, runNumber):
    xWisePixels = max(800, 3*histograms['pure'][histType].GetNbinsX())
    theCanvas = ROOT.TCanvas('theCanvas','theCanvas',xWisePixels, 600)
    theCanvas.SetLogy()

    theCanvas.Divide(1,2)
    plotPad = ROOT.gPad.GetPrimitive('theCanvas_1')
    ratioPad = ROOT.gPad.GetPrimitive('theCanvas_2')

    plotPad.SetLogy()
    plotPad.SetBottomMargin(0.0)

    ratioPad.SetTopMargin(0.0)
    ratioPad.SetBottomMargin(0.27)
    ratioPad.SetGridy()

    plotPad.cd()

    theLegend = ROOT.TLegend(0.15,0.8,0.85,0.9)
    theLegend.SetNColumns(2)

    histograms['pure'][histType].SetLineColor(ROOT.kRed)
    histograms['overall'][histType].SetLineColor(ROOT.kBlue)
    
    histograms['pure'][histType].SetLineWidth(2)
    histograms['overall'][histType].SetLineWidth(2)

    histograms['pure'][histType].Draw('L')
    histograms['overall'][histType].Draw('SAME L')

    theMax = max(
        histograms['pure'][histType].GetMaximum(),
        histograms['overall'][histType].GetMaximum(),
    )
    theMax = theMax * 10

    histograms['pure'][histType].SetMaximum(theMax)
    theMin = min(
        histograms['pure'][histType].GetMinimum(),
        histograms['overall'][histType].GetMinimum(),
    )
    if theMin == 0.0:
        theMin += 0.01

    histograms['pure'][histType].SetMinimum(theMin)
    histograms['pure'][histType].SetTitle('')
    #histograms['pure'][histType].GetXaxis().SetTitle('LS')
    histograms['pure'][histType].GetYaxis().SetTitle('Rate (kHz)')

    theLegend.AddEntry(histograms['pure'][histType], f'Pure {triggerName} rate', 'l')
    theLegend.AddEntry(histograms['overall'][histType], f'Overall {triggerName} rate', 'l')
    theLegend.Draw()

    cmsLatex = ROOT.TLatex()
    cmsLatex.SetTextSize(0.06)
    cmsLatex.SetNDC(True)
    cmsLatex.SetTextFont(61)
    cmsLatex.SetTextAlign(11)
    cmsLatex.DrawLatex(0.1, 0.91, "CMS")
    cmsLatex.SetTextFont(52)
    cmsLatex.DrawLatex(0.1+0.025+0.1, 0.91, "Preliminary")

    runLatex = ROOT.TLatex()
    runLatex.SetTextSize(0.06)
    runLatex.SetNDC(True)
    runLatex.SetTextFont(41)
    cmsLatex.SetTextAlign(11)
    runLatex.DrawLatex(0.65, 0.91, 'Run: '+runNumber)

    ratioPad.cd()
    
    divisionHistogram = histograms['pure'][histType].Clone()
    divisionHistogram.Divide(histograms['overall'][histType].Clone())
    
    divisionHistogram.SetLineColor(ROOT.kBlack)
    divisionHistogram.SetLineWidth(2)

    divisionHistogram.Draw('L')
    divisionHistogram.SetTitle('')
    divisionHistogram.GetXaxis().SetTitle('LS')
    divisionHistogram.GetYaxis().SetTitle('Pure Rate / Overall Rate')

    divisionHistogram.SetMaximum(1.1)
    divisionHistogram.SetMinimum(-0.1)

    theCanvas.SaveAs(f'Diff_{histType}_Run{runNumber}.png')


def getHistograms(theFile, histogramNames):
    histograms = {}
    for pureOrOverall in histogramNames:
        histograms[pureOrOverall] = {}
        for histType in histogramNames[pureOrOverall]:
            histograms[pureOrOverall][histType] = getattr(theFile, histogramNames[pureOrOverall][histType])
            
    return histograms

def main(args):
    ROOT.gStyle.SetOptStat(0)

    theFile = ROOT.TFile(args.theFile, 'READ')

    runNumberRE = re.search('[0-9]+(?=\.root)',args.theFile)
    runNumber = runNumberRE.group(0)

    histogramNames = {
        'overall': {
            'singleMuon': 'singleMuonHist',
            'singleJet': 'singleJetHist',
            'doubleTau': 'doubleTauHist',
            'AD3': 'AD3Hist',
            'AD4': 'AD4Hist',
            'AD5': 'AD5Hist',
            'AD6': 'AD6Hist',
        },
        'pure': {
            'singleMuon': 'pureSingleMuonHist',
            'singleJet': 'pureSingleJetHist',
            'doubleTau': 'pureDoubleTauHist',
            'AD3': 'pureAD3Hist',
            'AD4': 'pureAD4Hist',
            'AD5': 'pureAD5Hist',
            'AD6': 'pureAD6Hist',

        },
    }


    settings = {
        'lineColor':{
            'singleMuon': ROOT.kOrange-1,
            'singleJet': ROOT.kRed,
            'doubleTau': ROOT.kViolet,
            'AD3': ROOT.kBlue,
            'AD4': ROOT.kBlue-10,
            'AD5': ROOT.kBlue+3,
            'AD6': ROOT.kCyan+3,
        },
        'legendEntry':{
            'singleMuon': 'L1_SingleMu22',
            'singleJet': 'L1_SingleJet180',
            'doubleTau': 'L1_DoubleIsoTau34er2p1',
            'AD3': 'Calo Anomaly Score > 3',
            'AD4': 'Calo Anomaly Score > 4',
            'AD5': 'Calo Anomaly Score > 5',
            'AD6': 'Calo Anomaly Score > 6',
        },
    }

    
    histograms = getHistograms(theFile, histogramNames)
    histograms = convertDictFromEffToRate(histograms)
    if args.smoothPlots:
        histograms = smoothDictWithRunningAverage(histograms, args.runningAveragePeriod)

    createRatePlotForAllBits(histograms, 'pure', runNumber, settings)
    createRatePlotForAllBits(histograms, 'overall', runNumber, settings)

    for histType in histograms['pure']:
        createDiffPlotForHistType(histograms, histType, settings['legendEntry'][histType], runNumber)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Draw plots made with the combined High Eff L1 script')
    parser.add_argument('--theFile', required=True, nargs='?', help='File to extract from')
    parser.add_argument('--smoothPlots', action='store_true', help='smooth plots with a running average')
    parser.add_argument('--runningAveragePeriod', type=int, nargs='?', help='number of lumi sections to use as a running average',default=10)

    args = parser.parse_args()

    main(args)
