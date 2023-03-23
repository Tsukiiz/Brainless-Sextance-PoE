import pytesseract as tess
from PIL import Image

def ocr(imgName):
    tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    image = Image.open(imgName)
    # Extract text from the image and split into a list
    return tess.image_to_string(image).split("\n")

def cleanSpace(data):
    res = list()
    for i in data:
        if i != "":
            res.append(i)
    return res

def specifyMod(object):
    for i, x in enumerate(object):
        if i+1 >= len(object):
            return
        if "voidstone" in str(object[i]).lower():
            return object[i+1]
        

# Main function
imgName = "lfDrop.jpg"
readList = ocr(imgName)
cleanList = cleanSpace(readList)
mod = specifyMod(cleanList)
print(mod)


