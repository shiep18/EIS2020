import cv2
pd1 = cv2.imread('LOCK.jpg')
pd2 = cv2.imread('OFF.jpg')
pd3 = cv2.imread('ON.jpg')
global p
F=0
T=1
p=F
cv2.imshow('result',pd1)
print ('DOOR LOCK')
def click(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print('mouse coords:',x,y)
        #OFF
        if 110<x<220 and 1<y<260:
            print ('DOOR OFF')
            #p=T
            cv2.imshow('result',pd2)
            f=open("C:\Apache24\htdocs\index.html","w")
            #f.write("<meta http-equiv=\"refresh\" content=\"1\">\n")
            f.write(f'OFF')
            #pass
        #ON
        elif 1<x<100 and 1<y<280:
            print ('DOOR ON')
            cv2.imshow('result',pd3)
            cv2.setMouseCallback('result',click)
            f=open("C:\Apache24\htdocs\index.html","w")
            #f.write("<meta http-equiv=\"refresh\" content=\"1\">\n")
            f.write(f'ON')
        else:
            print ('DOOR LOCK')
            cv2.imshow('result',pd1)
            cv2.setMouseCallback('result',click)
            f=open("C:\Apache24\htdocs\index.html","w")
            #f.write("<meta http-equiv=\"refresh\" content=\"1\">\n")
            f.write(f'LOCK')
            
            
cv2.namedWindow('result')
cv2.setMouseCallback('result',click)
while True:
    if cv2.waitKey(10)&0xFF==27:
            break
cv2.destroyAllWindows()
