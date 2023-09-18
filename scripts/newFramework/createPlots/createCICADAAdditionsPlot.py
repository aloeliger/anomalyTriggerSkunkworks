# !/usr/bin/env python3
import ROOT

import argparse

from anomalyDetection.anomalyTriggerSkunkworks.samples.mcSamples2022.DYto2L import DYTo2LSample
from anomalyDetection.anomalyTriggerSkunkworks.samples.mcSamples2022.GGHTT import GGHTTSample
from anomalyDetection.anomalyTriggerSkunkworks.samples.mcSamples2022.HTo2LongLived4b import HTo2LongLived4bSample
from anomalyDetection.anomalyTriggerSkunkworks.samples.mcSamples2022.SUSYGGBBHtoBB import SUSYGGBBHtoBBSample
from anomalyDetection.anomalyTriggerSkunkworks.samples.mcSamples2022.TT import TTSample
from anomalyDetection.anomalyTriggerSkunkworks.samples.mcSamples2022.VBFHToInvisible import VBFHToInvisibleSample
from anomalyDetection.anomalyTriggerSkunkworks.samples.mcSamples2022.VBFHTT import VBFHTTSample
from anomalyDetection.anomalyTriggerSkunkworks.samples.mcSamples2022.ZPrimeTT import ZPrimeTTSample

def getListOfExtantUnprescaledBits(columnNames, unprescaledBits):
    # First let's boil the column names down to just the bits
    # print(columnNames)
    bitsPresent = [str(x) for x in columnNames if 'L1TTriggerBits' in str(x)]
    # print(bitsPresent)
    bitsPresent = [x for x in bitsPresent if 'prescale' not in x]
    # print(bitsPresent)
    bitsPresent = [x.split('.')[1] for x in bitsPresent]
    bitsPresent = [x for x in bitsPresent if 'L1' in x]
    # print(bitsPresent)
    # print(len(bitsPresent))

    unprescaledBitsPresent = [x for x in bitsPresent if x in unprescaledBits]
    # print(unprescaledBitsPresent)
    # print(len(unprescaledBitsPresent))

    missingUnprescaledBits = [x for x in unprescaledBits if x not in unprescaledBitsPresent]
    print('Missing unprescaled bits in the chain:')
    print(missingUnprescaledBits)

    return unprescaledBitsPresent

def getStringForBitPass(listOfUnprescaledBits):
    theString = ''
    for bit in listOfUnprescaledBits:
        theString += f'{bit}==1 ||'
    theString = theString[:-3]
    return theString

def main(args):
    dataframes = {
        'DYTo2L': DYTo2LSample.getNewDataframe(
            [
                f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
                'L1TTriggerBitsNtuplizer/L1TTriggerBits',  
            ]
        ),
        'GGHTT': GGHTTSample.getNewDataframe(
            [
                f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
                'L1TTriggerBitsNtuplizer/L1TTriggerBits',  
            ]
        ),
        'HTo2LongLived4b': HTo2LongLived4bSample.getNewDataframe(
            [
                f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
                'L1TTriggerBitsNtuplizer/L1TTriggerBits',  
            ]
        ),
        'SUSYGGBBHtoBB': SUSYGGBBHtoBBSample.getNewDataframe(
            [
                f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
                'L1TTriggerBitsNtuplizer/L1TTriggerBits',  
            ]
        ),
        'TT': TTSample.getNewDataframe(
            [
                f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
                'L1TTriggerBitsNtuplizer/L1TTriggerBits',  
            ]
        ),
        'VBFHToInvisible': VBFHToInvisibleSample.getNewDataframe(
            [
                f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
                'L1TTriggerBitsNtuplizer/L1TTriggerBits',  
            ]
        ),
        'VBFHTT': VBFHTTSample.getNewDataframe(
            [
                f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
                'L1TTriggerBitsNtuplizer/L1TTriggerBits',  
            ]
        ),
        'ZPrimeTT': ZPrimeTTSample.getNewDataframe(
            [
                f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
                'L1TTriggerBitsNtuplizer/L1TTriggerBits',  
            ]
        ),
    }

    unprescaledBits = [
        'L1_SingleMu25',
        'L1_SingleMu22',
        'L1_DoubleMu8_SQ',
        'L1_DoubleMu9_SQ',
        'L1_DoubleMu_15_5_SQ',
        'L1_DoubleMu_15_7',
        'L1_DoubleMu_15_7_SQ',
        'L1_DoubleMu18er2p1_SQ',
        'L1_DoubleMu0_Upt6_IP_Min1_Upt4',
        'L1_DoubleMu0_Upt15_Upt7',
        'L1_DoubleMu0er2p0_SQ_OS_dEta_Max1p5',
        'L1_DoubleMu0er1p5_SQ_OS_dR_Max1p4',
        'L1_DoubleMu0er1p4_SQ_OS_dR_Max1p4',
        'L1_DoubleMu4_SQ_OS_dR_Max1p2',
        'L1_DoubleMu4p5_SQ_OS_dR_Max1p2',
        'L1_DoubleMu4p5er2p0_SQ_OS_Mass_Min7',
        'L1_DoubleMu4p5er2p0_SQ_OS_Mass_7to18',
        'L1_TripleMu3_SQ',
        'L1_TripleMu_5_3_3',
        'L1_TripleMu_5_3_3_SQ',
        'L1_TripleMu_5_5_3',
        'L1_TripleMu_3SQ_2p5SQ_0OQ_Mass_Max12',
        'L1_TripleMu_5_3p5_2p5_DoubleMu_5_2p5_OS_Mass_5to17',
        'L1_TripleMu_5_4_2p5_DoubleMu_5_2p5_OS_Mass_5to17',
        'L1_TripleMu_5SQ_3SQ_0OQ_DoubleMu_5_3_SQ_OS_Mass_Max9',
        'L1_TripleMu_5SQ_3SQ_0_DoubleMu_5_3_SQ_OS_Mass_Max9',
        'L1_SingleMuShower_Nominal',
        'L1_SingleMuShower_Tight',
        'L1_Mu7_EG20er2p5',
        'L1_Mu7_EG23er2p5',
        'L1_Mu20_EG10er2p5',
        'L1_Mu7_LooseIsoEG20er2p5',
        'L1_Mu7_LooseIsoEG23er2p5',
        'L1_Mu6_DoubleEG12er2p5',
        'L1_Mu6_DoubleEG15er2p5',
        'L1_Mu6_DoubleEG17er2p5',
        'L1_DoubleMu5_SQ_EG9er2p5',
        'L1_DoubleMu3_OS_er2p3_Mass_Max14_DoubleEG7p5_er2p1_Mass_Max20',
        'L1_DoubleMu5_OS_er2p3_Mass_8to14_DoubleEG3er2p1_Mass_Max20',
        'L1_Mu3er1p5_Jet100er2p5_ETMHF40',
        'L1_Mu3er1p5_Jet100er2p5_ETMHF50',
        'L1_Mu6_HTT240er',
        'L1_Mu6_HTT250er',
        'L1_Mu12er2p3_Jet40er2p3_dR_Max0p4_DoubleJet40er2p3_dEta_Max1p6',
        'L1_Mu12er2p3_Jet40er2p1_dR_Max0p4_DoubleJet40er2p1_dEta_Max1p6',
        'L1_DoubleMu0_dR_Max1p6_Jet90er2p5_dR_Max0p8',
        'L1_DoubleMu3_dR_Max1p6_Jet90er2p5_dR_Max0p8',
        'L1_DoubleMu3_SQ_ETMHF40_HTT60er',
        'L1_DoubleMu3_SQ_ETMHF50_HTT60er',
        'L1_DoubleMu3_SQ_ETMHF40_Jet60er2p5_OR_DoubleJet40er2p5',
        'L1_DoubleMu3_SQ_ETMHF50_Jet60er2p5_OR_DoubleJet40er2p5',
        'L1_DoubleMu3_SQ_ETMHF50_Jet60er2p5',
        'L1_DoubleMu3_SQ_ETMHF60_Jet60er2p5',
        'L1_DoubleMu3_SQ_HTT220er',
        'L1_DoubleMu3_SQ_HTT240er',
        'L1_DoubleMu3_SQ_HTT260er',
        'L1_SingleEG36er2p5',
        'L1_SingleEG38er2p5',
        'L1_SingleEG40er2p5',
        'L1_SingleEG42er2p5',
        'L1_SingleEG45er2p5',
        'L1_SingleIsoEG30er2p5',
        'L1_SingleIsoEG30er2p1',
        'L1_SingleIsoEG32er2p5',
        'L1_SingleIsoEG32er2p1',
        'L1_SingleIsoEG34er2p5',
        'L1_DoubleEG_25_12_er2p5',
        'L1_DoubleEG_25_14_er2p5',
        'L1_DoubleEG_27_14_er2p5',
        'L1_DoubleEG_LooseIso22_12_er2p5',
        'L1_DoubleEG_LooseIso25_12_er2p5',
        'L1_DoubleEG_LooseIso18_LooseIso12_er1p5',
        'L1_DoubleEG_LooseIso20_LooseIso12_er1p5',
        'L1_DoubleEG_LooseIso22_LooseIso12_er1p5',
        'L1_DoubleEG_LooseIso25_LooseIso12_er1p5',
        'L1_DoubleLooseIsoEG22er2p1',
        'L1_DoubleLooseIsoEG24er2p1',
        'L1_TripleEG_18_17_8_er2p5',
        'L1_TripleEG_18_18_12_er2p5',
        'L1_TripleEG16er2p5',
        'L1_LooseIsoEG28er2p1_Jet34er2p5_dR_Min0p3',
        'L1_LooseIsoEG30er2p1_Jet34er2p5_dR_Min0p3',
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
        'L1_DoubleIsoTau34er2p1',
        'L1_DoubleIsoTau35er2p1',
        'L1_DoubleIsoTau36er2p1',
        'L1_Mu18er2p1_Tau24er2p1',
        'L1_Mu18er2p1_Tau26er2p1',
        'L1_Mu18er2p1_Tau26er2p1_Jet55',
        'L1_Mu18er2p1_Tau26er2p1_Jet70',
        'L1_DoubleIsoTau26er2p1_Jet70_RmOvlp_dR0p5',
        'L1_Mu22er2p1_IsoTau32er2p1',
        'L1_Mu22er2p1_IsoTau34er2p1',
        'L1_Mu22er2p1_IsoTau36er2p1',
        'L1_Mu22er2p1_IsoTau40er2p1',
        'L1_Mu22er2p1_Tau70er2p1',
        'L1_SingleJet180',
        'L1_SingleJet200',
        'L1_SingleJet180er2p5',
        'L1_ETMHF90_SingleJet60er2p5_dPhi_Min2p1',
        'L1_ETMHF90_SingleJet60er2p5_dPhi_Min2p6',
        'L1_ETMHF90_SingleJet80er2p5_dPhi_Min2p1',
        'L1_ETMHF90_SingleJet80er2p5_dPhi_Min2p6',
        'L1_DoubleJet150er2p5',
        'L1_DoubleJet112er2p3_dEta_Max1p6',
        'L1_DoubleJet30er2p5_Mass_Min300_dEta_Max1p5',
        'L1_DoubleJet30er2p5_Mass_Min330_dEta_Max1p5',
        'L1_DoubleJet30er2p5_Mass_Min360_dEta_Max1p5',
        'L1_DoubleJet_120_45_DoubleJet45_Mass_Min620',
        'L1_DoubleJet_115_40_DoubleJet40_Mass_Min620_Jet60TT28',
        'L1_DoubleJet_120_45_DoubleJet45_Mass_Min620_Jet60TT28',
        'L1_DoubleJet35_Mass_Min450_IsoTau45er2p1_RmOvlp_dR0p5',
        'L1_TripleJet_95_75_65_DoubleJet_75_65_er2p5',
        'L1_TripleJet_100_80_70_DoubleJet_80_70_er2p5',
        'L1_TripleJet_105_85_75_DoubleJet_85_75_er2p5',
        'L1_QuadJet_95_75_65_20_DoubleJet_75_65_er2p5_Jet20_FWD3p0',
        'L1_DoubleLLPJet40',
        'L1_HTT200_SingleLLPJet60',
        'L1_HTT240_SingleLLPJet70',
        'L1_HTT320er_QuadJet_70_55_40_40_er2p5',
        'L1_HTT320er_QuadJet_80_60_er2p1_45_40_er2p3',
        'L1_HTT320er_QuadJet_80_60_er2p1_50_45_er2p3',
        'L1_HTT360er',
        'L1_HTT400er',
        'L1_HTT450er',
        'L1_ETT2000',
        'L1_ETM150',
        'L1_ETMHF100',
        'L1_ETMHF110',
        'L1_ETMHF120',
        'L1_ETMHF130',
        'L1_ETMHF140',
        'L1_ETMHF150',
        'L1_ETMHF100_HTT60er',
        'L1_ETMHF110_HTT60er',
        'L1_ETMHF120_HTT60er',
        'L1_ETMHF130_HTT60er',
        'L1_SingleMuOpen_er1p4_NotBptxOR_3BX',
        'L1_SingleMuOpen_er1p1_NotBptxOR_3BX',
        'L1_SingleJet43er2p5_NotBptxOR_3BX',
        'L1_SingleJet46er2p5_NotBptxOR_3BX',
    ]

    # print(dataframes['DYTo2L'].GetColumnNames())
    availableUnprescaledBits = getListOfExtantUnprescaledBits(
        columnNames=dataframes['DYTo2L'].GetColumnNames(),
        unprescaledBits=unprescaledBits
    )

    #let's get a string for passing one of these unprescaled bits
    passesAnUnprescaledBit = getStringForBitPass(availableUnprescaledBits)

    for sample in dataframes:
        print(sample)
        sample_count_obj = dataframes[sample].Count()
        sample_unprescaled_obj = dataframes[sample].Filter(passesAnUnprescaledBit).Count()
        CICADA_low_threshold = 5.78
        sample_cicada_obj = dataframes[sample].Filter(f'anomalyScore >= {CICADA_low_threshold}').Count()
        sample_both_obj = dataframes[sample].Filter(f'{passesAnUnprescaledBit} || anomalyScore >= {CICADA_low_threshold}').Count()
        
        sample_unprescaled_eff = sample_unprescaled_obj.GetValue()/sample_count_obj.GetValue()
        sample_cicada_eff = sample_cicada_obj.GetValue()/sample_count_obj.GetValue()
        sample_both_eff = sample_both_obj.GetValue()/sample_count_obj.GetValue()

        print(f'Eff of unprescaled: {sample_unprescaled_eff:3.3%}')
        print(f'Eff of CICADA: {sample_cicada_eff:3.3%}')
        print(f'Eff of both: {sample_both_eff:3.3%}')
        print()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Create stability rate plots for CICADA versions")
    parser.add_argument(
        '-v',
        '--CICADAVersion',
        default=1,
        type=int,
        help='Version to pull the ntuplizer from',
        choices=[1,2],
        nargs='?',
    )

    args = parser.parse_args()

    main(args)  