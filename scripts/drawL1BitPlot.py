#okay. Now we need to draw the L1 bit plot files we made with the script

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

def main(args):
    ROOT.gStyle.SetOptStat(0)

    #Okay. Let's go and get the file, and our histograms
    theFile = ROOT.TFile(args.theFile, "READ")

    #get the run number
    runNumberRE = re.search('[0-9]+(?=\.root)',args.theFile)
    runNumber = runNumberRE.group(0)

    if args.pure:
        singleMuonHist = theFile.pureSingleMuonHist
        singleJetHist = theFile.pureSingleJetHist
        doubleTauHist = theFile.pureDoubleTauHist
        AD3Hist = theFile.pureAD3Hist
        AD4Hist = theFile.pureAD4Hist
        AD5Hist = theFile.pureAD5Hist
        AD6Hist = theFile.pureAD6Hist
    else:
        singleMuonHist = theFile.singleMuonHist
        singleJetHist = theFile.singleJetHist
        doubleTauHist = theFile.doubleTauHist
        AD3Hist = theFile.AD3Hist
        AD4Hist = theFile.AD4Hist
        AD5Hist = theFile.AD5Hist
        AD6Hist = theFile.AD6Hist

    if args.convertFromEff:
        singleMuonHist = convertHistFromEffToRate(singleMuonHist)
        singleJetHist = convertHistFromEffToRate(singleJetHist)
        doubleTauHist = convertHistFromEffToRate(doubleTauHist)
        AD3Hist = convertHistFromEffToRate(AD3Hist)
        AD4Hist = convertHistFromEffToRate(AD4Hist)
        AD5Hist = convertHistFromEffToRate(AD5Hist)
        AD6Hist = convertHistFromEffToRate(AD6Hist)

    #Okay. Let's try and make a convenient histogram for all the contents of this
    xWisePixels = max(800, 3*singleMuonHist.GetNbinsX())
    theCanvas = ROOT.TCanvas('theCanvas','theCanvas',xWisePixels, 600)
    theCanvas.SetLogy()

    singleMuonHist.SetLineColor(ROOT.kOrange-1)
    singleJetHist.SetLineColor(ROOT.kRed)
    doubleTauHist.SetLineColor(ROOT.kViolet)
    AD3Hist.SetLineColor(ROOT.kBlue)
    AD4Hist.SetLineColor(ROOT.kBlue-10)
    AD5Hist.SetLineColor(ROOT.kBlue+3)
    AD6Hist.SetLineColor(ROOT.kCyan+3)

    singleMuonHist.SetLineWidth(2)
    singleJetHist.SetLineWidth(2)
    doubleTauHist.SetLineWidth(2)
    AD3Hist.SetLineWidth
    AD4Hist.SetLineWidth(2)
    AD5Hist.SetLineWidth(2)
    AD6Hist.SetLineWidth(2)

    singleMuonHist.Draw("L")
    singleJetHist.Draw("SAME L")
    doubleTauHist.Draw("SAME L")
    AD3Hist.Draw("SAME L")
    AD4Hist.Draw("SAME L")
    AD5Hist.Draw("SAME L")
    AD6Hist.Draw("SAME L")
    
    singleMuonHist.SetMaximum(28.6*10e3)
    singleMuonHist.SetMinimum(0.01)

    singleMuonHist.SetTitle('')
    singleMuonHist.GetXaxis().SetTitle('LS')
    singleMuonHist.GetYaxis().SetTitle('Rate (kHz) (Running average over 5 LS)')

    theLegend = ROOT.TLegend(0.15,0.8,0.85,0.9)
    theLegend.AddEntry(singleMuonHist, 'L1_SingleMuon22', 'L')
    theLegend.AddEntry(singleJetHist, 'L1_SingleJet180', 'L')
    theLegend.AddEntry(doubleTauHist, 'L1_DoubleIsoTau36er2p1', 'L')
    theLegend.AddEntry(AD3Hist, 'Calo Anomaly Score > 3', 'L')
    theLegend.AddEntry(AD4Hist, 'Calo Anomaly Score > 4', 'L')
    theLegend.AddEntry(AD5Hist, 'Calo Anomaly Score > 5', 'L')
    theLegend.AddEntry(AD6Hist, 'Calo Anomaly Score > 6', 'L')
    theLegend.SetNColumns(3)
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

    if args.pure:
        theCanvas.SaveAs("PureRate_Run"+runNumber+".png")
    else:
        theCanvas.SaveAs("OverallRate_Run"+runNumber+".png")

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Draw plots made with the High Eff L1 script')
    parser.add_argument('--theFile',required=True,nargs='?',help='File to extract')
    parser.add_argument('--pure',action='store_true')
    parser.add_argument('--convertFromEff', action='store_true')
    
    args = parser.parse_args()
    
    main(args)
