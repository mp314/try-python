#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Machinelearing testing:
* Linear regression
"""

# Import required libraries:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import r2_score

# Read data
def read_data(source, debug=False):
    '''Read data'''
    data = pd.read_csv(source)
    if debug:
        print(data.head())
    # Let's select some features to explore more :
    data = data[["ENGINESIZE","CO2EMISSIONS"]] # pylint: disable=unsubscriptable-object
    return data

# Generating training and testing data from our data:
# We are using 80% data for training.
def gen_train_data(data, debug=False):
    '''Generate training dataset'''
    train_data = data[:(int((len(data)*0.8)))]
    if debug:
        print(train_data)
    return train_data

def gen_test_data(data, debug=False):
    '''Generate test dataset'''
    test_data = data[(int((len(data)*0.8))):]
    if debug:
        print(test_data)
    return test_data

# Plot scatter
def plot_scatter(data, title=None, debug=False):
    '''Plot scatter'''
    if debug:
        print(data)
    # ENGINESIZE vs CO2EMISSIONS:
    plt.scatter(data["ENGINESIZE"] , data["CO2EMISSIONS"] , color="blue")
    plt.title(title)
    plt.xlabel("ENGINESIZE")
    plt.ylabel("CO2EMISSIONS")
    plt.show()

# Plot the regression line
def plot_regression_line(data, regr, debug=False):
    '''Plot scatter + regression line'''
    train = gen_train_data(data,debug)
    plt.scatter(train["ENGINESIZE"], train["CO2EMISSIONS"], color='blue')
    train_x = np.array(train[["ENGINESIZE"]])
    #train_y = np.array(train[["CO2EMISSIONS"]])
    plt.plot(train_x, regr.coef_*train_x + regr.intercept_, '-r')
    plt.xlabel("Engine size")
    plt.ylabel("Emission")
    plt.show()


# Modeling:
# Using sklearn package to model data :
def model(data, debug=False):
    '''Model data'''
    train = gen_train_data(data)
    regr = linear_model.LinearRegression()
    train_x = np.array(train[["ENGINESIZE"]])
    train_y = np.array(train[["CO2EMISSIONS"]])
    regr.fit(train_x,train_y)
    if debug:
        # The coefficients:
        print ("coefficients : ",regr.coef_) #Slope
        print ("Intercept : ",regr.intercept_) #Intercept
    return regr





# Predicting values:
# Function for predicting future values :
def get_regression_predictions(input_features,intercept,slope):
    '''Predict regression'''
    predicted_values = input_features*slope + intercept
    return predicted_values

#################################
# MAIN
def main():
    '''Do some stuff'''
    debug=True

    data = read_data("https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/ML0101ENv3/labs/FuelConsumptionCo2.csv", debug)  # pylint: disable=line-too-long

    test_data = gen_test_data(data)
    plot_scatter(test_data, title="Test data")

    # Predicting emission for future car:
    my_engine_size = 3.5
    regr = model(data, debug)
    plot_scatter(data, title="Data")
    plot_regression_line(data, regr)
    estimated_emission = get_regression_predictions(
        my_engine_size,regr.intercept_[0],regr.coef_[0][0]
        )
    print (f"Estimated Emission : {estimated_emission:.2f}")
    # Checking various accuracy:
    if debug:
        test = gen_test_data(data)
        test_x = np.array(test[['ENGINESIZE']])
        test_y = np.array(test[['CO2EMISSIONS']])
        test_y_ = regr.predict(test_x)
        print(f"Mean absolute error: {np.mean(np.absolute(test_y_ - test_y)):.2f}")
        print(f"Mean sum of squares (MSE): {np.mean((test_y_ - test_y) ** 2):.2f}")
        print(f"R2-score: {r2_score(test_y_ , test_y):.2f}")

if __name__ == "__main__":
    main()
