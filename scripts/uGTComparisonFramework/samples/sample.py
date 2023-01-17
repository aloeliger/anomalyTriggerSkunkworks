from ROOT import TChain

class sample():
    def __init__(self, files:list):
        self.chain = TChain('L1TCaloSummaryTestNtuplizer/L1TCaloSummaryOutput')
        self.uGTChain = TChain('uGTModelNtuplizer/uGTModelOutput')
        self.triggerBitsChain = TChain('L1TTriggerBitsNtuplizer/L1TTriggerBits')
        self.boostedJetChain = TChain('boostedJetTriggerNtuplizer/boostedJetTrigger')
        self.upgradeTree = TChain('l1UpgradeEmuTree/L1UpgradeTree')
        self.eventChain = TChain('l1EventTree/L1EventTree')

        allChains = [
            self.chain,
            self.uGTChain,
            self.triggerBitsChain,
            self.boostedJetChain,
            self.upgradeTree,
            self.eventChain
        ]

        for fileName in files:
            for chain in allChains:
                chain.Add(fileName)
        
        self.chain.AddFriend(self.uGTChain)
        self.chain.AddFriend(self.triggerBitsChain)
        self.chain.AddFriend(self.boostedJetChain)
        self.chain.AddFriend(self.upgradeTree)
    
    def GetEntry(self, entryNum: int):
        self.chain.GetEntry(entryNum)
    
    def GetEntries(self) -> int:
        return self.chain.GetEntries()