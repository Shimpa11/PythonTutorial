import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

from sklearn import metrics
from sklearn.model_selection import train_test_split

# pip install statsmodel
import  statsmodels.api as sm

df=pd.read_csv("companies.csv")
print(df)

# plt.scatter(df['R&DSpend'],df['Profit'])
# plt.title('R&DSpend VS Profit', fontsize=14)
# plt.xlabel('R$DSpend',fontsize=14)
# plt.ylabel('Profit',fontsize=14)
# plt.show()
#
#
# plt.scatter(df['MarketingSpend'],df['Profit'])
# plt.title('MarketingSpend VS Profit',fontsize=14)
# plt.xlabel('Marketing',fontsize=14)
# plt.ylabel('Profit',fontsize=14)
# plt.show()

#  REgresssion
# X is dependent varibale
# represenrs x1 and x2 to determine y
X=df[['R&DSpend','MarketingSpend']]
Y=df['Profit']

print("X is",X)
print("Y is ",Y)

# solving the eqaution for multiple regression
# Y=b0+b1*R&DSpend+b2*MarketingSpend

# create a linear regression model
model=LinearRegression()

# split DAtAset
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=1)

# train the model with data
# X is basically x1 and x2
# model.fit(X,Y)
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print(y_pred)

# may not work for every model in the same manner
# percentage Score: how accurate  the model is?
# print("Accuracy Score: ",metrics.accuracy_score(y_test,y_pred))


print("Interceptor:",model.intercept_)
print("coefficients:",model.coef_)

print("Profit={}+{}*R&DSpend+{}*MarketingSpend".format(model.intercept_,model.coef_[0],model.coef_[1]))

RDSpend=144372.41
MKSpend=383199.62

predictedProfit=model.predict([[RDSpend,MKSpend]])
print(predictedProfit) # real value is 182901 | PRedicted Value is 173441.30
# PS: https://en.wikipedia.org/wiki/Linear_least_squares
# OLS, WLS, GLS | Statistical Mathematics :)

# Stats Model, adds up constants to our inputs to work
# print(X)
# print("==============")
X=sm.add_constant(X)
print("================")
print(X)

smModel=sm.OLS(Y,X).fit()   # Remember : input (Y), output(X) in API
predictions=smModel.predict(X)
printModel=smModel.summary()
print(printModel)