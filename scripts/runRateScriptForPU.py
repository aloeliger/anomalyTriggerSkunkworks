import subprocess

maxRateConfigurations = [
    ("40.0e3","LHCBX"),
    ("28.607e3","ZBBX")
]
PUConfigurations = [
    ("\"(0<npv && npv <= 10)\"",
     "\"0 < N_{PV} #leq 10\"",
     "PU_0_10"),

    ("\"(10<npv && npv <= 20)\"",
     "\"10 < N_{PV} #leq 20\"",
     "PU_10_20"),

    ("\"(20<npv && npv <= 30)\"",
     "\"20 < N_{PV} #leq 30\"",
     "PU_20_30"),
    
    ("\"(30<npv && npv <= 40)\"",
     "\"30 < N_{PV} #leq 40\"",
     "PU_30_40"),

    ("\"(40<npv && npv <= 50)\"",
     "\"40 < N_{PV} #leq 50\"",
     "PU_40_50")
]

for maxRateConfig in maxRateConfigurations:
    for PUConfig in PUConfigurations:
        theCall = ["python3",
                   "$CMSSW_BASE/src/L1Trigger/anomalyTriggerSkunkworks/scripts/efficiencyRatePlots.py",
                   "--condition",
                   PUConfig[0],
                   "--binLabel",
                   PUConfig[1],
                   "--zeroThresholdTriggerRate",
                   maxRateConfig[0],
                   "--fileExtension",
                   PUConfig[2]+"_"+maxRateConfig[1]]
        commandString = ''
        for x in theCall:
            commandString += x+' '
            
        subprocess.Popen([commandString], shell=True)
