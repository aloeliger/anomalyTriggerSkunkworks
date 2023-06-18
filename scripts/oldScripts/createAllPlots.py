import subprocess

scorePlotCall = ['python3 $CMSSW_BASE/src/anomalyDetection/anomalyTriggerSkunkworks/scripts/scorePlots.py']

ratePlotCall = ['python3 $CMSSW_BASE/src/anomalyDetection/anomalyTriggerSkunkworks/scripts/efficiencyRatePlots.py']

PUScoreCall = ['python3 $CMSSW_BASE/src/anomalyDetection/anomalyTriggerSkunkworks/scripts/PUScorePlots.py']

PURateCall = ['python3 $CMSSW_BASE/src/anomalyDetection/anomalyTriggerSkunkworks/scripts/runRateScriptForPU.py']

allPlotCalls = [scorePlotCall,
                ratePlotCall,
                PUScoreCall,
                PURateCall]
for call in allPlotCalls:
    subprocess.Popen(call, shell=True)
