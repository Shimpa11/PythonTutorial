import cv2
print(cv2.__version__)
# 1 means reading image as colored image
image=cv2.imread("download.jpg",1)

print("image")
print(image)

print("=====Image shape======")
print(image.shape)

print("=====image 0th index======")
print(image.shape)
print(image.shape[0])


print("===Length of image====")
print(len(image))
# rotate image