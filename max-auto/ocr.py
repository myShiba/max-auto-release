import easyocr
import os
from PIL import ImageGrab
reader = easyocr.Reader(["en"],True)

def screenGrab(rect):
    x, y, width, height = rect
    image = ImageGrab.grab(bbox=[x, y, x+width, y+height])
    image.save('/temp/img.png','PNG')

def getTXT():
    screenGrab([1618, 541, 338, 85])
    image = '/temp/img.png'
    text = ""
    try:
        text = reader.readtext(image, detail=0)[0]
    except:
        return False
    os.remove('/temp/img.png')
    if(int(text[1])<3):
        return True
    else:
        return False