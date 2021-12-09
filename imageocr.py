import pytesseract
import cv2
import matplotlib.pyplot as plt
from pdf2image import convert_from_path
import os
import glob
import sys
from PIL import Image

from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
#counter for file names - base value of 0
k=0

path = 'C:/Users/svintitskiy/lpthw/git/files'
for filename in glob.glob(os.path.join(path, '*.pdf')):
#increase of filename counter
    k+=1

    with open(filename) as f: # open in readonly mode
#taking only names of the input
        f_str=f.name
        # pdf2image magic here
        pages = convert_from_path(f_str, 500)
        image_counter = 1
        for page in pages:
            filename = "page_"+str(image_counter)+str(k)+".jpg"
            page.save(filename, 'JPEG')
            image_counter = image_counter + 1

m=1
filelimit = k

#image_counter-1

for i in range(1, k+1):
#filelimit + 1
    outfile = "out_text_page_"+str(m)+str(i)+".txt"
    f = open(outfile, "a")
    filename = "page_"+str(m)+str(i)+".jpg"
    text = str(((pytesseract.image_to_string(Image.open(filename), lang='rus'))))
    text = text.replace('-\n', '')
    f.write(text)
    f.close()




"""



#folder_path =   os.getcwd()


#PDF_file = "bill.pdf"
















def pdf_to_img(pdf_file):
    return pdf2image.convert_from_path(pdf_file)

def ocr_core(file):
    text = pytesseract.image_to_string(file)
    return text

def print_pages(pdf_file):
    images = pdf_to_img(pdf_file)
    for pg, img in enumerate(images):
        print(ocr_core(img))

image = cv2.imread("bill.jpg")

filename = "bill.jpg"
#pytesseract.pytesseract.tesseract_cmd = "C:\Program Files (x86)\Tesseract-OCR/tesseract.exe"
#tessdata_dir_config = r'--tessdata-dir "C:\Program Files (x86)\Tesseract-OCR\tessdata"'
img = Image.open(filename)
text = pytesseract.image_to_string(img, lang= 'rus')
print(text)

#string = pytesseract.image_to_string(image), lang='rus'
#print (string)  , config=tessdata_dir_config


print_pages('bill.pdf')
"""
