#coding=utf-8

import cv2
import numpy as np
import string
import os

col_source_path = "D:/Download/datasets/pairs_new_dataset/col"
col_save_path = "D:/Download/datasets/pairs_new_dataset/colrename"

print(os.listdir(col_source_path))
for imgname in os.listdir(col_source_path):
    if (imgname.split('.'))[1] == "ini":
        continue
    else:
        img = cv2.imdecode(np.fromfile(os.path.join(col_source_path, imgname), dtype=np.uint8), cv2.IMREAD_COLOR)
    print(imgname)
    print(((imgname.split('.'))[0])[:-5])
    print(img.shape)

    cv2.imwrite(os.path.join(col_save_path,((imgname.split('.'))[0])[:-5]+".jpg"), img)

# img = cv2.imdecode(np.fromfile(os.path.join(col_source_path, "J22 - 副本.jpg"), dtype=np.uint8), cv2.IMREAD_COLOR)
# cv2.imshow(img)
# print(img.shape)