import argparse
import ROOT
import statistics

def main(args):
    theFile = ROOT.TFile(args.theFile)

    caloScorePlots = {}
    uGTScorePlots = {}
    runs = ('RunA', 'RunB', 'RunC', 'RunD')

    for run in runs:
        caloScorePlots[run] = getattr(theFile, f'{run}CaloScores')
        uGTScorePlots[run] = getattr(theFile, f'{run}uGTScores')
    
    caloScorePlots['RunA'].SetLineColor(ROOT.kRed)
    caloScorePlots['RunB'].SetLineColor(ROOT.kBlue)
    caloScorePlots['RunC'].SetLineColor(ROOT.kGreen)
    caloScorePlots['RunD'].SetLineColor(ROOT.kOrange)

    caloScorePlots['RunA'].SetLineWidth(2)
    caloScorePlots['RunB'].SetLineWidth(2)
    caloScorePlots['RunC'].SetLineWidth(2)
    caloScorePlots['RunD'].SetLineWidth(2)

    caloScorePlots['RunA'].SetMarkerColor(ROOT.kRed)
    caloScorePlots['RunB'].SetMarkerColor(ROOT.kBlue)
    caloScorePlots['RunC'].SetMarkerColor(ROOT.kGreen)
    caloScorePlots['RunD'].SetMarkerColor(ROOT.kOrange)

    caloScorePlots['RunA'].SetMarkerStyle(20)
    caloScorePlots['RunB'].SetMarkerStyle(20)
    caloScorePlots['RunC'].SetMarkerStyle(20)
    caloScorePlots['RunD'].SetMarkerStyle(20)

    caloMaxes = [
        caloScorePlots['RunA'].GetMaximum(),
        caloScorePlots['RunB'].GetMaximum(),
        caloScorePlots['RunC'].GetMaximum(),
        caloScorePlots['RunD'].GetMaximum(),
    ]
    caloMax = max(caloMaxes) * 1.1

    caloMeans = {
        'RunA' : caloScorePlots['RunA'].GetMean(),
        'RunB' : caloScorePlots['RunB'].GetMean(),
        'RunC' : caloScorePlots['RunC'].GetMean(),
        'RunD' : caloScorePlots['RunD'].GetMean()
    }

    caloStdDevs = {
        'RunA' : caloScorePlots['RunA'].GetStdDev(),
        'RunB' : caloScorePlots['RunB'].GetStdDev(),
        'RunC' : caloScorePlots['RunC'].GetStdDev(),
        'RunD' : caloScorePlots['RunD'].GetStdDev(),
    }
    
    lineColors = {
        'RunA' : ROOT.kRed,
        'RunB' : ROOT.kBlue,
        'RunC' : ROOT.kGreen,
        'RunD' : ROOT.kOrange,
    }
    
    meansSetup = {
        'RunA': ('Run A', 0.6),
        'RunB': ('Run B', 0.5),
        'RunC': ('Run C', 0.4),
        'RunD': ('Run D', 0.3)
    }
    caloStdDevOfMeans = statistics.stdev([caloMeans[run] for run in caloMeans])

    caloScorePlots['RunA'].SetMaximum(caloMax)
    caloScorePlots['RunA'].SetTitle('')
    caloScorePlots['RunA'].GetXaxis().SetTitle('CICADA Score')
    caloScorePlots['RunA'].GetYaxis().SetTitle('Events (Normalized to 1)')

    uGTScorePlots['RunA'].SetMarkerColor(ROOT.kRed)
    uGTScorePlots['RunB'].SetMarkerColor(ROOT.kBlue)
    uGTScorePlots['RunC'].SetMarkerColor(ROOT.kGreen)
    uGTScorePlots['RunD'].SetMarkerColor(ROOT.kOrange)

    uGTScorePlots['RunA'].SetLineColor(ROOT.kRed)
    uGTScorePlots['RunB'].SetLineColor(ROOT.kBlue)
    uGTScorePlots['RunC'].SetLineColor(ROOT.kGreen)
    uGTScorePlots['RunD'].SetLineColor(ROOT.kOrange)

    uGTScorePlots['RunA'].SetLineWidth(2)
    uGTScorePlots['RunB'].SetLineWidth(2)
    uGTScorePlots['RunC'].SetLineWidth(2)
    uGTScorePlots['RunD'].SetLineWidth(2)

    uGTScorePlots['RunA'].SetMarkerStyle(22)
    uGTScorePlots['RunB'].SetMarkerStyle(22)
    uGTScorePlots['RunC'].SetMarkerStyle(22)
    uGTScorePlots['RunD'].SetMarkerStyle(22)

    uGTMaxes = [
        uGTScorePlots['RunA'].GetMaximum(),
        uGTScorePlots['RunB'].GetMaximum(),
        uGTScorePlots['RunC'].GetMaximum(),
        uGTScorePlots['RunD'].GetMaximum(),
    ]
    uGTMax = max(uGTMaxes) * 1.1

    uGTMeans = {
        'RunA' : uGTScorePlots['RunA'].GetMean(),
        'RunB' : uGTScorePlots['RunB'].GetMean(),
        'RunC' : uGTScorePlots['RunC'].GetMean(),
        'RunD' : uGTScorePlots['RunD'].GetMean(),
    }

    uGTStdDevs = {
        'RunA' : uGTScorePlots['RunA'].GetStdDev(),
        'RunB' : uGTScorePlots['RunB'].GetStdDev(),
        'RunC' : uGTScorePlots['RunC'].GetStdDev(),
        'RunD' : uGTScorePlots['RunD'].GetStdDev(),
    }
    uGTStdDevOfMeans = statistics.stdev([uGTMeans[run] for run in uGTMeans])

    uGTScorePlots['RunA'].SetMaximum(uGTMax)
    uGTScorePlots['RunA'].SetTitle('')
    uGTScorePlots['RunA'].GetXaxis().SetTitle('uGT Score')
    uGTScorePlots['RunA'].GetYaxis().SetTitle('Events (Normalized to 1)')

    caloCanvas = ROOT.TCanvas('caloCanvas', 'caloCanvas')
    uGTCanvas = ROOT.TCanvas('uGTCanvas', 'uGTCanvas')

    cmsLatex = ROOT.TLatex()
    cmsLatex.SetTextSize(0.06)
    cmsLatex.SetNDC(True)
    cmsLatex.SetTextAlign(11)
    #cmsLatex.DrawLatex(0.1,0.92, "#font[61]{CMS} #font[52]{Preliminary}")

    algoLatex = ROOT.TLatex()
    algoLatex.SetTextSize(0.06)
    algoLatex.SetNDC(True)
    algoLatex.SetTextAlign(31)
    #algoLatex.DrawLatex(0.9,0.92, f'{plotPair[2]}')

    meansLatex = ROOT.TLatex()
    meansLatex.SetTextSize(0.03)
    meansLatex.SetNDC(True)
    meansLatex.SetTextAlign(11)

    stdDevLatex = ROOT.TLatex()
    stdDevLatex.SetTextSize(0.03)
    stdDevLatex.SetNDC(True)
    stdDevLatex.SetTextAlign(21)


    ############################################
    # Draw Calo Stuff
    ############################################
    caloCanvas.cd()

    caloScorePlots['RunA'].Draw()
    caloScorePlots['RunB'].Draw('SAME')
    caloScorePlots['RunC'].Draw('SAME')
    caloScorePlots['RunD'].Draw('SAME')

    caloLegend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
    caloLegend.AddEntry(caloScorePlots['RunA'], 'Run A', 'lp')
    caloLegend.AddEntry(caloScorePlots['RunB'], 'Run B', 'lp')
    caloLegend.AddEntry(caloScorePlots['RunC'], 'Run C', 'lp')
    caloLegend.AddEntry(caloScorePlots['RunD'], 'Run D', 'lp')
    caloLegend.Draw()

    caloLines = []
    for run in caloMeans:
        theLine = ROOT.TLine(caloMeans[run], 0.0, caloMeans[run], caloMax)
        theLine.SetLineColor(lineColors[run])
        theLine.Draw()
        caloLines.append(theLine)
        meansLatex.DrawLatex(0.7, meansSetup[run][1], meansSetup[run][0]+' Mean: '+f'{caloMeans[run]:2.2f}')
        meansLatex.DrawLatex(0.7+0.04, meansSetup[run][1]-0.05, 'Std Dev: '+f'{caloStdDevs[run]:2.2f}')
    
    stdDevLatex.DrawLatex(0.5, 0.85, "Std Dev Of Means: "+f'{caloStdDevOfMeans:2.2f}')
    cmsLatex.DrawLatex(0.1,0.92, "#font[61]{CMS} #font[52]{Preliminary}")
    algoLatex.DrawLatex(0.9,0.92, 'CICADA')

    ############################################
    # Draw UGT Stuff
    ############################################
    uGTCanvas.cd()
    #uGTCanvas.SetLogx()

    uGTScorePlots['RunA'].Draw()
    uGTScorePlots['RunB'].Draw('SAME')
    uGTScorePlots['RunC'].Draw('SAME')
    uGTScorePlots['RunD'].Draw('SAME')

    uGTLegend = ROOT.TLegend(0.7, 0.7, 0.9, 0.9)
    uGTLegend.AddEntry(uGTScorePlots['RunA'], 'Run A', 'lp')
    uGTLegend.AddEntry(uGTScorePlots['RunB'], 'Run B', 'lp')
    uGTLegend.AddEntry(uGTScorePlots['RunC'], 'Run C', 'lp')
    uGTLegend.AddEntry(uGTScorePlots['RunD'], 'Run D', 'lp')
    uGTLegend.Draw()

    uGTLines = []
    for run in uGTMeans:
        theLine = ROOT.TLine(uGTMeans[run], 0.0, uGTMeans[run], uGTMax)
        theLine.SetLineColor(lineColors[run])
        theLine.Draw()
        uGTLines.append(theLine)
        meansLatex.DrawLatex(0.7, meansSetup[run][1], meansSetup[run][0]+' Mean: '+f'{uGTMeans[run]:2.2f}')
        meansLatex.DrawLatex(0.7+0.04, meansSetup[run][1]-0.05, 'Std Dev: '+f'{uGTStdDevs[run]:2.2f}')

    stdDevLatex.DrawLatex(0.5, 0.85, "Std Dev Of Means: "+f'{uGTStdDevOfMeans:2.2f}')
    cmsLatex.DrawLatex(0.1,0.92, "#font[61]{CMS} #font[52]{Preliminary}")
    algoLatex.DrawLatex(0.9,0.92, 'uGT AD')

    caloCanvas.SaveAs('CICADAScores.png')
    uGTCanvas.SaveAs('uGTScores.png') 

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Draw the plots of the compareStability script')

    parser.add_argument('--theFile', default='stabilityFile.root', nargs='?',help='File for drawing the plots from')

    args = parser.parse_args()

    main(args)