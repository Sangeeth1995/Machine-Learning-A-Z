#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 19:53:12 2020

@author: macbook
"""
#Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Importing Dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:,3].values


#Taking care of missing Data
#from sklearn.preprocessing import Imputer
#imputer = Imputer(missing_values="NaN", strategy="mean", axis=0)
#imputer = imputer.fit(X[:,1:3])
#X[:,1:3] = imputer.transform(X[:,1:3])
from sklearn.impute import SimpleImputer 
imputer = SimpleImputer(missing_values=np.nan, strategy="mean", fill_value=None) 
X[:,1:3] = imputer.fit_transform(X[:,1:3])



#Encoding Categorical Data
#from sklearn.preprocessing import LabelEncoder,OneHotEncoder
#X[:,0] = LabelEncoder().fit_transform(X[:,0])
#ohe = OneHotEncoder(categorical_features = [0])
#X = ohe.fit_transform(X).toarray()
#Y = LabelEncoder().fit_transform(Y)
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
ct = ColumnTransformer([('encoder', OneHotEncoder(categories='auto'), [0])], remainder='passthrough')
X = np.array(ct.fit_transform(X), dtype=np.float)
from sklearn.preprocessing import LabelEncoder
Y = LabelEncoder().fit_transform(Y)

#Splitting the dataset into training set and testing set
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=0)

#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)




