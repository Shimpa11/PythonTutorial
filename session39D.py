import cv2 as cv
import pytesseract
from pil import Image
# image=cv.imread("quote.jpg",1)
image=Image.open("images2.png")
# image=Image.open("images1.jpg")

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


text=pytesseract.image_to_string(image)
print(text)