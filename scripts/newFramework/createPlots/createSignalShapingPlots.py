# !/usr/bin/env python3

import ROOT
import argparse
import os

from rich.console import Console
from rich.traceback import install

from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.Hto2LongLivedTo4b import Hto2LongLivedTo4bSample
from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.SUSYGluGlutoBBHtoBB import SUSYGluGlutoBBHtoBBSample
from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.TT import TTSample
from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.VBFHto2C import VBFHto2CSample
from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.SUEP import SUEPSample

from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.largeRunDEphemeralZeroBias import largeRunDEphemeralZeroBiasSample


install()
console = Console()

def getVectorPropertyFunction(branchName, entry):
    theString = """
    try
    {"""+f"""
        return {branchName}.at({entry});"""+"""
    }
    catch (std::out_of_range const& exc)
    {
        return -1.0;
    }
    """
    return theString

def createHTo2LongLivedTo4bPlots(hDataframe, cicadaThresholds):
    hists = []
    hDataframe = hDataframe.Define('leadingJetPt', getVectorPropertyFunction("ptVector", 0))
    hDataframe = hDataframe.Define('leadingJetEta', getVectorPropertyFunction("etaVector", 0))
    hDataframe = hDataframe.Define('leadingJetPhi', getVectorPropertyFunction("phiVector", 0))
    hDataframe = hDataframe.Define('leadingJetMass', getVectorPropertyFunction("massVector", 0))

    hDataframe = hDataframe.Define('subleadingJetPt', getVectorPropertyFunction("ptVector", 1))
    hDataframe = hDataframe.Define('subleadingJetEta', getVectorPropertyFunction("etaVector", 1))
    hDataframe = hDataframe.Define('subleadingJetPhi', getVectorPropertyFunction("phiVector", 1))
    hDataframe = hDataframe.Define('subleadingJetMass', getVectorPropertyFunction("massVector", 1))

    hDataframe = hDataframe.Define('thirdLeadingJetPt', getVectorPropertyFunction("ptVector", 2))
    hDataframe = hDataframe.Define('thirdLeadingJetEta', getVectorPropertyFunction("etaVector", 2))
    hDataframe = hDataframe.Define('thirdLeadingJetPhi', getVectorPropertyFunction("phiVector", 2))
    hDataframe = hDataframe.Define('thirdLeadingJetMass', getVectorPropertyFunction("massVector", 2))

    hDataframe = hDataframe.Define('fourthLeadingJetPt', getVectorPropertyFunction("ptVector", 4))
    hDataframe = hDataframe.Define('fourthLeadingJetEta', getVectorPropertyFunction("etaVector", 4))
    hDataframe = hDataframe.Define('fourthLeadingJetPhi', getVectorPropertyFunction("phiVector", 4))
    hDataframe = hDataframe.Define('fourthLeadingJetMass', getVectorPropertyFunction("massVector", 4))

    invariantMassFunction = """
    if (nObjects >= 4) {
        TLorentzVector firstVector;
        firstVector.SetPtEtaPhiM(leadingJetPt, leadingJetEta, leadingJetPhi, leadingJetMass);

        TLorentzVector secondVector;
        secondVector.SetPtEtaPhiM(subleadingJetPt, subleadingJetEta, subleadingJetPhi, subleadingJetMass);

        TLorentzVector thirdVector;
        thirdVector.SetPtEtaPhiM(thirdLeadingJetPt, thirdLeadingJetEta, thirdLeadingJetPhi, thirdLeadingJetMass);

        TLorentzVector fourthVector;
        fourthVector.SetPtEtaPhiM(fourthLeadingJetPt, fourthLeadingJetEta, fourthLeadingJetPhi, fourthLeadingJetMass);

        return (firstVector + secondVector + thirdVector + fourthVector).M();
    }
    else
        return -1.0;
    """
    hDataframe = hDataframe.Define('invariantMass', invariantMassFunction)

    for threshold in cicadaThresholds:
        thresholdFrame = hDataframe.Filter(f'anomalyScore > {threshold}')
        hists.append(
            thresholdFrame.Histo1D(
                (f'Hto2LongLivedTo4b_invariantMass_CICADA{int(threshold)}', f'Hto2LongLivedTo4b_invariantMass_CICADA{int(threshold)}', 50, 0.0, 1000.0),
                'invariantMass'
            )
        )
        hists.append(
            thresholdFrame.Histo1D(
                (f'Hto2LongLivedTo4b_leadingJetPt_CICADA{int(threshold)}',f'Hto2LongLivedTo4b_leadingJetPt_CICADA{int(threshold)}', 50, 0.0, 300.0),
                'leadingJetPt'
            )
        )
    return hists

def createTwoJetPlots(sDataframe, cicadaThresholds, label):
    hists = []
    sDataframe = sDataframe.Define('leadingJetPt', getVectorPropertyFunction("ptVector", 0))
    sDataframe = sDataframe.Define('leadingJetEta', getVectorPropertyFunction("etaVector", 0))
    sDataframe = sDataframe.Define('leadingJetPhi', getVectorPropertyFunction("phiVector", 0))
    sDataframe = sDataframe.Define('leadingJetMass', getVectorPropertyFunction("massVector", 0))

    sDataframe = sDataframe.Define('subleadingJetPt', getVectorPropertyFunction("ptVector", 1))
    sDataframe = sDataframe.Define('subleadingJetEta', getVectorPropertyFunction("etaVector", 1))
    sDataframe = sDataframe.Define('subleadingJetPhi', getVectorPropertyFunction("phiVector", 1))
    sDataframe = sDataframe.Define('subleadingJetMass', getVectorPropertyFunction("massVector", 1))

    invariantMassFunction = """
    if (nObjects >= 2) {
        TLorentzVector firstVector;
        firstVector.SetPtEtaPhiM(leadingJetPt, leadingJetEta, leadingJetPhi, leadingJetMass);

        TLorentzVector secondVector;
        secondVector.SetPtEtaPhiM(subleadingJetPt, subleadingJetEta, subleadingJetPhi, subleadingJetMass);

        return (firstVector + secondVector).M();
    }
    else
        return -1.0;
    """
    sDataframe = sDataframe.Define('invariantMass', invariantMassFunction)

    for threshold in cicadaThresholds:
        thresholdFrame = sDataframe.Filter(f'anomalyScore > {threshold}')
        hists.append(
            thresholdFrame.Histo1D(
                (f'{label}_invariantMass_CICADA{int(threshold)}', f'{label}_invariantMass_CICADA{int(threshold)}', 50, 0.0, 1000.0),
                'invariantMass'
            )
        )
        hists.append(
            thresholdFrame.Histo1D(
                (f'{label}_leadingJetPt_CICADA{int(threshold)}', f'{label}_leadingJetPt_CICADA{int(threshold)}', 50, 0.0, 300.0),
                'leadingJetPt'
            )
        )
    return hists

def main(args):
    console.log('Forming relevant dataframes/histograms...')
    hists = []
    if args.CICADAVersion == 1:
        cicadaThresholds = [0.0, 7.0, 10.0, 11.0, 13.0]
    elif args.CICADAVersion == 2:
        cicadaThresholds = [0.0, 7.0, 8.5, 10.5, 14.0]
    outputFile = ROOT.TFile(f'/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/CICADASignalShapingCICADAv{args.CICADAVersion}.root', 'RECREATE')    
    # Let's start with H to 2 long lived to 4 b.
    # We want to demonstrate we can get something resembling a higgs peak from it,
    # Let's start with dataframes
    hDataframe = Hto2LongLivedTo4bSample.getNewDataframe(
        [
            f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
            'jetCounter/objectInfo',
        ]
    )
    hists += createHTo2LongLivedTo4bPlots(hDataframe, cicadaThresholds)

    # Let's take a look at the SUSY signal
    sDataframe = SUSYGluGlutoBBHtoBBSample.getNewDataframe(
        [
            f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
            'jetCounter/objectInfo',
        ]
    )

    hists += createTwoJetPlots(sDataframe, cicadaThresholds, label="SUSYGluGlutoBBHtoBB")

    zeroBiasDataframe = largeRunDEphemeralZeroBiasSample.getNewDataframe(
         [
            f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
            'jetCounter/objectInfo',
        ]       
    )
    hists += createTwoJetPlots(zeroBiasDataframe, cicadaThresholds, label="ZeroBias")

    console.log("Finalized histograms")
    with console.status("Writing stuff..."):
        for hist in hists:
            hist.Write()
        outputFile.Write()
        outputFile.Close()
    console.log("Done!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Look at the cicada effect of shaping plots")
    parser.add_argument(
        '-v',
        '--CICADAVersion',
        default=1,
        type=int,
        help='CICADA version to pull out of the ntuplizer',
        choices = [1,2],
        nargs='?',
    )

    args = parser.parse_args()

    main(args)