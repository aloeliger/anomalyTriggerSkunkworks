import ROOT
import argparse
from samples.dataSamples import runASample,runBSample,runCSample,runDSample
import json
from tqdm import tqdm
import math
from L1Trigger.anomalyTriggerSkunkworks.utilities.decorators import *

@debug_function
def getThresholdForRate(ratePlot, rate):
    nBins = ratePlot.GetNbinsX()
    theBin = 0
    actualRate = 0.0
    for i in range(1,nBins+1):
        if ratePlot.GetBinContent(i) <= rate:
            theBin = i
            actualRate = ratePlot.GetBinContent(i)
            break
    threshold = ratePlot.GetXaxis().GetBinLowEdge(theBin)

    return threshold

def convertEffToRate(eff):
    return eff * (2544.0 * 11425e-3)

def createRatePlot(scorePlot):
    integralPlot = scorePlot.Clone()
    integralPlot.Scale(1.0/integralPlot.Integral())

    nBins = scorePlot.GetNbinsX()
    
    ratePlot = ROOT.TH1F(
        scorePlot.GetName()+'Rate',
        scorePlot.GetTitle()+'Rate',
        nBins,
        scorePlot.GetXaxis().GetXmin(),
        scorePlot.GetXaxis().GetXmax(),
    )

    for i in range(1,nBins+1):
        ratePlot.SetBinContent(i, convertEffToRate(integralPlot.Integral(i, nBins)))

    return ratePlot

def main(args):
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
        caloMaxes.append(min(runs[run].chain.GetMaximum('anomalyScore'), 60))
        caloMins.append(runs[run].chain.GetMinimum('anomalyScore'))
        uGTMaxes.append(runs[run].chain.GetMaximum('uGTAnomalyScore'))
        uGTMins.append(runs[run].chain.GetMinimum('uGTAnomalyScore'))

    caloMax = math.ceil(max(caloMaxes))
    caloMin = math.floor(min(caloMins))
    uGTMax = math.ceil(max(uGTMaxes))
    uGTMin = math.floor(min(uGTMins))
    
    caloPlot = ROOT.TH1F(
        'caloPlot',
        'caloPlot',
        args.binGranularity,
        caloMin,
        caloMax
    )
    uGTPlot = ROOT.TH1F(
        'uGTPlot',
        'uGTPlot',
        args.binGranularity,
        uGTMin,
        uGTMax,
    )

    print('creating plots...')
    for runName in tqdm(runs):
        runSample = runs[runName]

        runSample.chain.Draw(f'anomalyScore>>{runName}CaloScore({args.binGranularity},{caloMin},{caloMax})')
        tempCaloPlot = ROOT.gPad.GetPrimitive(f'{runName}CaloScore').Clone()
        runSample.chain.Draw(f'uGTAnomalyScore>>{runName}uGTScore({args.binGranularity},{uGTMin},{uGTMax})')
        tempuGTPlot = ROOT.gPad.GetPrimitive(f'{runName}uGTScore').Clone()

        #ROOT.gPad.ls()
        #print(f'{runName}CaloScore')
    
        caloPlot.Add(tempCaloPlot)
        uGTPlot.Add(tempuGTPlot)
    
    caloPlot = createRatePlot(caloPlot)
    uGTPlot = createRatePlot(uGTPlot)

    plotDict = {
        'CICADA': caloPlot,
        'uGT': uGTPlot,
    }

    with open(args.jsonFile, 'r') as jsonFile:
        data = json.load(jsonFile)

    thresholds = {}    
    for trigger in plotDict:
        thresholds[trigger] = {}
        for rate in data['rates']:
            thresholds[trigger][rate] = getThresholdForRate(plotDict[trigger],rate)

    data['thresholds'] = thresholds

    with open(args.jsonFile, 'w') as jsonFile:
        json.dump(data, jsonFile, indent=4)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create threshold values for a series of predefined desired rates')

    parser.add_argument('--jsonFile', default='./anomalyTriggerThresholds/triggerThresholds.json', help='Place to read desired rate thresholds from, and write them to.')
    parser.add_argument('--binGranularity', type=int, default=500, help='Number of bins to use in the integration')

    args = parser.parse_args()

    main(args)