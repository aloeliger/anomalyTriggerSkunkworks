from anomalyDetection.anomalyTriggerSkunkworks.samples.sample import sample
import os

filePaths = [
    '/hdfs/store/user/aloelige/ZeroBias/CICADASkimNtuplization_2023RunB_ZB_17Nov2023/',
    '/hdfs/store/user/aloelige/ZeroBias/CICADASkimNtuplization_2023RunC_ZB_17Nov2023/',
    '/hdfs/store/user/aloelige/ZeroBias/CICADASkimNtuplization_2023RunD_ZB_17Nov2023/',
    # '/hdfs/store/user/aloelige/EphemeralZeroBias1/CICADASkimNtuplization_2023RunD_EZB1_25Nov2023/',
    # '/hdfs/store/user/aloelige/EphemeralZeroBias2/CICADASkimNtuplization_2023RunD_EZB2_25Nov2023/',
]

theFiles = []
for filePath in filePaths:
    for root, dirs, files in os.walk(filePath, topdown=True):
        for name in files:
            theFiles.append(os.path.join(root, name))

treeNames = [
    'CICADAv1ntuplizer/L1TCaloSummaryOutput',
    'CICADAv2ntuplizer/L1TCaloSummaryOutput',
    'boostedJetTriggerNtuplizer/boostedJetTrigger',
    'L1TTriggerBitsNtuplizer/L1TTriggerBits',
    'uGTModelNtuplizer/uGTModelOutput',
    'pileupInformationNtuplizer/pileupInformation',
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

allZeroBiasSample = sample(
    listOfFiles = theFiles,
    treeNames = treeNames,
)