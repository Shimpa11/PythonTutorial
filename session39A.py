import cv2,time
video=cv2.VideoCapture(0)
# two outputs, check and frame

# Capture frame-by-frame.returns a bool (True/False). If frame is read correctly, it will be True. So you can check end of
# the video by checking this return(check) value.
check,frame=video.read()

print("===check===")
print(check)

print("===frame===")
print(frame)
# program will halt for 5s at line 12
time.sleep(5)

print("Releasing video ")
video.release()
cv2.imshow("Myframe",frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
