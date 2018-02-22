from __future__ import print_function

import pytesseract as tt
import cv2
from PIL import Image

path = './ocr-example.png'
img = cv2.imread(path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('ocr-gray.png', img)

img = Image.open("C:\Users\Heba\Documents\ALL\ROV\pythonShapeRecognition\ocr-gray.png")
# print('Loaded!!', fflush=True)
# img.show()

text = tt.image_to_string(img)

print('OCR: ', text)
