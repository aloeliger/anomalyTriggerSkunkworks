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
    #print(theHistos)
    #print(uniqueHistos)
    for normalization in ('normalized', 'unnormalized'):
        for uniqueHisto in uniqueHistos:
            theCanvas = ROOT.TCanvas('theCanvas', 'theCanvas')
            #theCanvas.SetLogy()

            theCanvas.Divide(1,2)
            
            plotPad = ROOT.gPad.GetPrimitive('theCanvas_1')
            ratioPad = ROOT.gPad.GetPrimitive('theCanvas_2')

            plotPad.SetPad("pad1", "plot", 0.0, 0.4, 1.0, 1.0, 0)
            ratioPad.SetPad("pad2", "ratio", 0.0, 0.0, 1.0, 0.4, 0)

            plotPad.SetLogy()
            plotPad.SetBottomMargin(0.0)

            ratioPad.SetTopMargin(0.0)
            ratioPad.SetBottomMargin(0.27)
            ratioPad.SetGridy()
            ratioPad.SetLogy()

            plotPad.cd()
            baseHistogram = getattr(theFile, uniqueHisto+'_0.0').Clone()
            AD3Histogram = getattr(theFile, uniqueHisto+'_3.0').Clone()
            AD6Histogram = getattr(theFile, uniqueHisto+'_6.0').Clone()
            AD6p5Histogram = getattr(theFile, uniqueHisto+'_6.5').Clone()
            AD7Histogram = getattr(theFile, uniqueHisto+'_7.0').Clone()
            
            if normalization == 'normalized':
                baseHistogram.Scale(1.0/baseHistogram.Integral())
                AD3Histogram.Scale(1.0/AD3Histogram.Integral())
                AD6Histogram.Scale(1.0/AD6Histogram.Integral())
                AD6p5Histogram.Scale(1.0/AD6p5Histogram.Integral())
                AD7Histogram.Scale(1.0/AD7Histogram.Integral())

            theMax = baseHistogram.GetMaximum()*10
            for hist in [AD3Histogram, AD6Histogram, AD6p5Histogram, AD7Histogram]:
                theMax = max(theMax, hist.GetMaximum()*10)
            baseHistogram.SetMaximum(theMax)

            baseHistogram.SetLineWidth(2)
            AD3Histogram.SetLineWidth(2)
            AD6Histogram.SetLineWidth(2)
            AD6p5Histogram.SetLineWidth(2)
            AD7Histogram.SetLineWidth(2)

            baseHistogram.SetMarkerStyle(20)
            AD3Histogram.SetMarkerStyle(21)
            AD6Histogram.SetMarkerStyle(22)
            AD6p5Histogram.SetMarkerStyle(23)
            AD7Histogram.SetMarkerStyle(24)

            baseHistogram.SetLineColor(ROOT.kBlack)
            AD3Histogram.SetLineColor(ROOT.kRed)
            AD6Histogram.SetLineColor(ROOT.kBlue)
            AD6p5Histogram.SetLineColor(ROOT.kGreen)
            AD7Histogram.SetLineColor(ROOT.kMagenta)

            baseHistogram.SetMarkerColor(ROOT.kBlack)
            AD3Histogram.SetMarkerColor(ROOT.kRed)
            AD6Histogram.SetMarkerColor(ROOT.kBlue)
            AD6p5Histogram.SetMarkerColor(ROOT.kGreen)
            AD7Histogram.SetMarkerColor(ROOT.kMagenta)

            baseHistogram.Draw('E1 X0')
            AD3Histogram.Draw('SAME E1 X0')
            AD6Histogram.Draw('SAME E1 X0')
            AD6p5Histogram.Draw('SAME E1 X0')
            AD7Histogram.Draw('SAME E1 X0')

            baseHistogram.SetTitle('')
            #baseHistogram.GetXaxis().SetTitle(uniqueHisto)
            if normalization == 'normalized':
                baseHistogram.GetYaxis().SetTitle("Density (Normalized to 1)")
            else:
                baseHistogram.GetYaxis().SetTitle("Events (Unnormalized)")
            baseHistogram.GetXaxis().SetLabelSize(0.1)

            theLegend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
            theLegend.AddEntry(baseHistogram, 'No AD threshold', 'lp')
            theLegend.AddEntry(AD3Histogram, 'Calo Anomaly Score > 3.0', 'lp')
            theLegend.AddEntry(AD6Histogram, 'Calo Anomaly Score > 6.0', 'lp')
            theLegend.AddEntry(AD6p5Histogram, 'Calo Anomaly Score > 6.5', 'lp')
            theLegend.AddEntry(AD7Histogram, 'Calo Anomaly Score > 7.0', 'lp')
            theLegend.Draw()

            ratioPad.cd()
            
            denominator = baseHistogram.Clone()
            baseRatio = baseHistogram.Clone()
            AD3Ratio = AD3Histogram.Clone()
            AD6Ratio = AD6Histogram.Clone()
            AD6p5Ratio = AD6p5Histogram.Clone()
            AD7Ratio = AD7Histogram.Clone()

            baseRatio.Divide(denominator)
            AD3Ratio.Divide(denominator)
            AD6Ratio.Divide(denominator)
            AD6p5Ratio.Divide(denominator)
            AD7Ratio.Divide(denominator)

            baseRatio.Draw('E1 X0')
            AD3Ratio.Draw('SAME E1 X0')
            AD6Ratio.Draw('SAME E1 X0')
            AD6p5Ratio.Draw('SAME E1 X0')
            AD7Ratio.Draw('SAME E1 X0')

            theMax = baseRatio.GetMaximum()
            for hist in [AD3Ratio, AD6Ratio, AD6p5Ratio, AD7Ratio]:
                theMax = max(theMax, hist.GetMaximum())
            baseRatio.SetMaximum(theMax*10)
            baseRatio.SetMinimum(0.01)

            baseRatio.SetTitle('')
            baseRatio.GetXaxis().SetTitle(uniqueHisto)
            baseRatio.GetXaxis().SetTitleSize(0.1)
            baseRatio.GetYaxis().SetTitleSize(0.1)
            baseRatio.GetYaxis().SetTitle('Ratio to ZeroBias')

            theCanvas.SaveAs(f'{args.outputLocation}/{uniqueHisto}_{normalization}.png')

        

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
