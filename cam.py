
import cv2
face_classifier=cv2.CascadeClassifier(r'C:\Users\win\AppData\Local\Programs\Python\Python36\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')

def face_extractor(img):
    # if request.method == 'POST':

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    if faces is ():
        return None
        # crop all faces found

    for (x, y, w, h) in faces:
        # img=cv2.rectangle(frame, (x, y),(x + w, y + h), (0, 255, 255), 10)
        cropped_face = img[y:y + h, x:x + w]
    return cropped_face
    # print(cropped_face)