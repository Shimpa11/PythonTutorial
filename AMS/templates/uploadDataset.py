import cv2
import numpy as np
print(cv2.__version__)

# Load HAAR face classifier
face_classifier=cv2.CascadeClassifier(r'C:\Users\win\AppData\Local\Programs\Python\Python36\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(r'C:\Users\win\AppData\Local\Programs\Python\Python36\Lib\site-packages\cv2\data\haarcascade_eye.xml')

# Load function

def face_extractor(img):

    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    if faces is():
        return None
        # crop all faces found

    for(x,y,w,h) in faces:


        # img=cv2.rectangle(frame, (x, y),(x + w, y + h), (0, 255, 255),14i 10)
        cropped_face=img[y:y+h,x:x+w]
    return cropped_face

#  initialize webcam
cap=cv2.VideoCapture(0)
count=0

# collect 100 samples of the face  from the webcam input
while True:
    ret, frame=cap.read()
    # gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if face_extractor(frame) is not None:
        count+=1
        face=cv2.resize(face_extractor(frame),(200,200))
        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)

#         save file in the specified directory
        file_name_path='C:/Users/win/PycharmProjects/PythonTutorial/AMS/trainingSet/user'+str(count)+'.jpg'
        cv2.imwrite(file_name_path,face)

#         put count on images and display the count
        cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_DUPLEX,1,(0,255,0),2)

        cv2.imshow('face cropper',face)
    else:
        print("Face not found")
        pass

    if cv2.waitKey(1)=='q' or count==20:
        break
cap.release()
cv2.destroyAllWindows()
print("Collecting Samples complete")