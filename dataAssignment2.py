import matplotlib.pyplot as plt
from sklearn import svm,metrics
import os

import matplotlib.pyplot as plt
# List all files in a directory using os.listdir
# basepath = 'pizza/'
# for entry in os.listdir(basepath):
#     if os.path.isfile(os.path.join(basepath, entry)):
#         print(entry)


# List all files in a directory using scandir()
basepath = 'pizza/'
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():
            print(entry.name)
#
# first_img_data = dataset.images[0]
# print(first_img_data.shape)

# #
# pos=1
# for i in range(0,len(entry)):
#     plt.subplot(2,7,pos)
#     plt.imshow(entry[i],cmap=plt.cm.gray_r)
#     pos+=1
# plt.show()