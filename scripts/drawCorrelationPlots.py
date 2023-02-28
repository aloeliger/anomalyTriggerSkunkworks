#Script for drawing the output of the correlation 
import ROOT
import argparse
import re

def main(args):
    ROOT.gStyle.SetOptStat(0)
    ROOT.gROOT.SetBatch(True)

    theFile = ROOT.TFile(args.theFile)

    plotNames = [x.GetName() for x in list(theFile.GetListOfKeys())]

    for plotName in plotNames:
        thePlot = getattr(theFile, plotName)

        theCanvas = ROOT.TCanvas(plotName, plotName)

        thePlot.Scale(1.0/thePlot.Integral())

        #print(plotName)
        corrFactor = thePlot.GetCorrelationFactor()
        #print(corrFactor)

        thePlot.Draw('COLZ')
        thePlot.SetTitle('')
        thePlot.GetYaxis().SetTitle('Anomaly Score')
        xAxisName = re.search('.*(?=Correlation)', plotName).group(0)
        thePlot.GetXaxis().SetTitle(xAxisName)

        theCorrLatex = ROOT.TLatex()
        theCorrLatex.SetTextSize(0.04)
        theCorrLatex.SetNDC(True)
        theCorrLatex.SetTextAlign(11)
        theCorrLatex.DrawLatex(0.55, 0.91, f'Correlation Coefficient: {corrFactor:1.3f}')

        theCanvas.SaveAs(f'{plotName}.png')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Draw correlation plots from a file')

    parser.add_argument(
        '--theFile',
        required=True,
        nargs='?',
        help='File with the plots'
    )

    args = parser.parse_args()

    main(args)