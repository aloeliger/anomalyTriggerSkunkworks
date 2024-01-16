import argparse
import datetime
import subprocess
import os

parser = argparse.ArgumentParser(description='submit the l1 ntuple configuration for MC')
parser.add_argument(
    '--fileList',
    '-f',
    required=True,
    type=str,
    nargs='?',
    help='List of files to perform the L1 ntuplification on',
)
parser.add_argument(
    '--jobID',
    '-i',
    type=str,
    nargs='?',
    help='Unique string to insert into the job name to identify it',
)

args = parser.parse_args()

todaysDate = datetime.datetime.now().strftime('%d%b%Y_%H%M')

if args.jobID != None:
    jobName = f'L1Ntuples_{args.jobID}_{todaysDate}'
else:
    jobName = f'L1Ntuples_{todaysDate}'

nfs_location = f'/nfs_scratch/aloeliger/L1Ntuples/{jobName}/'
dag_location = f'{nfs_location}/dags/'
os.makedirs(dag_location, exist_ok=True)
submit_location = f'{nfs_location}/submit/'
output_dir = f'/store/user/aloeliger/L1Ntuples/{jobName}/'
config=f'{os.environ["CMSSW_BASE"]}/src/anomalyDetection/anomalyTriggerSkunkworks/python/newFrameworkNtuplization/l1NtupleFromMCSkim.py'

farmout_command = [
    'farmoutAnalysisJobs',
    f"--submit-dir={submit_location}",
    f"--output-dir={output_dir}",
    f"--output-dag-file={dag_location}/dag",
    "--use-singularity CentOS7",
    "--memory-requirements 4000",
    f"--input-file-list={args.fileList}",
    f'{jobName}',
    f'{os.environ["CMSSW_BASE"]}',
    config,
    "\'outputFile=$outputFileName\'",
    "\'inputFiles=$inputFileNames\'"
]

farmout_command = ' '.join(farmout_command)

print('Farmout command:')
print(farmout_command)

finishedProcess = subprocess.run(
    [farmout_command],
    shell=True,
    check=True,
)