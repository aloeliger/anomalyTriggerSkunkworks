import argparse

from samples.dataSamples import runASample, runBSample, runCSample, runDSample

from tqdm import tqdm

def main(args):
    ROOT.gStyle.SetOptStat(0)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Compare the dependence of rate on other things')

    parser.add_argument('--theFile', default='rateDependanceFile.root', help='Output plot file')

    args = parser.parse_args()