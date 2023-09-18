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

def convertEffToRate(eff):
    return eff * (2544.0 * 11425e-3)

def convertRateToEff(rate):
    return rate / (2544.0 * 11425e-3)