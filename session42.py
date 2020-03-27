import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn import metrics
dataSet=pd.DataFrame()


dataSet['outlook']=['sunny','sunny','overcast','rainy','rainy','rainy',
                    'overcast','sunny','sunny','rainy','sunny',
                    'overcast','overcast','rainy']

dataSet['temperature']=['hot','hot','hot','mild','cool',
                      'cool','cool','mild','cool','mild',
                        'mild','mild','hot','mild']

dataSet['humidity']=['high','high','high','high','normal',
                     'normal','normal','high','normal','normal','normal',
                     'high','normal','high']

dataSet['windy']=['false','true','false','false','false',
                  'true','true','false','false','false','true','true',
                  'false','true']

# dataSet['play']=['no','no','yes','yes','yes','no',
#                  'yes','no','yes','yes','yes','yes','yes','no']
dataSet['play']=['cant play','cant play','can play','can play','can play','cant play',
                 'can play','cant play','can play','can play','can play','can play','yes','cant play']

print(dataSet)

# dummy variables(sometimes called as indicator variables), used to reperesent categorical data with numeric data
# ONE-HOT--technique in ML where categorical data to convert data into numric data

# fn get.dummies is used

# one col outlook is converted into three cols each col having one or zero
one_hot_data=pd.get_dummies(dataSet[['outlook','temperature',
                            'humidity','windy']])
print(one_hot_data)

X=one_hot_data
Y=dataSet['play']

x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.3,random_state=1)
# create the model
model=tree.DecisionTreeClassifier()


# training the model
# model.fit(one_hot_data,dataSet['play'])

model.fit(x_train,y_train)

# metrics for Decision TreeClassifier
# explore the api



y_pred=model.predict(x_test)
print("pridicted data",y_pred)
print("Accuracy score:",metrics.accuracy_score(y_test,y_pred))

# testing the data manually with these im=nputs
# outlook=sunny,temperature=hot,humidity=normal,windy=false
# predict can we play
inputData=[0,0,1,0,1,0,0,1,1,0]

predictedClass=model.predict([inputData])
print("predicted class for",inputData, "is:",predictedClass)

