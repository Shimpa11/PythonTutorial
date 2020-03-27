from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pandas as pd
table=pd.read_csv("advertising.csv")
X=table.TV.values
Y=table.Sales.values

print(Y)

# X and Y are 1-D Arrays | 200, 0
# print(X,X.shape)
# print(Y,Y.shape)

# scikit works on 2d array
X=X.reshape(len(X),1)
Y=Y.reshape(len(Y),1)

# # converted X and Y as 200,1
# print(X,X.shape)
# print(Y,Y.shape)

model=LinearRegression()
model.fit(X,Y)

b0=model.intercept_
b1=model.coef_
print("Intercept is: ",b0)
print("coefficient is: ",b1)
Y1=model.predict(X)

print(Y1,Y1.shape)

score=r2_score(Y,Y1)
print("R2 score is: ",score)
print("Equation of line: Y={}+{}X".format(b0,b1))

