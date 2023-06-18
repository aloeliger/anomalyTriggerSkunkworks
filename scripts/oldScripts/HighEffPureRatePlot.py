#Okay. Similarly to the quick plotting of the overall L1 rates
#we need one that will do pure rate studies
#So this is going to be very similar, except for our passing region, 
# we look for no other un-prescaled bits firing
#which seems like a tall ask
#Also, this will require knowing which ones *are* the unprescaled bits
#which, initially, may be a plot I have to make myself.

import ROOT
import os
from tqdm import tqdm, trange

from anomalyDetection.anomalyTriggerSkunkworks.plotSettings.utilities import getListOfUniqueEntries, convertEffToRate

#This list may not be comprehensive, or right
#need to research how the l1GtUtils figured out the prescaling
#factor for these things, then add it to the ntuplizer
unPreScaledBits = [
    'L1_SingleMu22',
    'L1_SingleMu25',
    # 'L1_SingleMu10er1p5',
    # 'L1_SingleMu12er1p5',
    # 'L1_SingleMu14er1p5',
    # 'L1_SingleMu16er1p5',
    # 'L1_SingleMu18er1p5',
    # 'L1_DoubleMu8_SQ',
    'L1_DoubleMu9_SQ',
    'L1_DoubleMu_15_5_SQ',
    'L1_DoubleMu_15_7',
    'L1_DoubleMu_15_7_SQ',
    'L1_DoubleMu18er2p1',
    'L1_DoubleMu0er1p5_SQ_OS_dR_Max1p4',
    'L1_DoubleMu0er1p4_SQ_OS_dR_Max1p4',
    # 'L1_DoubleMu4_SQ_OS_dR_Max1p2',
    'L1_DoubleMu4p5_SQ_OS_dR_Max1p2',
    # 'L1_DoubleMu4p5er2p0_SQ_OS_Mass_Min7',
    'L1_DoubleMu4p5er2p0_SQ_OS_Mass7to18',
    'L1_TripleMu3_SQ',
    'L1_TripleMu_5_3_3',
    'L1_TripleMu_5_3_3_SQ',
    'L1_TripleMu_5_5_3',
    'L1_TripleMu_5_3p5_2p5_DoubleMu_5_2p5_OS_Mass_5to17',
    'L1_TripleMu_5_4_2p5_DoubleMu_5_2p5_OS_Mass_5to17',
    'L1_TripleMu_5SQ_3SQ_0OQ_DoubleMu_5_3_SQ_OS_Mass_Max9',
    'L1_TripleMu_5SQ_3SQ_0_DoubleMu_5_3_SQ_OS_Mass_Max9',
    # 'L1_Mu7_EG20er2p5',
    'L1_Mu7_EG23er2p5',
    'L1_Mu20_EG10er2p5',
    'L1_Mu7_LooseIsoEG20er2p5',
    'L1_Mu7_LooseIsoEG23er2p5',
    'L1_Mu6_DoubleEG12er2p5',
    'L1_Mu6_DoubleEG15er2p5',
    'L1_Mu6_DoubleEG17er2p5',
    'L1_DoubleMu5_SQ_EG9er2p5',
    'L1_DoubleMu3_OS_DoubleEG7p5Upsilon',
    'L1_DoubleMu5Upsilon_OS_DoubleEG3',
    'L1_Mu3er1p5_Jet100er2p5_ETMHF40',
    'L1_Mu3er1p5_Jet100er2p5_ETMHF50',
    'L1_Mu6_HTT240er',
    'L1_Mu6_HTT250er',
    'L1_Mu12er2p3_Jet40er2p3_dR_Max0p4_DoubleJet40er2p3_dEta_Max1p6',
    'L1_Mu12er2p3_Jet40er2p1_dR_Max0p4_DoubleJet40er2p1_dEta_Max1p6',
    'L1_DoubleMu0_dR_Max1p6_Jet90er2p5_dR_Max0p8',
    'L1_DoubleMu3_dR_Max1p6_Jet90er2p5_dR_Max0p8',
    'L1_DoubleMu3_SQ_ETMHF50_Jet60er2p5_OR_DoubleJet40er2p5',
    'L1_DoubleMu3_SQ_ETMHF50_Jet60er2p5',
    'L1_DoubleMu3_SQ_ETMHF60_Jet60er2p5',
    'L1_DoubleMu3_SQ_HTT220er',
    'L1_DoubleMu3_SQ_HTT240er',
    'L1_DoubleMu3_SQ_HTT260er',
    # 'L1_SingleEG36er2p5',
    # 'L1_SingleEG38er2p5',
    'L1_SingleEG40er2p5',
    'L1_SingleEG42er2p5',
    'L1_SingleEG45er2p5',
    'L1_SingleEG60',
    # 'L1_SingleLooseIsoEG28er2p5',
    # 'L1_SingleLooseIsoEG28er2p1',
    # 'L1_SingleLooseIsoEG30er2p5',
    # 'L1_SingleIsoEG28er2p5',
    # 'L1_SingleIsoEG28er1p5',
    # 'L1_SingleIsoEG30er2p5',
    'L1_SingleIsoEG30er2p1',
    'L1_SingleIsoEG32er2p5',
    'L1_SingleIsoEG32er2p1',
    'L1_SingleIsoEG34er2p5',
    'L1_IsoEG32er2p5_Mt40',
    'L1_IsoEG32er2p5_Mt44',
    'L1_IsoEG32er2p5_Mt48',
    # 'L1_DoubleEG_25_12_er2p5',
    'L1_DoubleEG_25_14_er2p5',
    'L1_DoubleEG_27_14_er2p5',
    'L1_DoubleEG_LooseIso22_12_er2p5',
    'L1_DoubleEG_LooseIso25_12_er2p5',
    'L1_DoubleLooseIsoEG22er2p1',
    'L1_DoubleLooseIsoEG24er2p1',
    'L1_TripleEG_18_17_8_er2p5',
    'L1_TripleEG_18_18_12_er2p5',
    'L1_TripleEG16er2p5',
    # 'L1_LooseIsoEG28er2p1_Jet34er2p5_dR_Min0p3',
    'L1_LooseIsoEG30er2p1_Jet34er2p5_dR_Min0p3',
    # 'L1_LooseIsoEG26er2p1_HTT100er',
    'L1_LooseIsoEG28er2p1_HTT100er',
    'L1_LooseIsoEG30er2p1_HTT100er',
    'L1_DoubleEG8er2p5_HTT300er',
    'L1_DoubleEG8er2p5_HTT320er',
    'L1_DoubleEG8er2p5_HTT340er',
    'L1_LooseIsoEG22er2p1_IsoTau26er2p1_dR_Min0p3',
    'L1_LooseIsoEG24er2p1_IsoTau27er2p1_dR_Min0p3',
    'L1_LooseIsoEG22er2p1_Tau70er2p1_dR_Min0p3',
    'L1_SingleTau120er2p1',
    'L1_SingleTau130er2p1',
    'L1_DoubleTau70er2p1',
    # 'L1_DoubleIsoTau30er2p1',
    # 'L1_DoubleIsoTau32er2p1',
    'L1_DoubleIsoTau34er2p1',
    'L1_DoubleIsoTau36er2p1',
    # 'L1_DoubleIsoTau28er2p1_Mass_Max80',
    'L1_DoubleIsoTau30er2p1_Mass_Max80',
    'L1_Mu18er2p1_Tau24er2p1',
    'L1_Mu18er2p1_Tau26er2p1',
    # 'L1_Mu22er2p1_IsoTau28er2p1',
    # 'L1_Mu22er2p1_IsoTau30er2p1',
    'L1_Mu22er2p1_IsoTau32er2p1',
    'L1_Mu22er2p1_IsoTau34er2p1',
    'L1_Mu22er2p1_IsoTau36er2p1',
    'L1_Mu22er2p1_IsoTau40er2p1',
    'L1_Mu22er2p1_Tau70er2p1',
    'L1_IsoTau40er2p1_ETMHF90',
    'L1_IsoTau40er2p1_ETMHF100',
    'L1_IsoTau40er2p1_ETMHF110',
    'L1_SingleJet180',
    'L1_SingleJet200',
    'L1_SingleJet180er2p5',
    'L1_DoubleJet150er2p5',
    'L1_DoubleJet112er2p3_dEta_Max1p6',
    'L1_DoubleJet30er2p5_Mass_Min300_dEta_Max1p5',
    'L1_DoubleJet30er2p5_Mass_Min330_dEta_Max1p5',
    'L1_DoubleJet30er2p5_Mass_Min360_dEta_Max1p5',
    # 'L1_DoubleJet_110_35_DoubleJet35_Mass_Min620',
    'L1_DoubleJet_115_40_DoubleJet40_Mass_Min620',
    'L1_DoubleJet_120_45_DoubleJet45_Mass_Min620',
    'L1_DoubleJet_115_40_DoubleJet40_Mass_Min620_Jet60TT28',
    'L1_DoubleJet_120_45_DoubleJet45_Mass_Min620_Jet60TT28',
    # 'L1_TripleJet_95_75_65_DoubleJet_75_65_er2p5',
    'L1_TripleJet_100_80_70_DoubleJet_80_70_er2p5',
    'L1_TripleJet_105_85_75_DoubleJet_85_75_er2p5',
    'L1_QuadJet_95_75_65_20_DoubleJet_75_65_er2p5_Jet20_FWD3p0',
    # 'L1_HTT320er_QuadJet_70_55_40_40_er2p4',
    'L1_HTT320er_QuadJet_80_60_er2p1_45_40_er2p3',
    'L1_HTT320er_QuadJet_80_60_er2p1_50_45_er2p3',
    'L1_HTT360er',
    'L1_HTT400er',
    'L1_HTT450er',
    'L1_ETT2000',
    'L1_ETM150',
    # 'L1_ETMHF100',
    # 'L1_ETMHF110',
    # 'L1_ETMHF120',
    'L1_ETMHF130',
    'L1_ETMHF140',
    'L1_ETMHF150',
    # 'L1_ETMHF100_HTT60er',
    'L1_ETMHF110_HTT60er',
    'L1_ETMHF120_HTT60er',
    'L1_ETMHF130_HTT60er',
]

#Okay. The information we want is scattered across trees.
#There just is no version of this where we get out of doing a loop,
#And judging this individually, for every single event, one by one.
#Yikes.

def convertEffToRate(eff): #returns the rate in kHz
    return eff * (2544.0 * 11425e-3) 
 
def getUniqueRunsAndLumis(theChain):
    runLumiDict = {}
    
    theChain.SetBranchStatus("*", 0)
    #reenable the ones we care about
    theChain.SetBranchStatus("run", 1)
    theChain.SetBranchStatus("lumi", 1)
    
    for i in trange(theChain.GetEntries()):
        theChain.GetEntry(i)
        run = theChain.run
        lumi = theChain.lumi
        if run not in runLumiDict:
            runLumiDict[run]=[]
        if lumi not in runLumiDict[run]:
            runLumiDict[run].append(lumi)

    #reenable branches
    theChain.SetBranchStatus("*", 1)

    return runLumiDict
        
def noUnprescaledBitPasses():
    finalRequirement = ''
    for bit in unPreScaledBits:
        finalRequirement += bit + ' == 0 &&'
    #remove the final 3 characters off the end of the string
    #because we don't need the and
    finalRequirement = finalRequirement[:-3]
    return finalRequirement

def noUnprescaledBitPassesExceptMe(theBit):
    bitRequirement = noUnprescaledBitPasses()
    myLocation = bitRequirement.find(theBit)
    if myLocation + 8 >= len(bitRequirement): # our thing + ' == 0 &&' was past the end of the string, because it was at the end.
        bitRequirement = bitRequirement.replace(theBit+' == 0', '')
    else:
        bitRequirement = bitRequirement.replace(theBit+' == 0 &&','')
    return bitRequirement
    
def main():
    #All we want, is to make the basic plots, 
    #save them to files,
    #And sort out the styling later
    #Let's make it happen I guess...

    caloSummaryChain = ROOT.TChain('L1TCaloSummaryTestNtuplizer/L1TCaloSummaryOutput')
    l1BitChain = ROOT.TChain('L1TTriggerBitsNtuplizer/L1TTriggerBits')
    
    filePath = '/hdfs/store/user/aloeliger/L1TriggerBitTest/allv4/'

    for name in os.listdir(filePath):
        caloSummaryChain.Add(filePath+name)
        l1BitChain.Add(filePath+name)

    #we're going to make our lives much easier doing this:
    caloSummaryChain.AddFriend(l1BitChain)

    #First, we want a listing of all the unique run lumi combinations in our chain
    runLumiDict = getUniqueRunsAndLumis(caloSummaryChain)
    
    triggers = ['AD3', 'AD4', 'AD5', 'AD6', 'L1_SingleMu22', 'L1_SingleJet180', 'L1_HTT450er']

    rates = {}
    averageOverLumis = 5
    for run in tqdm(runLumiDict, desc='runs'):
        rates[run] = {}
        for lumi in tqdm(runLumiDict[run], leave=False, desc='lumis'):
            rates[run][lumi]={}
            for trigger in tqdm(triggers, leave=False, desc='triggers'):
                rates[run][lumi][trigger] = {}
                rates[run][lumi][trigger]['total'] = caloSummaryChain.GetEntries(f'run == {run} && lumi == {lumi}')
                if trigger == 'AD3':
                    rates[run][lumi][trigger]['pass'] = caloSummaryChain.GetEntries(f'run == {run} && lumi == {lumi} && anomalyScore >= 3.0 && '+noUnprescaledBitPasses())
                elif trigger == 'AD4':
                    rates[run][lumi][trigger]['pass'] = caloSummaryChain.GetEntries(f'run == {run} && lumi == {lumi} && anomalyScore >= 4.0 && '+noUnprescaledBitPasses())
                elif trigger == 'AD5':
                    rates[run][lumi][trigger]['pass'] = caloSummaryChain.GetEntries(f'run == {run} && lumi == {lumi} && anomalyScore >= 5.0 && '+noUnprescaledBitPasses())
                elif trigger == 'AD6':
                    rates[run][lumi][trigger]['pass'] = caloSummaryChain.GetEntries(f'run == {run} && lumi == {lumi} && anomalyScore >= 6.0 && '+noUnprescaledBitPasses())
                else:
                    rates[run][lumi][trigger]['pass'] = caloSummaryChain.GetEntries(f'run == {run} && lumi == {lumi} && {trigger} == 1 && '+noUnprescaledBitPassesExceptMe(trigger))
                rates[run][lumi][trigger]['eff'] = rates[run][lumi][trigger]['pass'] / rates[run][lumi][trigger]['total']
                rates[run][lumi][trigger]['rate'] = convertEffToRate(rates[run][lumi][trigger]['eff'])
        #now that we have all the pure rates,
        #let's sit down and fill out some histograms 
        binToFill = 1.0
        triggerRunningPass = {}
        triggerRunningTotal = {}
        for trigger in triggers:
            triggerRunningPass[trigger] = []
            triggerRunningTotal[trigger] = []


        lumisInOrder = list(rates[run].keys())
        lumisInOrder.sort()
        numLumis = len(lumisInOrder)

        singleMuonHist = ROOT.TH1F('singleMuonHist', 'singleMuonHist', numLumis, 0.0, float(numLumis))
        singleJetHist = ROOT.TH1F('singleJetHist', 'singleJetHist', numLumis, 0.0, float(numLumis))
        HTHist = ROOT.TH1F('HTHist', 'HTHist', numLumis, 0.0, float(numLumis))
        AD3Hist = ROOT.TH1F('AD3Hist','AD3Hist', numLumis, 0.0, float(numLumis))
        AD4Hist = ROOT.TH1F('AD4Hist','AD4Hist', numLumis, 0.0, float(numLumis))
        AD5Hist = ROOT.TH1F('AD5Hist','AD5Hist', numLumis, 0.0, float(numLumis))
        AD6Hist = ROOT.TH1F('AD6Hist','AD6Hist', numLumis, 0.0, float(numLumis))

        #now let's go through the lumis and fill all of these up
        for lumi in lumisInOrder:
            triggerEff = {}
            for trigger in triggers:
                triggerRunningPass[trigger].append(rates[run][lumi][trigger]['pass'])
                triggerRunningTotal[trigger].append(rates[run][lumi][trigger]['total'])
                if len(triggerRunningPass[trigger]) > averageOverLumis:
                    triggerRunningPass[trigger].pop(0)
                    triggerRunningTotal[trigger].pop(0)
                totalPass = 0.0
                totalTotal = 0.0
                for i in range(len(triggerRunningPass[trigger])):
                    totalPass += triggerRunningPass[trigger][i]
                    totalTotal += triggerRunningTotal[trigger][i]
                triggerEff[trigger] = totalPass/totalTotal
            singleMuonRate = convertEffToRate(triggerEff['L1_SingleMu22'])
            singleJetRate = convertEffToRate(triggerEff['L1_SingleJet180'])
            HTRate = convertEffToRate(triggerEff['L1_HTT450er'])
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
        #Now let's just write these histograms to a file, and get out of here
        theFile = ROOT.TFile(f'MenuComparison_PureRateRun{run}.root', 'RECREATE')
        singleMuonHist.Write()
        singleJetHist.Write()
        HTHist.Write()
        AD3Hist.Write()
        AD4Hist.Write()
        AD5Hist.Write()
        AD6Hist.Write()
        theFile.Write()
        theFile.Close()

if __name__ == '__main__':
    main()
