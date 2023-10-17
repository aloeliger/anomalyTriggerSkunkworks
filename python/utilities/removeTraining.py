# Quick tool for taking a dataframe and removing a JSON list of runs and lumi sections from it to prevent data
# evaluation on data that may have been used to train CICADA

import json
import os

class removeTrainingTool():
    def __init__(self, JSONFile=f'{os.environ["CMSSW_BASE"]}/src/anomalyDetection/anomalyTriggerSkunkworks/metaData/TrainingRunLumi.json'):
        self.JSONFile = JSONFile
        with open(self.JSONFile, 'r') as theFile:
            self.JSONData = json.load(theFile)
    
    def removeTrainingDataFromDataframe(self, theDataframe):
        removalString = ''
        resultDF = theDataframe
        for run in self.JSONData:
            for lumi in self.JSONData[run]:
                if removalString == '':
                    removalString = f'!(run == {run} && lumi == {lumi})'
                else:
                    removalString += f' && !(run == {run} && lumi == {lumi})'
                # resultDF = resultDF.Filter(f"run != {run} || lumi != {lumi}")
        resultDF = resultDF.Filter(removalString)
        return resultDF
