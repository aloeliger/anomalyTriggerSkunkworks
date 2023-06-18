#This is going to be another "Toss it together" sort of nightmare

#We just want to pull open the file, and examine the iPhi,iEta et stuff and see if Adrian's numbers make sense
#And then we can try to compare TPs to what we can pull from the event.

import numpy as np
import uproot
import awkward as ak
from skimage.measure import block_reduce

theFile = uproot.open('/nfs_scratch/aloeliger/L1Ntuple_10.root')
theEventTree = theFile['l1EventTree/L1EventTree']
theCaloTowerTree = theFile['l1CaloTowerTree/L1CaloTowerTree']
theCaloTowerEmuTree = theFile['l1CaloTowerEmuTree/L1CaloTowerTree']

eventData = theEventTree.arrays()
caloData = theCaloTowerTree.arrays()
caloEmuData = theCaloTowerEmuTree.arrays()

#print(eventData)
print('Run:   {:>10}'.format(eventData[0]['run']))
print('Lumi:  {:>10}'.format(eventData[0]['lumi']))
print('Event: {:>10}'.format(eventData[0]['event']))

print('-'*50)
print(caloData[0]['nHCALTP'])
print(caloData[0]['hcalTPieta'])
print(caloData[0]['hcalTPiphi'])
print(caloData[0]['hcalTPet'])

print('-'*50)
print(caloData[0]['nECALTP'])
print(caloData[0]['ecalTPieta'])
print(caloData[0]['ecalTPiphi'])
print(caloData[0]['ecalTPet'])

print('-'*50)
print(caloData[0]['nTower'])
print(caloData[0]['ieta'])
print(caloData[0]['iphi'])
print(caloData[0]['iet'])
print('non-i coordinates')
print(caloEmuData[0]['eta'])
print(caloEmuData[0]['phi'])
print(caloEmuData[0]['et'])
print('-'*50)

print('*'*50)

print('-'*50)
print(caloEmuData[0]['nHCALTP'])
print(caloEmuData[0]['hcalTPieta'])
print(caloEmuData[0]['hcalTPiphi'])
print(caloEmuData[0]['hcalTPet'])
print('-'*50)
print(caloEmuData[0]['nECALTP'])
print(caloEmuData[0]['ecalTPieta'])
print(caloEmuData[0]['ecalTPiphi'])
print(caloEmuData[0]['ecalTPet'])
print('-'*50)
print(caloEmuData[0]['nTower'])
print(caloEmuData[0]['ieta'])
print(caloEmuData[0]['iphi'])
print(caloEmuData[0]['iet'])
print('non-i coordinates')
print(caloEmuData[0]['eta'])
print(caloEmuData[0]['phi'])
print(caloEmuData[0]['et'])
print('-'*50)

#emulator seems like a duplicate version of this, likely taken from the same 
#emulation bits we are using in cmssw. We'll work here since it seems this
#is what Adrian is doing.

iphi, ieta, iet = caloEmuData[0]['iphi'], caloEmuData[0]['ieta'], caloEmuData[0]['iet'],

print(iphi)
print(ieta)
print(iet)

etaMask = (ieta <= 28) & (ieta >= -28)

iphi, ieta, iet = iphi[etaMask], ieta[etaMask], iet[etaMask]

print(iphi)
print(ieta)
print(iet)

print('_'*75)
ieta = ak.where(ieta < 0, ieta, ieta - 1)
ieta = ieta + 28
iphi = (iphi + 2) % 72
print(ieta,' ',len(ieta))
print(iphi,' ',len(iphi))
print(iet,' ',len(iet))
print('_'*75)

theTPs = np.zeros((72,56))

for triple in zip(iphi,ieta,iet):
    theTPs[triple[0]][triple[1]]=triple[2]

print(theTPs)

for i in range(72):
    for j in range(56):
        print(' {:>2n}'.format(theTPs[i][j]), end='')
    print()

regionTPs = block_reduce(theTPs, (4, 4), np.sum)

print('_'*100)

for i in range(18):
    for j in range(14):
        print(' {:>2n}'.format(regionTPs[i][j]), end='')
    print()

#Do the same thing for HCAL
hcal_iphi, hcal_ieta, hcal_iet = caloEmuData[0]['hcalTPiphi'], caloEmuData[0]['hcalTPieta'], caloEmuData[0]['hcalTPet'],

print(hcal_iphi)
print(hcal_ieta)
print(hcal_iet)

etaMask = (hcal_ieta <= 28) & (hcal_ieta >= -28)

hcal_iphi, hcal_ieta, hcal_iet = hcal_iphi[etaMask], hcal_ieta[etaMask], hcal_iet[etaMask]

print(hcal_iphi)
print(hcal_ieta)
print(hcal_iet)

print('_'*75)
hcal_ieta = ak.where(hcal_ieta < 0, hcal_ieta, hcal_ieta - 1)
hcal_ieta = hcal_ieta + 28
hcal_iphi = (hcal_iphi + 2) % 72
print(hcal_ieta,' ',len(hcal_ieta))
print(hcal_iphi,' ',len(hcal_iphi))
print(hcal_iet,' ',len(hcal_iet))
print('_'*75)

hcal_TPs = np.zeros((72,56))

for triple in zip(hcal_iphi,hcal_ieta,hcal_iet):
    hcal_TPs[triple[0]][triple[1]]=triple[2]

print(hcal_TPs)

for i in range(72):
    for j in range(56):
        print(' {:>2n}'.format(hcal_TPs[i][j]), end='')
    print()

hcal_regionTPs = block_reduce(hcal_TPs, (4, 4), np.sum)

print('_'*100)

for i in range(18):
    for j in range(14):
        print(' {:>2n}'.format(hcal_regionTPs[i][j]), end='')
    print()

#Do the same thing for ECAL
ecal_iphi, ecal_ieta, ecal_iet = caloEmuData[0]['ecalTPiphi'], caloEmuData[0]['ecalTPieta'], caloEmuData[0]['ecalTPet'],

print(ecal_iphi)
print(ecal_ieta)
print(ecal_iet)

etaMask = (ecal_ieta <= 28) & (ecal_ieta >= -28)

ecal_iphi, ecal_ieta, ecal_iet = ecal_iphi[etaMask], ecal_ieta[etaMask], ecal_iet[etaMask]

print(ecal_iphi)
print(ecal_ieta)
print(ecal_iet)

print('_'*75)
ecal_ieta = ak.where(ecal_ieta < 0, ecal_ieta, ecal_ieta - 1)
ecal_ieta = ecal_ieta + 28
ecal_iphi = (ecal_iphi + 2) % 72
print(ecal_ieta,' ',len(ecal_ieta))
print(ecal_iphi,' ',len(ecal_iphi))
print(ecal_iet,' ',len(ecal_iet))
print('_'*75)

ecal_TPs = np.zeros((72,56))

for triple in zip(ecal_iphi,ecal_ieta,ecal_iet):
    ecal_TPs[triple[0]][triple[1]]=triple[2]

print(ecal_TPs)

for i in range(72):
    for j in range(56):
        print(' {:>2n}'.format(ecal_TPs[i][j]), end='')
    print()

ecal_regionTPs = block_reduce(ecal_TPs, (4, 4), np.sum)

print('_'*100)

for i in range(18):
    for j in range(14):
        print(' {:>2n}'.format(ecal_regionTPs[i][j]), end='')
    print()

print('_'*100)
print('combinations of ECAL/HCAL regions')
print('added')

for i in range(18):
    for j in range(14):
        print(' {:>2n}'.format(ecal_regionTPs[i][j]+hcal_regionTPs[i][j]), end='')
    print()

print('subtracted (HCAL - ECAL)')
for i in range(18):
    for j in range(14):
        print(' {:>2n}'.format(hcal_regionTPs[i][j]-ecal_regionTPs[i][j]), end='')
    print()
