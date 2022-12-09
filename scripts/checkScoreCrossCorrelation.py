import ROOT
import argparse

def main(args):
    ROOT.gStyle.SetOptStat(0)

    caloSummaryChain = ROOT.TChain('L1TCaloSummaryTestNtuplizer/L1TCaloSummaryOutput')
    uGTChain = ROOT.TChain('uGTModelNtuplizer/uGTModelOutput')

    caloSummaryChain.Add(args.theFile)
    uGTChain.Add(args.theFile)

    caloSummaryChain.AddFriend(uGTChain)

    theCanvas = ROOT.TCanvas('correlationCanvas')

    caloSummaryChain.Draw('anomalyScore:uGTAnomalyScore>>scoreCorrelation(60,0.0,200,30,0.0,7.0)','anomalyScore > 0.5 || uGTAnomalyScore > 10','COLZ')

    thePlot = ROOT.gDirectory.Get('scoreCorrelation').Clone()

    thePlot.SetTitle('')
    thePlot.Draw('COLZ')
    thePlot.GetXaxis().SetTitle('uGT AD Score')
    thePlot.GetYaxis().SetTitle('CICADA Score')

    cmsLatex = ROOT.TLatex()
    cmsLatex.SetTextSize(0.06)
    cmsLatex.SetNDC(True)
    cmsLatex.SetTextAlign(11)
    cmsLatex.DrawLatex(0.1,0.92, "#font[61]{CMS} #font[52]{Preliminary}")

    if args.centerText != None:
        centerLatex = ROOT.TLatex()
        centerLatex.SetTextSize(0.05)
        centerLatex.SetNDC(True)
        centerLatex.SetTextAlign(23)
        centerLatex.DrawLatex(0.5, 0.88, "#font[32]{"+args.centerText+"}")
    
    theCorrelation = thePlot.GetCorrelationFactor()
    corrString = f'{theCorrelation:1.4f}'

    correlationLatex = ROOT.TLatex()
    correlationLatex.SetTextSize(0.06)
    correlationLatex.SetNDC(True)
    correlationLatex.SetTextAlign(31)
    correlationLatex.DrawLatex(0.9, 0.92, "#font[52]{Correlation: "+corrString+"}")


    theCanvas.SaveAs("scoreCorrelation.png")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Script for examining the correlation between CICADA and the uGTAD model')

    parser.add_argument(
        '--theFile',
        required=True,
        nargs='?',
        help='File with available trees'
    )

    parser.add_argument(
        '--centerText',
        nargs='?',
        help='Any text to displayed in the center of the plot'
    )

    args = parser.parse_args()

    main(args)