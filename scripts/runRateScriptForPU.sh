#!/usr/bin/sh 
#just a quick set of preset calls to the rates script for doing pileup bins
python3 scripts/efficiencyRatePlots.py --condition '(0<npv && npv <= 10)' --binLabel '0 < N_{PV} #leq 10' --fileExtension 'PU_0_10'
python3 scripts/efficiencyRatePlots.py --condition '(10<npv && npv <= 20)' --binLabel '10 < N_{PV} #leq 20' --fileExtension 'PU_10_20'
python3 scripts/efficiencyRatePlots.py --condition '(20<npv && npv <= 30)' --binLabel '20 < N_{PV} #leq 30' --fileExtension 'PU_20_30'
python3 scripts/efficiencyRatePlots.py --condition '(30<npv && npv <= 40)' --binLabel '30 < N_{PV} #leq 40' --fileExtension 'PU_30_40'
python3 scripts/efficiencyRatePlots.py --condition '(40<npv && npv <= 50)' --binLabel '40 < N_{PV} #leq 50' --fileExtension 'PU_40_50'
