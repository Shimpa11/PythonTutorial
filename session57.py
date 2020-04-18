#Basic classification and NORMALIZATION OF DATA
import tensorflow as tf
# from tensorflow  import keras
# from tensorflow.contrib.keras.python.keras.models import Sequential
import tensorflow.contrib.keras as keras
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


df=pd.read_csv("covtype.csv")
print(df)

# Extract features from the Dataset
X=df[df.columns[:54]]#-> 0to 53

# Target variable(classes)
Y=df.Cover_Type

# Split the data
# same randomness in the program
x_train,x_test,y_train,y_test=train_test_split(X,Y,train_size=0.7,random_state=90)

# Create ANN Model
# Input layer| Hidden layer| Output layer

inputLayer=keras.layers.Dense(64,activation=tf.nn.relu,input_shape=(x_train.shape[1],))#-> shappe is number of features
hiddenLayer=keras.layers.Dense(32,activation=tf.nn.relu)
outputLayer=keras.layers.Dense(8,activation=tf.nn.softmax)#-> 8 classes to be predicted


ann=[inputLayer,hiddenLayer,outputLayer]
model=keras.Sequential(ann)

# Compiling the model
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

# Training the model
# training in 3 iterations each iterartion will have some results
history=model.fit(x_train,y_train,epochs=3,batch_size=60)

# History will contain the info about loss and accuracy
print("===HISTORY===")
print(history.history.keys())
print(history.history)

print("===Overall Metrics===")
#  Check for losses and Accuracy of the overall model
test_loss,test_acc=model.evaluate(x_test,y_test)
print("Loss:",test_loss)
print("Accuracy:",test_acc)

epochs=[1,2,3]
accuracyOverEpochs=history.history["accuracy"]

plt.plot(epochs,accuracyOverEpochs)
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.show()


# Making Predictions
probabilityModel=tf.keras.Sequential([model,tf.keras.layers.Softmax()])
predictions=probabilityModel.predict([x_test])

# List of probabilities
print(predictions[0])

# Class of Forest
print(np.argmax(predictions[0]))