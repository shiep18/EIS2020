import cv2
ON = cv2.imread('open.png')
OFF = cv2.imread('close.png')
LOCKED = cv2.imread('lock.png')
global p
F=0
T=1
p=F
cv2.imshow('result',ON)

def click(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print('mouse coords:',x,y)        
        if 40<x<70:
            print ('pd')
            #p=T
            cv2.imshow('result',ON)
            f = open("C:\\Apache24\\htdocs\\index2.html",'w')
            f.write("ON")
            f.close()
            #pass
        elif 70<x<100:
            cv2.imshow('result',OFF)
            cv2.setMouseCallback('result',click)
            f = open("C:\\Apache24\\htdocs\\index2.html",'w')
            f.write("OFF")
            f.close()
        else:
            cv2.imshow('result',LOCKED)
            cv2.setMouseCallback('result',click)
            f = open("C:\\Apache24\\htdocs\\index2.html",'w')
            f.write("LOCKED")
            f.close()

cv2.namedWindow('result')
cv2.setMouseCallback('result',click)
while True:
    if cv2.waitKey(10)&0xFF==27:
        break
cv2.destroyAllWindows()
