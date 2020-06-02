from flask import Flask
from flask import render_template,url_for
from flask import Response,stream_with_context
from camera import VideoCamera

import cv2
import time
# pip install imutils
from imutils.video import VideoStream
import imutils
time.sleep(3)
app = Flask(__name__)

cap = cv2.VideoCapture(0)
# videoStream = VideoStream(src=0).start()

@app.route("/")
def index():
    return render_template("videostream.html")

@app.route("/video_feed")
def video_feed():
    return Response(generateFrames(VideoCamera), mimetype='multipart/x-mixed-replace; boundary=frame')


def generateFrames(camera):
    while True:
        ret,frame = cap.read()
        # frame = camera.get_frame(videoStream)
        if ret ==True:

        # frame = imutils.resize(frame, width=600)
            (flag, encodedImage) = cv2.imencode(".jpg", frame)

        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')



if __name__ == '__main__':
    app.run(debug=True,port=5002)




# Assignment : Integrate Session67 in Session67A
#              Start Working on Face Recognition Projects: eg: Attendance Management
"""
        b' ' is a byte type string.
         http://stackoverflow.com/questions/6269765/what-does-the-b-character-do-in-front-of-a-string-literal

The obvious stuff, b' ' + frame + b' ' concatenates 2 strings with what ever frame is, 
creating a new string with those other strings added to it, \r and \n are string formatting characters for new lines.

The last invisible thing is b' ' b' ', putting 2 strings besides each other also concatenates them, putting braces ( )
 just makes python interpreter what ever is between those braces has a single line of code.

Just print what ever you're yielding there.
        """