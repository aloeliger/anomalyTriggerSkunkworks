import argparse
import ROOT
from tqdm import tqdm,trange
from triggers.unPrescaledTriggers import *

def main(args):
    ROOT.gStyle.SetOptStat(0)
    ROOT.gStyle.SetPaintTextFormat('1.2g')
    
    listOfSamples = [
        'SUEP',
        'VBFHTT',
        'HLongLived',
        #'TT': ttSample, #This is sort of too big to do this kind of analysis on.
        'GluGluHH4b_cHHH1',
        'GluGluHH4B_cHHH5',
    ]

    triggerGroups = {
        'CICADA3kHz' : ['CICADA3kHz'],
        'CICADA2kHz' : ['CICADA2kHz'],
        'CICADA1kHz' : ['CICADA1kHz'],
        'CICADA0p5kHz' : ['CICADA0p5kHz'],
        'uGT3kHz' : ['uGT3kHz'],
        'uGT2kHz' : ['uGT2kHz'],
        'uGT1kHz' : ['uGT1kHz'],
        'uGT0p5kHz' : ['uGT0p5kHz'],
        'pureMuonTriggers': pureMuonTriggers,
        'muonPlusEGTriggers': muonPlusEGTriggers,
        'muonPlusJetMETOrHT': muonPlusJetMETOrHT,
        'pureEGTriggers': pureEGTriggers,
        'EGPlusHTOrJet': EGPlusHTOrJet,
        'tauPlusOthers': tauPlusOthers,
        'pureTauTriggers': pureTauTriggers,
        'jetsPlusHTTriggers': jetsPlusHTTriggers,
        'HTETorMETTriggers': HTETorMETTriggers,
    } 

    axisLabels = {
        'CICADA3kHz' : 'CICADA (3 kHz)',
        'CICADA2kHz' : 'CICADA (2 kHz)',
        'CICADA1kHz' : 'CICADA (1 kHz)',
        'CICADA0p5kHz' : 'CICADA (0.5 kHz)',
        'uGT3kHz' : 'uGT AD (3 kHz)',
        'uGT2kHz' : 'uGT AD (2 kHz)',
        'uGT1kHz' : 'uGT AD (1 kHz)',
        'uGT0p5kHz' : 'uGT AD (0.5 kHz)',
        'pureMuonTriggers': 'Pure Muon Triggers (~9 kHz)',
        'muonPlusEGTriggers': 'Muon + EG Triggers (~2.5 kHz)'
        'muonPlusJetMETOrHT': 'Muon+Jet/MET/HT Triggers (~1.5 kHz)',
        'pureEGTriggers': 'Pure EG Triggers (~15 kHz)',
        'EGPlusHTOrJet': 'EG+HT/Jet Triggers (~6 kHz)',
        'tauPlusOthers': 'Tau Plus Other Triggers (5 kHz)',
        'pureTauTriggers': 'Pure Tau Triggers (~7 kHz)',
        'jetsPlusHTTriggers': 'Jets(+HT) Triggers (~4 kHz)',
        'HTETorMETTriggers': 'HT/ET/MET Triggers (~2 kHz)',
    }

    theFile = ROOT.TFile(args.theFile)

    for sample in listOfSamples:
        for i in range(len(triggerGroups.keys())):
            for j in range(i+1, len(triggerGroups.keys())):
                primaryTrigger = list(triggerGroups.keys())[i]
                secondaryTrigger = list(triggerGroups.keys())[j]

                if 'CICADA' in primaryTrigger and 'CICADA' in secondaryTrigger:
                    continue
                if 'uGT' in primaryTrigger and 'uGT' in secondaryTrigger:
                    continue
                
                plotName = f'{primaryTrigger}_{secondaryTrigger}_{sample}'
                theCanvas = ROOT.TCanvas(plotName)
                theCanvas.SetBottomMargin(0.33)

                thePlot = getattr(theFile, plotName)
                
                thePlot.Scale(1.0/thePlot.Integral())

                errorHisto = thePlot.Clone()
                
                thePlot.SetLineColor(ROOT.kRed)
                thePlot.SetLineWidth(2)

                errorHisto.SetFillColor(ROOT.kGray)
                errorHisto.SetFillStyle(3244)
                errorHisto.Draw('E2')
                thePlot.Draw('SAME HIST TEXT0')

                errorHisto.GetYaxis().SetTitle('Fraction')
                errorHisto.SetTitle('')

                cmsLatex = ROOT.TLatex()
                cmsLatex.SetTextSize(0.06)
                cmsLatex.SetNDC(True)
                cmsLatex.SetTextAlign(11)
                cmsLatex.DrawLatex(0.1,0.92, "#font[61]{CMS} #font[52]{Preliminary}")

                sampleLatex  = ROOT.TLatex()
                sampleLatex.SetTextSize(0.06)
                sampleLatex.SetNDC(True)
                sampleLatex.SetTextAlign(31)
                sampleLatex.DrawLatex(0.9,0.92, '#font[41]{'+sample+'}')

                theCanvas.SaveAs(f'{plotName}_individualSignalEfficiencies.png')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Draw a more one-on-one comparison of how we perform versus')

    parser.add_argument('--theFile', default='individualSignalEfficiencyFile.root',nargs='?',help='File to draw plots from')

    args = parser.parse_args()

    main(args)