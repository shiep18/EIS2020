import cv2
pd1 = cv2.imread('1.jpg')
pd = cv2.imread('2.jpg')
global p
F=0
T=1
p=F
cv2.imshow('result',pd)
def click(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print('mouse coords:',x,y)        
        if 135<x<295 and 90<y<290:
            print ('pd')
            #p=T
            cv2.imshow('result',pd)
            f = open("C:\\Apache24\\htdocs\\index.html",'w')
            f.write("on")
            #pass
        else:
            cv2.imshow('result',pd1)
            cv2.setMouseCallback('result',click)
            f = open("C:\\Apache24\\htdocs\\index.html",'w')
            f.write("off")
cv2.namedWindow('result')
cv2.setMouseCallback('result',click)
while True:
    if cv2.waitKey(10)&0xFF==27:
        break
cv2.destroyAllWindows()
