from sklearn import datasets,svm
digits=datasets.load_digits()

from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn.model_selection import train_test_split
from  sklearn import metrics

# X rep image s, numpy array of rgb values which are graysclae


X=digits.data
# Y rep labels 0,1,2
Y=digits.target

# no of classes
print(digits.target_names)
print(X[0])
print(Y[0])

x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=1)



# scv is class in svn module
# create the model

# model=svm.SVC()
model=tree.DecisionTreeClassifier()
# model=GaussianNB()
# train the model
model.fit(x_train,y_train)

# inputImage=X[4]
#
# predictedClass=model.predict([X[11]])
# print(predictedClass)
y_pred=model.predict(x_test)
print(y_pred)
print("Accuracy score of decision tree:", metrics.accuracy_score(y_test,y_pred))
# print("Accuracy score Naive bayes:", metrics.accuracy_score(y_test,y_pred))
# print("Accuracy score of SVM:", metrics.accuracy_score(y_test,y_pred))