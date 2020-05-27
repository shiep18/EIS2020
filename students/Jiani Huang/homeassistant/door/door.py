import cv2
on = cv2.imread('on.jpg')
off = cv2.imread('off.jpg')
lock = cv2.imread('lock.jpg')

global p
F=0
T=1
p=F
cv2.imshow('result',on)
def click(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print('mouse coords:',x,y)        
        if 0<x<285:
            print ('pd')
            #p=T
            cv2.imshow('result',on)
            f = open("C:\\Apache24\\htdocs\\index.html",'w')
            f.write("on")
            f.close()
            #pass
        elif 285<x<570:
            cv2.imshow('result',off)
            cv2.setMouseCallback('result',click)
            f = open("C:\\Apache24\\htdocs\\index.html",'w')
            f.write("off")
            f.close()
        else:
            cv2.imshow('result',lock)
            cv2.setMouseCallback('result',click)
            f = open("C:\\Apache24\\htdocs\\index.html",'w')
            f.write("lock")
            f.close()

cv2.namedWindow('result')
cv2.setMouseCallback('result',click)
while True:
    if cv2.waitKey(10)&0xFF==27:
        break
cv2.destroyAllWindows()
