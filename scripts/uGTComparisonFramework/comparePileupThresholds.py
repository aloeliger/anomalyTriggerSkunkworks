import argparse
from samples.pileupSamples import pileupSample
from tqdm import trange
import ROOT
from anomalyTriggerThresholds.thresholdHelper import thresholdHelper
import math

def main(args):
    ROOT.gStyle.SetOptStat(0)

    print('Determining Minimum and maximum')
    caloMax = pileupSample.chain.GetMaximum('precompiledModelAnomalyScore')
    caloMin = pileupSample.chain.GetMinimum('precompiledModelAnomalyScore')
    uGTMax = pileupSample.chain.GetMaximum('uGTAnomalyScore')
    uGTMin = pileupSample.chain.GetMinimum('uGTAnomalyScore')

    maxPU = 120.0
    minPU = 0.0
    PUperBin = 5.0
    puBins = math.ceil((maxPU-minPU)/PUperBin)
    
    histos = []

    for i in trange(puBins):
        caloName = f'CaloScore_PU_{i*5}_{(i+1)*5}'
        uGTName = f'uGTScore_PU_{i*5}_{(i+1)*5}'
        caloScorePlot = ROOT.TH1F(
            caloName,
            caloName,
            100,
            caloMin,
            caloMax,
        )
        uGTScorePlot = ROOT.TH1F(
            uGTName,
            uGTName,
            100,
            uGTMin,
            uGTMax
        )

        pileupExpression = f'npv >= {i*5} && npv < {(i+1)*5}'

        pileupSample.chain.Draw(f'precompiledModelAnomalyScore>>{caloName}',pileupExpression)
        pileupSample.chain.Draw(f'uGTAnomalyScore>>{uGTName}',pileupExpression)
        caloScorePlot.Scale(1.0/caloScorePlot.Integral())
        uGTScorePlot.Scale(1.0/caloScorePlot.Integral())

        histos.append(caloScorePlot)/ZeroBias/Run2018D-v1/RAW
        histos.append(uGTScorePlot)
    
    outputFile = ROOT.TFile(args.theFile, 'RECREATE')
    for histo in histos:
        histo.Write()
    outputFile.Write()
    outputFile.Close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get pileup threshold information')

    parser.add_argument(
        '--theFile',
        default='pileupThresholds.root',
        nargs='?',
        help='Output plot file'
    )

    args = parser.parse_args()
    main(args)