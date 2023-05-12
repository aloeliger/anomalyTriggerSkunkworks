import argparse
from utilities.trainingDataset import trainingDataset

from sklearn.model_selection import train_test_split

from tensorflow import keras

def main(args):
    theTrainingDataset = trainingDataset(args.trainingFile)
    xDataset, yDataset = theTrainingDataset.getTrainingData()

    xTrain, xVal, yTrain, yVal = train_test_split(
        xDataset,
        yDataset,
        test_size=0.3,
        random_state=1234
    )

    model = keras.models.Sequential([
        keras.layers.InputLayer(input_shape=[18,14,1]),
        keras.layers.Conv2D(
            filters=4,
            kernel_size=(6, 2),
            padding="valid"
        ),
        keras.layers.ReLU(),
        keras.layers.LayerNormalization(),
        keras.layers.Conv2D(
            filters=16,
            kernel_size=2,
            padding="valid"
        ),
        keras.layers.ReLU(),
        keras.layers.MaxPooling2D(pool_size=3),
        keras.layers.Conv2D(
            filters=16,
            kernel_size=2,
            padding="valid"
        ),
        # keras.layers.MaxPooling2D(pool_size=2),
        # keras.layers.Conv2D(
        #     filters=32,
        #     kernel_size=2,
        #     padding="valid"
        # ),
        # keras.layers.ReLU(),
        # keras.layers.LayerNormalization(),
        # keras.layers.Conv2D(
        #     filters=64,
        #     kernel_size=2,
        #     padding="valid"
        # ),
        # keras.layers.ReLU(),
        keras.layers.GlobalMaxPooling2D(),
        keras.layers.Dense(16),
        keras.layers.ReLU(),
        keras.layers.Dense(12),
        keras.layers.ReLU(),
        keras.layers.Dense(8),
        keras.layers.ReLU(),
        keras.layers.Dense(1),
    ])

    model.compile(
        loss='mse',
        optimizer='nadam',
        metrics=[keras.metrics.RootMeanSquaredError()]
    )
    
    model.summary()

    reduceLR = keras.callbacks.ReduceLROnPlateau(
        monitor="val_loss",
        factor=0.5,
        patience=5,
    )
    earlyStop = keras.callbacks.EarlyStopping(
        monitor='val_loss',
        patience=10
    )
    bestModel = keras.callbacks.ModelCheckpoint(
        filepath='./pileupModel',
        monitor='val_loss',
        save_best_only=True
    )

    model.fit(
        xTrain,
        yTrain,
        epochs=30,
        validation_data=(xVal,yVal),
        callbacks=[
            reduceLR, 
            #earlyStop,
            bestModel,
        ]
    )

    model.summary()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='test basic convolutional PU ')

    parser.add_argument(
        '--trainingFile',
        required=True,
        nargs='?',
        help='training file to read datasets from'
    )

    args = parser.parse_args()
    main(args)
