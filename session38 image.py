import cv2
import numpy as np
# 0 means reading image as B/W
image=cv2.imread("download.jpg",0)

# cv2.imshow("Image",image)
# cv2.waitKey(3000)
# cv2.destroyAllWindows()

rotatedimage=np.rot90(image)
cv2.imshow("rotated image:",rotatedimage)
# cv2.waitKey(5000)
# take any keyboard input and quit
cv2.waitkey(0)