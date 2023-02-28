from tensorflow import keras
import argparse
import os

def convertModel(fileName):
    assert('.hdf5' in fileName), f"fileName was not an .hdf5: {fileName}"
    theModel = keras.models.load_model(fileName)
    outputName = fileName
    if '/' in fileName:
        outputName = outputName.split('/')[-1]
    outputName = outputName.split('.')[0]
    theModel.save(outputName)

def main(args):
    convertModel(args.file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Take an HDF5 model and transform it into a saved model format')

    parser.add_argument(
        '-f',
        '--file',
        nargs='?',
        required=True,
        help='.hdf5 model to turn into saved model format'   
    )

    args = parser.parse_args()

    main(args)