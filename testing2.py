# import the necessary packages
# from vidgear.gears import VideoGear, NetGear
from flask import Response
from flask import Flask, current_app
from flask import render_template
from flask import jsonify
from random import random
import threading
import argparse
import datetime
import imutils
import time
import cv2

# initialize the output frame and a lock used to ensure thread-safe
# exchanges of the output frames (useful for multiple browsers/tabs
# are viewing tthe stream)

server_address='206.189.144.234'
options_cam={"CAP_PROP_FRAME_WIDTH":640,"CAP_PROP_FRAME_HEIGHT":480,"CAP_PROP_FPS":60}
options_client={'bidirectional_mode':True,'compression_format':'.jpg','compression_param':[cv2.IMWRITE_JPEG_QUALITY,80],'flag':0,'copy':False,'track':False}
# stream=VideoGear(enablePiCamera=False,logging=False,**options_cam).start()
# client=NetGear(address=server_address, port='20001', protocol='tcp', pattern=1, receive_mode=False, logging=True, **options_client)

app=Flask(__name__)

@app.route("/")
def index():
    # return the rendered template
    return render_template("index.html")

@app.route("/data_feed/<input_data>")
def data_feed(input_data):
    def dataStream(input_data):
        while True:
            print("get_data={}".format(input_data))
            yield "data: {}\n\n".format(input_data)
            time.sleep(1)
    return Response(dataStream(input_data), mimetype="text/event-stream")

@app.route("/video_feed/<input_frame>")
def video_feed(input_frame):
    # return the response generated along with the specific media
    # type (mime type)
    def display_frame(input_frame):
        while True:
            print("get_frame={}".format(input_frame))
            # encode the frame in JPEG format
            (flag, encodedImage) = cv2.imencode(".jpg", input_frame)

            # yield the output frame in the byte format
            yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
                bytearray(encodedImage) + b'\r\n')
    return Response(display_frame(input_frame),
        mimetype = "multipart/x-mixed-replace; boundary=frame")

def get_realtime_stream():
    while True:
        frame = stream.read()
        data_stream=round(random()*10,3)
        client.send(frame,message=data_stream)
        video_feed(frame)
        data_feed(data_stream)
    stream.stop()
    client.close()

# check to see if this is the main thread of execution
if __name__ == '__main__':
    t = threading.Thread(target=get_realtime_stream)
    t.start()

    app.run(host='0.0.0.0',port=8000,debug=True,threaded=True,use_reloader=False)