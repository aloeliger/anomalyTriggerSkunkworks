# !/usr/bin/env python3

import ROOT
import argparse
from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.largeRunDEphemeralZeroBias import largeRunDEphemeralZeroBiasSample

from rich.console import Console

console = Console()

def main(args):
    objects = {
        'EGamma':{
            'tree':'caloStage2EGammaNtuplizer/L1CaloEgammaInformation',        
        },
        'Jet': {
            'tree':'caloStage2JetNtuplizer/L1CaloJetInformation',
        },
        'Tau':{
            'tree':'caloStage2TauNtuplizer/L1CaloTauInformation',
        },
    }

    if args.CICADAVersion == 1:
        cicadaThresholds = [0.0, 7.0, 10.0, 11.0, 13.0]
    elif args.CICADAVersion == 2:
        cicadaThresholds = [0.0, 7.0, 8.5, 10.5, 14.0]


    outputFile = ROOT.TFile(f'/nfs_scratch/aloeliger/anomalyPlotFiles/rootFiles/unrolledTriggerObjectPlotsCICADAv{args.CICADAVersion}.root', 'RECREATE')
    # We want to unroll in number of objects
    # and by number of object
    for typeOfObject in objects:
        hists = []
        dfs = []
        with console.status(f'{typeOfObject}...'):
            theDataframe = largeRunDEphemeralZeroBiasSample.getNewDataframe(
                [
                    f'CICADAv{args.CICADAVersion}ntuplizer/L1TCaloSummaryOutput',
                    objects[typeOfObject]['tree']
                ]
            )
            for threshold in cicadaThresholds:
                thresholdDF = theDataframe.Filter(f'anomalyScore > {threshold}')
                for nObjects in range(1,13):
                    histoName = f'{typeOfObject}_n{nObjects}_pt_CICADA{int(threshold)}'
                    unrolledModel = ROOT.RDF.TH1DModel(
                        histoName,
                        histoName,
                        60,
                        0.0,
                        120.0
                    )
                    objectFilteredDF = thresholdDF.Filter(f'nObjects == {nObjects}')
                    objectFilteredPlot = objectFilteredDF.Histo1D(unrolledModel, 'ptVector')
                    hists.append(objectFilteredPlot)
                    dfs.append(objectFilteredDF)
                
                # lets also do the shaping plts by the number of the object
                for nthObject in range(1,4):
                    histoName = f'{typeOfObject}_pt_object{nthObject}_CICADA{int(threshold)}'
                    ptHistModel = ROOT.RDF.TH1DModel(
                        histoName,
                        histoName,
                        60, 
                        0.0,
                        120.0
                    )
                    specificObjectPtFunction = """
                    try
                    {"""+f"""
                        return ptVector.at({nthObject});"""+"""
                    }
                    catch (std::out_of_range const& exc)
                    {
                        return -1.0;
                    }
                    """
                    newColumnName = f'object{nthObject}_pt'
                    columnDefinedDF = thresholdDF.Define(newColumnName, specificObjectPtFunction)
                    objectFilteredPlot = columnDefinedDF.Histo1D(ptHistModel, newColumnName)
                    hists.append(objectFilteredPlot)
                    dfs.append(columnDefinedDF)
                dfs.append(thresholdDF)
            dfs.append(theDataframe)
            for hist in hists:
                hist.Write()
        console.log(f'{typeOfObject}', style='green')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="create plots about trigger objects that have been unrolled for certain CICADA thresholds")
    parser.add_argument(
        '-v',
        '--CICADAVersion',
        default=1,
        type=int,
        help='Version to pull the ntuplizer from',
        choices=[1,2],
        nargs='?'
    )

    args = parser.parse_args()

    main(args)