from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils import face_utils
import imutils
import dlib
import cv2

# aspect ratio threshold for the eye
aspectRatioThreshold=0.3
frameCountThreshold=50

# dlib utils fro detecting and predicting eyes from the landmarks
detector=dlib.get-frontal_face_detector()
predictor=dlib.shape_predictor("sleepiness/shape_predictor_68_face_landmarks.dat")


# on the facial landmoarks, obtained fro left and right eye
(leftEyeStart,leftEyeFinish)=face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(RightEyeStart,RightEyeFinish)=face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

vs=VideoStream(src=0).start()

while True:
    frame=vs.read()
    frame=imutils.resize(frame,width=450)

    # frame converted into gray  scale
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=detector(gray,0)
    # iteratein faces
    for face in faces:
        # predict the landmarks  on face shape
    shape=predictor(gray,face)
    #  get then mathematically as numpy array
     shape= face_utils.shape_to_np()