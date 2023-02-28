import argparse
from tensorflow import keras
import numpy as np
from tqdm import tqdm,trange
from array import array
import ROOT

from convertRootToHD5 import createRegionalInput

def main(args):
    theModel = keras.models.load_model(args.modelFile)

    for fileName in tqdm(args.files):
        theFile = ROOT.TFile(fileName, 'UPDATE')
        caloTree = theFile.L1TCaloSummaryTestNtuplizer.L1TCaloSummaryOutput
        NNOutputTree = ROOT.TTree('pileupNetworkOutput','pileupNetworkOutput')
        NNOutput = array('f', [0.])
        NNOutputTree.Branch('pileupPrediction',NNOutput,'pileupPrediction/F')
        for i in trange(caloTree.GetEntries(), leave=False):
            caloTree.GetEntry(i)

            inputList = createRegionalInput(caloTree.ecalRegionalTPs, caloTree.hcalRegionalTPs)
            inputArray = np.array([inputList])

            theOutputArray = theModel.predict(inputArray)

            NNOutput[0] = theOutputArray[0][0]

            NNOutputTree.Fill()

        caloTree.Write()
        theFile.Write()
        theFile.Close()

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description='apply pileup model to root files')
    
    
    parser.add_argument(
        '--files',
        nargs='+',
        required=True,
        help=''
    ) 

    parser.add_argument(
        '--modelFile',
        nargs='?',
        default='pileupModel.hdf5',
        help='Model to load and apply'
    )

    args=parser.parse_args()
    main(args)