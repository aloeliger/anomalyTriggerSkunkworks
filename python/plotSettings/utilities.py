def getListOfUniqueEntries(theChain, branchName):
    theList = []
    
    #disable all branches except the ones we *really* need
    theChain.SetBranchStatus("*", 0)
    #reenable runs
    theChain.SetBranchStatus(branchName,1)
    #print('getting unique entries for: %s...' % branchName)
    for i in range(theChain.GetEntries()):
        theChain.GetEntry(i)
        if getattr(theChain, branchName) not in theList:
            theList.append(getattr(theChain, branchName))  

    #reenable everything
    theChain.SetBranchStatus("*", 1)
    return theList

def convertEffToRate(eff, nBunches = 2544):
    return eff * (float(nBunches) * 11425e-3)

def convertRateToEff(rate, nBunches = 2544):
    return rate / (float(nBunches) * 11425e-3)
