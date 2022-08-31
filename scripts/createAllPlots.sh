#!/usr/bin/sh

#Run the basic score plots
python3 $CMSSW_BASE/src/L1Trigger/anomalyTriggerSkunkworks/scripts/scorePlots.py

#Run the basic rate plots
python3 $CMSSW_BASE/src/L1Trigger/anomalyTriggerSkunkworks/scripts/efficiencyRatePlots.py

#Run the basic PU plots
python3 $CMSSW_BASE/src/L1Trigger/anomalyTriggerSkunkworks/scripts/PUScorePlots.py

#run the PU bin plots
sh $CMSSW_BASE/src/L1Trigger/anomalyTriggerSkunkworks/scripts/runRateScriptForPU.sh
