import argparse
import ROOT

def main(args):
    ROOT.gStyle.SetOptStat(0)
    
    theFile = ROOT.TFile(args.theFile)
    
    variablesToCompare = {
        'nEGs': 'N_{e}',
        'leading_egEt' : 'Leading Electron E_{t}',
        'leading_egEta': 'Leading Electron #eta',
        'leading_egIso': 'Leading Electron Isolation',
        'nTaus' : 'N_{#tau}',
        'leading_tauEt': 'Leading #tau E_{t}',
        'leading_tauEta': 'Leading #tau #eta',
        'leading_tauIso': 'Leading #tau Isolation',
        'nJets': 'N_{Jet}',
        'leading_jetEt': 'Leading Jet E_{t}',
        'leading_jetEta': 'Leading Jet #eta',
        'nMuons': 'N_{#mu}',
        'leading_muonEt': 'Leading #mu E_{t}',
        'leading_muonEta': 'Leading #mu #eta',
        'leading_muonIso': 'Leading #mu Isolation',
    }

    for variable in variablesToCompare:
        for trigger in ('CICADA', 'uGT'):
            canvasName = f'{variable}_{trigger}'
            theCanvas = ROOT.TCanvas(canvasName)

            thePlot = getattr(theFile, f'{trigger}_{variable}_RunA')

            thePlot.Draw('COL')

            thePlot.GetXaxis().SetTitle(variablesToCompare[variable])
            yAxisTitle = ''
            if trigger == 'CICADA':
                yAxisTitle = 'CICADA Score'
            elif trigger == 'uGT':
                yAxisTitle = 'uGT AD Score'
            thePlot.GetYaxis().SetTitle(yAxisTitle)
            thePlot.SetTitle('')
            
            cmsLatex = ROOT.TLatex()
            cmsLatex.SetTextSize(0.06)
            cmsLatex.SetNDC(True)
            cmsLatex.SetTextAlign(11)
            cmsLatex.DrawLatex(0.1,0.92, "#font[61]{CMS} #font[52]{Preliminary}")

            theCorrelation = thePlot.GetCorrelationFactor()
            corrString = f'{theCorrelation:1.4f}'

            correlationLatex = ROOT.TLatex()
            correlationLatex.SetTextSize(0.06)
            correlationLatex.SetNDC(True)
            correlationLatex.SetTextAlign(31)
            correlationLatex.DrawLatex(0.9, 0.92, "#font[52]{"+f'{trigger}'+" Correlation: "+corrString+"}")

            theCanvas.SaveAs(f'{trigger}_{variable}_correlation.png')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Draw the correlation of anomaly scores to L1 variables')

    parser.add_argument('--theFile', default='l1correlationFile.root', help='File to draw plots from')

    args = parser.parse_args()

    main(args)