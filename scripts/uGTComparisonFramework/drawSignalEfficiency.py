import argparse
import ROOT

def main(args):
    ROOT.gStyle.SetOptStat(0)
    theFile = ROOT.TFile(args.theFile)

    data = [
        'RunA',
        'RunB',
        'RunC',
        'RunD',
    ]

    signals = {
        'SUEP': 'SUEP',
        'VBFHTT': 'VBF H#rightarrow#tau#tau',
        'HLongLived': 'H#rightarrow 2 Long Lived #rightarrow 4b',
        'TT': 't#bar{t}',
        'GluGluToHHto4B_highSample': 'HH#rightarrow 4b (ggH, kl-1p00_kt-1p00_c2-3p00)',
        'GluGluToHHTo4B_lowSample': 'HH#rightarrow 4b (kl-0p00_kt-1p00_c2-0p00)',
        'SUSY': 'SUSY gg #rightarrow bbH #rightarrow bb',
        'DYLLSample': 'DY #rightarrow LL (m 4-50)'
    }

    zeroBiasAccepts = getattr(theFile, f'{data[0]}Numerator').Clone()
    zeroBiasTotal = getattr(theFile, f'{data[0]}Denominator').Clone()
    for i in range(1,len(data)):
        zeroBiasAccepts.Add(getattr(theFile, f'{data[i]}Numerator').Clone())
        zeroBiasTotal.Add(getattr(theFile, f'{data[i]}Denominator').Clone())

    ROOT.gStyle.SetPaintTextFormat('1.2g')

    for sample in signals:
        theCanvas = ROOT.TCanvas(f'{sample}',f'{sample}')
        theCanvas.SetBottomMargin(0.33)
        theCanvas.SetGridx()
        theCanvas.SetGridy()
        theCanvas.SetLogy()

        sampleAccepts = getattr(theFile, f'{sample}Numerator').Clone()
        sampleTotals = getattr(theFile, f'{sample}Denominator').Clone()

        theAcceptancePlot = sampleAccepts.Clone()
        #theAcceptancePlot.Divide(sampleTotals.Clone())
        theAcceptancePlot.Scale(1.0 / sampleTotals.GetBinContent(1))

        errorHisto = theAcceptancePlot.Clone()

        #theAcceptancePlot.SetMaximum(1.2)
        #theAcceptancePlot.SetMinimum(0.0)

        theAcceptancePlot.SetLineColor(ROOT.kRed)
        theAcceptancePlot.SetLineWidth(2)

        errorHisto.SetFillColor(ROOT.kGray)
        errorHisto.SetFillStyle(3244)
        errorHisto.Draw('E2')
        theAcceptancePlot.Draw('SAME HIST TEXT0')

        #theAcceptancePlot.GetYaxis().SetRangeUser(0.0, 1.2)

        errorHisto.GetYaxis().SetTitle('Fraction Acceptance')
        errorHisto.LabelsOption('v','x')
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
        sampleLatex.DrawLatex(0.9,0.92, '#font[41]{'+signals[sample]+'}')

        theCanvas.SaveAs(f'{sample}_acceptance.png')

        #Now we do an actual efficiency plot
        effPlot = sampleAccepts.Clone()
        #effPlot.Divide(sampleTotals.Clone())
        effPlot.Scale(1.0/sampleTotals.GetBinContent(1))

        dataAcceptance = zeroBiasAccepts.Clone()
        #dataAcceptance.Divide(zeroBiasTotal.Clone())
        dataAcceptance.Scale(1.0/zeroBiasTotal.GetBinContent(1))

        effPlot.Divide(dataAcceptance)

        effErrorHisto = effPlot.Clone()

        effPlot.SetLineColor(ROOT.kRed)
        effPlot.SetLineWidth(2)

        effErrorHisto.SetFillColor(ROOT.kGray)
        effErrorHisto.SetFillStyle(3244)
        effErrorHisto.Draw('E2')
        effPlot.Draw('SAME HIST TEXT0')

        #effPlot.GetYaxis().SetRangeUser(0.0, 1.2*effPlot.GetMaximum())
        effErrorHisto.GetYaxis().SetTitle('Signal Accptance to Background Acceptance')
        effErrorHisto.LabelsOption('v', 'x')
        effErrorHisto.SetTitle('')

        cmsLatex.DrawLatex(0.1,0.92, "#font[61]{CMS} #font[52]{Preliminary}")
        sampleLatex.DrawLatex(0.9,0.92, '#font[41]{'+signals[sample]+'}')

        theCanvas.SaveAs(f'{sample}_efficiency.png')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Draw the plots of the signal efficiency script')

    parser.add_argument('--theFile', default='sampleFile.root',nargs='?',help='plot file')

    args = parser.parse_args()

    main(args)