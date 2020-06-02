from flask import *
import cv2


from imutils.video import VideoStream

app=Flask(__name__)
@app.route('/')
def home():
    return render_template("data.html")
face_classifier=cv2.CascadeClassifier(r'C:\Users\win\AppData\Local\Programs\Python\Python36\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(r'C:\Users\win\AppData\Local\Programs\Python\Python36\Lib\site-packages\cv2\data\haarcascade_eye.xml')


@app.route("/upload",methods=['GET','POST'])
def upload():
    return Response(generateFrames(), mimetype='multipart/x-mixed-replace; boundary=frame')

def generateFrames():
    webcam = cv2.VideoCapture(0)  # '0' is use for my webcam, if you've any other camera attached use '1' like this

    # The program loops until it has 30 images of the face.
    count = 0
    Id = input('enter your id: ')
    while count < 30:
        (_, im) = webcam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        faces = face_classifier.detectMultiScale(gray, 1.3, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
            face = gray[y:y + h, x:x + w]
            # face_resize = cv2.resize(face, (width, height))
            file_name_path = 'C:/Users/win/PycharmProjects/PythonTutorial/AMS/trainingSet/user.' +Id +'.'+ str(count) + '.jpg'
            cv2.imwrite(file_name_path, face)
            cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0), 2)

        count += 1

        cv2.imshow('OpenCV', im)

        key = cv2.waitKey(10)
        if key == 27:
            break

#
# @app.route('/upload')
# def upload():
#     if request.method == 'POST':
#         if request.form['submit'] == 'Submit':
#             return Response(face_extractor(),mimetype='multipart/x-mixed-replace; boundary=frame')
#
#



if __name__=="__main__":
    app.run(debug=True,port=5007)

