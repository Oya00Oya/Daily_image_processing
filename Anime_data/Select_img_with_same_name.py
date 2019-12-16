#coding=utf-8

import cv2
import numpy as np
import string
import os

col_source_path = "G:/w/s/select"
target_path = "G:/w/duibi/美人(canna)"
save_line_path = "G:/w/s/canna"

print(os.listdir(col_source_path))
for imgname in os.listdir(col_source_path):
    if (imgname.split('.'))[1] == "ini":
        continue
    else:
        # if string.find((imgname.split('.'))[0],'(') == -1:
        if (imgname.split('.'))[0].find('(') == -1:
            img = cv2.imdecode(np.fromfile(os.path.join(target_path, imgname), dtype=np.uint8), cv2.IMREAD_COLOR)
            cv2.imwrite(os.path.join(save_line_path,imgname), img)
        else:
            imgname = (imgname.split('.'))[0].split(' ')
            img = cv2.imdecode(np.fromfile(os.path.join(target_path, imgname[0]+'.png'), dtype=np.uint8), cv2.IMREAD_COLOR)
            print(os.path.join(target_path,imgname[0]+'.png'))
            cv2.imwrite(os.path.join(save_line_path,imgname[0]+'.png'), img)