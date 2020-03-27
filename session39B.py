# opencv is a framework

import cv2,time
video=cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc('*XVID')
out = cv2.VideoWriter("myvideo.mp4", fourcc, 20, 0(640, 480))

frameCount=0
while True:
    check,frame=video.read()
    frameCount+=1
    # frame_array=[]
    # print(frame)
    if check== True:
        out.write(frame)

        cv2.imshow("MyVideo",frame)
    # cv2.imshow("MyVideo",np.rot90(frame))
    # frame_array.append(frame)
    # out=cv2.imwrite("video.avi",frame_array)
    # for i in range(len(frame_array)):
    #     out.write(frame_array[i])
    # getting key after every 1 ms

        key=cv2.waitKey(1)

        if key==ord('q'):
         break
print("Total Frames Captured:",frameCount)

# Close the window
video.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()

# Assignment:use OpenCV API and convert list of frames as video and save it
# ref:https://docs.opencv.org/master/d9/df8/tutorial_root.html