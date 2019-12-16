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
getImglist("D:/Download/datasets/lineart")
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
driver.get("http://210.30.96.139:8000")


for input_file in input_files[2582::]:
    img_str = getByte("D:/Download/datasets/lineart/"+input_file)
    data = {'room': 'new', 'step': 'new', 'sketch': img_str, 'method': 'colorization','imgname': input_file[0:-4],
            'options': '{"alpha":0,"points":[],"method":"colorization","lineColor":[0,0,0],"line":false,"hasReference":false}'}
    req = requests.post(url='http://210.30.96.139:8000/upload_sketch', data=data)
    print(req)
    print(input_file)