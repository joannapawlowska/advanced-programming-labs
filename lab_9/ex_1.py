import cv2
import numpy
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def image_to_str(img: numpy.ndarray) -> str:
    return pytesseract.image_to_string(Image.fromarray(img), lang='eng')


def read_from_image(path: str) -> str:
    img = cv2.imread(path)
    return image_to_str(img)


def read_from_image_with_invert(path: str) -> str:
    img = cv2.imread(path)
    img = cv2.bitwise_not(img)
    return image_to_str(img)


def read_from_image_with_bilateral_filter(path: str) -> str:
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    img = cv2.threshold(cv2.bilateralFilter(img, 5, 75, 75), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return image_to_str(img)
