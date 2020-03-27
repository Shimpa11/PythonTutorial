from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.naive_bayes import GaussianNB

from sklearn.model_selection import train_test_split
from sklearn import metrics
irisData=load_iris()
print("==IRIS DATASET===")
print(irisData)
print("type of iris data is:",(irisData))
print()

# explore features in dataset
print("==IRIS DATA FEATURES===")
print(irisData.data)
print()

# explore target in dataset
print("==IRIS DATA TARGET===")
print(irisData.target)
print()



# explore targetNames in dataset
print("==IRIS DATA TARGET NAMES===")
print(irisData.target_names)
print()
x_train,x_test,y_train,y_test=train_test_split(irisData.data,irisData.target,test_size=0.3,random_state=1)

# create the model
model=GaussianNB()
# training the model
model.fit(irisData.data,irisData.target)



# Lets Test The Model with a Sample Input
# inputData = [5.5, 2.3, 4.0,1.3]
# predictedTarget = model.predict([inputData])
# print(predictedTarget)

# inputData1=[5.5,2.3,4.0,1.3]
# inputData2 = [5.43, 3.90, 1.15, 0.32]
# predictedTargets=model.predict([inputData1,inputData2])
# print(predictedTargets)

y_pred=model.predict(x_test)
print(y_pred)

print("Accuracy score with Naive Bayes  is:",metrics.accuracy_score(y_test,y_pred))



