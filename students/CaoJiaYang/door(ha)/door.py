import cv2
pd = cv2.imread('11.jpg')
pd1 = cv2.imread('22.jpg')
pd2= cv2.imread('33.jpg')
global p
F=0
T=1
p=F
cv2.imshow('result',pd)

def click(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print('mouse coords:',x,y)        
        if 0<x<135 :
            print ('pd')
            #p=T
            f=open('C:\Apache24\htdocs\index1.html','w')
            cv2.imshow('result',pd)
            f.write("close      ")
            #pass
        elif 136<x<270:
            cv2.imshow('result',pd1)
            cv2.setMouseCallback('result',click)
            f=open('C:\Apache24\htdocs\index1.html','w')
            f.write("open       ")
        else:
            cv2.imshow('result',pd2)
            cv2.setMouseCallback('result',click)
            f=open('C:\Apache24\htdocs\index1.html','w')
            f.write("lock       ")
cv2.namedWindow('result')
cv2.setMouseCallback('result',click)
while True:
    if cv2.waitKey(10)&0xFF==27:
            break
cv2.destroyAllWindows()

