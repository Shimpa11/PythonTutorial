# https://en.wikipedia.org/wiki/Iris_flower_data_set

# sample dataset already there
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn import metrics

from sklearn.model_selection import train_test_split
irisData=load_iris()
print("====Iris Data======")
print(irisData)
print("Type of irisData is:", type(irisData))

print()

# # labeling with numeric values (0,1,2)
#
# # explore features in dataset
# # features are observations
# print(irisData.data)
#
# # explore target->  labels
# print(irisData.target)
#
#
# print(irisData.target_names)


# Explore Features in DataSet
print("===IRIS DATA FEATURES===")
print(irisData.data)

print()

# Explore Target in DataSet
print("===IRIS DATA TARGET===")
print(irisData.target)

print()

# Explore Target NAMES in DataSet
print("===IRIS DATA TARGET NAMES===")
print(irisData.target_names)


# create the model
x_train,x_test,y_train,y_test=train_test_split(irisData.data,irisData.target,test_size=0.3,random_state=1)

model=tree.DecisionTreeClassifier()

# training the model
model.fit(x_train,y_train)

# Lets test the model with sample imput/testing data
# inputData=[5.5,2.3,4.0,1.3]
# # passing data as a list in predict func
# predictedTarget=model.predict([inputData])
# print(predictedTarget)

# inputData1=[5.5,2.3,4.0,1.3]
# inputData2=[5.43, 3.9, 1.1, 0.32]
# predictedTargets=model.predict([inputData1],[inputData2])
# print(predictedTargets)

y_pred=model.predict(x_test)
print(y_pred)
print("accuracy score is with decision tree:",metrics.accuracy_score(y_test,y_pred))



import graphviz
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

data=tree.export_graphviz(model,out_file=None,feature_names=irisData.feature_names, class_names=irisData.target_names)

graph=graphviz.Source(data)
graph.render("IRIS DATASET DECISION TREE2")
graph.view()

# Train the DecisionTreeClassifier with DataSet as in Session40
# Try looking for APIs to convert the string dataset into numbered dataset

