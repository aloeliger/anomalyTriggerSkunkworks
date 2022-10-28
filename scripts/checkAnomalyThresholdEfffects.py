import ROOT
import os
import argparse
import re

def createHistogramForAnomalyScore(tree, histogramExpression, histogramName, histogramBinning, anomalyScore, condition=None):
    if condition == None:
        tree.Draw(histogramExpression+'>>'+histogramName+histogramBinning, 'anomalyScore > '+anomalyScore)
    else:
        tree.Draw(histogramExpression+'>>'+histogramName+histogramBinning, 'anomalyScore > '+anomalyScore+' && '+condition)
    theHisto = ROOT.gDirectory.Get(histogramName).Clone()
    
    return theHisto

def createHistogramSweep(tree, histogramExpression, histogramName, histogramBinning, condition=None):
    print('\tbase...')
    baseHisto = createHistogramForAnomalyScore(tree, histogramExpression, histogramName+'_0.0', histogramBinning, '0.0')
    print('\tAD > 3...')
    AD3Histo = createHistogramForAnomalyScore(tree, histogramExpression, histogramName+'_3.0', histogramBinning, '3.0')
    print('\tAD > 6...')
    AD6Histo = createHistogramForAnomalyScore(tree, histogramExpression, histogramName+'_6.0', histogramBinning, '6.0')
    print('\tAD > 6.5...')
    AD6p5Histo = createHistogramForAnomalyScore(tree, histogramExpression, histogramName+'_6.5', histogramBinning, '6.5')
    print('\tAD > 7...')
    AD7Histo = createHistogramForAnomalyScore(tree, histogramExpression, histogramName+'_7.0', histogramBinning, '7.0')

    return baseHisto, AD3Histo, AD6Histo, AD6p5Histo, AD7Histo

def main(args):
    ROOT.gROOT.SetBatch(True)

    theFile = ROOT.TFile(args.outputFile,'RECREATE')

    caloSummaryChain = ROOT.TChain('L1TCaloSummaryTestNtuplizer/L1TCaloSummaryOutput')
    upgradeChain = ROOT.TChain('l1UpgradeEmuTree/L1UpgradeTree')
    #upgradeChain = ROOT.TChain('l1UpgradeTree/L1UpgradeTree')

    filePath = '/hdfs/store/user/aloeliger/L1TriggerBitTest/allv5/'

    for name in os.listdir(filePath):
        caloSummaryChain.Add(filePath+name)
        upgradeChain.Add(filePath+name)

    caloSummaryChain.AddFriend(upgradeChain)

    histoList = []
    print("Performing basic calculations...")
    print()
    basicHistograms = [
        ('nEGs', 'nEGs', '(20, 0.0, 20.0)',  None),
        ('egEt', 'egEt', '(50, 0.0, 20.0)',  None),
        ('egEta', 'egEta', '(40, -2.7, 2.7)',  None),
        ('egPhi', 'egPhi', '(30, -3.14, 3.14)',  None),
        ('nTaus', 'nTaus', '(20, 0.0, 20.0)',  None),
        ('tauEt', 'tauEt', '(50, 0.0, 30.0)',  None),
        ('tauEta', 'tauEta', '(40, -2.7, 2.7)',  None),
        ('tauPhi', 'tauPhi', '(30, -3.14, 3.14)',  None),
        ('nJets', 'nJets', '(20, 0.0, 20.0)',  None),
        ('jetEt', 'jetEt', '(50, 0.0, 100.0)',  None),
        ('jetEta', 'jetEta', '(40, -2.7, 2.7)',  None),
        ('jetPhi', 'jetPhi', '(30, -3.14, 3.14)',  None),
        ('nMuons', 'nMuons', '(20, 0.0, 20.0)',  None),
        ('muonEt', 'muonEt', '(50, 0.0, 20.0)',  None),
        ('muonEta', 'muonEta', '(40, -2.7, 2.7)',  None),
        ('muonPhi', 'muonPhi', '(30, -3.14, 3.14)',  None),
        ('nSums', 'nSums', '(20, 0.0, 20.0)',  None),
        ('sumType', 'sumType','(8,0.0,8.0)',  None),
        ('sumEt', 'sumEt','(50,0.0,40.0)',  None),
        ('sumPhi', 'sumPhi','(30, -3.14, 3.14)',  None),
        ('sumEt[29]', 'MET', '(50.0, 0.0, 500.0)', 'sumType == 2'), #29 is the central BX index for this sumEt type
        ('sumEt[27]', 'HT', '(50.0, 0.0, 500.0)', 'sumType == 1'), #27 is the central BX index for this sumEt type
        ('sumEt[24]', 'ET', '(50.0, 0.0, 800.0)', 'sumType == 0'), #24 is the central BX index for this sumEt type
    ]

    for histoTuple in basicHistograms:
        print(f'{histoTuple[1]}...')
        if not re.search(args.re, histoTuple[1]):
            continue
        basicHisto, AD3Histo, AD6Histo, AD6p5Histo, AD7Histo = createHistogramSweep(caloSummaryChain, histoTuple[0], histoTuple[1], histoTuple[2])
        histoList.append(basicHisto)
        histoList.append(AD3Histo)
        histoList.append(AD6Histo)
        histoList.append(AD6p5Histo)
        histoList.append(AD7Histo)

    for histogram in histoList:
        histogram.Write(histogram.GetName(), ROOT.TObject.kSingleKey)
    theFile.Write()
    theFile.Close()

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Draw plots for ephemeral zero bias based on certain anomaly score thresholds')
    parser.add_argument('--re',
                        default='.*',
                        nargs='?',
                        help='Regular expression for the histograms to be drawn to match (based on the name)')
    parser.add_argument('--outputFile',
                        default = 'AnomalyScoreThresholdTests.root',
                        nargs='?',
                        help='Name for the file to store results in')

    args = parser.parse_args()

    main(args)
