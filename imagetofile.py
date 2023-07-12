import pytesseract
import os 
from PIL import Image

pytesseract.pytesseract.tesseract_cmd= r"D:\New folder\tesseract.exe"

def convert():
  img = Image.open('rishi.jpg')
  text= pytesseract.image_to_string(img)
  print(text)
  
convert()
