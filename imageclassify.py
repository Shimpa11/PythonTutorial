import numpy as np
import cv2


# First we need to load the required XML classifiers.
# Then load our input image (or video) in grayscale mode.
face_cascade=cv2.CascadeClassifier(r'C:\Users\win\AppData\Local\Programs\Python\Python36\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier( r'C:\Users\win\AppData\Local\Programs\Python\Python36\Lib\site-packages\cv2\data\haarcascade_eye.xml')

img = cv2.imread('shimpa.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

"""
Now we find the faces in the image. If faces are found, it returns
 the positions of detected faces as Rect(x,y,w,h). Once we get these locations,
  we can create a ROI for 
the face and apply eye detection on this ROI (since eyes are always on the face !!! ).
"""
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()