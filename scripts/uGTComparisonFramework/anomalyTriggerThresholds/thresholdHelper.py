import json
import os

class thresholdHelper():
    def __init__(self, thresholdFileName=os.path.dirname(os.path.abspath(__file__))+'/'+'triggerThresholds.json'):
        self.jsonFile = open(thresholdFileName, 'r')
        self.triggerData = json.load(self.jsonFile)
    
    def getTriggerThreshold(self, trigger,rate):
        return self.triggerData['thresholds'][trigger][rate]