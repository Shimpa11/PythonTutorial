from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

df=pd.read_csv("covid19-world.csv")
print(df)


X=df['Confirmed']
Y=df['Recovered']
nozero=['Confirmed','Recovered']
# X1=pd.to_datetime(X,infer_datetime_format=True)
for col in nozero:
    df[col]=df[col].replace(0,np.NaN)

    mean=int(df[col].mean(skipna=True))
    df[col]=df[col].replace(np.NaN,mean)

# transform
X1=df[col]
print(X1)
X1=X1[:,np.newaxis]
Y=Y[:,np.newaxis]

x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.3,random_state=1)
model=KNeighborsClassifier()
# model.fit(X,Y)
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
# print(y_pred)