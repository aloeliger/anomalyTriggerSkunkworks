import argparse
from samples.dataSamples import runASample,runBSample,runCSample,runDSample

from tqdm import trange, tqdm
import math
import ROOT

def main(args):
    ROOT.gStyle.SetOptStat(0)
    #Okay, let's get score plots
    #print(runASample.chain.GetMaximum("anomalyScore"))
    #print(runBSample.chain.GetMaximum("anomalyScore"))
    caloScorePlots = {}
    uGTScorePlots = {}
    runs = {
        'RunA': runASample,
        'RunB': runBSample,
        'RunC': runCSample,
        'RunD': runDSample,
    }

    caloMaxes = []
    caloMins = []
    uGTMaxes = []
    uGTMins = []

    print('Determining maximum and minimum score...')
    for run in tqdm(runs):
        caloMaxes.append(runs[run].chain.GetMaximum('anomalyScore'))
        caloMins.append(runs[run].chain.GetMinimum('anomalyScore'))
        uGTMaxes.append(runs[run].chain.GetMaximum('uGTAnomalyScore'))
        uGTMins.append(runs[run].chain.GetMinimum('uGTAnomalyScore'))

    caloMax = math.ceil(max(caloMaxes))
    caloMin = math.floor(min(caloMins))
    uGTMax = math.ceil(max(uGTMaxes))
    uGTMin = math.floor(min(uGTMins))

    #caloMax = 10.0
    #caloMin = 0.0
    #uGTMax = 200
    #uGTMin = 0.0

    print('Looping over runs...')
    for runName in tqdm(runs):
        runSample = runs[runName]
        caloScorePlots[runName] = ROOT.TH1F(
            f'{runName}CaloScores',
            f'{runName}CaloScores',
            100,
            caloMin,
            caloMax,
        )
        uGTScorePlots[runName] = ROOT.TH1F(
            f'{runName}uGTScores',
            f'{runName}uGTScores',
            100,
            uGTMin,
            uGTMax,
        )

        #entriesToProcess = int(min(runSample.GetEntries(), 5e5))

        # for i in trange(entriesToProcess):
        #     runSample.GetEntry(i)
        #     caloScorePlots[runName].Fill(runSample.chain.anomalyScore)
        #     uGTScorePlots[runName].Fill(runSample.chain.uGTAnomalyScore)
        runSample.chain.Draw(f'anomalyScore>>{runName}CaloScores')
        runSample.chain.Draw(f'uGTAnomalyScore>>{runName}uGTScores')
        caloScorePlots[runName].Scale(1.0/caloScorePlots[runName].Integral())
        uGTScorePlots[runName].Scale(1.0/uGTScorePlots[runName].Integral())
    
    outputFile = ROOT.TFile(args.theFile, 'RECREATE')
    for name in caloScorePlots:
        caloScorePlots[name].Write()
    for name in uGTScorePlots:
        uGTScorePlots[name].Write()
    outputFile.Write()
    outputFile.Close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compare the stability of scores between the uGT and CICADA')

    parser.add_argument('--theFile', default='stabilityFile.root', nargs='?',help='Output plot file')

    args = parser.parse_args()

    main(args)