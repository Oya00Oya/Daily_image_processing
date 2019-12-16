#coding=utf-8

import cv2
import numpy as np
import string
import os

col_source_path = "D:/Download/datasets/Danbooru/col"
col_save_path = "D:/Download/datasets/Danbooru/colnew"

ske_source_path = "D:/Download/datasets/Danbooru/ske"
ske_save_path = "D:/Download/datasets/Danbooru/skenew"

count = 0
print(os.listdir(ske_source_path))
for imgname in os.listdir(ske_source_path):
    if (imgname.split('.'))[1] == "ini":
        continue
    else:
        img = cv2.imdecode(np.fromfile(os.path.join(ske_source_path, imgname), dtype=np.uint8), cv2.IMREAD_COLOR)

    print(imgname)
    height = img.shape[0]
    width = img.shape[1]
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    ret, binary = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY)
    coledge = 0
    for i in range(width):
        if (binary[int(height/2),i]) != 0:
            coledge = i
            break
    print(coledge)

    rowedge = 0
    for j in range(height):
        if (binary[j,int(width/2)]) != 0:
            rowedge = j
            break
    print(rowedge)

    colimg = cv2.imdecode(
        np.fromfile(os.path.join(col_source_path, (imgname.split('.'))[0][:-5] + ".jpg"), dtype=np.uint8),
        cv2.IMREAD_COLOR)
    colimgnew = colimg
    imgnew = img

    if coledge!= 0 :
        imgnew = img[0:height,coledge:width-coledge]
        colimgnew = colimg[0:height,coledge:width-coledge,:]

    if rowedge!= 0 :
        imgnew = imgnew[rowedge:height-rowedge,0:width]
        colimgnew = colimgnew[rowedge:height-rowedge,0:width,:]

    newimgname = int((imgname.split('.'))[0][:-5]) + 5000
    cv2.imwrite(os.path.join(ske_save_path, (str(newimgname)) + ".jpg"), imgnew)
    cv2.imwrite(os.path.join(col_save_path, (str(newimgname)) + ".jpg"), colimgnew)