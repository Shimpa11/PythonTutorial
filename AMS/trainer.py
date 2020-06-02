import cv2,os
import imutils
import numpy as np
from pil import Image
# print(help(cv2.face))

# initialize the recognizer and the face detector
recognizer = cv2.face.LBPHFaceRecognizer_create()

# recognizer = cv2.face.createLBPHFaceRecognizer()


detector=cv2.CascadeClassifier(r'C:\Users\win\AppData\Local\Programs\Python\Python36\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
path='trainingSet'

# load the training images from dataSet .
def getImagesAndLabels(path):
    # get the path of the files in dataset folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    # create empty facelist
    faceSamples=[]
    # create empty ID list
    ids=[]
    # loop thr all the image paths and loading the ids ans images
    for imagePath in imagePaths:
    #   loading the image and converting into grayscale
        pilImage=Image.open(imagePath).convert('L')
      # converting pil Image into numpy array
        imageNp=np.array(pilImage,'uint8')
    #   getting the ids from the image
        id=int(os.path.split(imagePath)[-1].split(".")[1])
        faces=detector.detectMultiScale(imageNp)
        # if face is there then append that in list along with the ids
        for (x,y,w,h) in faces:
            faceSamples.append(imageNp[y:y+h,x:x+w])
            ids.append(id)
        return  faceSamples, ids

#     path to save  file that is generated after training.
faces,ids=getImagesAndLabels('trainingSet')
recognizer.train(faces,np.array(ids))
recognizer.save('trainner.yml')

