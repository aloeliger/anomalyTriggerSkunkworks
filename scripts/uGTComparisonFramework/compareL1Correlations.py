import argparse

from samples.dataSamples import runASample,runBSample,runCSample,runDSample

from tqdm import tqdm
import ROOT

def main(args):
    ROOT.gStyle.SetOptStat(0)

    #We have to spell out which L1 variables we want because there are non 1:1 collections in the tree
    variablesToCompare = {
        'nEGs' : 'nEGs',
        'egEt[0]' : 'leading_egEt',
        'egEta[0]' : 'leading_egEta',
        'egIso[0]' : 'leading_egIso',
        'nTaus' : 'nTaus',
        'tauEt[0]' : 'leading_tauEt',
        'tauEta[0]' : 'leading_tauEta',
        'tauIso[0]' : 'leading_tauIso',
        'nJets' : 'nJets',
        'jetEt[0]' : 'leading_jetEt',
        'jetEta[0]' : 'leading_jetEta',
        'nMuons' : 'nMuons',
        'muonEt[0]' : 'leading_muonEt',
        'muonEta[0]' : 'leading_muonEta',
        'muonIso[0]' : 'leading_muonIso',
    }

    limits = {
        'nEGs' : (13, 0.0, 13.0),
        'egEt[0]' : (100, 0.0, 100.0),
        'egEta[0]' : (100, -2.4, 2.4),
        'egIso[0]' : (100, 0.0, 10.0),
        'nTaus' : (13, 0.0, 13.0),
        'tauEt[0]' : (100, 0.0, 100.0),
        'tauEta[0]' : (100, -2.4, 2.4),
        'tauIso[0]' : (100, 0.0, 10.0),
        'nJets' : (13, 0.0, 13.0),
        'jetEt[0]' : (100, 0.0, 100.0),
        'jetEta[0]' : (100, -2.4, 2.4),
        'nMuons' : (13, 0.0, 13.0),
        'muonEt[0]' : (100, 0.0, 100.0),
        'muonEta[0]' : (100, -2.4, 2.4),
        'muonIso[0]' : (100, 0.0, 10.0),     
    }

    samples = {
        'RunA': runASample,
        'RunB': runBSample,
        'RunC': runCSample,
        'RunD': runDSample,
    }

    triggerVariables = {
        'CICADA': 'anomalyScore',
        'uGT': 'uGTAnomalyScore',
    }

    uGTCorrelationPlots = []
    CICADACorrelationPlots = []

    theCanvas = ROOT.TCanvas('default', 'default')

    for var in tqdm(variablesToCompare, desc='L1 variables'):
        tempCICADAPlots = []
        tempuGTPlots = []
        for sample in tqdm(samples, desc='Data samples', leave=False):
            sampleChain = samples[sample]
            for trigger in triggerVariables:
                if trigger == 'CICADA':
                    triggerLimits = (50, 0.0, 7.0)
                elif trigger == 'uGT':
                    triggerLimits = (50, 0.0, 1000.0)
                plotName = f'{trigger}_{variablesToCompare[var]}_{sample}'
                drawString = f'{triggerVariables[trigger]}:{var}>>{plotName}({limits[var][0]},{limits[var][1]},{limits[var][2]},{triggerLimits[0]},{triggerLimits[1]},{triggerLimits[2]})'
                #print(f'Draw string: {drawString}')
                sampleChain.chain.Draw(drawString)
                thePlot = ROOT.gPad.GetPrimitive(plotName).Clone()
                #print(thePlot.GetNbinsX())
                #print(thePlot.GetXaxis().GetXmax())
                #print(thePlot.GetXaxis().GetXmin())
                if trigger == 'CICADA':
                    tempCICADAPlots.append(thePlot.Clone())
                elif trigger == 'uGT':
                    tempuGTPlots.append(thePlot.Clone())
        CICADAPlot = tempCICADAPlots[0].Clone()
        uGTPlot = tempuGTPlots[0].Clone()
        for i in range(1,4):
            CICADAPlot.Add(tempCICADAPlots[i])
            uGTPlot.Add(tempuGTPlots[i])
        uGTCorrelationPlots.append(uGTPlot.Clone())
        CICADACorrelationPlots.append(CICADAPlot.Clone())
    outputFile = ROOT.TFile(args.theFile, 'RECREATE')
    for plot in CICADACorrelationPlots:
        plot.Write()
    for plot in uGTCorrelationPlots:
        plot.Write()
    outputFile.Write()
    outputFile.Close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Compare the correlation of the anomaly scores')

    parser.add_argument('--theFile', default='l1correlationFile.root', help='Output plot file')

    args = parser.parse_args()

    main(args)