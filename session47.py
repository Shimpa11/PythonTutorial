"""
overfitting  and underfitting->regression line does not fit
# predicted values
# good fit / robust fit
# DT limitations
# computationally expensive to train
# carry big risk if overfitting

ENSEMBLE LEARNING
Supervised learning where no of models are combined for prediction

BOOSTING->grp of algos that utilizes weighted avgs to make weak learners into stronger learners
each model predicts the feature for next model
kind synchronus
BOOTSTRAP AGGREGATION(BAGGING)
Running models independently and aggregates output at the end without pref to other model
Ansync or multuthreading


Random Forest Algorithn
->classification and regression
a bagging technique
moedls running parallel with no interaction
tress in RF
operates by constructing a mutltitude of DT at training time and outputting the class is the
model of classes
1.how many DTtrees to be used
2. Dataset to be divided in n number of instances
eg; dataset with 100 records
choose  n as 3
T1=33
T2=33
T3->34
three DTrees
predictions from T1, T2 and T2 will be used  for final prediction
"""
# working on covid 19 dataset

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
from sklearn.preprocessing import  FunctionTransformer
df=pd.read_csv("covid19-world.csv")
print(df)

indiaDF=df[df['Country']=='India']
print(indiaDF)

X=indiaDF['Date']
Y=indiaDF['Confirmed']
# log=PowerTransformer()
# log.fit(df[['Date']])
# df['log_convertedDF']=log.transform(df[['Date']])
# X=df['log_convertedDF']
print("data for X:")
print(X)
print("Data for Y:")
print(Y)



# plt.plot(X,Y)
# plt.xlabel("Date")
# plt.ylabel("Confirmed cases")
# plt.grid(True)
# plt.show()


# formatting date for our graph
fig,ax=plt.subplots()
ax.plot_date(X,Y, marker='',linestyle="-.")
fig.autofmt_xdate()
plt.show()

# create the model
# 100 DTrees in our model who shall work with bagging technique
model=RandomForestRegressor(n_estimators=100)

# train the model
# transform into 2D array
# X=X[:,np.newaxis]
# date is in string format cannot  train  model on string
# so we get an error
# So we data Preprocessing-> refining dataset so optimally so that model works perfectly fine

# new transformation

X1=pd.to_datetime(indiaDF['Date'],infer_datetime_format=True)

print(type(X1))

# lg=np.log(indiaDF['Date'])
# X1=pd.to_datetime(indiaDF['Date'],format='%Y-%m-%d')


# converting date type string to datetime which is mathematical


X1=X1[:,np.newaxis]

print(X1)
print()
print(type(X1))

# model.fit(X,Y)-> generates error withX

x_train, x_test, y_train,y_test=train_test_split(X1,Y,test_size=0.2,random_state=1)
# model.fit(X1,Y)
model.fit(x_train,y_train)


# X=sm.add_constant(X)
# model=sm.OLS(y_train,X)
print("Model Trained")
y_pred=model.predict(x_test)
# print(y_pred)
# print(x_test)
#


futurePredictionDates=pd.Series(['2020-02-12','2020-03-12','2020-04-12','2020-05-12'])
futurePredictionDates=pd.to_datetime(futurePredictionDates,infer_datetime_format=True)

print("==========================================")
# 2D array
futurePredictionDates=futurePredictionDates[:,np.newaxis]
futureConfirmedPredictions=model.predict(futurePredictionDates)
print(futurePredictionDates)
print(futureConfirmedPredictions)

# regression model is lagging  because predictions are not accurate as data is exponential not linear

# Conclusion : Predictions are not accurate.
# Since as per our dataset, we do have exponential behaviour in our data.
# So we need to do some more of pre-processing

