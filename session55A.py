#Ml Problems ->KERAS in Tensorflow

# Keras , a high level API to build and train the model
import tensorflow as tf
from tensorflow import keras


import numpy as np
import matplotlib.pyplot as plt
import os
os.environ['HDF5_DISABLE_VERSION_CHECK']='2'



os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#  Fashion DataSet-> 70 000 gray scale images , 10 categories
# eg shirts, boots , and resolution is 28 x 28  28 array with 28 elememts in each
#  Image classification | training  data and testing data

# 60 000  images -> to Train the Model
#  10 000 images -> to Test the Model

#  Exploring DataSet

fashionDataSet=keras.datasets.fashion_mnist

# create Training  and testing data
(train_images,train_labels), (test_images,test_labels)=fashionDataSet.load_data()
print(len(train_images),len(train_labels))
print(len(test_images),len(test_labels))


# labels-> 0 to 9
class_names=['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

print("===Training Image 0 ====")
print(train_images[0])
print(train_images[0].shape)
print(train_labels[0])
print(class_names[train_labels[0]])

print(train_images[3])
print(train_images[3].shape)
print(train_labels[3])
print(class_names[train_labels[3]])

# Just execute a loop and see some samples in  the dataset :)
plt.subplot(2,4,1)
plt.imshow(train_images[0],cmap=plt.cm.gray_r)

plt.subplot(2,4,2)
plt.imshow(train_images[3])

# obtaining values  between the  range of 0 to 1 | Fuzzy data

train_images=train_images/255.0
test_images=test_images/255.0

print(train_images[0])
print(train_images[3])

plt.show()

#  create ANN Mode;

#  in ANN , we have input layer, hidden layer , output layer
#  pass list of layers
inputLayer=keras.layers.Flatten(input_shape=(28,28))
hiddenLayer=keras.layers.Dense(32,activation=tf.nn.relu)
outputLayer=keras.layers.Dense(10,activation=tf.nn.softmax)

#   creating ann  model on layers
ann=[inputLayer,hiddenLayer,outputLayer]

model=keras.Sequential(ann)


#  COMPILING Model-> optimize, figure losses and accuracy
# https://towardsdatascience.com/adam-latest-trends-in-deep-learning-optimization-6be9a291375c
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# TRain the model
#  to acheive better accuracy, train the model again and again . epoch
model.fit(train_images,train_labels,epochs=5)


#  check for losses and accuracy of model
test_loss, test_acc=model.evaluate(test_images,test_labels)
print("Losses", test_loss)
print("Accuracy",test_acc)
print()

probability_model=tf.keras.Sequential([model,tf.keras.layers.Softmax()])
predictions=probability_model.predict(test_images)

print(np.argmax(predictions[0]),class_names[np.argmax(predictions[0])])
print(test_labels[0],class_names[test_labels[0]])

# Try getting datasets from google exploration for some images on flowers or animals
#  and see of you can predict

"""
Vehicle Detector using Convolutional Neural Networks
Making a Predictive Keyboard using Recurrent Neural Networks
Human Activity Recognition
Credit Card Fraud Detection using Autoencoders in Keras
"""


