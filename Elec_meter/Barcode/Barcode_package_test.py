import os
import cv2
from pyzbar import pyzbar
import zxing

source_path = "E:/jingxuan/code"
imglist = os.listdir(source_path)

file = open("barcode.txt","w")
for imgname in imglist:

    img = cv2.imread(os.path.join(source_path,imgname))
    zbar_result = "zbarnone"
    try:
        zbarcode = pyzbar.decode(img)[0]
        zbar_result = str(zbarcode.data).replace("b", "").replace("'", "")
    except Exception as e:
        print("no zbar code detect")
        zbar_result = "zbarnone"
    # if zbarcode:
    #     print(str(zbarcode.data))
    #     zbar_result = str(zbarcode.data)
    # else:
    #     zbar_result = "none"

    zxing_result = "zxnone"
    zx = zxing.BarCodeReader()
    zxingcode = zx.decode("file:/"+source_path + "/" + imgname)
    print("file:/"+source_path + "/" + imgname)
    print(zxingcode)
    if zxingcode.parsed != '':
        print(zxingcode.parsed)
        zxing_result = str(zxingcode.parsed)
    else:
        zxing_result = "zxnone"
    file.write(imgname +"   " + zbar_result + "  " + zxing_result + "\n")