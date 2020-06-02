import numpy as np
import cv2
from camera import VideoCamera
from imutils.video import VideoStream




# # Loading Recognizer
recognizer=cv2.face.LBPHFaceRecognizer_create()

#
recognizer.cv2.CascadeClassifier('trainner.yml')
#
# # cascades
face_classifier=cv2.CascadeClassifier(r'C:\Users\win\AppData\Local\Programs\Python\Python36\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(r'C:\Users\win\AppData\Local\Programs\Python\Python36\Lib\site-packages\cv2\data\haarcascade_eye.xml')


# video capture object


cam=cv2.VideoCapture(0)
font=cv2.cv.InitFont(cv2.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)

# Capturing frames from the video capture object

while True:
    ret,im=cam.read()
    if ret==True:

#     converting images into grayscale
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x - 50, y - 50), (x + w + 50, y + h + 50), (225, 0, 0), 2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 40):
                if (Id == 1):
                    Id = "Ankit"
                elif (Id == 2):
                    Id = "Rahul"
            else:
                Id = "Unknown"
            cv2.cv.PutText(cv2.cv.fromarray(im), str(Id), (x, y + h), font, 255)
    cv2.imshow('im', im)
    if cv2.waitKey(10)  == ord('q'):
        break
        cam.release()
        cv2.destroyAllWindows()


#
