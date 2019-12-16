file = open('recognition_gt.txt','r')
fileresult = open('result.txt','w')

line = file.readline()
while line:
    line = line.split(' ')
    info = []
    for i in range(len(line)):
        if(line[i]!=''):
            info.append(line[i])
    print(info[0])

    filesource = open('recognition_rotation.txt', 'r')
    sourceline = filesource.readline()
    while sourceline:
        sourceline = sourceline.split(' ')
        sourceinfo = []
        for j in range(len(sourceline)):
            if (sourceline[j] != ''):
                sourceinfo.append(sourceline[j])
        #print(sourceinfo)
        if (info[0] == sourceinfo[0]):
            for k in range(3):
                if info[k+4] != sourceinfo[k+4] or info[k+4] != sourceinfo[k+4] or info[k+4] != sourceinfo[k+4]:
                    fileresult.write(info[0]+'\n')
                    break
            break
        sourceline = filesource.readline()

    line = file.readline()