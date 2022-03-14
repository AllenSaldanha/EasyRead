import cv2
import numpy as np
import pytesseract
import re
import PIL
from PIL import Image

# ----------------------------------The tesseract OCR section-------------------------
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'

def get_string(img_path):
    # Read image with opencv
    img = cv2.imread(img_path)

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    cv2.imwrite("removed_noise.png", img)

    # Write the image after apply opencv to do some ...
    cv2.imwrite(img_path, img)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open(img_path))

    return result

def contentCorrection(str):
  str=re.sub("\n+"," ",str)
  str=str.replace("- ","")
  return str

def recognize():
    filename="./uploadedImages/imageToBeRecognized.jpg"
    recognised_content = get_string(filename)
    finalPrediction =  contentCorrection(recognised_content)
    # return {"result":finalPrediction}
    return finalPrediction
