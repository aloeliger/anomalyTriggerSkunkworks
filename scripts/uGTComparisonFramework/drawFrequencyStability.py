import argparse
import ROOT
import statistics

def createPlotTable(theDict):
    for column in range(5):
        for row in range(7):
            theBox = ROOT.TPaveText(
                0.1+column*((0.7-0.1)/5.0),
                0.9-row*((0.9-0.7)/7.0),
                0.1+(column+1)*((0.7-0.1)/5.0),
                0.9-(row+1)*((0.9-0.7)/7.0),
                'NDC'
            )
            theBox.SetLineWidth(1)
            theBox.SetLineColor(ROOT.kBlack)
            theBox.Draw()

def getThresholdForRate(ratePlot, rate):
    nBins = ratePlot.GetNbinsX()
    theBin = 0
    actualRate = 0.0
    for i in range(1,nBins+1):
        if ratePlot.GetBinContent(i) <= rate:
            theBin = i
            actualRate = ratePlot.GetBinContent(i)
            break
    threshold = ratePlot.GetXaxis().GetBinLowEdge(theBin)
    #print(f'Threshold for rate {rate}kHz: {threshold:.3f}')
    #print(f'Actual rate for rate {rate}kHz: {actualRate:.3f}')

    return threshold

def convertEffToRate(eff):
    return eff * (2544.0 * 11425e-3)

def createRatePlot(scorePlot):
    integralPlot = scorePlot.Clone()
    integralPlot.Scale(1.0/integralPlot.Integral())
    
    nBins = scorePlot.GetNbinsX()
    
    ratePlot = ROOT.TH1F(
        scorePlot.GetName()+'Rate',
        scorePlot.GetTitle()+'Rate',
        nBins,
        scorePlot.GetXaxis().GetXmin(),
        scorePlot.GetXaxis().GetXmax(),
    )

    for i in range(1,nBins+1):
        ratePlot.SetBinContent(i, convertEffToRate(integralPlot.Integral(i, nBins)))

    return ratePlot

def main(args):
    theFile = ROOT.TFile(args.theFile)
    ROOT.gStyle.SetOptStat(0)

    caloScorePlots = {}
    uGTScorePlots = {}
    runs = ('RunA', 'RunB', 'RunC', 'RunD')

    for run in runs:
        caloScorePlots[run] = getattr(theFile, f'{run}CaloScores')
        uGTScorePlots[run] = getattr(theFile, f'{run}uGTScores')
    
    caloRatePlots = {}
    uGTRatePlots = {}

    for run in runs:
        caloRatePlots[run] = createRatePlot(caloScorePlots[run])
        uGTRatePlots[run] = createRatePlot(uGTScorePlots[run])
    
    caloSettings = {
        'RunA': (ROOT.kRed, 2, 20),
        'RunB': (ROOT.kBlue,2, 20),
        'RunC': (ROOT.kGreen,2,20),
        'RunD': (ROOT.kOrange,2,20),
    }

    caloMaxes = [
        caloRatePlots['RunA'].GetMaximum(),
        caloRatePlots['RunB'].GetMaximum(),
        caloRatePlots['RunC'].GetMaximum(),
        caloRatePlots['RunD'].GetMaximum(),
    ]
    caloMax = max(caloMaxes) * 10E2

    uGTSettings = {
        'RunA': (ROOT.kRed,2,22),
        'RunB': (ROOT.kBlue,2,22),
        'RunC': (ROOT.kGreen,2,22),
        'RunD': (ROOT.kOrange,2,22),
    }

    uGTMaxes = [
        uGTRatePlots['RunA'].GetMaximum(),
        uGTRatePlots['RunB'].GetMaximum(),
        uGTRatePlots['RunC'].GetMaximum(),
        uGTRatePlots['RunD'].GetMaximum(),
    ]
    uGTMax = max(uGTMaxes) * 10E2

    for run in runs:
        caloRatePlots[run].SetLineColor(caloSettings[run][0])
        caloRatePlots[run].SetMarkerColor(caloSettings[run][0])
        caloRatePlots[run].SetLineWidth(caloSettings[run][1])
        caloRatePlots[run].SetMarkerStyle(caloSettings[run][2])

        uGTRatePlots[run].SetLineColor(uGTSettings[run][0])
        uGTRatePlots[run].SetMarkerColor(uGTSettings[run][0])
        uGTRatePlots[run].SetLineWidth(uGTSettings[run][1])
        uGTRatePlots[run].SetMarkerStyle(uGTSettings[run][2])

    caloRatePlots['RunA'].SetMaximum(caloMax)
    caloRatePlots['RunA'].SetTitle('')
    caloRatePlots['RunA'].GetXaxis().SetTitle('CICADA Score Threshold')
    caloRatePlots['RunA'].GetYaxis().SetTitle('Rate (kHz)')

    uGTRatePlots['RunA'].SetMaximum(uGTMax)
    uGTRatePlots['RunA'].SetTitle('')
    uGTRatePlots['RunA'].GetXaxis().SetTitle('uGT Score Threshold')
    uGTRatePlots['RunA'].GetYaxis().SetTitle('Rate (kHz)')

    caloCanvas = ROOT.TCanvas('caloCanvas', 'caloCanvas')
    uGTCanvas = ROOT.TCanvas('uGTCanvas', 'uGTCanvas')

    cmsLatex = ROOT.TLatex()
    cmsLatex.SetTextSize(0.06)
    cmsLatex.SetNDC(True)
    cmsLatex.SetTextAlign(11)
    #cmsLatex.DrawLatex(0.1,0.92, "#font[61]{CMS} #font[52]{Preliminary}")

    algoLatex = ROOT.TLatex()
    algoLatex.SetTextSize(0.06)
    algoLatex.SetNDC(True)
    algoLatex.SetTextAlign(31)
    #algoLatex.DrawLatex(0.9,0.92, f'{plotPair[2]}')

    #freqBox = ROOT.TPave(0.1,0.7,0.7,0.9, 1, 'NDC')
    #freqBox.SetFillStyle(0)
    #freqBox.SetLineColor(ROOT.kBlack)
    #freqBox.SetLineWidth(1)

    #caloRunAThreeKhzThreshold = getThresholdForRate(caloRatePlots['RunA'], 3.0)
    thresholds = {}
    for plotType in ('calo', 'ugt'):
        thresholds[plotType] = {}
        for run in runs:
            thresholds[plotType][run] = {}
            for rate in (3.0, 2.0, 1.0, 0.5):
                if plotType == 'calo':
                    theDict = caloRatePlots
                elif plotType == 'ugt':
                    theDict = uGTRatePlots
                thresholds[plotType][run][rate] = getThresholdForRate(theDict[run], rate)

    #We're going to make a table of the form:

    # Run/Threshold | 3 kHZ | 2 kHz | 1 kHz | 0.5 kHz
    # Run A
    # Run B
    # Run C
    # Run D
    # Mean
    # Std Dev
    
    # 5 columns split 0.1 to 0.7
    #7 rows split between 0.7 to 0.9

    ############################################
    # Draw Calo Stuff
    ############################################
    caloCanvas.cd()
    caloCanvas.SetLogy()

    caloRatePlots['RunA'].Draw('P0')
    caloRatePlots['RunB'].Draw('SAME P0')
    caloRatePlots['RunC'].Draw('SAME P0')
    caloRatePlots['RunD'].Draw('SAME P0')

    caloLegend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
    caloLegend.AddEntry(caloRatePlots['RunA'], 'Run A', 'lp')
    caloLegend.AddEntry(caloRatePlots['RunB'], 'Run B', 'lp')
    caloLegend.AddEntry(caloRatePlots['RunC'], 'Run C', 'lp')
    caloLegend.AddEntry(caloRatePlots['RunD'], 'Run D', 'lp')
    caloLegend.Draw()

    caloThreeKHZLine = ROOT.TLine(
        caloRatePlots['RunA'].GetXaxis().GetXmin(),
        3.0,
        caloRatePlots['RunA'].GetXaxis().GetXmax(),
        3.0
    )
    caloThreeKHZLine.SetLineColor(ROOT.kBlack)
    caloThreeKHZLine.SetLineWidth(2)
    caloThreeKHZLine.SetLineStyle(5)
    caloThreeKHZLine.Draw()

    caloTwoKHZLine = ROOT.TLine(
        caloRatePlots['RunA'].GetXaxis().GetXmin(),
        2.0,
        caloRatePlots['RunA'].GetXaxis().GetXmax(),
        2.0
    )
    caloTwoKHZLine.SetLineColor(ROOT.kBlack)
    caloTwoKHZLine.SetLineWidth(2)
    caloTwoKHZLine.SetLineStyle(7)
    caloTwoKHZLine.Draw()

    caloOneKHZLine = ROOT.TLine(
        caloRatePlots['RunA'].GetXaxis().GetXmin(),
        1.0,
        caloRatePlots['RunA'].GetXaxis().GetXmax(),
        1.0
    )
    caloOneKHZLine.SetLineColor(ROOT.kBlack)
    caloOneKHZLine.SetLineWidth(2)
    caloOneKHZLine.SetLineStyle(9)
    caloOneKHZLine.Draw()

    caloHalfKHZLine = ROOT.TLine(
        caloRatePlots['RunA'].GetXaxis().GetXmin(),
        0.5,
        caloRatePlots['RunA'].GetXaxis().GetXmax(),
        0.5
    )
    caloHalfKHZLine.SetLineColor(ROOT.kBlack)
    caloHalfKHZLine.SetLineWidth(2)
    caloHalfKHZLine.SetLineStyle(10)
    caloHalfKHZLine.Draw()

    #createPlotTable(thresholds['calo'])
    caloTable = []
    for column in range(5):
        for row in range(7):
            theBox = ROOT.TPaveText(
                0.1+column*((0.7-0.1)/5.0),
                0.9-row*((0.9-0.7)/7.0),
                0.1+(column+1)*((0.7-0.1)/5.0),
                0.9-(row+1)*((0.9-0.7)/7.0),
                'NDC'
            )
            theBox.SetLineWidth(1)
            theBox.SetLineColor(ROOT.kBlack)
            theBox.SetBorderSize(1)
            theBox.SetFillColor(0)
            theBox.Draw()

            if row == 0:
                if column == 0:
                    theBox.AddText("Run/Threshold")
                elif column == 1:
                    theBox.AddText('3 kHz')
                elif column == 2:
                    theBox.AddText('2 kHz')
                elif column == 3:
                    theBox.AddText('1 kHz')
                elif column == 4:
                    theBox.AddText('0.5 kHz')
            elif column == 0:
                if row < 5:
                    theBox.AddText(runs[row-1])
                elif row == 5:
                    theBox.AddText('Mean')
                elif row == 6:
                    theBox.AddText('Std Dev')
            else:
                if row < 5:
                    if column == 1:
                        threshold = thresholds['calo'][runs[row-1]][3.0] 
                    elif column == 2:
                        threshold = thresholds['calo'][runs[row-1]][2.0]
                    elif column == 3:
                        threshold = thresholds['calo'][runs[row-1]][1.0]
                    elif column == 4:
                        threshold = thresholds['calo'][runs[row-1]][0.5]
                    theBox.AddText(f'{threshold:.2f}')  
                else:  
                    if column == 1:
                        rate = 3.0
                    elif column == 2:
                        rate = 2.0
                    elif column == 3:
                        rate = 1.0
                    elif column == 4:
                        rate = 0.5   

                    thresholdList =[
                                thresholds['calo']['RunA'][rate],
                                thresholds['calo']['RunB'][rate],
                                thresholds['calo']['RunC'][rate],
                                thresholds['calo']['RunD'][rate],
                            ]

                    if row == 5:
                        mean = statistics.mean(thresholdList)
                        theBox.AddText(f'{mean:.2f}')
                    if row == 6:
                        stddev = statistics.stdev(thresholdList)
                        theBox.AddText(f'{stddev:.2f}')

            caloTable.append(theBox)

    cmsLatex.DrawLatex(0.1,0.92, "#font[61]{CMS} #font[52]{Preliminary}")
    algoLatex.DrawLatex(0.9,0.92, 'CICADA')

    caloCanvas.SaveAs('CICADARates.png')

    ############################################
    # Draw UGT Stuff
    ############################################
    uGTCanvas.cd()
    uGTCanvas.SetLogy()

    uGTRatePlots['RunA'].Draw('P0')
    uGTRatePlots['RunB'].Draw('SAME P0')
    uGTRatePlots['RunC'].Draw('SAME P0')
    uGTRatePlots['RunD'].Draw('SAME P0')

    uGTLegend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
    uGTLegend.AddEntry(uGTRatePlots['RunA'], 'Run A', 'lp')
    uGTLegend.AddEntry(uGTRatePlots['RunB'], 'Run B', 'lp')
    uGTLegend.AddEntry(uGTRatePlots['RunC'], 'Run C', 'lp')
    uGTLegend.AddEntry(uGTRatePlots['RunD'], 'Run D', 'lp')
    uGTLegend.Draw()

    uGTThreeKHZLine = ROOT.TLine(
        uGTRatePlots['RunA'].GetXaxis().GetXmin(),
        3.0,
        uGTRatePlots['RunA'].GetXaxis().GetXmax(),
        3.0
    )
    uGTThreeKHZLine.SetLineColor(ROOT.kBlack)
    uGTThreeKHZLine.SetLineWidth(2)
    uGTThreeKHZLine.SetLineStyle(5)
    uGTThreeKHZLine.Draw()

    uGTTwoKHZLine = ROOT.TLine(
        uGTRatePlots['RunA'].GetXaxis().GetXmin(),
        2.0,
        uGTRatePlots['RunA'].GetXaxis().GetXmax(),
        2.0
    )
    uGTTwoKHZLine.SetLineColor(ROOT.kBlack)
    uGTTwoKHZLine.SetLineWidth(2)
    uGTTwoKHZLine.SetLineStyle(7)
    uGTTwoKHZLine.Draw()

    uGTOneKHZLine = ROOT.TLine(
        uGTRatePlots['RunA'].GetXaxis().GetXmin(),
        1.0,
        uGTRatePlots['RunA'].GetXaxis().GetXmax(),
        1.0
    )
    uGTOneKHZLine.SetLineColor(ROOT.kBlack)
    uGTOneKHZLine.SetLineWidth(2)
    uGTOneKHZLine.SetLineStyle(9)
    uGTOneKHZLine.Draw()

    uGTHalfKHZLine = ROOT.TLine(
        uGTRatePlots['RunA'].GetXaxis().GetXmin(),
        0.5,
        uGTRatePlots['RunA'].GetXaxis().GetXmax(),
        0.6
    )
    uGTHalfKHZLine.SetLineColor(ROOT.kBlack)
    uGTHalfKHZLine.SetLineWidth(2)
    uGTHalfKHZLine.SetLineStyle(10)
    uGTHalfKHZLine.Draw()

    uGTTable = []
    for column in range(5):
        for row in range(7):
            theBox = ROOT.TPaveText(
                0.1+column*((0.7-0.1)/5.0),
                0.9-row*((0.9-0.7)/7.0),
                0.1+(column+1)*((0.7-0.1)/5.0),
                0.9-(row+1)*((0.9-0.7)/7.0),
                'NDC'
            )
            theBox.SetLineWidth(1)
            theBox.SetLineColor(ROOT.kBlack)
            theBox.SetBorderSize(1)
            theBox.SetFillColor(0)
            theBox.Draw()

            if row == 0:
                if column == 0:
                    theBox.AddText("Run/Threshold")
                elif column == 1:
                    theBox.AddText('3 kHz')
                elif column == 2:
                    theBox.AddText('2 kHz')
                elif column == 3:
                    theBox.AddText('1 kHz')
                elif column == 4:
                    theBox.AddText('0.5 kHz')
            elif column == 0:
                if row < 5:
                    theBox.AddText(runs[row-1])
                elif row == 5:
                    theBox.AddText('Mean')
                elif row == 6:
                    theBox.AddText('Std Dev')
            else:
                if row < 5:
                    if column == 1:
                        threshold = thresholds['ugt'][runs[row-1]][3.0] 
                    elif column == 2:
                        threshold = thresholds['ugt'][runs[row-1]][2.0]
                    elif column == 3:
                        threshold = thresholds['ugt'][runs[row-1]][1.0]
                    elif column == 4:
                        threshold = thresholds['ugt'][runs[row-1]][0.5]
                    theBox.AddText(f'{threshold:.2f}')  
                else:  
                    if column == 1:
                        rate = 3.0
                    elif column == 2:
                        rate = 2.0
                    elif column == 3:
                        rate = 1.0
                    elif column == 4:
                        rate = 0.5   

                    thresholdList =[
                                thresholds['ugt']['RunA'][rate],
                                thresholds['ugt']['RunB'][rate],
                                thresholds['ugt']['RunC'][rate],
                                thresholds['ugt']['RunD'][rate],
                            ]

                    if row == 5:
                        mean = statistics.mean(thresholdList)
                        theBox.AddText(f'{mean:.2f}')
                    if row == 6:
                        stddev = statistics.stdev(thresholdList)
                        theBox.AddText(f'{stddev:.2f}')

            uGTTable.append(theBox)

    cmsLatex.DrawLatex(0.1,0.92, "#font[61]{CMS} #font[52]{Preliminary}")
    algoLatex.DrawLatex(0.9,0.92, 'uGT AD')

    uGTCanvas.SaveAs('uGTRates.png')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create and draw frequency plots from the stability score plots file')

    parser.add_argument('--theFile',nargs='?',default='stabilityFile.root',help='File to create plots from')

    args = parser.parse_args()

    main(args)