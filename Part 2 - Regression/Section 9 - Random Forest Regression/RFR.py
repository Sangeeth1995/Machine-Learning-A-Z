#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 10:49:06 2020

@author: macbook
"""
#Random Forest Regression

#Importing Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Importing Dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:,1:2].values
y = dataset.iloc[:,2].values


#Fitting RTR to the dataset
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 300 ,random_state = 0)
regressor.fit(X,y)

#Predicting a new result with RTR
y_pred = regressor.predict([[6.5]])


#Visualising the RTR  results on a more smoother curve
X_grid = np.arange(min(X),max(X),0.01)
X_grid = X_grid.reshape(len(X_grid),1)
plt.scatter(X,y,color='red')
plt.plot(X_grid,regressor.predict(X_grid),color='blue')
plt.title('Truth or Bluff (RTR)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()