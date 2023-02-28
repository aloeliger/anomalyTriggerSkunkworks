import argparse
import subprocess

def main(args):
    initialScoreCommands = [
        ['python3','compareStability.py']
        ['python3','testRateThresholds.py']
    ]

    firstProcs = [subprocess.Popen(command,shell=True,check=True) for command in initialScoreCommands]

    for p in firstProcs:
        p.wait()

    compareCommands = [
        ['python3', 'compareSignalEfficiencies.py'],
        ['python3', 'comparePurity.py'],
        ['python3', 'compareIndividualTriggerPurity.py'],
        ['python3', 'compareIndividualSignalEfficiencies.py']
    ]

    compareProcs = [subprocess.Popen(command, shell=True, check=True) for command in compareCommands]

    for p in compareProcs:
        p.wait()

    drawCommands = [
        ['python3', 'drawFrequencyStability.py'],
        ['python3', 'drawIndividualSignalEfficiencyOverlaps.py'],
        ['python3', 'drawPurityComparison.py'],
        ['python3', 'drawSignalEfficiency.py'],
        ['python3', 'drawStabilityComparison.py']
    ]

    drawProcs = [subprocess.Popen(command, shell=True, check=True) for command in drawCommands]

    for p in drawProcs:
        p.wait()
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Rerun the scripts in this repository')

    args = parser.parse_args()

    main(args)