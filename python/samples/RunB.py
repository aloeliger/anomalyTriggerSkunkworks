#!/usr/bin/env python3
from .sample import sample
import os

basePath = '/hdfs/store/user/aloelige'

filePaths = [
    f'{basePath}/ZeroBias/CICADA_RunB_ZB_20Jun2023/'
]

theFiles = []
for filePath in filePaths:
    for root, dirs, files in os.walk(filePath, topdown = True):
        for name in files:
            theFiles.append(os.path.join(root, name))

treeNames = [
  'CICADAv1ntuplizer/L1TCaloSummaryOutput',
  'CICADAv2ntuplizer/L1TCaloSummaryOutput',
  'CICADAInputNetworkAnalyzerv1p0/CICADAInputNetworkTree',
  'CICADAv1FromCINv1Analyzer/CICADAPlusCIN',
  'CICADAv2FromCINv1Analyzer/CICADAPlusCIN',
  'miniCICADAAnalyzer/miniCICADAScoreTree',
  'miniCICADAAnalyzerCICADAv1/miniCICADAScoreTree',
  'miniCICADAv1p1AnalyzerCICADAv1/miniCICADAScoreTree',
  'miniCICADAv1p1AnalyzerCICADAv2/miniCICADAScoreTree',
  'chargedHadronPFcandidateAnalyzer/chargedHadronPFcands',
  'neutralHadronPFcandidateAnalyzer/neutralHadronPFcands',
  'muonPFcandidateAnalyzer/muonPFcands',
  'electronPFcandidateAnalyzer/electronPFcands',
  'gammaPFcandidateAnalyzer/gammaPFcands',
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

RunBSample = sample(
    listOfFiles=theFiles,
    # listOfFiles=theFiles[:10],
    treeNames=treeNames
)