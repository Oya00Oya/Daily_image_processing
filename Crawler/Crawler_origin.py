# decoding=utf-8
import logging
import os
import time

import requests
import socket
import base64
import json
from selenium import webdriver


def getByte(path):
    with open(path, 'rb') as f:
        img_byte = base64.b64encode(f.read())
    img_str = img_byte.decode('ascii')
    return img_str


input_files=[]
def getImglist(path):
    for imgname in os.listdir(path):
        input_files.append(imgname)
getImglist("E:/yanshou/add/")
print(len(input_files))

logger = logging.getLogger("logger")
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter("[%(levelname)s][%(asctime)s] - %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)


session = requests.session()
driver = webdriver.Chrome()
driver.get("file:///C:/Users/OyaoOya/Desktop/%E7%94%B5%E8%A1%A8/testhtml/testwyw.html")


if len(input_files) <= 1:
    print("missing input_files")
    exit(-1)

time.sleep(1)

filerec = open('recognition_yanshou_add.txt','w')
for input_file in input_files:
    try:
        driver.find_element_by_id("image_file").send_keys("E:/yanshou/add/"+input_file)
        driver.find_element_by_id("upJQuery").click()
        time.sleep(5)
        readings = driver.find_element_by_id("readings")
        elecclass= driver.find_element_by_id("class")
        code = driver.find_element_by_id("code")
        pgjfz = driver.find_element_by_id("pgjfz")
        ywgong = driver.find_element_by_id("ywgong")
        zfxiang = driver.find_element_by_id("zfxiang")
        # filerec.write("E:/shibie/"+input_file + " "+ readings.text + " "+  elecclass.text + " " +
        #               code.text+ " " + pgjfz.text + " " + ywgong.text + " " + zfxiang.text + '\n')
        filerec.write('{0:20} {1:15} {2:^15} {3:^25} {4:^12} {5:^12} {6:^12}\n'.format(input_file, readings.text, elecclass.text,
                                                                                    code.text, pgjfz.text,
                                                                                    ywgong.text, zfxiang.text))
        time.sleep(1)

    except Exception as e:
        logger.exception(e)



