
# PLoynomail Regression / Quadratic  Regression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error,r2_score


df=pd.read_csv('speeds.csv')
print(df)

X=df['hour'].values
Y=df['speed'].values

#
# # transforming data into 2d array

# ReShape Data so as to train the Mode with 2-D Array
# Transforming 1-D Array into 2-D Array
# X=X.reshape(len(X),1)
# Y=Y.reshape(len(Y),1)

#  transform with numpy
X=X[:,np.newaxis]
Y=Y[:,np.newaxis]

# for sklearn, to work on polynomialLinear Regression use PolynomialFeatuesto transform
polyFeatures=PolynomialFeatures(degree=2)

# changing data into polynomial dataset
polyX=polyFeatures.fit_transform(X)

# transform the data for model
model=LinearRegression()
# err as X and Y needs to be transformed as this is 1d array
# model.fit(X,Y)
model.fit(polyX,Y)
y_pred=model.predict(polyX)
b0=model.intercept_
b1=model.coef_

print("interceptor:",b0)
print("coefficient:",b1)

rootMeanSquareError=np.sqrt(mean_squared_error(Y,y_pred))
r2=r2_score(Y,y_pred)
print("rootMeanSquareError:",rootMeanSquareError)
print("r2:",r2)