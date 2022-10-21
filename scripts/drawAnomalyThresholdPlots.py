import ROOT
import argparse
import os

def main(args):
    ROOT.gStyle.SetOptStat(0)

    theFile = ROOT.TFile(args.inputFile)

    os.system(f'mkdir -p {args.outputLocation}')

    #okay, let's figure out how to read all of the histograms in type
    theHistos = [key.GetName() for key in list(theFile.GetListOfKeys())]
    uniqueHistos = []
    for name in theHistos:
        if name[:-4] not in uniqueHistos:
            uniqueHistos.append(name[:-4])
    print(theHistos)
    print(uniqueHistos)
    for uniqueHisto in uniqueHistos:
        theCanvas = ROOT.TCanvas('theCanvas', 'theCanvas')
        baseHistogram = getattr(theFile, uniqueHisto+'_0.0')
        AD3Histogram = getattr(theFile, uniqueHisto+'_3.0')
        AD6Histogram = getattr(theFile, uniqueHisto+'_6.0')
        AD6p5Histogram = getattr(theFile, uniqueHisto+'_6.5')
        AD7Histogram = getattr(theFile, uniqueHisto+'_7.0')

        baseHistogram.Scale(1.0/baseHistogram.Integral())
        AD3Histogram.Scale(1.0/AD3Histogram.Integral())
        AD6Histogram.Scale(1.0/AD6Histogram.Integral())
        AD6p5Histogram.Scale(1.0/AD6p5Histogram.Integral())
        AD7Histogram.Scale(1.0/AD7Histogram.Integral())
        
        theMax = baseHistogram.GetMaximum()*1.1

        for hist in [AD3Histogram, AD6Histogram, AD6p5Histogram, AD7Histogram]:
            theMax = max(theMax, hist.GetMaximum()*1.1)
        baseHistogram.SetMaximum(theMax)

        baseHistogram.SetLineWidth(2)
        AD3Histogram.SetLineWidth(2)
        AD6Histogram.SetLineWidth(2)
        AD6p5Histogram.SetLineWidth(2)
        AD7Histogram.SetLineWidth(2)

        baseHistogram.SetMarkerStyle(20)
        AD3Histogram.SetMarkerStyle(20)
        AD6Histogram.SetMarkerStyle(20)
        AD6p5Histogram.SetMarkerStyle(20)
        AD7Histogram.SetMarkerStyle(20)

        baseHistogram.SetLineColor(ROOT.kBlack)
        AD3Histogram.SetLineColor(ROOT.kRed)
        AD6Histogram.SetLineColor(ROOT.kBlue)
        AD6p5Histogram.SetLineColor(ROOT.kGreen)
        AD7Histogram.SetLineColor(ROOT.kMagenta)
        
        baseHistogram.Draw('HIST L')
        AD3Histogram.Draw('SAME HIST L')
        AD6Histogram.Draw('SAME HIST L')
        AD6p5Histogram.Draw('SAME HIST L')
        AD7Histogram.Draw('SAME HIST L')

        baseHistogram.SetTitle('')
        baseHistogram.GetXaxis().SetTitle(uniqueHisto)
        baseHistogram.GetYaxis().SetTitle("Density (Normalized to 1)")

        theLegend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
        theLegend.AddEntry(baseHistogram, 'No AD threshold', 'l')
        theLegend.AddEntry(AD3Histogram, 'Calo Anomaly Score > 3.0', 'l')
        theLegend.AddEntry(AD6Histogram, 'Calo Anomaly Score > 6.0', 'l')
        theLegend.AddEntry(AD6p5Histogram, 'Calo Anomaly Score > 6.5', 'l')
        theLegend.AddEntry(AD7Histogram, 'Calo Anomaly Score > 7.0', 'l')
        theLegend.Draw()

        theCanvas.SaveAs(f'{args.outputLocation}/{uniqueHisto}.png')

        

if __name__=='__main__':

    parser = argparse.ArgumentParser(description='Draw plots produced by the treshold scultping checker')

    parser.add_argument('--inputFile',
                        required=True,
                        nargs='?',
                        help='File to read from')
    parser.add_argument('--outputLocation',
                        required=True,
                        nargs='?',
                        help='Directory to write plots to. Will be made if not extant.')

    args = parser.parse_args()

    main(args)
