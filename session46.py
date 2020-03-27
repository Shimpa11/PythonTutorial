"""Decision Trees
1.as Classifier for categorical data hwre predictions are classes
2. as Regressor
for numerical data , where predictions are numerical or continous data
Tree has  nodes and branches decicion made at node and data spiltted Left or right

leaf nodes carry the results
split the data on gender , thats kind of classification and futher how many play cricket, thats a kind of regression

four parameter-> Entropy, Information gain   chi square
gini index-->if we select two items randomly from a population,
 both have same class and probability for this is 1 if population/dataset is pure
chi sq-> diff of info between sub nodes and parent nodes
info gain-> decrease in randomness
entropy-> randomnsess in data
to decide which attribute has more information to make the decision tree


working on Gini Index
eg categorical data->  either target as play or no play,
success or failure, positive or negative

for numerical datasets
calculation of gini index

total 30 students-> 10F(2 play crik) and 20M(13 play crik)
sum of sq of probabality of success p(S) and failure p(F)
p(s)*P(s) +p(f)*P(f)

for female node
success->20% and failure->80%
prob-> P(s)0.20 ans P(f) is 0.80

for male node
success->65% and failure->35%
prob-> P(s)0.65 ans P(f) is 0.35

Gini for attribute gender
Female:(0.20*0.20)+(0.80*0.80)=0.68
male:(0.65*0.65)+(0.35*0.35)=0.55

Calculate weigted Gini for Gender split
(10/30)*0.68 +(20/30)*0.55=0.59


calculate weigted gini for every attribute

for class  IX and  X
14 and 16 play cricket
43% and 56%
S       S

0.43*0.43+0.57*0.57=0.50

0.56*0.56+0.44*0.44=0.507
Calculate weigted Gini for Class split
14/30*0.50 +16/30*0.507=0.233+0.270=0.51

Gini Impurity=1-Gini

Chi Square->
shall find out statistical difference between sub nodes(children node) and parent node

Calculation:
2 nodes: F and M
Nodes   Play Cricket not play Cricket   Total  ExpectedPlay ExpectedNotPlay(50%)
Female      2           8                10F      5               5
MAle        13          7                20M      10              10

Nodes   DeviationPlay   DeviationNotPlay (not play- ExpectedNotPlay)
Female      2-5=-3          8-5=3
Male        13-10=3         7-10=-3

Chi square of node: sqrt (((Actual-Expected)*(Actual-Expected))/Expected)
nodes    PlayCricket                           NotPlayCricket
Female   2-5=-3  sqrt((-3)*(-3)))/5=1.34               sqrt((3*3)/5)=1.34
Male            0.95                                      0.95

Total Chi square for Attribute Gender= 1.34+1.34+0.95+0.95=4.58


for class:

Nodes   Play Cricket not play Cricket   Total  ExpectedPlay ExpectedNotPlay(50%)
Female      6          8                14F      7              7
MAle        9         7                16M        8

Nodes   DeviationPlay   DeviationNotPlay (not play- ExpectedNotPlay)
Female      6-7=-1         8-7=1
Male        9-8=1           7-8=-1


Chi square of node: sqrt (((Actual-Expected)*(Actual-Expected))/Expected)
nodes    PlayCricket                           NotPlayCricket
Female    sqrt((-1)*(1)))/7=     0.377          sqrt((1*1)/7)=0.37
Male            1*(-1) /8       =0.35                       0.35

Total Chi square for Attribute Class= 0.38+0.38+0.35+0.35=1.45





"""
import  pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn import datasets
import matplotlib.pyplot as plt
#
# bostonDataSet=datasets.load_boston()
# print(bostonDataSet)

df=pd.read_csv("corona-india-cases.csv")
print(df)

X=df["Day"].values
Y=df["Cases"].values

# transform the data X and Y 1D to 2D
X=X[:,np.newaxis]
Y=Y[:,np.newaxis]

model=DecisionTreeRegressor()
model.fit(X,Y)
predictedY=model.predict(X)
print("Original cases")
print(Y)
print("Predicted cased for the  model")
print(predictedY)

print("Model score:", model.score(X,predictedY))
predictCasesToday=model.predict([[15]])
print("cases today may be:",predictCasesToday)

plt.figure(figsize=(16,8))
plt.scatter(X,Y,color='red')
plt.plot(X,predictedY,color="green")
plt.xlabel("Days")
plt.ylabel("Cases")
plt.show()

# pydotplus

import graphviz
import os
from sklearn import tree
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'


data=tree.export_graphviz(model,out_file=None)
graph=graphviz.Source(data)
graph.render("CRICKET DATASET DECISION TREE")
graph.view()