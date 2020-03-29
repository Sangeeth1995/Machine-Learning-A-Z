#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 20:32:45 2020

@author: macbook
"""

#Importing Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Importing Dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:,1:2].values
y = dataset.iloc[:,2].values

#Feature Scaling
#from sklearn.preprocessing import StandardScaler
#sc_X = StandardScaler()
#sc_y = StandardScaler()
#X = sc_X.fit_transform(X)
#y = sc_y.fit_transform(y.reshape(-1, 1))

#Fitting DTR to the dataset
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X,y)

#Predicting a new result with DTR
y_pred = regressor.predict([[6.5]])


#Visualising the DTR  results on a more smoother curve
X_grid = np.arange(min(X),max(X),0.01)
X_grid = X_grid.reshape(len(X_grid),1)
plt.scatter(X,y,color='red')
plt.plot(X_grid,regressor.predict(X_grid),color='blue')
plt.title('Truth or Bluff (DTR)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()