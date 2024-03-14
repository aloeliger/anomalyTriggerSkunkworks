import argparse
from rich.console import Console
import re
from pathlib import Path
import os
import hashlib
from rich.table import Table

console = Console()

def removeWhitespace(theString):
    return theString.replace(" ","").replace("\t", "").replace("\n","").replace("\r", "")

def hashFile(fileName):
    with open(fileName) as theFile:
        fileContent = theFile.read()
        fileContent = removeWhitespace(fileContent)
    hashFn = hashlib.new("sha256", fileContent.encode())
    theDigest = hashFn.hexdigest()
    return theDigest

def hashAllFiles(fileDict):
    hashDict = {}
    for name in fileDict:
        hashDict[name] = hashFile(fileDict[name])
    return hashDict

def main(args):
    filesToHash = {}
    if args.fileName is not None:
        filePath = Path(args.fileName)
        filesToHash = {
            filePath.name: filePath
        }
    elif args.directory is not None:
        for root, dirs, files in os.walk(args.directory):
            for fileName in files:
                filePath = Path(f"{root}/{fileName}")
                if filePath.suffix == '.vhd':
                    filesToHash [filePath.name] = filePath

    hashes = hashAllFiles(filesToHash)

    outputGrid = Table.grid(expand=True)
    outputGrid.add_column("File:",justify="left",no_wrap=True)
    outputGrid.add_column("Hash:",justify="right",no_wrap=True)

    fileNames = list(hashes.keys())
    fileNames.sort()

    for fileName in fileNames:
        outputGrid.add_row(fileName, hashes[fileName])
    console.print(outputGrid)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Check VHDL Files or directories for hashes to verify contents")

    targetGroup = parser.add_mutually_exclusive_group(required=True)

    targetGroup.add_argument(
        '-f',
        '--fileName',
        nargs='?',
        help='File to make a hash of',
    )
    targetGroup.add_argument(
        '-d',
        '--directory',
        nargs='?',
        help='Directory full of files to hash'
    )

    args = parser.parse_args()

    main(args)
