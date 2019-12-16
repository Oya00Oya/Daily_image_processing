import cv2
import numpy as np
import string
import os
import random
from math import *

source_path = "D:/labelimg/diya_200"
save_path = "D:/labelimg/diya_200"

def rotate_img(img,angel):
    height, width = img.shape[:2]

    degree = angel
    # 旋转后的尺寸
    heightNew = int(width * fabs(sin(radians(degree))) + height * fabs(cos(radians(degree))))
    widthNew = int(height * fabs(sin(radians(degree))) + width * fabs(cos(radians(degree))))

    matRotation = cv2.getRotationMatrix2D((width / 2, height / 2), degree, 1)
    matRotation[0, 2] += (widthNew - width) / 2  # 重点在这步，目前不懂为什么加这步
    matRotation[1, 2] += (heightNew - height) / 2  # 重点在这步
    imgRotation = cv2.warpAffine(img, matRotation, (widthNew, heightNew), borderValue=(255, 255, 255))

    return imgRotation

def rename(imgname,count):

    # strlen = len(imgname.split('.')[0])
    # zeros = ''
    # for i in range(6-strlen):
    #     zeros =  '0' +zeros
    # newimgname = zeros + imgname

    newimgname = 'A' + str(count) + '.jpg'

    # print(imgname)
    # print(newimgname)

    return newimgname

def resize(img):
    height,width = img.shape[:2]
    print(height,width)

    # side_length = min(width,height)
    # heightnew = int((height /side_length) * 256)
    # widthnew = int((width / side_length) * 256)

    heightnew = (height // 8) * 4
    widthnew = (width // 8) * 4

    # heightnew = int(height*(720/width))
    # widthnew = 720

    print(heightnew, widthnew)
    imgnew = cv2.resize(img,(widthnew,heightnew),interpolation=cv2.INTER_CUBIC)

    return imgnew

def RandomCrop(img,size):
    w = img.shape[1]
    h = img.shape[0]
    th=tw= size
    if w == tw and h == th:  # ValueError: empty range for randrange() (0,0, 0)
        return img

    if w == tw:
        x1 = 0
        y1 = random.randint(0, h - th)
        return img[y1:y1+th, x1:x1+tw]

    elif h == th:
        x1 = random.randint(0, w - tw)
        y1 = 0
        return img[y1:y1 + th, x1:x1 + tw]

    else:
        x1 = random.randint(0, w - tw)
        y1 = random.randint(0, h - th)
        return img[y1:y1 + th, x1:x1 + tw]


def main():
    count = 0
    for imgname in os.listdir(source_path):
        # img = cv2.imdecode(np.fromfile(os.path.join(source_path,imgname),dtype=np.uint8),cv2.IMREAD_COLOR)
        img = cv2.imread(os.path.join(source_path,imgname))
        img = rotate_img(img,90)

        #imgname = rename(imgname,count)

        cv2.imwrite(os.path.join(save_path,imgname),img)
        count = count + 1

main()