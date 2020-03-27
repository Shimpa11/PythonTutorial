import pandas as pd
import numpy as np
import  matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn import metrics


df=pd.read_csv('kc_house_data.csv')
# print(df)
# df.hist('price',figsize=(8,5))
# plt.title('Number of houses vs Price')
# plt.ylabel('Number of Houses')
# plt.xlabel("Price")
# plt.show()
X=df['sqft_living']
Y=df['price']
# print(Y)

df['log_sqft_living'] = np.log(df['sqft_living'])
X1=df['log_sqft_living']
print(X1)
print(X)
print(Y)
#
# df.hist('log_price',figsize=(8,5))
# plt.title('Number of houses vs log(Price)')
# plt.ylabel('Number of Houses')
# plt.xlabel("log(Price)")
# plt.show()




# import statsmodels.api as sm
# from statsmodels.formula.api import ols
# f='price~sqft_living'
# model=ols(formula=f,data=df).fit()
# fig=plt.figure(figsize=(15,8))
# fig=sm.graphics.plot_regress_exog(model,'sqft_living',fig=fig)
#
# df['log_bedrooms'] = np.log(df['bedrooms'])
#
# f = 'log_price~log_sqft_living'
# model_log = ols(formula=f, data=df).fit()
#
# fig = plt.figure(figsize =(15,8))
# fig = sm.graphics.plot_regress_exog(model_log,'log_sqft_living', fig=fig)
#
# print(model.summary())
X=X[:,np.newaxis]
X1=X1[:,np.newaxis]
Y=Y[:,np.newaxis]

# x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.1,random_state=1)
# model=RandomForestRegressor(n_estimators=100)
x_train,x_test,y_train,y_test=train_test_split(X1,Y,test_size=0.1,random_state=1)
# x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.1,random_state=1)
model=LinearRegression()
# model.fit(X1,Y)
model.fit(x_train,y_train)


y_pred=model.predict(x_test)
print(y_pred)
print(x_test)

print("Accuracy score:",model.score(x_test,y_pred))

predictPriceToday=model.predict([[7.073270]])


print("Price today may be:",predictPriceToday)