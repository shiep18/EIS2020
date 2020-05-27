import cv2
pd = cv2.imread('OPEN.JPG')
pd1 = cv2.imread('CLOSED.JPG')
pd2 = cv2.imread('LOCKED.JPG')
global p
F=0
T=1
p=F
cv2.imshow('result',pd)

def click(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print('mouse coords:',x,y)        
        if x<134:
            print ('pd')
            #p=T
            cv2.imshow('result',pd)
            with open('C:\Apache24\htdocs\index2.html','w') as f:
                f.write("<meta http-equiv=\"refresh\" content=\"1\">\n")
                f.write('OPEN')
        elif 134<=x<269:
            print ('pd')
            #p=T
            cv2.imshow('result',pd1)
            with open('C:\Apache24\htdocs\index2.html','w') as f:
                f.write("<meta http-equiv=\"refresh\" content=\"1\">\n")
                f.write('CLOSED')
        else:
            cv2.imshow('result',pd2)
            cv2.setMouseCallback('result',click)
            with open('C:\Apache24\htdocs\index2.html','w') as f:
                f.write("<meta http-equiv=\"refresh\" content=\"1\">\n")
                f.write('LOCKED')
cv2.namedWindow('result')
cv2.setMouseCallback('result',click)
while True:
    if cv2.waitKey(10)&0xFF==27:
            break
cv2.destroyAllWindows()

