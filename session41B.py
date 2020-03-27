import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np
dataSet=pd.DataFrame()



#
# #Import the CSV file into Python using read_csv() from pandas
# dataframe = pd.read_csv("data_pandas1.csv")

# #Create the dictionary of key-value pair, where key is
# #your old value(string) and value is your new value(integer).
# Recommendation = {'Buy': 1, 'Hold': 2, 'Underperform': 3}

# #Assign these different key-value pair from above dictiionary to your table
# dataframe.Recommendation = [Recommendation[item] for item in dataframe.Recommendation]
# #New table
# print(dataframe)

dataSet['outlook']=['sunny','sunny','overcast','rainy','rainy','rainy',
                    'overcast','sunny','sunny','rainy','sunny',
                    'overcast','overcast','rainy']


dataSet.outlook[dataSet.outlook=='sunny']=0
dataSet.outlook[dataSet.outlook=='overcast']=1
dataSet.outlook[dataSet.outlook=='rainy']=2
print(dataSet)
dataSet['temperature']=['hot','hot','hot','mild','cool',
                      'cool','cool','mild','cool','mild',
                        'mild','mild','hot','mild']
dataSet.temperature[dataSet.temperature=='hot']=0
dataSet.temperature[dataSet.temperature=='cool']=1
dataSet.temperature[dataSet.temperature=='mild']=2


dataSet['humidity']=['high','high','high','high','normal',
                     'normal','normal','high','normal','normal','normal',
                     'high','normal','high']

dataSet.humidity[dataSet.humidity=='high']=0
dataSet.humidity[dataSet.humidity=='normal']=1


dataSet['windy']=['false','true','false','false','false',
                  'true','true','false','false','false','true','true',
                  'false','true']

dataSet.windy[dataSet.windy=='false']=0
dataSet.windy[dataSet.windy=='true']=1
#
dataSet['play']=['no','no','yes','yes','yes','no',
                 'yes','no','yes','yes','yes','yes','yes','no']


dataSet.play[dataSet.play=='no']=0
dataSet.play[dataSet.play=='yes']=1


print(dataSet)

column=['outlook','temperature','humidity','windy']
X=dataSet[column]
Y=dataSet['play']
Y=Y.astype(int)
# Y=diabetesDataSet.label

print("==Features======")
print(X,type(X))
print("=====Labels=====")
print(Y)

x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.3,random_state=1)

model=tree.DecisionTreeClassifier()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print(y_pred)
print("Accuracy score:",metrics.accuracy_score(y_test,y_pred))

import graphviz
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
# Export/Print a decision tree in DOT format.

#Create Dot Data
data=tree.export_graphviz(model,out_file=None)
graph=graphviz.Source(data)
feature_names=list(column)
class_names=['Not_Play', 'Play'],

#Create Graph from DOT data



graph.render(" weather DECISION TREE")
graph.view()

