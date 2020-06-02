# import numpy as np
import cv2
#
#
# # First we need to load the required XML classifiers.
# # Then load our input image (or video) in grayscale mode.
face_cascade=cv2.CascadeClassifier(r'C:\Users\win\AppData\Local\Programs\Python\Python36\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
# # face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier( r'C:\Users\win\AppData\Local\Programs\Python\Python36\Lib\site-packages\cv2\data\haarcascade_eye.xml')
#
#
cap=cv2.VideoCapture(0)


# """
# Now we find the faces in the image. If faces are found, it returns
#  the positions of detected faces as Rect(x,y,w,h). Once we get these locations,
#   we can create a ROI for
# the face and apply eye detection on this ROI (since eyes are always on the face !!! ).
#
#
# """
#
frameCount=0

while True:
     ret,frame=cap.read()
     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

     faces=face_cascade.detectMultiScale(gray,1.3,5)
     eyes = eye_cascade.detectMultiScale(gray)#

     frameCount+=1
#
     for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
     cv2.imshow('face', frame)

     for (ex, ey, ew, eh) in eyes:
         cv2.rectangle(frame, (ex, ey), (ex + ew, ey + eh), (0, 255, 255), 2)

     cv2.imshow('face', frame)



     if cv2.waitKey(1)==ord('q'):
                 break;
print(frameCount)

cap.release()
cv2.destroyAllWindows()
#
#
#
# cv2.destroyAllWindows()




# import cv2
#
# cap = cv2.VideoCapture(0)
#
# while(True):
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#
#     # Our operations on the frame come here
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     # Display the resulting frame
#     cv2.imshow('frame',gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # When everything done, release the capture
# cap.release()
# cv2.destroyAllWindows()