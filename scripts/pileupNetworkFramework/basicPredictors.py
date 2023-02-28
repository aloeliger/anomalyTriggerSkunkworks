import argparse
from utilities.trainingDataset import trainingDataset

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.dummy import DummyRegressor
from sklearn import linear_model
from sklearn import svm
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor

import math

def evaluateRegressor(regressor, xTrain, yTrain, xVal, yVal):
    regressor.fit(xTrain, yTrain)
    performanceOnTrain = mean_squared_error(
        regressor.predict(xTrain),
        yTrain
    )
    performanceOnVal = mean_squared_error(
        regressor.predict(xVal),
        yVal
    )
    print(f'\t\tMSE Training: {performanceOnTrain:^8.3f} RMSE: {math.sqrt(performanceOnTrain):^8.3f}')
    print(f'\t\tMSE Validation: {performanceOnVal:^8.3f} RMSE: {math.sqrt(performanceOnVal):^8.3f}')

    return regressor

def main(args):
    theTrainingDataset = trainingDataset(args.trainingFile)
    xDataset, yDataset = theTrainingDataset.getTrainingData()

    xDataset = xDataset.reshape((-1,18*14))
    yDataset = yDataset.reshape((-1))

    print(xDataset.shape)
    print(yDataset.shape)

    xTrain, xVal, yTrain, yVal = train_test_split(
        xDataset,
        yDataset,
        test_size=0.3,
        random_state=1234
    )

    print('First testing some dummy estimators...')
    print('\tMean dummy regressor:')
    medianRegressor = evaluateRegressor(
        DummyRegressor(strategy='mean'),
        xTrain,
        yTrain,
        xVal,
        yVal
    )

    print('\tMedian dummy regressor')
    medianRegressor = evaluateRegressor(
        DummyRegressor(strategy='median'),
        xTrain,
        yTrain,
        xVal,
        yVal,
    ) 

    print('Testing Simple line estimators')
    print('\tNo regularization')
    noRegLine = evaluateRegressor(
        linear_model.LinearRegression(),
        xTrain,
        yTrain,
        xVal,
        yVal
    )
    print('\tRidge Regression: 0.25')
    ridgeSmall = evaluateRegressor(
        linear_model.Ridge(alpha=0.25),
        xTrain,
        yTrain,
        xVal,
        yVal,
    )
    print('\tRidge Regression: 0.75')
    ridgeLarge = evaluateRegressor(
        linear_model.Ridge(alpha=0.75),
        xTrain,
        yTrain,
        xVal,
        yVal,
    )

    print('Support vector machine')
    print('\tdefault')
    supportVectorReg = evaluateRegressor(
        svm.SVR(),
        xTrain,
        yTrain,
        xVal,
        yVal,
    )
    print('Gradient Boosted Trees')
    print('\t10 Estimators')
    tenGBReg = evaluateRegressor(
        GradientBoostingRegressor(n_estimators=10),
        xTrain,
        yTrain,
        xVal,
        yVal,
    )

    print('\t20 estimators')
    twentyGBReg = evaluateRegressor(
        GradientBoostingRegressor(n_estimators=20),
        xTrain,
        yTrain,
        xVal,
        yVal,
    )
    print('\tMax Depth 3')
    twentyGBReg = evaluateRegressor(
        GradientBoostingRegressor(max_depth=3),
        xTrain,
        yTrain,
        xVal,
        yVal,
    )
    print('\tMax Depth 6')
    twentyGBReg = evaluateRegressor(
        GradientBoostingRegressor(max_depth=6),
        xTrain,
        yTrain,
        xVal,
        yVal,
    )
    print('\tMin Samples per leaf 2')
    twentyGBReg = evaluateRegressor(
        GradientBoostingRegressor(min_samples_leaf=2),
        xTrain,
        yTrain,
        xVal,
        yVal,
    )
    print('\tMin Samples per leaf 5')
    twentyGBReg = evaluateRegressor(
        GradientBoostingRegressor(min_samples_leaf=5),
        xTrain,
        yTrain,
        xVal,
        yVal,
    )

    print("Random Forests")
    print('\t10 Estimators')
    tenGBReg = evaluateRegressor(
        RandomForestRegressor(n_estimators=10),
        xTrain,
        yTrain,
        xVal,
        yVal,
    )

    print('\t20 estimators')
    twentyGBReg = evaluateRegressor(
        RandomForestRegressor(n_estimators=20),
        xTrain,
        yTrain,
        xVal,
        yVal,
    )
    print('\tMax Depth 3')
    twentyGBReg = evaluateRegressor(
        RandomForestRegressor(max_depth=3),
        xTrain,
        yTrain,
        xVal,
        yVal,
    )
    print('\tMax Depth 6')
    twentyGBReg = evaluateRegressor(
        RandomForestRegressor(max_depth=6),
        xTrain,
        yTrain,
        xVal,
        yVal,
    )
    print('\tMin Samples per leaf 2')
    twentyGBReg = evaluateRegressor(
        RandomForestRegressor(min_samples_leaf=2),
        xTrain,
        yTrain,
        xVal,
        yVal,
    )
    print('\tMin Samples per leaf 5')
    twentyGBReg = evaluateRegressor(
        RandomForestRegressor(min_samples_leaf=5),
        xTrain,
        yTrain,
        xVal,
        yVal,
    )
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Test numerous more basic predictors for a PU predictor from calorimeter TPs')

    parser.add_argument(
        '--trainingFile',
        required=True,
        nargs='?',
        help='training file to read datasets from'
    )

    args = parser.parse_args()
    main(args)