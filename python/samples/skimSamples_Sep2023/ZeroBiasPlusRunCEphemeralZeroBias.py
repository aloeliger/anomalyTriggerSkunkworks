from anomalyDetection.anomalyTriggerSkunkworks.samples.sample import sample

theFiles = [
    '/hdfs/store/user/aloeliger/ntuplizedSkims_7_Sep_2023/RunCEphemeralZeroBias0.root',
    '/hdfs/store/user/aloeliger/ntuplizedSkims_7_Sep_2023/ZeroBiasRunA.root',
    '/hdfs/store/user/aloeliger/ntuplizedSkims_7_Sep_2023/ZeroBiasRunB.root',
    '/hdfs/store/user/aloeliger/ntuplizedSkims_7_Sep_2023/ZeroBiasRunC.root',
    '/hdfs/store/user/aloeliger/ntuplizedSkims_7_Sep_2023/ZeroBiasRunD.root',
]

treeNames = [
    'CICADAv1ntuplizer/L1TCaloSummaryOutput',
    'CICADAv2ntuplizer/L1TCaloSummaryOutput',
    'boostedJetTriggerNtuplizer/boostedJetTrigger',
    'uGTModelNtuplizer/uGTModelOutput',
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