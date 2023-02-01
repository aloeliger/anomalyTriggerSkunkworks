#an equivalent of the HighEffSinglRunL1TriggerBitPlot from the scripts before
#Should be alternately usable in a multiprocessing, or subprocess style set-up
#Because this can take a pretty long amount of time, 
#and we would like to leverage as many CPUs to the task as possible.

#We can also probably do ourselves some favors in regards to how the calls to the 
#get entries or the draw are done

import argparse
from samples.ephemeralZeroBiasSamples import ephemeralZeroBiasSample
from tqdm import trange
import ROOT
import time
from anomalyTriggerThresholds.thresholdHelper import thresholdHelper

def getRunLumiDict(theSample, numberOfEvents):
    runLumiDict = {}

    theSample.chain.SetBranchStatus('*', 0)
    theSample.chain.SetBranchStatus('run', 1)
    theSample.chain.SetBranchStatus('lumi', 1)

    for i in trange(numberOfEvents, desc='Run-Lumi pairs...'):
        theSample.GetEntry(i)
        if theSample.chain.run not in runLumiDict:
            runLumiDict[theSample.chain.run] = []
        if theSample.chain.lumi not in runLumiDict[theSample.chain.run]:
            runLumiDict[theSample.chain.run].append(theSample.chain.lumi)
    
    theSample.chain.SetBranchStatus('*', 1)

    return runLumiDict

def main(args):
    ROOT.gStyle.SetOptStat(0)

    theThresholdHelper = thresholdHelper()
    triggers = {
        
    }

    print('Getting number of entries...')
    startTime = time.perf_counter()
    chainEvents = ephemeralZeroBiasSample.GetEntries()
    endTime = time.perf_counter()
    print(f'Found {chainEvents} entries in {endTime-startTime:.2f} seconds')

    print('Creating the dictionary of run-lumi pairs...')
    runLumiDict = getRunLumiDict(ephemeralZeroBiasSample, chainEvents)
    print('Done!')

    print('Creating the list of plots...')
    plotDict = {}
    for trigger in triggers:
        plotDict[trigger] = {}
        for run in runLumiDict:
            nBins = max(runLumiDict[run])-min(runLumiDict[run])+1
            plotDict[trigger][run] = ROOT.TH1F(
                f'{trigger}_{run}',
                f'{trigger}_{run}',
                nBins,
                min(runLumiDict[run]),
                max(runLumiDict[run])+1.0,
            )
    totalsDict = {}
    for run in runLumiDict:
        nBins = max(runLumiDict[run])-min(runLumiDict[run])+1
        totalsDict[run] = ROOT.TH1F(
            f'Total_{run}',
            f'Total_{run}',
            nBins,
            min(runLumiDict[run]),
            max(runLumiDict[run])+1.0,
        )
    print('Done!')

    #We need a list of the unique lumi-sections in this run
    print('Making plots')
    for i in trange(chainEvents):
        ephemeralZeroBiasSample.GetEntry(i)

        theRun = ephemeralZeroBiasSample.chain.run
        theLumi = ephemeralZeroBiasSample.chain.lumi

        totalsDict[theRun].Fill(theLumi)

        for trigger in triggers:
            triggerTuple = triggers[trigger]

            if getattr(ephemeralZeroBiasSample.chain, triggerTuple[0]) > float(triggerTuple[1]):
                plotDict[trigger][theRun].Fill(theLumi)
  
    print('Writing out the plots...')
    theFile = ROOT.TFile(args.theFile, 'RECREATE')
    for trigger in plotDict:
        for run in plotDict[trigger]:
            plotDict[trigger][run].Write()
    for run in totalsDict:
        totalsDict[run].Write()
    theFile.Write()
    theFile.Close()
    print('Done!')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='get basic lumi section score plots')

    parser.add_argument(
        '--theFile',
        default='lumiScoreFile.root',
        nargs='?',
        help='Output plot file'
    )
    parser.add_argument(
        '--pure',
        action='store_true',
        help='draw pure rate plots or not'
    )

    args = parser.parse_args()
    main(args)