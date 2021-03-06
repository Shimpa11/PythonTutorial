import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
import numpy as np
import pil
from pil import Image
# import image as Image

# Tensorflow Hub: https://tfhub.dev/

# Tensorflow Hub shall give us pre trained model URLs
classifierUrl = "https://tfhub.dev/google/tf2-preview/mobilenet_v2/classification/4"
imageUrl = "https://storage.googleapis.com/download.tensorflow.org/example_images/grace_hopper.jpg"
labelsUrl = "https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt"

IMAGE_SHAPE=(224,224)
INPUT_IMAGE_SHAPE=(224,224,3)
# Deep Learning model from TF HUB
model=tf.keras.Sequential([hub.KerasLayer(classifierUrl,input_shape=INPUT_IMAGE_SHAPE)])
print(model.summary())

# read the Image from URL
graceHopperImage=tf.keras.utils.get_file('image.jpg',imageUrl)
graceHopperImage=Image.open(graceHopperImage).resize(IMAGE_SHAPE)
print(graceHopperImage)

# Image preprocessing for deep learming model Input

graceHopperImage=np.array(graceHopperImage)/255.0
print(graceHopperImage.shape)

# read the Labels and store them in a list
labelPath=tf.keras.utils.get_file("ImageNetLabels.txt",labelsUrl)
labels=np.array(open(labelPath).read().splitlines())
print(labels)

# Lets Use the Model for making predictions
result = model.predict(graceHopperImage[np.newaxis, :])
predictedClassLabelIdx= np.argmax(result[0], axis=-1)
print("PREDICTED LABEL INDEX :", predictedClassLabelIdx)
print("PREDICTED LABEL:", labels[predictedClassLabelIdx])

plt.imshow(graceHopperImage)
plt.title(labels[predictedClassLabelIdx])
plt.show()

# Assignment : https://www.tensorflow.org/lite/models/pose_estimation/overview
# Learning now is all about Exploration
# Explore More Here : https://www.tensorflow.org/lite/models/text_classification/overview