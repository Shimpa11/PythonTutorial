import cv2
import numpy as np
# every image is represented as numpy array
image=cv2.imread("download.jpg",1)
print("original image")
print(image)

print("original image shape")
shape=image.shape
print(shape)

# resize image
resizedImage=cv2.resize(image,(shape[1]//2,shape[0]//2))
print("resized image shape")

resizedShape=resizedImage.shape
print(resizedShape)
rotatedImage=np.rot90(resizedImage)

cv2.imshow("resized image",resizedImage)

cv2.imwrite("newdownload.jpg",resizedImage)
print("new download saved")
cv2.imwrite("download90.jpg",rotatedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()