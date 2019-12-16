#coding=utf-8

import cv2
import numpy as np
import string
import os

col_source_path = "D:/Download/datasets/pairs_finetune/col"
# col_save_path = "D:/Download/datasets/pairs_finetune/binary"
col_save_path = "D:/Download/datasets/pairs_finetune/S"

def small_component_removal(im_bw):
    """
    remove small chokes
    :param imgs: 1 channel opencv np array 0-255
    :return: 1 channel opencv np array 0-255
    """
    thresh = 127
    # im_bw = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)[1]
    im_bw = im_bw * -1 + 255
    # find connected black components
    nb_components, output, stats, centroids = cv2.connectedComponentsWithStats(im_bw.astype(np.uint8), connectivity=8)

    sizes = stats[1:, -1]
    nb_components = nb_components - 1

    min_size = 20

    # answer image
    img2 = np.zeros(output.shape)
    for i in range(0, nb_components):
        if sizes[i] >= min_size:
            img2[output == i + 1] = 255
    return img2.astype(np.float32) * -1 + 255



print(os.listdir(col_source_path))
for imgname in os.listdir(col_source_path):
    if (imgname.split('.'))[1] == "ini":
        continue
    else:
        img = cv2.imdecode(np.fromfile(os.path.join(col_source_path, imgname), dtype=np.uint8), cv2.IMREAD_COLOR)
    print(imgname)
    # Gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    H, S, V = cv2.split(HSV)
    # ret2, binary = cv2.threshold(Gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    ret2, binary = cv2.threshold(S, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    binary = small_component_removal(binary)
    cv2.imwrite(os.path.join(col_save_path,imgname), binary)

# img = cv2.imdecode(np.fromfile(os.path.join(col_source_path, "J22 - 副本.jpg"), dtype=np.uint8), cv2.IMREAD_COLOR)
# cv2.imshow(img)
# print(img.shape)