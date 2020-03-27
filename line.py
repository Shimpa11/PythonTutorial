import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)
cv2.imshow("black image",img)

cv2.waitKey(5000)
# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img,(0,0),(211,211),(255,0,0),5)
cv2.imshow("lined image",img)
img = cv2.circle(img,(447,63), 63, (0,0,255), -1)
cv2.imshow("circle image",img)

cv2.waitKey(3000)