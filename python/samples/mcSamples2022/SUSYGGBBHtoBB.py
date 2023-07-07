# !/usr/bin/env python3
from ..sample import sample
import os

basePath = '/hdfs/store/user/aloelige'

filePaths = [
    f'{basePath}/SUSYGluGluToBBHToBB_NarrowWidth_M-350_TuneCP5_13p6TeV_pythia8/CICADA_2022_SUSYggBBH_05Jul2023/'
]

theFiles = []
for filePath in filePaths:
    for root, dirs, files in os.walk(filePath, topdown = True):
        for name in files:
            theFiles.append(os.path.join(root, name))

treeNames = [
    'CICADAv1ntuplizer/L1TCaloSummaryOutput',
    'CICADAv2ntuplizer/L1TCaloSummaryOutput',    
    'boostedJetTriggerNtuplizer/boostedJetTrigger',
    'L1TTriggerBitsNtuplizer/L1TTriggerBits',
    'uGTModelNtuplizer/uGTModelOutput',     
    'pileupNetworkNtuplizer/pileupTree',      
    'inciSNAILv0p1Ntuplizer/pileupTree',       
    'pileupInformationNtuplizer/pileupInformation',
    'metInformationNtuplizer/metInformation',
    'caloStage2EGammaNtuplizer/L1CaloEgammaInformation',
    'caloStage2JetNtuplizer/L1CaloJetInformation',
    'caloStage2TauNtuplizer/L1CaloTauInformation',
    'caloStage2EtSumNtuplizer/L1CaloEtSumInformation',
    'electronCounter/objectInfo',
    'jetCounter/objectInfo',
    'fatJetCounter/objectInfo',
    'muonCounter/objectInfo',
    'photonCounter/objectInfo',
    'tauCounter/objectInfo',
    'boostedTauCounter/objectInfo',
]

SUSYGGBBHtoBBSample = sample(
    listOfFiles = theFiles,
    treeNames = treeNames
)