#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import required libraries:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

# Read data
def read_data(source, debug=False):
    data = pd.read_csv(source)
    if debug==True:
        print(data.head())
    # Let's select some features to explore more :
    data = data[["ENGINESIZE","CO2EMISSIONS"]]
    return data

# Generating training and testing data from our data:
# We are using 80% data for training.
def gen_train_data(data, debug=False):
    train_data = data[:(int((len(data)*0.8)))]
    return train_data

def gen_test_data(data, debug=False):
    test_data = data[(int((len(data)*0.8))):]
    return test_data

# Plot scatter
def plot_scatter(data, debug=False):
    # ENGINESIZE vs CO2EMISSIONS:
    plt.scatter(data["ENGINESIZE"] , data["CO2EMISSIONS"] , color="blue")
    plt.xlabel("ENGINESIZE")
    plt.ylabel("CO2EMISSIONS")
    plt.show()

# Plot the regression line
def plot_regression_line(data, regr, debug=False):
    train = gen_train_data(data,debug)
    plt.scatter(train["ENGINESIZE"], train["CO2EMISSIONS"], color='blue')
    train_x = np.array(train[["ENGINESIZE"]])
    train_y = np.array(train[["CO2EMISSIONS"]])
    plt.plot(train_x, regr.coef_*train_x + regr.intercept_, '-r')
    plt.xlabel("Engine size")
    plt.ylabel("Emission")
    plt.show()


# Modeling:
# Using sklearn package to model data :
def model(data, debug=False):
    train = gen_train_data(data)
    regr = linear_model.LinearRegression()
    train_x = np.array(train[["ENGINESIZE"]])
    train_y = np.array(train[["CO2EMISSIONS"]])
    regr.fit(train_x,train_y)
    if debug==True:
        # The coefficients:
        print ("coefficients : ",regr.coef_) #Slope
        print ("Intercept : ",regr.intercept_) #Intercept
    return regr





# Predicting values:
# Function for predicting future values :
def get_regression_predictions(input_features,intercept,slope):
    predicted_values = input_features*slope + intercept
    return predicted_values

#################################
# MAIN
def main():
    debug=True

    data = read_data("https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/ML0101ENv3/labs/FuelConsumptionCo2.csv", debug)

    t = gen_test_data(data)
    plot_scatter(t)

    
    # Predicting emission for future car:
    my_engine_size = 3.5
    regr = model(data, debug)
    plot_scatter(data)
    plot_regression_line(data, regr)
    estimatd_emission = get_regression_predictions(my_engine_size,regr.intercept_[0],regr.coef_[0][0])
    print ("Estimated Emission :",estimatd_emission)
    # Checking various accuracy:
    if debug==True:
        from sklearn.metrics import r2_score
        test = gen_test_data(data)
        test_x = np.array(test[['ENGINESIZE']])
        test_y = np.array(test[['CO2EMISSIONS']])
        test_y_ = regr.predict(test_x)
        print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_ - test_y)))
        print("Mean sum of squares (MSE): %.2f" % np.mean((test_y_ - test_y) ** 2))
        print("R2-score: %.2f" % r2_score(test_y_ , test_y) )

if __name__ == "__main__":
    main()