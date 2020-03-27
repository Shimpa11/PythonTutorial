# PyDotPlus is an improved version of the old pydot project that
# provides a Python Interface to Graphviz's Dot language.

import pydotplus
import  pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import  tree
import matplotlib.pyplot as plt
#
# bostonDataSet=datasets.load_boston()
# print(bostonDataSet)

df=pd.read_csv("corona-india-cases.csv")
# df=datasets.load_boston()
# df=datasets.load_diabetes()

print(df)

X=df["Day"].values
Y=df["Cases"].values

# transform the data X and Y 1D to 2D
X=X[:,np.newaxis]
Y=Y[:,np.newaxis]

# feature_names: ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']
# print(df['feature_names'])
# print(df.data)
# print(df.target)




# plt.figure(figsize=(16,8))
# plt.scatter(X,Y,color='red')
# plt.plot(X,predictedY,color="green")
# plt.xlabel("Days")
# plt.ylabel("Cases")
# plt.show()


x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.3,random_state=1)
model=tree.DecisionTreeClassifier()
# model=DecisionTreeRegressor()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)

print(y_pred)
print("Accuracy Score:", metrics.accuracy_score(y_test,y_pred))
# print(model.score(X,y_pred))

#
import graphviz
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'


data=tree.export_graphviz(model,out_file=None)
graph=graphviz.Source(data)
graph.render("IRIS DATASET DECISION TREE3")
graph.view()