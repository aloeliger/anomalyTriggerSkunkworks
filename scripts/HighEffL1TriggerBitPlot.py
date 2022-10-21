#Plot CaloL1 Ad scores against Other L1 Trigger Bits
#But do so in a quick and memory efficient way.

import ROOT
import os
from tqdm import tqdm
#oh man. Let's start getting *fancy*
from multiprocessing import Queue, Pool, Lock
import time

import subprocess

#Okay. We're going to do this in a few steps

#The first step, is to create the quickest list of all the runs we have available
#Then we split the tree into these runs with copytree

#for each of these trees we hand it off to a function that will make our plot for us

#this plot function will use GetEntries() with an appropriate cut instead of looping the hard way
#And hopefully this will make our life much easier

#given a chain, get the unique entries of the given branch
#branch name given as a string
def getListOfUniqueEntries(theChain, branchName):
    theList = []
    
    #disable all branches except the ones we *really* need
    theChain.SetBranchStatus("*", 0)
    #reenable runs
    theChain.SetBranchStatus(branchName,1)
    #print('getting unique entries for: %s...' % branchName)
    for i in range(theChain.GetEntries()):
        theChain.GetEntry(i)
        if getattr(theChain, branchName) not in theList:
            theList.append(getattr(theChain, branchName))  

    #reenable everything
    theChain.SetBranchStatus("*", 1)
    return theList

def convertEffToRate(eff):
    return eff * (2544.0 * 11425e-3)


#Independent self-contained (mostly function)
#for getting all the files, making a chain,
#getting the proper 
def makePlotFile(theRun):    
    #let's let the function do the cutting, so we can farm that out to different processes
    theFile = ROOT.TFile('MenuComparison_Run%i.root' % theRun, 'RECREATE')

    caloSummaryChain = ROOT.TChain('L1TCaloSummaryTestNtuplizer/L1TCaloSummaryOutput')
    l1BitChain = ROOT.TChain('L1TTriggerBitsNtuplizer/L1TTriggerBits')

    filePath = '/hdfs/store/user/aloeliger/L1TriggerBitTest/allv4/'

    #We need the files that we have stored away on hdfs
    for name in os.listdir(filePath):
        caloSummaryChain.Add(filePath+name)
        l1BitChain.Add(filePath+name)

    theCaloTree = caloSummaryChain.CopyTree('run==%i'%theRun)
    theL1Tree = l1BitChain.CopyTree('run==%i'%theRun)

    #okay. First things first is to get a unique list of lumi sections in this run
    lumis = getListOfUniqueEntries(theCaloTree, 'lumi')
    lumis.sort()
    numLumis = len(lumis)

    singleMuonHist = ROOT.TH1F('singleMuonHist','singleMuonHist', numLumis, 0.0, float(numLumis))
    singleJetHist = ROOT.TH1F('singleJetHist', 'singleJetHist', numLumis, 0.0, float(numLumis))
    HTHist = ROOT.TH1F('HTHist', 'HTHist', numLumis, 0.0, float(numLumis))
    AD3Hist = ROOT.TH1F('AD3Hist','AD3Hist', numLumis, 0.0, float(numLumis))
    AD4Hist = ROOT.TH1F('AD4Hist','AD4Hist', numLumis, 0.0, float(numLumis))
    AD5Hist = ROOT.TH1F('AD5Hist','AD5Hist', numLumis, 0.0, float(numLumis))
    AD6Hist = ROOT.TH1F('AD6Hist','AD6Hist', numLumis, 0.0, float(numLumis))
    
    #okay. Now for each lumi we would like to get the efficiency of each of the triggers
    binToFill = 1
    for lumi in lumis:
        singleMuonEff = theL1Tree.GetEntries('lumi==%i && L1_SingleMu22 > 0' % lumi) / theL1Tree.GetEntries('lumi==%i' % lumi)
        singleJetEff = theL1Tree.GetEntries('lumi==%i && L1_SingleJet180 > 0' % lumi) / theL1Tree.GetEntries('lumi==%i' % lumi)
        HTEff = theL1Tree.GetEntries('lumi==%i && L1_HTT450er > 0' % lumi) / theL1Tree.GetEntries('lumi==%i' % lumi)
        AD3Eff = theCaloTree.GetEntries('lumi==%i && anomalyScore > 3.0' % lumi) / theCaloTree.GetEntries('lumi == %i' % lumi)
        AD4Eff = theCaloTree.GetEntries('lumi==%i && anomalyScore > 4.0' % lumi) / theCaloTree.GetEntries('lumi == %i' % lumi)
        AD5Eff = theCaloTree.GetEntries('lumi==%i && anomalyScore > 5.0' % lumi) / theCaloTree.GetEntries('lumi == %i' % lumi)
        AD6Eff = theCaloTree.GetEntries('lumi==%i && anomalyScore > 6.0' % lumi) / theCaloTree.GetEntries('lumi == %i' % lumi)

        singleMuonRate = convertEffToRate(singleMuonEff)
        singleJetRate = convertEffToRate(singleJetEff)
        HTRate = convertEffToRate(HTEff)
        AD3Rate = convertEffToRate(AD3Eff)
        AD4Rate = convertEffToRate(AD4Eff)
        AD5Rate = convertEffToRate(AD5Eff)
        AD6Rate = convertEffToRate(AD6Eff)

        singleMuonHist.SetBinContent(binToFill, singleMuonRate)
        singleJetHist.SetBinContent(binToFill, singleJetRate)
        HTHist.SetBinContent(binToFill, HTRate)
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
    HTHist.Write()
    AD3Hist.Write()
    AD4Hist.Write()
    AD5Hist.Write()
    AD6Hist.Write()
    
    theFile.Write()
    theFile.Close()

def main():
    ROOT.gStyle.SetOptStat(0)

    caloSummaryChain = ROOT.TChain('L1TCaloSummaryTestNtuplizer/L1TCaloSummaryOutput')
    l1BitChain = ROOT.TChain('L1TTriggerBitsNtuplizer/L1TTriggerBits')

    filePath = '/hdfs/store/user/aloeliger/L1TriggerBitTest/allv4/'

    #We need the files that we have stored away on hdfs
    for name in os.listdir(filePath):
        caloSummaryChain.Add(filePath+name)
        l1BitChain.Add(filePath+name)

    #get the list of runs to make plots for
    print("getting unique runs...")
    runList = getListOfUniqueEntries(caloSummaryChain, 'run')
    print("done!")
    
    #loop over the runs.
    #for each run, make a set of trees that 
    #is the input to our plot making function.
    #then make the plots
    #print("making unique histograms per run...")
    #okay, instead of doing it this way:
    """
    for run in runList:
        #theCaloTree = caloSummaryChain.CopyTree('run==%i' % run)
        #theL1Tree = l1BitChain.CopyTree('run==%i' % run)

        makePlotGivenTree(caloSummaryChain, l1BitChain, run)
    """
    #let's instead try work pooling this out
    """
    print("farming out plot creation per run...")
    runList = tuple(runList)
    workPool = Pool(20)
    startTime = time.perf_counter()
    workPool.map(makePlotFile, runList)
    endTime = time.perf_counter()
    print("done!")
    print(f'elapsed multiprocessing time: {endTime-startTime} seconds')
    """

    """
    workCalls = ['python3 $CMSSW_BASE/src/L1Trigger/anomalyTriggerSkunkworks/scripts/HighEffSingleRunL1TriggerBitPlot.py --theRun %i' % run for run in runList]

    for call in workCalls:
        subprocess.Popen(call, shell=True)
    """
    
    #At long last, I can't force this to multithread other than by hand.
    #I just need a list of the runs
    print(runList)

if __name__ == '__main__':
    main()
