"""
Explore skimage library
https://scikit-image.org/docs/dev/auto_examples/index.html

"""
import platform
print( platform.architecture()[0] == "64bit")
# import platform
# print(platform.architecture())

import pandas as pd
from skimage import io
import os
import matplotlib.pyplot as plt

def showLandMarks(image,landMarks):
    plt.imshow(image)
    plt.scatter(landMarks[:,0],landMarks[:,1], s=100, marker='.',c='r')
    plt.show()

def main():
    landmarksDataSet=pd.read_csv("faces/face_landmarks.csv")
    print(landmarksDataSet)
    imageNum=60
    imageName=landmarksDataSet.iloc[imageNum,0]
    print("image name:",imageName)


    # pts on image for certain features , x and y coordinates
    landMarks=landmarksDataSet.iloc[imageNum,1:].to_numpy()
    print(landMarks)
    print(landMarks.shape)

    landMarks=landMarks.astype("float").reshape(-1,2)
    print("Reshaped landmarks Array")
    print(landMarks)
    print(landMarks.shape)

    showLandMarks(io.imread(os.path.join('faces/',imageName)),landMarks)

if __name__=='__main__':
    main()