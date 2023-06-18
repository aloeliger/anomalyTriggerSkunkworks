import ROOT
import argparse

def createEfficiencyPlot(thePlot, name):
    nBins = thePlot.GetNbinsX()
    nBinsNew = nBins+1
    
    oldXaxis = thePlot.GetXaxis()

    lowBound = oldXaxis.GetXmin()
    highBound = oldXaxis.GetXmax()

    efficiencyPlot = ROOT.TH1D(name, name, nBinsNew, lowBound, highBound)

    for i in range(nBinsNew):
        lowBound = nBins - i
        eff = thePlot.Integral(i, nBins)

        efficiencyPlot.SetBinContent(i+1, eff)

    return efficiencyPlot

def main(args):
    ROOT.gStyle.SetOptStat(0)

    ZBChain = ROOT.TChain('L1TCaloSummaryTestNtuplizer/L1TCaloSummaryOutput')
    ZB_uGTChain = ROOT.TChain('uGTModelNtuplizer/uGTModelOutput')

    SUEPChain = ROOT.TChain('L1TCaloSummaryTestNtuplizer/L1TCaloSummaryOutput')
    SUEP_uGTChain = ROOT.TChain('uGTModelNtuplizer/uGTModelOutput')

    ZBChain.Add(args.zeroBias)
    ZB_uGTChain.Add(args.zeroBias)
    ZBChain.AddFriend(ZB_uGTChain)

    SUEPChain.Add(args.SUEP)
    SUEP_uGTChain.Add(args.SUEP)
    SUEPChain.AddFriend(SUEP_uGTChain)

    theCanvas = ROOT.TCanvas('Score Canvas')
    theCanvas.SetLogy()

    ZBChain.Draw('anomalyScore>>ZBScore(100,-1.0,10.0)')
    ZBPlot = ROOT.gDirectory.Get('ZBScore').Clone()

    ZBChain.Draw('uGTAnomalyScore>>uZBScore(200,-1.0,1000.0)')
    uZBPlot = ROOT.gDirectory.Get('uZBScore').Clone()

    ZBPlot.SetLineColor(ROOT.kBlue)
    uZBPlot.SetLineColor(ROOT.kBlue)

    ZBPlot.Scale(1.0/ZBPlot.Integral())
    uZBPlot.Scale(1.0/uZBPlot.Integral())

    SUEPChain.Draw('anomalyScore>>SUEPScore(100,-1.0,10.0)')
    SUEPPlot = ROOT.gDirectory.Get('SUEPScore').Clone()

    SUEPChain.Draw('uGTAnomalyScore>>uSUEPScore(200,-1.0,1000.0)')
    uSUEPPlot = ROOT.gDirectory.Get('uSUEPScore').Clone()

    SUEPPlot.SetLineColor(ROOT.kRed)
    uSUEPPlot.SetLineColor(ROOT.kRed)

    SUEPPlot.Scale(1.0/SUEPPlot.Integral())
    uSUEPPlot.Scale(1.0/uSUEPPlot.Integral())

    for plotPair in [(ZBPlot,SUEPPlot, 'CICADA'),(uZBPlot,uSUEPPlot,'uGT')]:
        plotPair[0].Draw()
        plotPair[1].Draw('SAME')

        plotPair[0].SetTitle('')
        if plotPair[2] == 'CICADA':
            plotPair[0].GetXaxis().SetTitle('CICADA Score')
        else:
            plotPair[0].GetXaxis().SetTitle('uGT AD Score')
        plotPair[0].GetYaxis().SetTitle('Response (normalized to 1)')

        cmsLatex = ROOT.TLatex()
        cmsLatex.SetTextSize(0.06)
        cmsLatex.SetNDC(True)
        cmsLatex.SetTextAlign(11)
        cmsLatex.DrawLatex(0.1,0.92, "#font[61]{CMS} #font[52]{Preliminary}")   

        algoLatex = ROOT.TLatex()
        algoLatex.SetTextSize(0.06)
        algoLatex.SetNDC(True)
        algoLatex.SetTextAlign(31)
        algoLatex.DrawLatex(0.9,0.92, f'{plotPair[2]}')

        theLegend = ROOT.TLegend(0.7,0.7,0.9,0.9)
        theLegend.AddEntry(plotPair[0], "ZB Response", 'l')
        theLegend.AddEntry(plotPair[1], "SUEP Response", 'l')
        theLegend.Draw()
        theCanvas.SaveAs(f'{plotPair[2]}_SUEPComparison.png')

    plotDict = {
        'CICADA': {
            'ZB': ZBPlot,
            'SUEP': SUEPPlot,
        },
        'uGT': {
            'ZB': uZBPlot,
            'SUEP': uSUEPPlot,
        }
    }

    effDict = {}
    for key in plotDict:
        effDict[key] = {}

    for algo in ('CICADA', 'uGT'):
        for plotType in ('ZB', 'SUEP'):
            effDict[algo][plotType] = createEfficiencyPlot(plotDict[algo][plotType], f'{algo}{plotType}Eff')
    
    for plotPair in [(effDict['CICADA']['ZB'],effDict['CICADA']['SUEP'], 'CICADA'), (effDict['uGT']['ZB'], effDict['uGT']['SUEP'], 'uGT')]:
        plotPair[0].SetLineColor(ROOT.kBlue)
        plotPair[1].SetLineColor(ROOT.kRed)
        
        plotPair[0].Draw()
        plotPair[1].Draw('SAME')

        plotPair[0].SetTitle('')
        if plotPair[2] == 'CICADA':
            plotPair[0].GetXaxis().SetTitle('CICADA Score Threshold')
        else:
            plotPair[0].GetXaxis().SetTitle('uGT AD Score Threshold')
        plotPair[0].GetYaxis().SetTitle('Efficiency (normalized to 1)')

        cmsLatex = ROOT.TLatex()
        cmsLatex.SetTextSize(0.06)
        cmsLatex.SetNDC(True)
        cmsLatex.SetTextAlign(11)
        cmsLatex.DrawLatex(0.1,0.92, "#font[61]{CMS} #font[52]{Preliminary}")   

        algoLatex = ROOT.TLatex()
        algoLatex.SetTextSize(0.06)
        algoLatex.SetNDC(True)
        algoLatex.SetTextAlign(31)
        algoLatex.DrawLatex(0.9,0.92, f'{plotPair[2]}')

        theLegend = ROOT.TLegend(0.7,0.7,0.9,0.9)
        theLegend.AddEntry(plotPair[0], "ZB", 'l')
        theLegend.AddEntry(plotPair[1], "SUEP", 'l')
        theLegend.Draw()
        theCanvas.SaveAs(f'{plotPair[2]}_SUEPEffComparison.png')

    CICADARoc = ROOT.TGraph()
    uGTRoc = ROOT.TGraph()

    for i in range(effDict['CICADA']['ZB'].GetNbinsX()):
        CICADARoc.AddPoint(effDict['CICADA']['ZB'].GetBinContent(i+1), effDict['CICADA']['SUEP'].GetBinContent(i+1))
    for i in range(effDict['uGT']['ZB'].GetNbinsX()):
        #print('(',effDict['uGT']['ZB'].GetBinContent(i+1),effDict['uGT']['SUEP'].GetBinContent(i+1),')')
        uGTRoc.AddPoint(effDict['uGT']['ZB'].GetBinContent(i+1), effDict['uGT']['SUEP'].GetBinContent(i+1))
    
    CICADARoc.SetLineColor(ROOT.kBlue)
    uGTRoc.SetLineColor(ROOT.kRed)

    rocCanvas = ROOT.TCanvas('rocCanvas')
    #rocCanvas.SetLogy()
    rocCanvas.SetLogx()

    rocCanvas.Clear()

    CICADARoc.Draw('AL')
    uGTRoc.Draw('L')

    CICADARoc.GetHistogram().GetXaxis().SetTitle('ZB Eff')
    CICADARoc.GetHistogram().GetXaxis().CenterTitle()
    CICADARoc.GetHistogram().GetYaxis().SetTitle('SUEP Eff')
    CICADARoc.GetHistogram().GetYaxis().CenterTitle()

    cmsLatex = ROOT.TLatex()
    cmsLatex.SetTextSize(0.06)
    cmsLatex.SetNDC(True)
    cmsLatex.SetTextAlign(11)
    cmsLatex.DrawLatex(0.1,0.92, "#font[61]{CMS} #font[52]{Preliminary}")

    theLegend = ROOT.TLegend(0.7,0.1,0.9,0.3)
    theLegend.AddEntry(CICADARoc, "CICADA", 'l')
    theLegend.AddEntry(uGTRoc, "uGT", 'l')
    theLegend.Draw()

    rightLatex = ROOT.TLatex()
    rightLatex.SetTextSize(0.06)
    rightLatex.SetNDC(True)
    rightLatex.SetTextAlign(31)
    rightLatex.DrawLatex(0.9, 0.92, "#font[52]{Run C Vs. SUEP MC}")
        
    rocCanvas.SaveAs('SUEPComparisonROC.png')

        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Check SUEP versus Zero Bias for uGT versus CICADA")

    parser.add_argument(
        '--zeroBias',
        required=True,
        nargs='?',
        help='File with ZeroBias events in it'
    )
    parser.add_argument(
        '--SUEP',
        required=True,
        nargs='?',
        help='File with SUEP events in it'
    )

    args = parser.parse_args()

    main(args)