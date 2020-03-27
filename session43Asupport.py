# from sklearn.datasets import load_digits
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets,metrics,svm

digits=datasets.load_digits()
print(digits)
# all built in datasets have type called bunch
print(type(digits))
#
print("===print images==")
# images are printed as numpy array
# print(digits.images)
print(digits['images']) # nd array type

print(len(digits.images))
# labels for differnt Digit Images
print(digits.target)
# print(digits['target'])
print(len(digits.target))



# using first two images in datasets
print("0th image")
print(digits['images'][0])
print(digits['images'][0].shape)
print(digits['target'][0])

print("ist image data")
print(digits['images'][1])
print(digits['images'][1].shape)
print(digits['target'][1])


# plt.subplot(2,4,1)
# plt.imshow(digits['images'][0],cmap=plt.cm.gray_r)
#
# plt.subplot(2,4,2)
# plt.imshow(digits['images'][1],cmap=plt.cm.gray_r)
#
# plt.subplot(2,4,3)
# plt.imshow(digits['images'][2],cmap=plt.cm.gray_r)
#
# plt.subplot(2,4,4)
# plt.imshow(digits['images'][3],cmap=plt.cm.gray_r)
#
# plt.subplot(2,4,5)
# plt.imshow(digits['images'][4],cmap=plt.cm.gray_r)
#
# plt.subplot(2,4,6)
# plt.imshow(digits['images'][5],cmap=plt.cm.gray_r)
#
# plt.show()


pos=1
for i in range(0,8):
    plt.subplot(2,4,pos)
    plt.imshow(digits['images'][i],cmap=plt.cm.gray_r)
    pos+=1
plt.show()

# grayscale the image and train the model

# create the model
