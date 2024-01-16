# !/usr/bin/env python3
# Script for parsing a test vector file to a usable input for the emulator test suite

import re
import argparse
from rich.console import Console, Group
from rich.traceback import install
from rich.text import Text
from rich.syntax import Syntax
from rich.panel import Panel

install(show_locals=True)
console = Console()

# toss out anything that doesn't look like an event formatted thing
def deleteNonEventLines(fileContents):
    indicesToDelete = []
    for index, line in enumerate(fileContents):
        if not re.match('0x[0-9A-Fa-f]{4}\t(0x[0-9A-Fa-f]{8}\t){36}', line):
            indicesToDelete.append(index)
    indicesToDelete.sort(reverse=True)
    for index in indicesToDelete:
        del fileContents[index]

    return fileContents

def makeBlankRegions():
    result = []
    for iPhi in range(18):
        result.append([])
        for iEta in range(14):
            result[iPhi].append(0)
    return result

def splitLinkInfoIntoRegions(linkInfo: int):
    eightBitPattern = 0b11111111
    sixteenBitPattern = 0xffff

    commaPattern = linkInfo & eightBitPattern
    crcPattern = (linkInfo >> 120) & eightBitPattern

    regionInfo = []
    for i in range(7): #14 eta regions per link
        regionInfo.append(
            (linkInfo >> (i*16)+8) & sixteenBitPattern
        )

    return regionInfo

    

def getEtiEtaiPhiFromRegionInfo(regionInfo, regionIndex, linkIndex):
    # 
    # energy derivation
    # 
    energyExtractPattern = 0b1111111111
    et = regionInfo & energyExtractPattern

    # 
    # region iEta + index derivation
    # 
    negativeLink = linkIndex % 2  == 0
    linkRegionNum = 6-regionIndex
    iEta = 0
    if negativeLink:
        iEta = linkRegionNum
    else:
        iEta = linkRegionNum+7

    # 
    # region iPhi + index derivation
    # 
    iPhi = linkIndex // 2

    return et, iEta, iPhi

def parseEventToRegions(event):
    regionArray = makeBlankRegions()
    eventInfo = []
    # First parse the event strings into a bunch of words that are ints
    for lineIndex, line in enumerate(event):
        event[lineIndex] = event[lineIndex].split('\t')[1:-1] #we don't need the event number or empty string we get at the end.
        for wordIndex, word in enumerate(event[lineIndex]):        
            event[lineIndex][wordIndex] = int(event[lineIndex][wordIndex], 16)

    # now we merge all 4 lines together to form a total event int per link
    # We should end up with 36 links worth of 128 bits transfered.
    for i in range(len(event[0])):
        eventInfo.append(
            event[0][i] | event[1][i] << 32 | event[2][i] <<32*2 | event[3][i] << 32*3
        )
    eventInfo.reverse() #flips the list so link 0 is at index 0

    for linkIndex, linkInfo in enumerate(eventInfo):
        linkRegionInfo = splitLinkInfoIntoRegions(linkInfo)
        for regionIndex, regionInfo in enumerate(linkRegionInfo):
            energy, iEta, iPhi = getEtiEtaiPhiFromRegionInfo(regionInfo, regionIndex, linkIndex)
            regionArray[iPhi][iEta] = energy

    return regionArray

def arrayToString(regionArray):
    resultString = ''
    for iPhi in range(18):
        for iEta in range(14):
            resultString += f'{regionArray[iPhi][iEta]:>4d}, '
        resultString += '\n'
    return resultString

def formEvents(fileContents):
    eventGroups = []
    for i in range(len(fileContents)//4):
        eventGroups.append(
            [
                fileContents[i*4],
                fileContents[(i*4)+1],
                fileContents[(i*4)+2],
                fileContents[(i*4)+3],
            ]
        )
    return eventGroups

def regionsToSyntax(regionEnergies):
    syntaxText = "cms.PSet(\n"
    for phiIndex in range(len(regionEnergies)):
        iPhi = phiIndex + 1
        syntaxText += f"\tiPhi_{iPhi} = cms.vuint32("
        for etaIndex in range(len(regionEnergies[phiIndex])):
            syntaxText += f'{regionEnergies[phiIndex][etaIndex]},'
        syntaxText+="),\n"
    syntaxText+="),"
    return syntaxText

def main(args):
    with open(args.fileToParse) as theFile:
        fileContents = theFile.read()
    fileContents = fileContents.split('\n')

    fileContents = deleteNonEventLines(fileContents)

    numberOfEvents = len(fileContents)//4
    eventsToProcess = numberOfEvents
    if args.maxEvents != None:
        eventsToProcess = min(numberOfEvents, args.maxEvents)
    console.print(f'Processing {eventsToProcess} events...')

    # each link in each line is 32 bits, we need to merge these together into groups of 4
    eventGroups = formEvents(fileContents)

    for eventIndex in range(eventsToProcess):
        regionEnergies = parseEventToRegions(eventGroups[eventIndex])
        arrayText = Text(arrayToString(regionEnergies))
        syntaxString = regionsToSyntax(regionEnergies)
        energySyntax = Syntax(syntaxString, 'python')
        renderGroup = Group(
            arrayText,
            energySyntax,
        )
        renderPanel = Panel(renderGroup,title=f'{eventIndex}')
        console.print(renderPanel)
        # console.print(arrayText)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Parse a text vector file into input that can be used at in the emulator")
    parser.add_argument(
        '-n',
        '--maxEvents',
        type=int,
        help='Pick the maximum amount of events to use for output, default: all of them'
    )
    parser.add_argument(
        'fileToParse',
        help='The text vector text file'
    )
    parser.add_argument(
        '--outputFile',
        '-o',
        help='File to'
    )

    args = parser.parse_args()
    main(args)