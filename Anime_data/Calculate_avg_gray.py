#coding=utf-8

import cv2
import numpy as np
import os

source_path = "D:\Download\datasets\ske"

singel_count = 0
singel = 0
total = 0
total_count = 0
for imgname in os.listdir(source_path):
    singel_count = 0
    singel = 0
    img = cv2.imdecode(np.fromfile(os.path.join(source_path,imgname),dtype=np.uint8),cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    height = img.shape[0]
    width = img.shape[1]
    for i in range(height):
        for j in range(width):
            if(img[i,j] < 220):
                singel_count = singel_count + 1
                singel = singel + img[i,j]
    total = total + (singel/singel_count)
    total_count = total_count + 1
    print(total_count)

print("avg")
print(total/total_count)