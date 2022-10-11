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

def printExistingL1BitInfo(theBit, theTree):
    print('')
    totalEvents = theTree.GetEntries()
    print('Total Events: ', totalEvents)
    
    totalEventsPassing = theTree.GetEntries(f'{theBit} == 1')
    print(f'Total events passing {theBit}: ', totalEventsPassing)

    eff = totalEventsPassing/totalEvents
    print(f'Eff: {eff: }')
    
    rate = convertEffToRate(eff)
    print(f'Implied overall average rate: {rate} (kHz)')

    eventsWithNoUnprescaledBit = theTree.GetEntries(noUnprescaledBitPasses())
    print(f'total events with no unprescaled bit: {eventsWithNoUnprescaledBit}')

    eventsNoBitNotCounting = theTree.GetEntries(noUnprescaledBitPassesExceptMe(theBit))
    print(f'total events with no unprescaled bit (not counting {theBit}): {eventsNoBitNotCounting}')

    pureBitEvents = theTree.GetEntries(f'{theBit} == 1 && '+noUnprescaledBitPassesExceptMe(theBit))
    print(f'total events with {theBit} and no other bit: ', pureBitEvents)

    pureEff = pureBitEvents / totalEvents
    print(f'pure {theBit} eff: {pureEff}')

    pureRate = convertEffToRate(pureEff)
    print(f'pure {theBit} rate: {pureRate}')

def printAnomalyScoreInfo(threshold, theTree):
    print('')
    totalEvents = theTree.GetEntries()
    print('Total Events: ', totalEvents)
    
    totalEventsPassing = theTree.GetEntries(f'anomalyScore > {threshold}')
    print(f'Total events passing anomalyScore > {threshold}: ', totalEventsPassing)

    eff = totalEventsPassing/totalEvents
    print(f'Eff: {eff}')
    
    rate = convertEffToRate(eff)
    print(f'Implied overall average rate: {rate} (kHz)')

    eventsWithNoUnprescaledBit = theTree.GetEntries(noUnprescaledBitPasses())
    print(f'total events with no unprescaled bit: {eventsWithNoUnprescaledBit}')

    pureEvents = theTree.GetEntries(f'anomalyScore > {threshold} && '+noUnprescaledBitPasses())
    print(f'total events with no unprescaled bit and anomalyScore > {threshold}: {pureEvents}')

    pureEff = pureEvents / totalEvents
    print(f'pure anomaly score > {threshold} eff: {pureEff}')

    pureRate = convertEffToRate(pureEff)
    print(f'pure anomaly score > {threshold} rate: {pureRate} kHz')

    print('')
    

def main(args):
    theFile = ROOT.TFile(f'/nfs_scratch/aloeliger/MenuComparison_Run{args.theRun}.root', 'RECREATE')

    caloSummaryChain = ROOT.TChain('L1TCaloSummaryTestNtuplizer/L1TCaloSummaryOutput')
    l1BitChain = ROOT.TChain('L1TTriggerBitsNtuplizer/L1TTriggerBits')

    filePath = '/hdfs/store/user/aloeliger/L1TriggerBitTest/allv4/'

    #We need the files that we have stored away on hdfs
    for name in os.listdir(filePath):
        caloSummaryChain.Add(filePath+name)
        l1BitChain.Add(filePath+name)

    theTree = caloSummaryChain.CopyTree('run==%i'%args.theRun)
    theL1Tree = l1BitChain.CopyTree('run==%i'%args.theRun)

    theL1Tree.SetBranchStatus('run', 0)
    theL1Tree.SetBranchStatus('lumi', 0)
    theL1Tree.SetBranchStatus('evt', 0)

    theTree.AddFriend(theL1Tree)

    lumis = getListOfUniqueEntries(theTree, 'lumi')
    lumis.sort()
    print(lumis)
    numLumis = len(lumis)
    print('total lumi: ',numLumis)

    printExistingL1BitInfo('L1_SingleMu22', theTree)
    printExistingL1BitInfo('L1_SingleJet180', theTree)
    printExistingL1BitInfo('L1_DoubleIsoTau34er2p1', theTree)

    printAnomalyScoreInfo(3.0, theTree)
    printAnomalyScoreInfo(6.0, theTree)
    printAnomalyScoreInfo(7.0, theTree)
    printAnomalyScoreInfo(8.0, theTree)

    singleMuonHist = ROOT.TH1F('singleMuonHist','singleMuonHist', numLumis, 0.0, float(numLumis))
    singleJetHist = ROOT.TH1F('singleJetHist', 'singleJetHist', numLumis, 0.0, float(numLumis))
    doubleTauHist = ROOT.TH1F('doubleTauHist', 'doubleTauHist', numLumis, 0.0, float(numLumis))
    AD3Hist = ROOT.TH1F('AD3Hist','AD3Hist', numLumis, 0.0, float(numLumis))
    AD6Hist = ROOT.TH1F('AD6Hist','AD6Hist', numLumis, 0.0, float(numLumis))
    AD7Hist = ROOT.TH1F('AD7Hist','AD7Hist', numLumis, 0.0, float(numLumis))
    AD8Hist = ROOT.TH1F('AD8Hist','AD8Hist', numLumis, 0.0, float(numLumis))

    pureSingleMuonHist = ROOT.TH1F('pureSingleMuonHist','pureSingleMuonHist', numLumis, 0.0, float(numLumis))
    pureSingleJetHist = ROOT.TH1F('pureSingleJetHist', 'pureSingleJetHist', numLumis, 0.0, float(numLumis))
    pureDoubleTauHist = ROOT.TH1F('pureDoubleTauHist', 'pureDoubleTauHist', numLumis, 0.0, float(numLumis))
    pureAD3Hist = ROOT.TH1F('pureAD3Hist','pureAD3Hist', numLumis, 0.0, float(numLumis))
    pureAD6Hist = ROOT.TH1F('pureAD6Hist','pureAD6Hist', numLumis, 0.0, float(numLumis))
    pureAD7Hist = ROOT.TH1F('pureAD7Hist','pureAD7Hist', numLumis, 0.0, float(numLumis))
    pureAD8Hist = ROOT.TH1F('pureAD8Hist','pureAD8Hist', numLumis, 0.0, float(numLumis))

    binToFill = 1
    for lumi in lumis:
        print(f'Lumi: {lumi}, bin: {binToFill}')
        
        singleMuonEff = theTree.GetEntries(f'lumi=={lumi} && L1_SingleMu22 == 1') / theTree.GetEntries(f'lumi=={lumi}')
        singleJetEff = theTree.GetEntries(f'lumi=={lumi} && L1_SingleJet180 == 1') / theTree.GetEntries(f'lumi == {lumi}')
        doubleTauEff = theTree.GetEntries(f'lumi=={lumi} && L1_DoubleIsoTau34er2p1 == 1') / theTree.GetEntries(f'lumi == {lumi}')
        AD3Eff = theTree.GetEntries(f'lumi=={lumi} && anomalyScore > 3.0') / theTree.GetEntries(f'lumi=={lumi}')
        AD6Eff = theTree.GetEntries(f'lumi=={lumi} && anomalyScore > 6.0') / theTree.GetEntries(f'lumi=={lumi}')
        AD7Eff = theTree.GetEntries(f'lumi=={lumi} && anomalyScore > 7.0') / theTree.GetEntries(f'lumi=={lumi}')
        AD8Eff = theTree.GetEntries(f'lumi=={lumi} && anomalyScore > 8.0') / theTree.GetEntries(f'lumi=={lumi}')

        singleMuonRate = convertEffToRate(singleMuonEff)
        singleJetRate = convertEffToRate(singleJetEff)
        doubleTauRate = convertEffToRate(doubleTauEff)
        AD3Rate = convertEffToRate(AD3Eff)
        AD6Rate = convertEffToRate(AD6Eff)
        AD7Rate = convertEffToRate(AD7Eff)
        AD8Rate = convertEffToRate(AD8Eff)

        print()
        print(f'\t L1_SingleMu22 eff: {singleMuonEff}')
        print(f'\t L1_SingleJet180 eff: {singleJetEff}')
        print(f'\t L1_DoubleIsoTau34er2p1 eff: {doubleTauEff}')
        print(f'\t AD3 eff: {AD3Eff}')
        print(f'\t AD6 eff: {AD6Eff}')
        print(f'\t AD7 eff: {AD7Eff}')
        print(f'\t AD8 eff: {AD8Eff}')
        print()

        print()
        print(f'\t L1_SingleMu22 rate: {singleMuonRate}')
        print(f'\t L1_SingleJet180 rate: {singleJetRate}')
        print(f'\t L1_DoubleIsoTau34er2p1 rate: {doubleTauRate}')
        print(f'\t AD3 rate: {AD3Rate}')
        print(f'\t AD6 rate: {AD6Rate}')
        print(f'\t AD7 rate: {AD7Rate}')
        print(f'\t AD8 rate: {AD8Rate}')
        print()
        
        pureSingleMuonEff = theTree.GetEntries(f'lumi=={lumi} && L1_SingleMu22 == 1 && '+noUnprescaledBitPassesExceptMe('L1_SingleMu22')) / theTree.GetEntries(f'lumi=={lumi}')
        pureSingleJetEff = theTree.GetEntries(f'lumi=={lumi} && L1_SingleJet180 == 1 && '+noUnprescaledBitPassesExceptMe('L1_SingleJet180')) / theTree.GetEntries(f'lumi == {lumi}')
        pureDoubleTauEff = theTree.GetEntries(f'lumi=={lumi} && L1_DoubleIsoTau34er2p1 == 1 && '+noUnprescaledBitPassesExceptMe('L1_DoubleIsoTau34er2p1')) / theTree.GetEntries(f'lumi == {lumi}')
        pureAD3Eff = theTree.GetEntries(f'lumi=={lumi} && anomalyScore > 3.0 && '+noUnprescaledBitPasses()) / theTree.GetEntries(f'lumi=={lumi}')
        pureAD6Eff = theTree.GetEntries(f'lumi=={lumi} && anomalyScore > 6.0 && '+noUnprescaledBitPasses()) / theTree.GetEntries(f'lumi=={lumi}')
        pureAD7Eff = theTree.GetEntries(f'lumi=={lumi} && anomalyScore > 7.0 && '+noUnprescaledBitPasses()) / theTree.GetEntries(f'lumi=={lumi}')
        pureAD8Eff = theTree.GetEntries(f'lumi=={lumi} && anomalyScore > 8.0 && '+noUnprescaledBitPasses()) / theTree.GetEntries(f'lumi=={lumi}')


        pureSingleMuonRate = convertEffToRate(pureSingleMuonEff)
        pureSingleJetRate = convertEffToRate(pureSingleJetEff)
        pureDoubleTauRate = convertEffToRate(pureDoubleTauEff)
        pureAD3Rate = convertEffToRate(pureAD3Eff)
        pureAD6Rate = convertEffToRate(pureAD6Eff)
        pureAD7Rate = convertEffToRate(pureAD7Eff)
        pureAD8Rate = convertEffToRate(pureAD8Eff)

        print()
        print(f'\t pure L1_SingleMu22 eff: {pureSingleMuonEff}')
        print(f'\t pure L1_SingleJet180 eff: {pureSingleJetEff}')
        print(f'\t pure L1_DoubleIsoTau34er2p1 eff: {pureDoubleTauEff}')
        print(f'\t pure AD3 eff: {pureAD3Eff}')
        print(f'\t pure AD7 eff: {pureAD7Eff}')
        print(f'\t pure AD8 eff: {pureAD8Eff}')
        print(f'\t pure AD6 eff: {pureAD6Eff}')
        print()

        print()
        print(f'\t pure L1_SingleMu22 rate: {pureSingleMuonRate}')
        print(f'\t pure L1_SingleJet180 rate: {pureSingleJetRate}')
        print(f'\t pure L1_DoubleIsoTau34er2p1 rate: {pureDoubleTauRate}')
        print(f'\t pure AD3 rate: {pureAD3Rate}')
        print(f'\t pure AD7 rate: {pureAD7Rate}')
        print(f'\t pure AD8 rate: {pureAD8Rate}')
        print(f'\t pure AD6 rate: {pureAD6Rate}')
        print()

        singleMuonHist.SetBinContent(binToFill, singleMuonEff)
        singleJetHist.SetBinContent(binToFill, singleJetEff)
        doubleTauHist.SetBinContent(binToFill, doubleTauEff)
        AD3Hist.SetBinContent(binToFill, AD3Eff)
        AD7Hist.SetBinContent(binToFill, AD7Eff)
        AD8Hist.SetBinContent(binToFill, AD8Eff)
        AD6Hist.SetBinContent(binToFill, AD6Eff)
        
        pureSingleMuonHist.SetBinContent(binToFill, pureSingleMuonEff)
        pureSingleJetHist.SetBinContent(binToFill, pureSingleJetEff)
        pureDoubleTauHist.SetBinContent(binToFill, pureDoubleTauEff)
        pureAD3Hist.SetBinContent(binToFill, pureAD3Eff)
        pureAD7Hist.SetBinContent(binToFill, pureAD7Eff)
        pureAD8Hist.SetBinContent(binToFill, pureAD8Eff)
        pureAD6Hist.SetBinContent(binToFill, pureAD6Eff)
        
        binToFill += 1

    theFile.cd()

    singleMuonHist.Write()
    singleJetHist.Write()
    doubleTauHist.Write()
    AD3Hist.Write()
    AD7Hist.Write()
    AD8Hist.Write()
    AD6Hist.Write()

    pureSingleMuonHist.Write()
    pureSingleJetHist.Write()
    pureDoubleTauHist.Write()
    pureAD3Hist.Write()
    pureAD7Hist.Write()
    pureAD8Hist.Write()
    pureAD6Hist.Write()
    
    theFile.Write()
    theFile.Close()


if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Make Efficiency plots and print debug numbers for both Overall, and pure rates')
    parser.add_argument('--theRun', nargs='?', required=True, type=int, help='Run number to make the plots for')

    args = parser.parse_args()

    main(args)
