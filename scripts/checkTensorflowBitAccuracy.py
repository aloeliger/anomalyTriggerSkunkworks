#Script for checking whether or not the bit accurate implementation of the HLS code
#And Tensorflow's own seemingly bit accurate representations line up

import ROOT
import argparse
from tqdm import trange

def main(args):
    ROOT.gStyle.SetOptStat(0)
    theFile = ROOT.TFile(args.inputFile)

    theTree = theFile.L1TCaloSummaryTestNtuplizer.L1TCaloSummaryOutput

    #numEvents = theTree.GetEntries()
    numEvents = 200
    anomalyScoreHisto = ROOT.TH1F("anomalyScore", "anomalyScore", numEvents, 0.0, numEvents)
    bitAccurateAnomalyScoreHisto = ROOT.TH1F("bitAccurateAnomalyScore", "bitAccurateAnomalyScore", numEvents, 0.0, numEvents)

    for i in trange(numEvents):
        theTree.GetEntry(i)
        anomalyScoreHisto.Fill(i, theTree.anomalyScore)
        bitAccurateAnomalyScoreHisto.Fill(i, theTree.bitAccurateAnomalyScore)

    #theTree.Draw('anomalyScore>>anomalyScore')
    #anomalyScoreHisto = ROOT.gDirectory.Get('anomalyScore').Clone()
    #theTree.Draw('bitAccurateAnomalyScore>>bitAccurateAnomalyScore')
    #bitAccurateAnomalyScoreHisto = ROOT.gDirectory.Get('bitAccurateAnomalyScore').Clone()

    anomalyScoreHisto.SetLineColor(ROOT.kRed)
    bitAccurateAnomalyScoreHisto.SetLineColor(ROOT.kBlack)

    theCanvas = ROOT.TCanvas('theCanvas', 'theCanvas')
    
    theCanvas.Divide(1,2)
    
    plotPad = ROOT.gPad.GetPrimitive('theCanvas_1')
    subtractionPad = ROOT.gPad.GetPrimitive('theCanvas_2')

    plotPad.SetPad("pad1","plot", 0.0, 0.4, 1.0, 1.0, 0)
    subtractionPad.SetPad("pad2", "subtraction", 0.0, 0.0, 1.0, 0.4, 0)

    plotPad.SetLogy()
    plotPad.SetBottomMargin(0.0)
    
    subtractionPad.SetTopMargin(0.0)
    subtractionPad.SetBottomMargin(0.27)
    subtractionPad.SetGridy()

    plotPad.cd()
    anomalyScoreHisto.Draw("HIST")
    bitAccurateAnomalyScoreHisto.Draw("HIST SAME")
    anomalyScoreHisto.SetTitle("")
    anomalyScoreHisto.GetYaxis().SetTitle("Anomaly Score")
    
    theLegend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
    theLegend.AddEntry(bitAccurateAnomalyScoreHisto, "Bit Accurate/HLS implementation", 'l')
    theLegend.AddEntry(anomalyScoreHisto, "Tensorflow implementation", 'l')
    theLegend.Draw()

    subtractionPad.cd()
    bitAccurateSubtractionHisto = bitAccurateAnomalyScoreHisto.Clone()
    anomalyScoreSubtractionHisto = anomalyScoreHisto.Clone()

    bitAccurateSubtractionHisto.Add(bitAccurateAnomalyScoreHisto, -1.0)
    anomalyScoreSubtractionHisto.Add(bitAccurateAnomalyScoreHisto, -1.0)

    bitAccurateSubtractionHisto.Draw("HIST")
    anomalyScoreSubtractionHisto.Draw("SAME HIST")
    bitAccurateSubtractionHisto.SetTitle("")
    bitAccurateSubtractionHisto.GetYaxis().SetTitle("Difference w.r.t Bit Accurate Implementation")
    bitAccurateSubtractionHisto.GetXaxis().SetTitle("Event")

    bitAccurateSubtractionHisto.SetMaximum(.1)
    bitAccurateSubtractionHisto.SetMinimum(-0.1)

    theCanvas.SaveAs("tensorFlowAccuracy.png")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check a file that has the HLS file and TensorFlow anomalyScores to check if they yield the same thing always')
    
    parser.add_argument('--inputFile',
                        required=True,
                        nargs='?',
                        help='Input file for the script')

    args = parser.parse_args()
    
    main(args)
