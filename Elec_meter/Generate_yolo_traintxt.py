#coding=utf-8

import cv2
import numpy as np
import string
import os

source_path = "D:/labelimg/diya_status_dataset/"

count = 0
fileo = open('vaild.txt','w')
for filename in os.listdir(source_path + 'labels_of_diya23'):
    if (filename.split('.'))[1] == "ini":
        continue
    else:
        imgxdog = cv2.imdecode(np.fromfile(os.path.join(source_path + 'diya23', filename.split('.')[0]+'.jpg'), dtype=np.uint8), cv2.IMREAD_COLOR)
        count = count + 1
        fileo.writelines(os.path.join(source_path + 'diya23', filename.split('.')[0]+'.jpg'+'\n'))
        print(count)

# for filename in os.listdir(source_path + 'diya23'):
#     if (filename.split('.'))[1] == "ini":
#         continue
#     else:
#         if(os.path.exists(os.path.join(source_path + 'labels_of_diya23', filename.split('.')[0]+'.txt'))):
#             count = count + 1
#             fileo.writelines(os.path.join(source_path + 'diya_23', filename+'\n'))
#             #print(count)
#         else:
#             print(filename)
