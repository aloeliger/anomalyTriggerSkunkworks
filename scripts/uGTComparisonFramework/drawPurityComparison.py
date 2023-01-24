import argparse
import ROOT
from tqdm import tqdm
from triggers.unPrescaledTriggers import *

def main(args):
    ROOT.gStyle.SetOptStat(0)
    theFile = ROOT.TFile(args.theFile)

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
        'pureMuonTriggers': 'Pure Muon Triggers',
        'muonPlusEGTriggers': 'Muon+EG Triggers',
        'muonPlusJetMETOrHT': 'Muon+Jet/MET/HT Triggers',
        'pureEGTriggers': 'Pure EG Triggers',
        'EGPlusHTOrJet': 'EG+HT/Jet Triggers',
        'tauPlusOthers': 'Tau Plus Other Triggers',
        'pureTauTriggers': 'Pure Tau Triggers',
        'jetsPlusHTTriggers': 'Jets(+HT) Triggers',
        'HTETorMETTriggers': 'HT/ET/MET Triggers',
    }

    ROOT.gStyle.SetPaintTextFormat('1.2g')

    for triggerGroup in tqdm(triggerGroups):
        theCanvas = ROOT.TCanvas(f'{triggerGroup}',f'{triggerGroup}')
        theCanvas.SetBottomMargin(0.33)
        theCanvas.SetGridx()
        theCanvas.SetGridy()
        theCanvas.SetLogy()

        thePlot = getattr(theFile, f'{triggerGroup}')

        errHisto = thePlot.Clone()

        #thePlot.SetMaximum(1.2)
        #thePlot.SetMinimum(0.0)

        thePlot.SetLineColor(ROOT.kRed)
        thePlot.SetLineWidth(2)

        errHisto.SetFillColor(ROOT.kGray)
        errHisto.SetFillStyle(3244)
        errHisto.Draw('E2')
        thePlot.Draw('SAME HIST TEXT0')

        errHisto.GetYaxis().SetTitle('Fraction')
        errHisto.LabelsOption('v','x')
        errHisto.SetTitle('')

        cmsLatex = ROOT.TLatex()
        cmsLatex.SetTextSize(0.06)
        cmsLatex.SetNDC(True)
        cmsLatex.SetTextAlign(11)
        cmsLatex.DrawLatex(0.1,0.92, "#font[61]{CMS} #font[52]{Preliminary}")

        triggerGroupLatex = ROOT.TLatex()
        triggerGroupLatex.SetTextSize(0.06)
        triggerGroupLatex.SetNDC(True)
        triggerGroupLatex.SetTextAlign(31)
        triggerGroupLatex.DrawLatex(0.9,0.92, '#font[41]{'+axisLabels[triggerGroup]+'}')

        theCanvas.SaveAs(f'{triggerGroup}_overlap.png')
    #Also draw the 'any' overlap plot
    theCanvas = ROOT.TCanvas('anyOverlap','anyOverlap')
    theCanvas.SetBottomMargin(0.33)
    theCanvas.SetGridx()
    theCanvas.SetGridy()
    theCanvas.SetLogy()

    anyOverlapPlot = theFile.anyOverlap
    overlapErrPlot = anyOverlapPlot.Clone()
    
    #anyOverlapPlot.SetMaximum(1.2)
    #anyOverlapPlot.SetMinimum(0.0)

    anyOverlapPlot.SetLineColor(ROOT.kRed)
    anyOverlapPlot.SetLineWidth(2)

    overlapErrPlot.SetFillColor(ROOT.kGray)
    overlapErrPlot.SetFillStyle(3244)
    overlapErrPlot.Draw('E2')
    anyOverlapPlot.Draw('SAME HIST TEXT0')

    overlapErrPlot.GetYaxis().SetTitle('Fraction')
    overlapErrPlot.LabelsOption('v', 'x')
    overlapErrPlot.SetTitle('')

    cmsLatex = ROOT.TLatex()
    cmsLatex.SetTextSize(0.06)
    cmsLatex.SetNDC(True)
    cmsLatex.SetTextAlign(11)
    cmsLatex.DrawLatex(0.1,0.92, "#font[61]{CMS} #font[52]{Preliminary}")

    triggerGroupLatex = ROOT.TLatex()
    triggerGroupLatex.SetTextSize(0.06)
    triggerGroupLatex.SetNDC(True)
    triggerGroupLatex.SetTextAlign(31)
    triggerGroupLatex.DrawLatex(0.9,0.92, '#font[41]{'+'Total Overlap'+'}')

    theCanvas.SaveAs('any_overlap.png')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Draw the plots of the compareStability script')

    parser.add_argument('--theFile', default='purityFile.root', nargs='?',help='File for drawing the plots from')

    args = parser.parse_args()

    main(args)