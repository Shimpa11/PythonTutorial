import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
import numpy as np

# Analyzing data
df=pd.read_csv("titanic.csv")
print(df)
print("number of passengers", str(len(df.index)))

# sns.countplot(x='Survived',data=df)

# sns.countplot(x='Survived', hue= 'Sex',data=df)
# sns.countplot(x='Survived', hue= 'Pclass',data=df)
# df['Age'].plot.hist(figsize=(5,4))
# df.info()
#
# plt.show()


# Data wrangling

# False for where the value id not none
# True where the value is none

print(df.isnull())

# no of passengers who have Nan value in ecjh col
print(df.isnull().sum())
hp=df.isnull()

# The heatmap is a way of representing the data in a 2-dimensional form.
# The data values are represented as colors in the graph.
# The goal of the heatmap is to provide a colored visual summary of information.
# sns.heatmap(hp,yticklabels=False,cmap="BuGn")

# passengers in class 1 and 2 tend to be older
# sns.boxplot(x='Pclass',y='Age',data=df)
# plt.show()

print(df.head(5))
df.drop('Cabin',axis=1,inplace=True)
print(df.head(5))

# sns.heatmap(df.isnull(),yticklabels=False,cbar=False)
# plt.show()

# df.dropna(inplace=True)
# sns.heatmap(df.isnull(),yticklabels=False,cbar=False)
# plt.show()

# print(df.isnull().sum())

# converting categorical variabble into dummy values
sex=pd.get_dummies(df['Sex'],drop_first=True)
print(sex.head(5))
# keeping on;ly one col-> drop

embark=pd.get_dummies(df['Embarked'],drop_first=True)
print(embark.head(5))



pcl=pd.get_dummies(df['Pclass'],drop_first=True)
print(pcl.head(5))

# cncatenate all col into dataset
df=pd.concat([df,sex,embark,pcl],axis=1)
print("New set")
print(df.head(5))

print(df.drop(['Sex','Embarked','PassengerId','Name','Age','Fare','Ticket'],axis=1,inplace=True))

# Training and testing data

X=df.drop('Survived',axis=1)
print(X)

# X=X[:,np.newaxis]
print()
Y=df['Survived']
print(Y)

x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.3,random_state=1)

model=LogisticRegression()

# model.fit(X,Y)
model.fit(x_train,y_train)

predictions=model.predict(x_test)
# predictions=model.predict(X)
print(predictions)

print("Accuracy score", accuracy_score(y_test,predictions))
CR=classification_report(y_test,predictions)
print(CR)

confM=confusion_matrix(y_test,predictions)
print(confM)


# print("Accuracy score", accuracy_score(Y,predictions))
# CR=classification_report(Y,predictions)
# print(CR)
#
# confM=confusion_matrix(Y,predictions)
# print(confM)


dfConfMatrix = pd.DataFrame(confM)
print(dfConfMatrix)
sns.heatmap(dfConfMatrix)
plt.show()

