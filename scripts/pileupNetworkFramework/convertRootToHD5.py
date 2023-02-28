#!/usr/bin/env/python3
import argparse
import ROOT
import h5py
import numpy as np
from tqdm import trange

def createRegionalInput(ecalTPs, hcalTPs):
    
    regionalInput = []
    
    assert(len(ecalTPs) == 18*14), "ECAL is not properly sized"
    assert(len(hcalTPs) == 18*14), "HCAL is not properly sized"

    for i in range(18):
        arrayRow = []
        for j in range(14):
            cellNum = i*14+j
            regionalContent  = [ecalTPs[cellNum]+hcalTPs[cellNum]]
            arrayRow.append(regionalContent)
        regionalInput.append(arrayRow)

    return regionalInput

def main(args):
    #theFile = ROOT.TFile(args.inputFile)
    #theTree = theFile.L1TCaloSummaryTestNtuplizer.L1TCaloSummaryOutput

    print('Creating tree')
    theTree = ROOT.TChain('L1TCaloSummaryTestNtuplizer/L1TCaloSummaryOutput')
    for fileName in args.inputFiles:
        theTree.AddFile(fileName)

    listOfnpv = []
    listOfRegionalTPs = []
    print('Calculating entries to process...')
    entriesToProcess = theTree.GetEntries()
    print(f'Entries to be processed: {entriesToProcess}')
    for entryNum in trange(entriesToProcess):
        theTree.GetEntry(entryNum)
        listOfnpv.append([theTree.npv])
        listOfRegionalTPs.append(
            createRegionalInput(theTree.ecalRegionalTPs, theTree.hcalRegionalTPs)
        )
    npvArray = np.array(listOfnpv)
    regionalTPArray = np.array(listOfRegionalTPs)

    with h5py.File(args.outputFile, 'w') as outFile:
        outFile.create_dataset('TPs', data=regionalTPArray)
        outFile.create_dataset('PU', data=npvArray)
        outFile.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Converts a root file with TP and PU information into a usable hdf5 file for training')

    parser.add_argument(
        '--inputFiles',
        required=True,
        nargs='+',
        help='inputFile to create an hdf5 file out of'
    )
    parser.add_argument(
        '--outputFile',
        default='trainingFile.hdf5',
        nargs='?',
        help='output file to store data in'
    )

    args = parser.parse_args()
    main(args)