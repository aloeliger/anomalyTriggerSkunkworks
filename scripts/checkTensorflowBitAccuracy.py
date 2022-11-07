#Script for checking whether or not the bit accurate implementation of the HLS code
#And Tensorflow's own seemingly bit accurate representations line up

import ROOT
import argparse
from tqdm import trange
import struct

def findDifferentBits(bitStringOne, bitStringTwo):
    stringLen = len(bitStringOne)
    if not stringLen == len(bitStringTwo):#Should be an assert, but I am too lazy to look up the syntax
        raise RuntimeError('Tried to find different bits in strings of two different lengths')
    
    differentBits = []
    for i in range(stringLen):
        if bitStringOne[stringLen-1-i] != bitStringTwo[stringLen-1-i]:
            differentBits.append(i)
    return differentBits
    

def convertNumToAPFixedBitString(num, numberIntegerBits, numberFloatBits):
    integerBits = list(range(numberIntegerBits))
    floatBits = list(range(-1*numberFloatBits, 0))
    
    allPowers = integerBits+floatBits
    allPowers.sort(reverse=True)

    tempNum = num
    bitString = ''
    for power in allPowers:
        if tempNum >= 2.0**power:
            bitString+='1'
            tempNum -= 2.0**power
        else:
            bitString+='0'
    if tempNum > 0:
        print('Found number that was not completely expressable with the number of bits provided! ', num)
    return bitString

def main(args):
    ROOT.gStyle.SetOptStat(0)
    theFile = ROOT.TFile(args.inputFile)

    theTree = theFile.L1TCaloSummaryTestNtuplizer.L1TCaloSummaryOutput

    #numEvents = theTree.GetEntries()
    numEvents = 200
    anomalyScoreHisto = ROOT.TH1F("anomalyScore", "anomalyScore", numEvents, 0.0, numEvents)
    bitAccurateAnomalyScoreHisto = ROOT.TH1F("bitAccurateAnomalyScore", "bitAccurateAnomalyScore", numEvents, 0.0, numEvents)
    numberOfBitsWrongHisto = ROOT.TH1I('numerOfBitsWrong', 'numberOfBitsWrong', 12, 0, 12)
    mostSignificantBitWrongHisto = ROOT.TH1I('mostSignificantBitWrong', 'mostSignificantBitWrong', 11, 0, 11)
    for i in trange(numEvents):
        theTree.GetEntry(i)
        anomalyScoreHisto.Fill(i, theTree.anomalyScore)
        bitAccurateAnomalyScoreHisto.Fill(i, theTree.bitAccurateAnomalyScore)
        #Let's cheeck the bit accuracy of these two things.
        #if theTree.anomalyScore != theTree.bitAccurateAnomalyScore:
        anomalyScoreBits = convertNumToAPFixedBitString(theTree.anomalyScore, numberIntegerBits=5, numberFloatBits=6)
        bitAccurateAnomalyScoreBits = convertNumToAPFixedBitString(theTree.bitAccurateAnomalyScore, numberIntegerBits=5, numberFloatBits=6)
        #print('********************')
        #print('Anomaly score: ',theTree.anomalyScore,': ', anomalyScoreBits)
        #print('Bit accurate anomaly score: ',theTree.bitAccurateAnomalyScore, ': ', bitAccurateAnomalyScoreBits)
        differentBits = findDifferentBits(anomalyScoreBits, bitAccurateAnomalyScoreBits)
        #print('Different bits: ', differentBits)
        
        if differentBits != []:
            numberOfBitsWrongHisto.Fill(len(differentBits))
            mostSignificantBitWrongHisto.Fill(max(differentBits))
        else:
            numberOfBitsWrongHisto.Fill(0)
            mostSignificantBitWrongHisto.Fill(-1)
        
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

    theCanvas = ROOT.TCanvas('theCanvas', 'theCanvas')

    numberOfBitsWrongHisto.SetMarkerStyle(20)
    numberOfBitsWrongHisto.SetMarkerColor(ROOT.kBlack)

    numberOfBitsWrongHisto.Draw('e1')

    numberOfBitsWrongHisto.GetXaxis().SetTitle('Number of Bits Wrong')
    numberOfBitsWrongHisto.GetYaxis().SetTitle('Counts')
    numberOfBitsWrongHisto.SetTitle('')

    theCanvas.SaveAs('numberOfBitsWrong.png')

    mostSignificantBitWrongHisto.SetMarkerStyle(20)
    mostSignificantBitWrongHisto.SetMarkerColor(ROOT.kBlack)
    
    mostSignificantBitWrongHisto.Draw('e1')

    mostSignificantBitWrongHisto.GetXaxis().SetTitle('Most Significant Bit Wrong (Lower = less significant, starting at 0)')
    mostSignificantBitWrongHisto.GetYaxis().SetTitle('Counts')
    mostSignificantBitWrongHisto.SetTitle('')

    mostSignificantBitWrongHisto.Draw('e1')

    theCanvas.SaveAs('mostSignificantBitWrong.png')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check a file that has the HLS file and TensorFlow anomalyScores to check if they yield the same thing always')
    
    parser.add_argument('--inputFile',
                        required=True,
                        nargs='?',
                        help='Input file for the script')

    args = parser.parse_args()
    
    main(args)
