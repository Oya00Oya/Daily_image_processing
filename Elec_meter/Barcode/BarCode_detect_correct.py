# -*- coding: utf-8 -*-
import numpy as np
import cv2
import os
import math
if __name__ == "__main__":
    dir = 'E:/jingxuan/code/'
    dirList = os.listdir(dir)
    
    for i in dirList:
        if i[-4:] in ['.jpg', '.JPG', 'jpeg', '.png', '.PNG']:
            img_path = os.path.join(dir, i)
            image = cv2.imread(img_path)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            height, width = gray.shape[:2]
            # 固定高H
            size = (int(256 * width / height), 256)
            gray = cv2.resize(gray, size)
            # compute the Scharr gradient magnitude representation of the images
             # in both the x and y direction
            gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
            gradY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=-1)
            
            # subtract the y-gradient from the x-gradient
            gradient = cv2.subtract(gradX, gradY)
            gradient = cv2.convertScaleAbs(gradient)
            blurred = cv2.blur(gradient, (5, 5))
            _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
            closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
            closed = cv2.erode(closed, None, iterations=4)
            closed = cv2.dilate(closed, None, iterations=4)
            (cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)
            c = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
            rect = cv2.minAreaRect(c)
            box = cv2.boxPoints(rect)
            if sum((box[0]-box[1])**2) > sum((box[2]-box[1])**2):
                x1 = box[0][0]
                x2 = box[1][0]
                y1 = box[0][1]
                y2 = box[1][1]
            else:
                x1 = box[2][0]
                x2 = box[1][0]
                y1 = box[2][1]
                y2 = box[1][1]
            theta = math.atan((y2 - y1) / (x2 - x1 + 1e-7) * 1.) * 57.3
            center = (width // 2, height // 2)
            M = cv2.getRotationMatrix2D(center, theta, 1.0)
            image = cv2.warpAffine(image, M, (width, height))
            box = np.rint(box).astype(np.int32)
            # draw a bounding box arounded the detected barcode and display the
            # image
            cv2.drawContours(gray, [box], -1, (0, 255, 0), 3)
            #cv2.imshow("gray", gray)
            #cv2.imshow('Image', image)
            cv2.imwrite('E:/jingxuan/code_rotate/'+i,image)
            cv2.waitKey(0)