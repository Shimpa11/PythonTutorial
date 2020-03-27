# working on covid 19 dataset

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PowerTransformer
df=pd.read_csv("covid19-world.csv")
print(df)

indiaDF=df[df['Country']=='India']
print(indiaDF)


X=indiaDF['Date'].values
cases=indiaDF['Confirmed'].values

print("data for X:",X)
print("Data for Y:",cases)
# plt.plot(X,Y)
# plt.xlabel("Date")
# plt.ylabel("Confirmed cases")
# plt.grid(True)
# plt.show()


# formatting date for our graph
# fig,ax=plt.subplot()
# ax.plot_date(X,Y, marker='',linestyle="-.")
# fig.autofmt_xdate()
# plt.show()

# create the model
# 100 DTrees in our model who shall work with bagging technique

# as per data preprocessing, we will convert date into day of year to make it a number

days=[]
for date in X:
    print(date)
    print(pd.Period(date,freq='D').dayofyear)
    days.append(pd.Period(date,freq='D').dayofyear)
days=np.array(days)

print(days)


#     solve the above use case with lambdas
# 100 Decision trees
model=RandomForestRegressor(n_estimators=100)

days=days[:,np.newaxis]

x_train,x_test,y_train,y_test=train_test_split(days,cases,test_size=0.2,random_state=1)

# train the model with X and cases as Y
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print(x_test)
print(y_pred)
print("=======================")
futurePredictionsDays=np.array([12,24,48,61,96,120])
futurePredictionsDays=futurePredictionsDays[:,np.newaxis]

futureConfirmedCasesPredictions=model.predict(futurePredictionsDays)
print(futurePredictionsDays)
print(futureConfirmedCasesPredictions)
# Conclusion : Predictions are not accurate.
# Since as per our dataset, we do have exponential behaviour in our data.
# So we need to do some more of pre-processing
