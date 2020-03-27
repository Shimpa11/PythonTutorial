import cv2
import os
import glob

import matplotlib.pyplot as plt

img_dir = "C:/Users/win/PycharmProjects/PythonTutorial/pizza" # Enter Directory of all images
data_path = os.path.join(img_dir,'*g')
files = glob.glob(data_path)
data = []
for f1 in files:
    img = cv2.imread(f1)
    data.append(img)
    print(img)
# print(data[0])
print(len(data))
pos=1
for i in range(0,len(data)):
    plt.subplot(9,6,pos)
    # plt.imshow(data[i],cmap=plt.cm.gray_r)
    plt.imshow(data[i])
    pos+=1
plt.show()