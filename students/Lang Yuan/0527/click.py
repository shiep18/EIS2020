import cv2
ON = cv2.imread('open.jpg')
OFF = cv2.imread('close.jpg')
LOCK = cv2.imread('lock.jpg')
global p
F=0
T=1
p=F
cv2.imshow('result',ON)
f = open("E:\Apache24\Apache24\htdocs\index0.html",'r+')
f.truncate()

def click(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print('mouse coords:',x,y)        
        if 77<x<325 and 249<y<395:
            print ('pd')
            #p=T
            cv2.imshow('result',ON)
            f = open("E:\Apache24\Apache24\htdocs\index0.html",'r+')
            f.write("open  ")
            #f.write("<meta http-equiv=\"refresh\" content=\"1\">\n")
            #pass
        elif 343<x<390 and 276<y<326:
            print ('pd')
            #p=T
            cv2.imshow('result',LOCK)
            f = open("C:\Apache24\htdocs\index0.html",'r+')
            f.write("lock")
            #f.write("<meta http-equiv=\"refresh\" content=\"1\">\n")
        else:
            cv2.imshow('result',OFF)
            f = open("C:\Apache24\htdocs\index0.html",'r+')
            f.write("close ")
            #f.write("<meta http-equiv=\"refresh\" content=\"1\">\n")
            cv2.setMouseCallback('result',click)
            
cv2.namedWindow('result')
cv2.setMouseCallback('result',click)
while True:
    if cv2.waitKey(10)&0xFF==27:
            break
cv2.destroyAllWindows()
