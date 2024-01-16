# !/usr/bin/env python3
import ROOT
import argparse
import os
from array import array

from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.RunDEphemeralZeroBias0 import RunDEphemeralZeroBias0Sample # should this be a larger non-training example?

from rich.console import Console
from rich.progress import track

console = Console()

def main(args):
    console.log("Making data/sample histograms...")
    theDataSample = RunDEphemeralZeroBias0Sample.getNewDataframe(
        [
            'pileupInformationNtuplizer/pileupInformation',
        ]
    )
    pileupModel = ROOT.RDF.TH1DModel(
        "PU",
        "PU",
        100,
        0.0,
        100.0,
    )
    dataPUHisto = theDataSample.Histo1D(pileupModel, "npv")
    dataPUHisto = dataPUHisto.GetValue()
    dataPUHisto.Scale(1.0/dataPUHisto.Integral())

    # make a sample dataframe
    sampleDF = ROOT.RDataFrame("pileupInformationNtuplizer/pileupInformation", args.mcFile)
    samplePUHisto = sampleDF.Histo1D(pileupModel, "npv")
    samplePUHisto = samplePUHisto.GetValue()
    samplePUHisto.Scale(1.0/samplePUHisto.Integral())

    console.log("Making weight histogram...")
    
    weightHisto = dataPUHisto.Clone()
    nBins = weightHisto.GetNbinsX()
    # console.print(nBins)
    for binNum in range(1, nBins+1):
        dataPercentage = dataPUHisto.GetBinContent(binNum)
        samplePercentage = samplePUHisto.GetBinContent(binNum)
        try:
            scaleFactor = dataPercentage / samplePercentage
        except ZeroDivisionError:
            scaleFactor = 0.0
        # console.print(f'{binNum:2g}: {dataPercentage:3.1%} {samplePercentage:3.1%} {scaleFactor:3.2e}')
        weightHisto.SetBinContent(binNum, scaleFactor)

    # console.print(weightHisto.Integral())
    # Okay, now we open the file proper
    updateFile = ROOT.TFile(args.mcFile, "UPDATE")
    thePileupTree = updateFile.pileupInformationNtuplizer.pileupInformation

    theDir = updateFile.mkdir("pileupWeightDirectory", "pileupWeightDirectory")
    theDir.cd()
    theTree = ROOT.TTree("pileupWeightTree","pileupWeightTree")
    pileupWeight = array('f', [0.])
    theBranch = theTree.Branch("pileupWeight", pileupWeight, 'pileupWeight/F')

    for entryNum in track(range(thePileupTree.GetEntries()), description="Adding weights..."):
        thePileupTree.GetEntry(entryNum)
        thePU = thePileupTree.npv
        theBinNum = weightHisto.FindBin(thePU)
        pileupWeight[0] = weightHisto.GetBinContent(theBinNum)

        # theBranch.Fill()
        theTree.Fill()
    
    theDir.Write()
    theTree.Write()
    updateFile.Write()
    updateFile.Close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Add pileup weights to MC files')
    parser.add_argument(
        '-m',
        '--mcFile',
        required=True,
        help='MC file to add a reweight tree to',
        nargs='?'
    )

    args = parser.parse_args()

    main(args)
