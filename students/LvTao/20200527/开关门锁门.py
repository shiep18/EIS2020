import cv2
pd = cv2.imread('k.jpg')
pd1 = cv2.imread('g.jpg')
pd2 = cv2.imread('s.jpg')
global p
F=0
T=1
p=F
global door
door = 0
global lock
lock = 0
cv2.imshow('result',pd)
f = open('C:\Apache24\htdocs\index.html','r+')
f.seek(0)
f.truncate()
f.write(f"OPEN ")
def click(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        global door
        global lock
        print('mouse coords:',x,y,door,lock)        
        if 190<x<300 and 260<y<350 and lock == 0 and door == 1:
            print ('pd')
            #p=T
            cv2.imshow('result',pd)
            f = open('C:\Apache24\htdocs\index.html','w')
            f.write(f"OPEN ")
            f.close()
            door=0
            lock = 0
            #pass
        elif 200<x<300 and 500<y<600 and door==1 and lock == 0:
            print ('pd2')
            #p=T
            cv2.imshow('result',pd2)
            f = open('C:\Apache24\htdocs\index.html','w')
            f.write(f"LOCK ")
            f.close()
            lock = 1
            door=1
            #pass
        elif 190<x<300 and 260<y<350 and door == 0 and lock == 0:
            cv2.imshow('result',pd1)
            cv2.setMouseCallback('result',click)
            f = open('C:\Apache24\htdocs\index.html','w')
            f.write(f"CLOSE")       
            f.close()
            door=1
            lock = 0
        elif 200<x<300 and 500<y<600 and door == 1 and lock == 1:
            cv2.imshow('result',pd1)
            cv2.setMouseCallback('result',click)
            f = open('C:\Apache24\htdocs\index.html','w')
            f.write(f"CLOSE")       
            f.close()
            door=1
            lock = 0
cv2.namedWindow('result')
cv2.setMouseCallback('result',click)
while True:
    if cv2.waitKey(10)&0xFF==27:
            break
cv2.destroyAllWindows()
