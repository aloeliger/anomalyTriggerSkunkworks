
import ROOT
import os
import argparse

from L1Trigger.anomalyTriggerSkunkworks.plotSettings.utilities import getListOfUniqueEntries, convertEffToRate

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

def main(args):
    theFile = ROOT.TFile('/nfs_scratch/aloeliger/MenuComparison_PureRate_Run%i.root' % args.theRun, 'RECREATE')
    
    caloSummaryChain = ROOT.TChain('L1TCaloSummaryTestNtuplizer/L1TCaloSummaryOutput')
    l1BitChain = ROOT.TChain('L1TTriggerBitsNtuplizer/L1TTriggerBits')

    filePath = '/hdfs/store/user/aloeliger/L1TriggerBitTest/allv4/'


    #We need the files that we have stored away on hdfs
    for name in os.listdir(filePath):
        caloSummaryChain.Add(filePath+name)
        l1BitChain.Add(filePath+name)

    #caloSummaryChain.AddFriend(l1BitChain)


    #print(caloSummaryChain.GetEntries(f'run=={args.theRun}'))
    theTree = caloSummaryChain.CopyTree(f'run=={args.theRun}')
    theL1Tree = l1BitChain.CopyTree(f'run=={args.theRun}')
    theTree.AddFriend(theL1Tree)
    lumis = getListOfUniqueEntries(theTree, 'lumi')
    numLumis = len(lumis)
    print('total lumi: ',numLumis)

    print('total events with no unprescaled bit: ', theTree.GetEntries(noUnprescaledBitPasses()))

    print('total events with L1_SingleMu22', theTree.GetEntries('L1_SingleMu22==1'))
    print('total events with no unprescaled bit (not counting L1_SingleMu22)', theTree.GetEntries(noUnprescaledBitPassesExceptMe('L1_SingleMu22')))
    print('total events with L1_SingleMu22 and no other bit: ', theTree.GetEntries('L1_SingleMu22==1 && '+noUnprescaledBitPassesExceptMe('L1_SingleMu22')))
    #print('condition: '+noUnprescaledBitPassesExceptMe('L1_SingleMu22==1L1_SingleMu22'))


    print('total events with L1_SingleJet180', theTree.GetEntries('L1_SingleJet180==1'))
    print('total events with no unprescaled bit (not counting L1_SingleJet180)', theTree.GetEntries(noUnprescaledBitPassesExceptMe('L1_SingleJet180')))
    print('total events with L1_SingleJet180 and no other bit: ', theTree.GetEntries('L1_SingleJet180==1 && '+noUnprescaledBitPassesExceptMe('L1_SingleJet180')))
    #print('condition: '+noUnprescaledBitPassesExceptMe('L1_SingleJet180'))


    print('total events with L1_HTT450er', theTree.GetEntries('L1_HTT450er==1'))
    print('total events with no unprescaled bit (not counting L1_HTT450er)', theTree.GetEntries(noUnprescaledBitPassesExceptMe('L1_HTT450er')))
    print('total events with L1_HTT450er and no other bit: ', theTree.GetEntries('L1_HTT450er==1 && '+noUnprescaledBitPassesExceptMe('L1_HTT450er')))
    #print('condition: '+noUnprescaledBitPassesExceptMe('L1_HTT450er'))


    print('total events with anomaly score > 3.0: ', theTree.GetEntries('anomalyScore>3.0'))
    print('total events with anomaly score > 3.0, and no bits: ',theTree.GetEntries('anomalyScore>3.0&& '+noUnprescaledBitPasses()))

    print('total events with anomaly score > 4.0: ', theTree.GetEntries('anomalyScore>4.0'))
    print('total events with anomaly score > 4.0, and no bits: ',theTree.GetEntries('anomalyScore>4.0&& '+noUnprescaledBitPasses()))

    print('total events with anomaly score > 5.0: ', theTree.GetEntries('anomalyScore>5.0'))
    print('total events with anomaly score > 5.0, and no bits: ',theTree.GetEntries('anomalyScore>5.0&& '+noUnprescaledBitPasses()))

    print('total events with anomaly score > 6.0: ', theTree.GetEntries('anomalyScore>6.0'))
    print('total events with anomaly score > 6.0, and no bits: ',theTree.GetEntries('anomalyScore>6.0&& '+noUnprescaledBitPasses()))

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
        
        singleMuonEff = theTree.GetEntries(f'lumi=={lumi} && L1_SingleMu22 > 0 && '+noUnprescaledBitPassesExceptMe('L1_SingleMu22')) / theTree.GetEntries(f'lumi=={lumi}')
        singleJetEff = theTree.GetEntries(f'lumi=={lumi} && L1_SingleJet180 > 0 && '+noUnprescaledBitPassesExceptMe('L1_SingleJet180')) / theTree.GetEntries(f'lumi=={lumi}')
        HTEff = theTree.GetEntries(f'lumi=={lumi} && L1_HTT450er > 0 && '+noUnprescaledBitPassesExceptMe('L1_HTT450er')) / theTree.GetEntries(f'lumi=={lumi}')
        AD3Eff = theTree.GetEntries(f'lumi=={lumi} && anomalyScore > 3.0 && '+noUnprescaledBitPasses()) / theTree.GetEntries(f'lumi=={lumi}')
        AD4Eff = theTree.GetEntries(f'lumi=={lumi} && anomalyScore > 4.0 && '+noUnprescaledBitPasses()) / theTree.GetEntries(f'lumi=={lumi}')
        AD5Eff = theTree.GetEntries(f'lumi=={lumi} && anomalyScore > 5.0 && '+noUnprescaledBitPasses()) / theTree.GetEntries(f'lumi=={lumi}')
        AD6Eff = theTree.GetEntries(f'lumi=={lumi} && anomalyScore > 6.0 && '+noUnprescaledBitPasses()) / theTree.GetEntries(f'lumi=={lumi}')

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

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='make a single Run\'s L1 Pure Rate Plot')
    parser.add_argument('--theRun', nargs='?', required=True, type=(int), help='Run number to make the plots for')

    args = parser.parse_args()

    main(args)
