import h5py
import numpy as np

class trainingDataset():
    def __init__(self, fileToRead: str):
        self.fileToRead = fileToRead

        with h5py.File(self.fileToRead, 'r') as self.theFile:
            self.TPData = np.array(self.theFile['TPs'][:])
            self.PUData = np.array(self.theFile['PU'][:])

    def getTrainingData(self):
        return self.TPData, self.PUData