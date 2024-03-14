import argparse
from rich.console import Console
import re
from pathlib import Path
import hashlib

console = Console()

def removeWhitespace(theString):
    return theString.replace(" ","").replace("\t", "").replace("\n","").replace("\r", "")

def main(args):
    projectAbsolutePath = Path(args.main).absolute()
    if not projectAbsolutePath.is_file():
        console.log(f":warning-emoji: -m/--main should be a file, but a file was not passed! exiting.", style="bold red")
        exit(1)
    weightsAbsolutePath = Path(args.weightsDirectory).absolute()
    if not weightsAbsolutePath.is_dir():
        console.log(f':warning-emoji: -w/--weightsDirectory should be a directory, but a directory was not passed! exiting.', style="bold red")
        exit(1)
    
    
    console.log(f'Using {projectAbsolutePath} as the main project file')
    with open(projectAbsolutePath, "r") as theFile:
        fileContents = theFile.read()
    #console.print(fileContents)
    textFilePattern=re.compile(r"(?<=\")\w+\.txt(?=\")")
    textFileMentions = textFilePattern.search(fileContents)

    weightFilesMentions = None
    if (textFileMentions is None):
        console.log(f':warning-emoji: Found no weights file mentions!', style="bold red")
        exit(2)
    else:
        weightFilesMentions = textFilePattern.findall(fileContents)
        
    console.log("Mentioned weights:")
    console.log(weightFilesMentions)

    weightFilesToUse = []
    for weightFileName in weightFilesMentions:
        filePath = weightsAbsolutePath / f'{weightFileName}'
        if not filePath.exists():
            console.log(f"Weight file: {filePath} does not exist in the weights directory. Skipping...")
            continue
        else:
            weightFilesToUse.append(filePath)
    
    if weightFilesToUse == []:
        console.log(":warning-emoji: Failed to find any weights to use!", style='bold red')
        exit(3)
    
    weightFilesToUse.sort()
    console.log(f'Using files (in order):')
    console.log(weightFilesToUse)

    totalWeightContent = ''
    for fileName in weightFilesToUse:
        console.log(f'Reading: {fileName}')
        with open(fileName) as theWeightFile:
            fileContent = theWeightFile.read()
            #strip any whitespace disagreement.
            fileContent = removeWhitespace(fileContent)
            totalWeightContent += fileContent
    #console.log(totalWeightContent)
    hashFn = hashlib.new("sha256", totalWeightContent.encode())
    theDigest = hashFn.hexdigest()
    console.print()
    console.print("CICADA thumbprint:")
    console.print(theDigest)
    console.print()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Check a cicada main file for weights used, and then check the weights to create a hash of model weights")

    parser.add_argument(
        "-m",
        "--main",
        required=True,
        nargs='?',
        help="Main cicada project file to search for the used weights"
    )

    parser.add_argument(
        '-w',
        "--weightsDirectory",
        required=True,
        nargs='?',
        help="CICADA weights directory to process into a hash",
    )

    args = parser.parse_args()

    main(args)
