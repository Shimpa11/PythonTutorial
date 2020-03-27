import os
import matplotlib.pyplot as plt
import numpy as np
import cv2
path=os.getcwd()
print(path)

train_path=path+'/pizza'
train_batch=os.listdir(train_path)
x_train=[]
print(len(train_batch))
x=np.array(train_batch)
print(x)
print(type(x))
# # data in the form of image
# pos=1
# for i in range(0,len(train_batch)):
#     plt.subplot(2,7,pos)
#     plt.imshow(train_batch.data[i],cmap=plt.cm.gray_r)
#     pos+=1
# plt.show()
f=cv2.imread([x])
print(f)