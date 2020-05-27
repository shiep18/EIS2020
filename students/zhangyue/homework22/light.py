import cv2
pd = cv2.imread('LOCK.jpg')
pd1 = cv2.imread('OPEN.jpg')
pd2 = cv2.imread('CLOSE.jpg')
global p
F=0
T=1
p=F
cv2.imshow('result',pd)
def click(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print('mouse coords:',x,y)        
        if 180<x<225 and 290<y<350:
            #p=T
            cv2.imshow('result',pd)
            print('LOCK')
            with open('D:\\Apache24\\htdocs\\index1.html', 'w', newline='') as f:
                f.truncate()  # 清空文件
                f.write("<!DOCTYPE html>\n")
                f.write("<head>\n")
                f.write("<meta http-equiv=\"refresh\" content=\"1\">\n")
                f.write("</head>\n")
                f.write("<body>\n")
                f.write("LOCK\n")
                f.write("</body>")
                
            #pass
        elif 75<x<325 and 170<y<400:
            cv2.imshow('result',pd1)
            cv2.setMouseCallback('result',click)
            print('OPEN')
            with open('D:\\Apache24\\htdocs\\index1.html', 'w', newline='') as f:
                f.truncate()  # 清空文件
                f.write("<!DOCTYPE html>\n")
                f.write("<head>\n")
                f.write("<meta http-equiv=\"refresh\" content=\"1\">\n")
                f.write("</head>\n")
                f.write("<body>\n")
                f.write("OPEN\n")
                f.write("</body>")
        else:
            cv2.imshow('result',pd2)
            cv2.setMouseCallback('result',click)
            print('CLOSE')
            with open('D:\\Apache24\\htdocs\\index1.html', 'w', newline='') as f:
                f.truncate()  # 清空文件
                f.write("<!DOCTYPE html>\n")
                f.write("<head>\n")
                f.write("<meta http-equiv=\"refresh\" content=\"1\">\n")
                f.write("</head>\n")
                f.write("<body>\n")
                f.write("CLOSE\n")
                f.write("</body>")
            
cv2.namedWindow('result')
cv2.setMouseCallback('result',click)
while True:
    if cv2.waitKey(10)&0xFF==27:
            break
cv2.destroyAllWindows()
