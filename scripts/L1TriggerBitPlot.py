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

    filePath = '/hdfs/store/user/aloeliger/L1TriggerBitTest/all/'

    #We need the files that we have stored away on hdfs
    for name in os.listdir(filePath):
        caloSummaryChain.Add(filePath+name)
        l1BitChain.Add(filePath+name)
    
    runLumiDict = {}
    triggers = ['AD3', 'AD4', 'AD5', 'AD6', 'singleMuon']
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
        if l1BitChain.L1_SingleMu20:
            runLumiDict[theRun][theLumi]['singleMuon']['pass'] += 1.0

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
    print("total lumi bins: ", totalLumiBins)
    singleMuonHist = ROOT.TH1F('singleMuonHist','singleMuonHist', totalLumiBins+20, -20.0, float(totalLumiBins)+1.0)
    AD3Hist = ROOT.TH1F('AD3Hist','AD3Hist', totalLumiBins+20, -20.0, float(totalLumiBins)+1.0)
    AD4Hist = ROOT.TH1F('AD4Hist','AD4Hist', totalLumiBins+20, -20.0, float(totalLumiBins)+1.0)
    AD5Hist = ROOT.TH1F('AD5Hist','AD5Hist', totalLumiBins+20, -20.0, float(totalLumiBins)+1.0)
    AD6Hist = ROOT.TH1F('AD6Hist','AD6Hist', totalLumiBins+20, -20.0, float(totalLumiBins)+1.0)

    def convertEffToRate(eff): #returns the rate in kHz
        return eff * (2544.0 * 11425e-3) 
                    

    binsToPlaceLines = {}
    triggerRunningPass={}
    triggerRunningTotal = {}
    for trigger in triggers:
        triggerRunningPass[trigger] = []
        triggerRunningTotal[trigger] = []
    binToFill = 20.0
    runsInOrder = list(runLumiDict.keys())
    runsInOrder.sort()
    for run in runsInOrder:
        print("run: ",run)
        print("Starting at bin: ", binToFill)
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
                AD3Rate = convertEffToRate(triggerEff['AD3'])
                AD4Rate = convertEffToRate(triggerEff['AD4'])
                AD5Rate = convertEffToRate(triggerEff['AD5'])
                AD6Rate = convertEffToRate(triggerEff['AD6'])

                singleMuonHist.SetBinContent(int(binToFill), singleMuonRate)
                AD3Hist.SetBinContent(int(binToFill), AD3Rate)
                AD4Hist.SetBinContent(int(binToFill), AD4Rate)
                AD5Hist.SetBinContent(int(binToFill), AD5Rate)
                AD6Hist.SetBinContent(int(binToFill), AD6Rate)
                
                binToFill += 1.0

        """
        for lumi in lumisInOrder:
            print("lumi: ", lumi)
            lumisProcessed += 1
            for trigger in triggers:
                runLumiDict[run][lumi][trigger]['eff'] = runLumiDict[run][lumi][trigger]['pass'] / runLumiDict[run][lumi][trigger]['total']
            singleMuonRate = convertEffToRate(runLumiDict[run][lumi]['singleMuon']['eff'])
            AD3Rate = convertEffToRate(runLumiDict[run][lumi]['AD3']['eff'])
            AD4Rate = convertEffToRate(runLumiDict[run][lumi]['AD4']['eff'])
            AD5Rate = convertEffToRate(runLumiDict[run][lumi]['AD5']['eff'])
            AD6Rate = convertEffToRate(runLumiDict[run][lumi]['AD6']['eff'])

            singleMuonHist.SetBinContent(int(binToFill), singleMuonRate)
            AD3Hist.SetBinContent(int(binToFill), AD3Rate)
            AD4Hist.SetBinContent(int(binToFill), AD4Rate)
            AD5Hist.SetBinContent(int(binToFill), AD5Rate)
            AD6Hist.SetBinContent(int(binToFill), AD6Rate)

            binToFill += 1.0
        print("total lumis: ",lumisProcessed)
        """

    singleMuonHist.SetLineColor(ROOT.kOrange)
    AD3Hist.SetLineColor(ROOT.kAzure)
    AD4Hist.SetLineColor(ROOT.kAzure-3)
    AD5Hist.SetLineColor(ROOT.kAzure-6)
    AD6Hist.SetLineColor(ROOT.kAzure-9)

    singleMuonHist.Draw('L')
    AD3Hist.Draw('L SAME')
    AD4Hist.Draw('L SAME')
    AD5Hist.Draw('L SAME')
    AD6Hist.Draw('L SAME')

    #singleMuonHist.SetMaximum(28.6e3)
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
    theLegend.AddEntry(singleMuonHist, "Single Muon 20", "l")
    theLegend.AddEntry(AD3Hist, "Calo Anomaly Score > 3", "l")
    theLegend.AddEntry(AD4Hist, "Calo Anomaly Score > 4", "l")
    theLegend.AddEntry(AD5Hist, "Calo Anomaly Score > 5", "l")
    theLegend.AddEntry(AD6Hist, "Calo Anomaly Score > 6", "l")
    theLegend.Draw()

    theCanvas.SaveAs('L1MenuComparisons.png')

if __name__=='__main__':
    main()
