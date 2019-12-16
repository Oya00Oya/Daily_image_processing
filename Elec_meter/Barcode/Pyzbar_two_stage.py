import os
import cv2
from pyzbar import pyzbar

imgname = "test.jpg"
img = cv2.imread(imgname)
height,width = img.shape[:2]
print(img.shape)
imgdown = cv2.resize(img,(int(width/5),int(height/5)))

zbar_result = "0"
try:
    zbarcode = pyzbar.decode(imgdown)[0]
    zbar_result = str(zbarcode.data).replace("b", "").replace("'", "")
    print(zbar_result)
except Exception as e:
    try:
        print("pyzbar two stage detect")
        zbarcode = pyzbar.decode(img)[0]
        zbar_result = str(zbarcode.data).replace("b", "").replace("'", "")
        print(zbar_result)
    except Exception as e:
        print("no zbar code detect")
        zbar_result = "-1"