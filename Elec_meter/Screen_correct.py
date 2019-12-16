# -*- coding: utf-8 -*-
import cv2
import numpy as np
import os
import math

def Screen_Rotation(img_origin):
    height_o, width_o = img_origin.shape[:2]
    if width_o < height_o:
        return img_origin
    # resize
    size = (int(256 * width_o / height_o), 256)
    img = cv2.resize(img_origin, size)
    img = cv2.GaussianBlur(img, (3, 3), 0)
    #mask
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.adaptiveThreshold(hsv[:, :, 2], 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 10)
    #line
    lines = cv2.HoughLinesP(mask, 1, np.pi / 180, 50, lines=100, minLineLength=60, maxLineGap=0)
    thetaList = []
    for (x1, y1, x2, y2) in np.squeeze(lines, axis=1):
        if abs(y1 - y2) < 50 and (40 > max(y1, y2) or min(y1, y2) > 231):
            th = math.atan((y2 - y1) / (x2 - x1) * 1.)
            thetaList.append([th, np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)])
            img = cv2.line(img, tuple((x1, y1)), tuple((x2, y2)), (0, 0, 255), 2)
    if len(thetaList) != 0:
        #weighted mean
        thetaList = np.array(thetaList)
        thetaList[:, 1] = thetaList[:, 1] / np.sum(thetaList[:, 1])
        theta = np.sum(thetaList[:, 0] * thetaList[:, 1]) * 57.3
        #rotation
        center = (width_o // 2, height_o // 2)
        M = cv2.getRotationMatrix2D(center, theta, 1.0)
        img_origin = cv2.warpAffine(img_origin, M, (width_o, height_o))
        img = cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 1)
    return img_origin,img
    


if __name__ == '__main__':
    dir = 'E:/jingxuan/code/'
    dirList = os.listdir(dir)
    
    for i in dirList:

        if i[-3:] == 'png':
            image_path = os.path.join(dir, i)
            img_origin = cv2.imread(image_path)
            img,aa = Screen_Rotation(img_origin)
            cv2.imshow('rotation', img)
            cv2.imshow('img', img_origin)
            cv2.imshow('aa', aa)
            #cv2.imwrite('E:/jingxuan/rotate/'+i,img)
            cv2.waitKey(0)
            