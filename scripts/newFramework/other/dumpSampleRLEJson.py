import argparse
import ROOT

from rich.console import Console
from rich.traceback import install
from rich.progress import Progress
from rich.live import Live
from rich.tree import Tree

console = Console()
install()

import numpy as np
import json

from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.RunA import RunASample
from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.RunB import RunBSample
from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.RunC import RunCSample
from anomalyDetection.anomalyTriggerSkunkworks.samples.skimSamples_Sep2023.RunD import RunDSample

def getUniqueValues(theDataframe, key: str):
    numpy_runs = theDataframe.AsNumpy([key])[key]
    numpy_runs = np.unique(numpy_runs)
    theList = list(numpy_runs)
    theList = [int(x) for x in theList]
    return theList
    

def main():
    theSamples = [
        RunASample.getNewDataframe(
            [
                'CICADAv1ntuplizer/L1TCaloSummaryOutput',
            ]
        ),
        RunBSample.getNewDataframe(
            [
                'CICADAv1ntuplizer/L1TCaloSummaryOutput',
            ]
        ),
        RunCSample.getNewDataframe(
            [
                'CICADAv1ntuplizer/L1TCaloSummaryOutput',
            ]
        ),
        RunDSample.getNewDataframe(
            [
                'CICADAv1ntuplizer/L1TCaloSummaryOutput',
            ]
        ),
    ]

    console.log("Determining unique runs and lumis...")

    progress = Progress()

    runLumi = {}

    # with Progress() as progress:
    with Live(progress, refresh_per_second=4, console=console) as live:
        sampleTask = progress.add_task('Processing samples', total=len(theSamples))

        for sampleIndex, theSample in enumerate(theSamples):
            uniqueRuns = getUniqueValues(theSample, key='run')
            nUniqueRuns = len(uniqueRuns)
            live.console.log(f'Found {nUniqueRuns} runs...')

            lumiTask = progress.add_task(f'Processing lumis for sample {sampleIndex}...', total=nUniqueRuns)

            for run in uniqueRuns:

                live.console.log(f'Run {run}...')
                runSample = theSample.Filter(f'run == {run}')
                uniqueLumis = getUniqueValues(runSample, key='lumi')

                runLumi[run] = uniqueLumis

                progress.update(lumiTask, advance=1.0)

            progress.update(sampleTask, advance=1.0)

    console.log('Writing to JSON...')
    with open("TrainingRunLumi.json", "w") as theFile:
        json.dump(runLumi, theFile, indent=4)
    console.log('Done!')
    console.print('')




if __name__ == '__main__':
    main()