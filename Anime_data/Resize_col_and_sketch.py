#coding=utf-8

import cv2
import numpy as np
import string
import os


col_source_path = "D:/Download/datasets/pairs_new_dataset/origin/col"
col_save_path = "D:/Download/datasets/pairs_new_dataset/origin/colresize"

ske_source_path = "D:/Download/datasets/pairs_new_dataset/origin/ske"
ske_save_path = "D:/Download/datasets/pairs_new_dataset/origin/skeresize"

count = 0
print(os.listdir(ske_source_path))
for imgname in os.listdir(ske_source_path):
    if (imgname.split('.'))[1] == "ini":
        continue
    else:
        img = cv2.imdecode(np.fromfile(os.path.join(ske_source_path, imgname), dtype=np.uint8), cv2.IMREAD_COLOR)

    print(imgname)
    print(img.shape)
    height = img.shape[0]
    width = img.shape[1]
    side_length = min(width,height)
    height = int((img.shape[0] /side_length) * 512)
    width = int((img.shape[1] / side_length) * 512)
    
    print(height,width)
    width = (width // 4) * 4
    height = (height // 4) * 4
    imgnew = cv2.resize(img,(width,height),interpolation=cv2.INTER_CUBIC)


    # colimg = cv2.imdecode(np.fromfile(os.path.join(col_source_path,(imgname.split('.'))[0] + " - 副本.jpg" ),dtype=np.uint8),cv2.IMREAD_COLOR)
    colimg = cv2.imdecode(np.fromfile(os.path.join(col_source_path, imgname), dtype=np.uint8), cv2.IMREAD_COLOR)
    colimgnew = cv2.resize(colimg, (width, height), interpolation=cv2.INTER_CUBIC)


    cv2.imwrite(os.path.join(ske_save_path,imgname),imgnew)
    cv2.imwrite(os.path.join(col_save_path,imgname), colimgnew)
    count = count + 1
    print(count)
