import subprocess

scorePlotCall = ['python3 $CMSSW_BASE/src/L1Trigger/anomalyTriggerSkunkworks/scripts/scorePlots.py']

ratePlotCall = ['python3 $CMSSW_BASE/src/L1Trigger/anomalyTriggerSkunkworks/scripts/efficiencyRatePlots.py']

PUScoreCall = ['python3 $CMSSW_BASE/src/L1Trigger/anomalyTriggerSkunkworks/scripts/PUScorePlots.py']

PURateCall = ['python3 $CMSSW_BASE/src/L1Trigger/anomalyTriggerSkunkworks/scripts/runRateScriptForPU.py']

allPlotCalls = [scorePlotCall,
                ratePlotCall,
                PUScoreCall,
                PURateCall]
for call in allPlotCalls:
    subprocess.Popen(call, shell=True)
