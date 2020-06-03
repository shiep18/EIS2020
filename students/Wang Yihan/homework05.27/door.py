import cv2
pd1 = cv2.imread('on.jpg')
pd2 = cv2.imread('off.jpg')
pd3 = cv2.imread('lock.jpg')
global p
F=0
T=1
p=F
cv2.imshow('result',pd3)
print ('Door Lock')
def click(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print('mouse coords:',x,y)
        if 154<x<308 and 1<y<305:
            print ('Door Off')
            cv2.imshow('result',pd2)
            f=open("C:\Apache24\htdocs\index.html","w")
            f.write(f'OFF')

        elif 1<x<154 and 1<y<305:
            print ('Door on')
            cv2.imshow('result',pd1)
            cv2.setMouseCallback('result',click)
            f=open("C:\Apache24\htdocs\index.html","w")
            f.write(f'ON')
        else:
            print ('Door Lock')
            cv2.imshow('result',pd3)
            cv2.setMouseCallback('result',click)
            f=open("C:\Apache24\htdocs\index.html","w")
            f.write(f'LOCK')
            
            
cv2.namedWindow('result')
cv2.setMouseCallback('result',click)
while True:
    if cv2.waitKey(10)&0xFF==27:
            break
cv2.destroyAllWindows()
