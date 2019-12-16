#coding=utf-8

import os
import os.path
import xml.dom.minidom


source_path = "E://1400xml"
save_path = "E://newxml"
files = os.listdir(source_path)  # 得到文件夹下所有文件名称
s = []
count = 0
for xmlFile in files:  # 遍历文件夹
    if not os.path.isdir(xmlFile):  # 判断是否是文件夹,不是文件夹才打开
        print (xmlFile)
        # TODO
        # xml文件读取操作
        num = int(xmlFile[0:-4])
        if(count != num):
            print(num)
        count = count+1
        # # 将获取的xml文件名送入到dom解析
        # dom = xml.dom.minidom.parse(os.path.join(source_path, xmlFile))  ###最核心的部分os.path.join(path,xmlFile),路径拼接,输入的是具体路径
        # root = dom.documentElement
        # #获取标签对name/pose之间的值
        # name = root.getElementsByTagName('name')
        # filename = root.getElementsByTagName('filename')
        # print(name[0].firstChild.data)
        # print(filename[0].firstChild.data)
        # # 重命名class name
        # for i in range(len(name)):
        #     print(name[i].firstChild.data)
        #     name[i].firstChild.data = 'number'
        #     print(name[i].firstChild.data)
        # # 重命名filename
        # for i in range(len(filename)):
        #     print(filename[i].firstChild.data)
        #     strlen = len(filename[i].firstChild.data) - 4
        #     zeros = ''
        #     for j in range(6 - strlen):
        #         zeros = '0' + zeros
        #     newimgname = zeros + filename[i].firstChild.data
        #     filename[i].firstChild.data = newimgname
        #     print(filename[i].firstChild.data)
        # #
        # strlen = len(xmlFile) - 4
        # zeros = ''
        # for j in range(6 - strlen):
        #     zeros = '0' + zeros
        # newxmlFile = zeros + xmlFile
        #
        # # 保存修改到xml文件中
        # with open(os.path.join(source_path, xmlFile), 'w',encoding='utf-8') as fh:
        #     dom.writexml(fh)
        # os.rename(os.path.join(source_path,xmlFile),os.path.join(source_path,newxmlFile))
        # print('写入name/pose OK!')