from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
from numpy import array
import matplotlib.pyplot as plt
from scipy import stats
table=pd.read_csv("IPL-TEAMS-DATA.csv")
table1=table[table.teams=="Mumbai Indians"]
# print(table1)
# X=table1.year
# Y=table1.won
# print(X,X.shape)
# print(Y)

#
# X=X.reshape(len(X),1)
# Y=Y.reshape(len(Y),1)
X=[2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]
Y=[7,5,10,9,10,11,7,8,7,10,6,9]
# print(X,X.shape)

data=stats.linregress(X,Y)
print(data[0])
print(data[1])
#
maxX=max(X)
minY=min(Y)
#
x=np.linspace(minY,maxX,50)
y=data[1]+data[0]*x
X=array(X)
Y=array(Y)
X=X.reshape(len(X),1)
Y=Y.reshape(len(Y),1)

print(X,X.shape)
model=LinearRegression()
model.fit(X,Y)

X_new=[2020]
X_new=array(X_new)
X_new=X_new.reshape(len(X_new),1)
Y1=model.predict(X_new)

print("predicted output",Y1)

# plt.plot(x,y)
plt.scatter(X,Y)
plt.show()