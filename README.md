# Anomaly Trigger Skunkworks
Andrew's private working repository to investigate CaloL1 AD algoirthm integration with the
emulator subsystem.

##Prerequisites.
This repository should work largely out of the box. The one requirement is my commits to the emulator must be installed alongside. These commits were made to the 
[L1Trigger/L1TCaloLayer1/L1TCaloSummary](https://github.com/cms-sw/cmssw/blob/master/L1Trigger/L1TCaloLayer1/plugins/L1TCaloSummary.cc) path. My commits were made in CMSSW_12_4_3,
but should be simple enough that if any porting is needed, they can be recreated 
in any version of CMSSW that supports Marcel Rieger's [CMSSW TensorFlow/DNN interface](https://gitlab.cern.ch/mrieger/CMSSW-DNN)

The branch I keep my working copy of the emulator (with model included) can be found 
[here](https://github.com/aloeliger/cmssw/tree/anomalyTrigger), with specific L1TCaloSummary code found [here](https://github.com/aloeliger/cmssw/blob/anomalyTrigger/L1Trigger/L1TCaloLayer1/plugins/L1TCaloSummary.cc) ([git blame](https://github.com/aloeliger/cmssw/blame/anomalyTrigger/L1Trigger/L1TCaloLayer1/plugins/L1TCaloSummary.cc) to check the differences).

The current CaloL1 AD model has also been uploaded to my branch under L1Trigger/L1TCaloLayer1/data/

## Contents and usage

### plugins
- `L1TCaloSummaryTestNtuplizer.cc` is a basic ntuplizer to grab the current L1TCaloSummary embedded score and put it into a tree alongside some basic run information. It also currently stores the emulator regions, and the digis that are given to the emulator.
- `L1TTriggerBitsNtuplizer.cc` an Ntuplizer I am working with to put the some of the L1 menu and the acceptance bits into an ntuple for comparison on an event by event basis with the CaloL1 AD
- `anomalyTriggerSkunkworks.cc` This was some test code to work out the technical implementation of implementing the model in CMSSW. This should be largely deprecated, and is only kept around for legacy reasons.

### python
- `L1TCaloSummary2018Configs/` contains configurations used to make 1e5 events from RAW data using the emulator and L1TCaloSummaryTestNtuplizer. There are confiugrations for 4 different eras of 2018, and a base configuration that contains the majority of the code. Worth nothing, these all use a synchronized set of MiniAOD and RAW files
- `plotSettings` just some common code for plot creation scripts
- `productionFragments` now deprecated repository for storing fragments I was going to use to make custom samples to test on.
- `L1MultiNtupleization_cff.py` configuration for testing the combination of Ntuplizers
- `L1TCaloSummaryTestNtuplizer_cfi.py` basic settings  for the L1TCaloSummaryTestNtuplizer
- `L1TCaloSummaryTestNtuplizer_singleRun_cff.py` script for running the L1TCaloSummaryTestNtuplizer on a single RAW file
- `L1TTriggerBitsNtuplizer_cfi.py` basic settings for the L1 Trigger bits ntuplizer
- `anomalyTriggerSkunkworks*.py` deprecated technical test and settings

### scripts

this contains the scripts for making score plots, efficiency/rate plots, and pileup binned versions of these plots, as well as some utility scripts for running all of these at once.