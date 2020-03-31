import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# then model predicts, purchase is made by male or female

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score


dataSet=pd.read_csv("purchases.csv")
print(dataSet)

# sns.countplot("Gender",hue="Purchased",data=dataSet)

sns.countplot("Age",hue="Purchased",data=dataSet)
plt.show()
X=dataSet.drop("Gender",axis=1)
Y=dataSet["Gender"]

print(X)
print(Y)

x_train, x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=1)
# create the model
model=LogisticRegression()

# train the model
model.fit(x_train,y_train)

# make predictions
predictions=model.predict(x_test)
print(y_test)  #  expected ouput
print(predictions)  # predicted output

print("Accuracy Score",accuracy_score(y_test,predictions))

# Classification reports
classificationReport=classification_report(y_test,predictions)
print(classificationReport)

"""
classificationReport displays 
precision->level upto which predictions made by model are precise
recall-> amount upto which the model can predict the outputs
 f1score and support-> amount of data tested for the  prediction

"""

# Confusion Matrix
"""
kind of table tat describes performance of prediction model
contains actual values and predicted values
 data in the matrix cab be used to compute the  accuracty score


"""


matrix=confusion_matrix(y_test,predictions)
print(matrix)


# changing data into numerical data , work on purchase column as output to be predicted
# ctrl r, replace


# HEAT MAP draw the same using seaborn, what it represents

# links on which we can tetst for self examination based on various inputs
#  write logistic regression model to predict

dfConfMatrix=pd.DataFrame(confusion_matrix(y_test,predictions))
print(dfConfMatrix)

sns.heatmap(dfConfMatrix)
plt.show()