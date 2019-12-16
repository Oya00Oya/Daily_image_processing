import os
import cv2

source_path = "D:/labelimg"
target_path = "D:/labelimg/jingxuan/code"

filelist = os.listdir(os.path.join(source_path,"labels_of_jingxuan"))

for filename in filelist:
    print(filename)
    file = open(os.path.join(source_path,"labels_of_jingxuan",filename),'r')
    info = file.readline().split()
    x,y,w,h = info[1],info[2],info[3],info[4]
    #print(x,y,w,h)

    img = cv2.imread(os.path.join(source_path,"jingxuan",filename.split('.')[0]+'.jpg'))
    height, width = img.shape[:2]
    #print(height,width)
    x,y,w,h = float(x)*width, float(y)*height, float(w)*width, float(h)*height
    x,y,w,h = round(x),round(y),round(w),round(h)

    xmin = int(x - w / 2)
    ymin = int(y - h / 2)
    xmax = int(x + w / 2)
    ymax = int(y + h / 2)

    imgres = img[ymin:ymax, xmin:xmax]
    cv2.imwrite(os.path.join(target_path,filename.split('.')[0]+'.jpg'), imgres)