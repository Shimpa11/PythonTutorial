
# PLoynomail Regression / Quadratic  Regression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('speeds.csv')
print(df)

X=df['hour'].values
Y=df['speed'].values

#  to validate sample input size and output size
# print(len(X),len(Y))

# 3 for cubic equation
npModel=np.poly1d(np.polyfit(X,Y,3))

print(npModel)
# Taking some 100 unknown data points between hour 1 to 24
LinearInputPoints=np.linspace(1,24,100)
print(LinearInputPoints)
print()

# for 100 unknown datapoints, we got predicred output in the form oof speed
predictedOutput=npModel(LinearInputPoints)
print(predictedOutput)

plt.scatter(X,Y,color='orange')
plt.plot(LinearInputPoints,predictedOutput,color='green')
plt.show()



# for sklearn model, we need to tranform X and Y
