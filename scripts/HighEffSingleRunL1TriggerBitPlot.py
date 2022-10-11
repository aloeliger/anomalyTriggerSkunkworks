#Okay. We need a script that can be run individually, or as a subprocess,
#htat makes the plots/files we want so we can get around ROOT's
#questionable memory/affiliating techniques.

import ROOT
import os
import argparse

from L1Trigger.anomalyTriggerSkunkworks.plotSettings.utilities import getListOfUniqueEntries, convertEffToRate

def main(args):
    theFile = ROOT.TFile('/nfs_scratch/aloeliger/MenuComparison_Run%i.root' % args.theRun, 'RECREATE')
    
    caloSummaryChain = ROOT.TChain('L1TCaloSummaryTestNtuplizer/L1TCaloSummaryOutput')
    l1BitChain = ROOT.TChain('L1TTriggerBitsNtuplizer/L1TTriggerBits')

    filePath = '/hdfs/store/user/aloeliger/L1TriggerBitTest/allv4/'

    #We need the files that we have stored away on hdfs
    for name in os.listdir(filePath):
        caloSummaryChain.Add(filePath+name)
        l1BitChain.Add(filePath+name)

    theCaloTree = caloSummaryChain.CopyTree('run==%i'%args.theRun)
    theL1Tree = l1BitChain.CopyTree('run==%i'%args.theRun)

    #okay. First things first is to get a unique list of lumi sections in this run
    lumis = getListOfUniqueEntries(theCaloTree, 'lumi')
    lumis.sort()
    numLumis = len(lumis)

    singleMuonHist = ROOT.TH1F('singleMuonHist','singleMuonHist', numLumis, 0.0, float(numLumis))
    singleJetHist = ROOT.TH1F('singleJetHist', 'singleJetHist', numLumis, 0.0, float(numLumis))
    doubleTauHist = ROOT.TH1F('doubleTauHist', 'doubleTauHist', numLumis, 0.0, float(numLumis))
    AD3Hist = ROOT.TH1F('AD3Hist','AD3Hist', numLumis, 0.0, float(numLumis))
    AD4Hist = ROOT.TH1F('AD4Hist','AD4Hist', numLumis, 0.0, float(numLumis))
    AD5Hist = ROOT.TH1F('AD5Hist','AD5Hist', numLumis, 0.0, float(numLumis))
    AD6Hist = ROOT.TH1F('AD6Hist','AD6Hist', numLumis, 0.0, float(numLumis))
    
    #okay. Now for each lumi we would like to get the efficiency of each of the triggers
    binToFill = 1
    for lumi in lumis:
        singleMuonEff = theL1Tree.GetEntries('lumi==%i && L1_SingleMu22 > 0' % lumi) / theL1Tree.GetEntries('lumi==%i' % lumi)
        singleJetEff = theL1Tree.GetEntries('lumi==%i && L1_SingleJet180 > 0' % lumi) / theL1Tree.GetEntries('lumi==%i' % lumi)
        doubleTauEff = theL1Tree.GetEntries('lumi==%i && L1_DoubleIsoTau36er2p1 > 0' % lumi) / theL1Tree.GetEntries('lumi==%i' % lumi)
        AD3Eff = theCaloTree.GetEntries('lumi==%i && anomalyScore > 3.0' % lumi) / theCaloTree.GetEntries('lumi == %i' % lumi)
        AD4Eff = theCaloTree.GetEntries('lumi==%i && anomalyScore > 4.0' % lumi) / theCaloTree.GetEntries('lumi == %i' % lumi)
        AD5Eff = theCaloTree.GetEntries('lumi==%i && anomalyScore > 5.0' % lumi) / theCaloTree.GetEntries('lumi == %i' % lumi)
        AD6Eff = theCaloTree.GetEntries('lumi==%i && anomalyScore > 6.0' % lumi) / theCaloTree.GetEntries('lumi == %i' % lumi)

        singleMuonRate = convertEffToRate(singleMuonEff)
        singleJetRate = convertEffToRate(singleJetEff)
        doubleTauRate = convertEffToRate(doubleTauEff)
        AD3Rate = convertEffToRate(AD3Eff)
        AD4Rate = convertEffToRate(AD4Eff)
        AD5Rate = convertEffToRate(AD5Eff)
        AD6Rate = convertEffToRate(AD6Eff)

        singleMuonHist.SetBinContent(binToFill, singleMuonRate)
        singleJetHist.SetBinContent(binToFill, singleJetRate)
        doubleTauHist.SetBinContent(binToFill, doubleTauRate)
        AD3Hist.SetBinContent(binToFill, AD3Rate)
        AD4Hist.SetBinContent(binToFill, AD4Rate)
        AD5Hist.SetBinContent(binToFill, AD5Rate)
        AD6Hist.SetBinContent(binToFill, AD6Rate)
        
        binToFill += 1
    
    #it seems like it is going to take so long to actually make these histograms, that we don't 
    #want to have to run the risk of goofing the styling and making these histograms 
    #over and over so often that it takes all week.
    #instead, let's just save the bare histograms to a file,
    #and we can make a styling/drawing plot later that 
    #can run on pre-calculated stuff

    #make a unique file we can save all of the histograms to
    theFile.cd()

    singleMuonHist.Write()
    singleJetHist.Write()
    doubleTauHist.Write()
    AD3Hist.Write()
    AD4Hist.Write()
    AD5Hist.Write()
    AD6Hist.Write()
    
    theFile.Write()
    theFile.Close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Make a single Run\'s L1 Trigger Bit Rate Plot')
    parser.add_argument('--theRun', nargs='?', required=True, type=(int), help='Run number to make the plots for')

    args = parser.parse_args()
    
    main(args)
