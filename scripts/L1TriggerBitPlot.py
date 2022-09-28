#Plot CaloL1 AD scores against other L1 Trigger bits

import ROOT
import os
from tqdm import tqdm
import math

def main():
    ROOT.gStyle.SetOptStat(0)
    #okay, let's chain together all the files we have stored, and figure out how we want to do this.
    caloSummaryChain = ROOT.TChain('L1TCaloSummaryTestNtuplizer/L1TCaloSummaryOutput')
    l1BitChain = ROOT.TChain('L1TTriggerBitsNtuplizer/L1TTriggerBits')

    filePath = '/hdfs/store/user/aloeliger/L1TriggerBitTest/allv3/'

    #We need the files that we have stored away on hdfs
    for name in os.listdir(filePath):
        caloSummaryChain.Add(filePath+name)
        l1BitChain.Add(filePath+name)
    
    runLumiDict = {}
    triggers = ['AD3', 'AD4', 'AD5', 'AD6', 'singleMuon', 'singleJet', 'HT']
    #I think that we have to this event by event unfortunately, which is going to be a bit obnoxious
    for indexNum in tqdm(range(caloSummaryChain.GetEntries())):
        #for each event, we go ahead and get it, and figure out if it passes AD thresholds, and L1 Bits for 
        #each whatever it is
        caloSummaryChain.GetEntry(indexNum)
        l1BitChain.GetEntry(indexNum)
        
        theRun = caloSummaryChain.run
        theLumi = caloSummaryChain.lumi
        
        if theRun not in runLumiDict.keys():
            runLumiDict[theRun] = {}
        if theLumi not in runLumiDict[theRun].keys():
            runLumiDict[theRun][theLumi] = {}
            for trigger in triggers:
                runLumiDict[theRun][theLumi][trigger] = {}
                runLumiDict[theRun][theLumi][trigger]['pass'] = 0.0
                runLumiDict[theRun][theLumi][trigger]['total'] = 0.0
        #add to the total of all of our triggers
        for trigger in triggers:
            runLumiDict[theRun][theLumi][trigger]['total'] += 1.0

        #let's check if we have passed our various anomaly triggers
        #If it does, we add it to a running efficiency total for the run and lumi section
        theScore = caloSummaryChain.anomalyScore
        if theScore >= 3.0:
            runLumiDict[theRun][theLumi]['AD3']['pass'] += 1.0
        if theScore >= 4.0:
            runLumiDict[theRun][theLumi]['AD4']['pass'] += 1.0
        if theScore >= 5.0:
            runLumiDict[theRun][theLumi]['AD5']['pass'] += 1.0
        if theScore >= 6.0:
            runLumiDict[theRun][theLumi]['AD6']['pass'] += 1.0

        #let's also check the L1 trigger bit results
        if l1BitChain.L1_SingleMu22:
            runLumiDict[theRun][theLumi]['singleMuon']['pass'] += 1.0
        if l1BitChain.L1_SingleJet180:
            runLumiDict[theRun][theLumi]['singleJet']['pass'] += 1.0
        if l1BitChain.L1_HTT450er:
            runLumiDict[theRun][theLumi]['HT']['pass'] += 1.0

    #Provided that all fit into memory, we're now ready to try and do some actual plotting
    
    theCanvas = ROOT.TCanvas('theCanvas','theCanvas', 5000, 600)
    theCanvas.SetLogy()
    #Okay. As it stands, we are looking at too many lumis at once. We need a way to do the rate over 
    #we need a way to do a running average
    averageOverLumis = 5
    totalLumiBins = 0
    #totalLumis = 0
    for run in runLumiDict:
        #totalLumis += len(runLumiDict.keys())
        totalLumiBins += len(runLumiDict.keys())
    totalLumiBins = totalLumiBins - (averageOverLumis -1) #we can't do a running average for the first n-1 bins
    #print("total lumi bins: ", totalLumiBins)
    singleMuonHist = ROOT.TH1F('singleMuonHist','singleMuonHist', totalLumiBins, 0.0, float(totalLumiBins)+1.0)
    singleJetHist = ROOT.TH1F('singleJetHist', 'singleJetHist', totalLumiBins, 0.0, float(totalLumiBins)+1.0)
    HTHist = ROOT.TH1F('HTHist', 'HTHist', totalLumiBins, 0.0, float(totalLumiBins)+1.0)
    AD3Hist = ROOT.TH1F('AD3Hist','AD3Hist', totalLumiBins, 0.0, float(totalLumiBins)+1.0)
    AD4Hist = ROOT.TH1F('AD4Hist','AD4Hist', totalLumiBins, 0.0, float(totalLumiBins)+1.0)
    AD5Hist = ROOT.TH1F('AD5Hist','AD5Hist', totalLumiBins, 0.0, float(totalLumiBins)+1.0)
    AD6Hist = ROOT.TH1F('AD6Hist','AD6Hist', totalLumiBins, 0.0, float(totalLumiBins)+1.0)

    def convertEffToRate(eff): #returns the rate in kHz
        return eff * (2544.0 * 11425e-3) 
                    
    #okay. Doing a single histogram is simply not going to work
    #we need to do a running average histogram for each run.

    runsInOrder = list(runLumiDict.keys())
    runsInOrder.sort()
    for run in runsInOrder:
        binToFill = 1.0

        triggerRunningPass = {}
        triggerRunningTotal = {}
        for trigger in triggers:
            triggerRunningPass[trigger] = []
            triggerRunningTotal[trigger] = []


        lumisInOrder = list(runLumiDict[run].keys())
        lumisInOrder.sort()
        numLumis = len(lumisInOrder)

        singleMuonHist = ROOT.TH1F('singleMuonHist', 'singleMuonHist', numLumis, 0.0, float(numLumis))
        singleJetHist = ROOT.TH1F('singleJetHist', 'singleJetHist', numLumis, 0.0, float(numLumis))
        HTHist = ROOT.TH1F('HTHist', 'HTHist', numLumis, 0.0, float(numLumis))
        AD3Hist = ROOT.TH1F('AD3Hist','AD3Hist', numLumis, 0.0, float(numLumis))
        AD4Hist = ROOT.TH1F('AD4Hist','AD4Hist', numLumis, 0.0, float(numLumis))
        AD5Hist = ROOT.TH1F('AD5Hist','AD5Hist', numLumis, 0.0, float(numLumis))
        AD6Hist = ROOT.TH1F('AD6Hist','AD6Hist', numLumis, 0.0, float(numLumis))
        
        #now let's go through the lumis and fill each of these up
        for lumi in lumisInOrder:
            triggerEff = {}
            for trigger in triggers:
                triggerRunningPass[trigger].append(runLumiDict[run][lumi][trigger]['pass'])
                triggerRunningTotal[trigger].append(runLumiDict[run][lumi][trigger]['total'])
                if len(triggerRunningPass[trigger]) > averageOverLumis:
                    triggerRunningPass[trigger].pop(0)
                    triggerRunningTotal[trigger].pop(0)
                totalPass = 0.0
                totalTotal = 0.0
                for i in range(len(triggerRunningPass[trigger])):
                    totalPass += triggerRunningPass[trigger][i]
                    totalTotal += triggerRunningTotal[trigger][i]
                triggerEff[trigger] = totalPass/totalTotal
            singleMuonRate = convertEffToRate(triggerEff['singleMuon'])
            singleJetRate = convertEffToRate(triggerEff['singleJet'])
            HTRate = convertEffToRate(triggerEff['HT'])
            AD3Rate = convertEffToRate(triggerEff['AD3'])
            AD4Rate = convertEffToRate(triggerEff['AD4'])
            AD5Rate = convertEffToRate(triggerEff['AD5'])
            AD6Rate = convertEffToRate(triggerEff['AD6'])

            singleMuonHist.SetBinContent(int(binToFill), singleMuonRate)
            singleJetHist.SetBinContent(int(binToFill), singleJetRate)
            HTHist.SetBinContent(int(binToFill), HTRate)
            AD3Hist.SetBinContent(int(binToFill), AD3Rate)
            AD4Hist.SetBinContent(int(binToFill), AD4Rate)
            AD5Hist.SetBinContent(int(binToFill), AD5Rate)
            AD6Hist.SetBinContent(int(binToFill), AD6Rate)
            
            binToFill += 1.0
        #okay. The histograms should be mostly filled and correct at this point
        #let's style them up, and get them ready for writing, 
        singleMuonHist.SetLineColor(ROOT.kOrange)
        singleJetHist.SetLineColor(ROOT.kGreen)
        HTHist.SetLineColor(ROOT.kMagenta)
        AD3Hist.SetLineColor(ROOT.kAzure)
        AD4Hist.SetLineColor(ROOT.kAzure-3)
        AD5Hist.SetLineColor(ROOT.kAzure-6)
        AD6Hist.SetLineColor(ROOT.kAzure-9)

        singleMuonHist.Draw('L')
        singleJetHist.Draw('L SAME')
        HTHist.Draw('L SAME')
        AD3Hist.Draw('L SAME')
        AD4Hist.Draw('L SAME')
        AD5Hist.Draw('L SAME')
        AD6Hist.Draw('L SAME')
        
        singleMuonHist.SetMaximum(28.6e3+10.0e3)
        singleMuonHist.SetMinimum(0.01)
        singleMuonHist.GetXaxis().SetLabelSize(0.0)
        singleMuonHist.GetYaxis().SetTitle("Rate (kHz)")
        
        runText = ROOT.TText(len(lumisInOrder)/2, 28.6e3, 'Run %i' % run)
        runText.SetTextAlign(22)
        runText.SetTextSize(0.05)
        #runText.SetTextAngle(270)
        runText.Draw()

        theLegend = ROOT.TLegend(0.1, 0.75, 0.3, 0.9)
        theLegend.AddEntry(singleMuonHist, "Single Muon 22", "l")
        theLegend.AddEntry(singleJetHist, 'Single Jet 180', 'l')
        theLegend.AddEntry(HTHist, 'HTT450er')
        theLegend.AddEntry(AD3Hist, "Calo Anomaly Score > 3", "l")
        theLegend.AddEntry(AD4Hist, "Calo Anomaly Score > 4", "l")
        theLegend.AddEntry(AD5Hist, "Calo Anomaly Score > 5", "l")
        theLegend.AddEntry(AD6Hist, "Calo Anomaly Score > 6", "l")
        theLegend.Draw()
        #the we write them, and move on to the next
        theCanvas.SaveAs('MenuComparison_Run%i.png' % run)
"""
    binsToPlaceLines = {}
    triggerRunningPass={}
    triggerRunningTotal = {}
    for trigger in triggers:
        triggerRunningPass[trigger] = []
        triggerRunningTotal[trigger] = []
    binToFill = 1.0
    runsInOrder = list(runLumiDict.keys())
    runsInOrder.sort()
    for run in runsInOrder:
        #print("run: ",run)
        #print("Starting at bin: ", binToFill)
        lumisProcessed = 0
        binsToPlaceLines[run] = binToFill
        lumisInOrder = list(runLumiDict[run].keys())
        lumisInOrder.sort()
        for lumi in lumisInOrder:
            #add the current pass/total to the lists
            # if we don't have enough of these, just continue
            #if end up having more than enough, remove the one at the front of the list
            #then if we have enough, we can calculate an overall efficiency with these
            triggerEff = {}
            for trigger in triggers:
                triggerRunningPass[trigger].append(runLumiDict[run][lumi][trigger]['pass'])
                triggerRunningTotal[trigger].append(runLumiDict[run][lumi][trigger]['total'])
                if len(triggerRunningPass[trigger]) >= averageOverLumis:
                    if len(triggerRunningPass[trigger]) > averageOverLumis:
                        triggerRunningPass[trigger].pop(0)
                        triggerRunningTotal[trigger].pop(0)
                    totalPass = 0.0
                    totalTotal = 0.0
                    for i in range(averageOverLumis):
                        totalPass += triggerRunningPass[trigger][i]
                        totalTotal += triggerRunningTotal[trigger][i]
                    triggerEff[trigger] = totalPass/totalTotal
            if len(triggerRunningPass['singleMuon']) == averageOverLumis:
                singleMuonRate = convertEffToRate(triggerEff['singleMuon'])
                singleJetRate = convertEffToRate(triggerEff['singleJet'])
                HTRate = convertEffToRate(triggerEff['HT'])
                AD3Rate = convertEffToRate(triggerEff['AD3'])
                AD4Rate = convertEffToRate(triggerEff['AD4'])
                AD5Rate = convertEffToRate(triggerEff['AD5'])
                AD6Rate = convertEffToRate(triggerEff['AD6'])

                singleMuonHist.SetBinContent(int(binToFill), singleMuonRate)
                singleJetHist.SetBinContent(int(binToFill), singleJetRate)
                HTHist.SetBinContent(int(binToFill), HTRate)
                AD3Hist.SetBinContent(int(binToFill), AD3Rate)
                AD4Hist.SetBinContent(int(binToFill), AD4Rate)
                AD5Hist.SetBinContent(int(binToFill), AD5Rate)
                AD6Hist.SetBinContent(int(binToFill), AD6Rate)
                
                binToFill += 1.0

    singleMuonHist.SetLineColor(ROOT.kOrange)
    singleJetHist.SetLineColor(ROOT.kGreen)
    HTHist.SetLineColor(ROOT.kMagenta)
    AD3Hist.SetLineColor(ROOT.kAzure)
    AD4Hist.SetLineColor(ROOT.kAzure-3)
    AD5Hist.SetLineColor(ROOT.kAzure-6)
    AD6Hist.SetLineColor(ROOT.kAzure-9)

    singleMuonHist.Draw('L')
    singleJetHist.Draw('L SAME')
    HTHist.Draw('L SAME')
    AD3Hist.Draw('L SAME')
    AD4Hist.Draw('L SAME')
    AD5Hist.Draw('L SAME')
    AD6Hist.Draw('L SAME')

    #singleMuonHist.SetMaximum(28.6e3)
    singleMuonHist.SetMaximum(28.6e3+10.0e3)
    singleMuonHist.SetMinimum(0.01)
    singleMuonHist.GetXaxis().SetLabelSize(0.0)
    singleMuonHist.GetYaxis().SetTitle("Rate (kHz)")

    #let's draw lines at the appropriate spots
    lines = []
    text = []
    for run in binsToPlaceLines:
        theLine = ROOT.TLine(binsToPlaceLines[run],0.01, 
                             binsToPlaceLines[run], singleMuonHist.GetMaximum())
        theLine.SetLineStyle(9)
        theLine.Draw()
        lines.append(theLine)
        runText = ROOT.TText(binsToPlaceLines[run]+2, singleMuonHist.GetMaximum()/(2*1e3), 'Run %i' % run)
        runText.SetTextAlign(22)
        runText.SetTextSize(0.05)
        runText.SetTextAngle(270)
        runText.Draw()
        text.append(runText)

    theLegend = ROOT.TLegend(0.1, 0.75, 0.3, 0.9)
    theLegend.AddEntry(singleMuonHist, "Single Muon 22", "l")
    theLegend.AddEntry(singleJetHist, 'Single Jet 180', 'l')
    theLegend.AddEntry(HTHist, 'HTT450er')
    theLegend.AddEntry(AD3Hist, "Calo Anomaly Score > 3", "l")
    theLegend.AddEntry(AD4Hist, "Calo Anomaly Score > 4", "l")
    theLegend.AddEntry(AD5Hist, "Calo Anomaly Score > 5", "l")
    theLegend.AddEntry(AD6Hist, "Calo Anomaly Score > 6", "l")
    theLegend.Draw()

    theCanvas.SaveAs('L1MenuComparisons.png')
"""
if __name__=='__main__':
    main()
