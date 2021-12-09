import pytesseract
import cv2
import matplotlib.pyplot as plt
import pdf2image
from PIL import Image

from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

pdfs = r"provide path to pdf file"
pages = pdf2image.convert_from_path(pdfs, 350)

i = 1
for page in pages:
    image_name = "Page_" + str(i) + ".jpg"
    page.save(image_name, "JPEG")
    i = i+1
