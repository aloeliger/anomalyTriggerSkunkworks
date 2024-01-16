from anomalyDetection.anomalyTriggerSkunkworks.samples.sample import sample

theFiles = [
    '/hdfs/store/user/aloeliger/ntuplizedSkims_17_Nov_2023/RunCEZB0.root',
    '/hdfs/store/user/aloeliger/ntuplizedSkims_17_Nov_2023/RunAZB.root',
    '/hdfs/store/user/aloeliger/ntuplizedSkims_17_Nov_2023/RunBZB.root',
    '/hdfs/store/user/aloeliger/ntuplizedSkims_17_Nov_2023/RunCZB.root',
    '/hdfs/store/user/aloeliger/ntuplizedSkims_17_Nov_2023/RunDZB.root',
]

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


ZeroBiasPlusRunCEZBSample = sample(
    listOfFiles=theFiles,
    treeNames=treeNames
)