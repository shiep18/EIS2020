import cv2
pd = cv2.imread('1.jpg')
pd1 = cv2.imread('2.jpg')
global p
F=0
T=1
p=F
cv2.imshow('result',pd)
def click(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print('mouse coords:',x,y)        
        if 135<x<295 and 90<y<290:
            print ('led_on')
            #p=T
            cv2.imshow('result',pd)
            f=open('C:\Apache24\htdocs\index1.html','r+')
            #f.write("<meta http-equiv=\"refresh\" content=\"1\">\n")
            f.truncate()
            f.write(f"ON")
            #pass
        else:
            print ('led_off')
            cv2.imshow('result',pd1)
            cv2.setMouseCallback('result',click)
            f=open('C:\Apache24\htdocs\index1.html','r+')
            #f.write("<meta http-equiv=\"refresh\" content=\"1\">\n")
            f.write(f"OFF")
            
cv2.namedWindow('result')
cv2.setMouseCallback('result',click)
while True:
    if cv2.waitKey(10)&0xFF==27:
            break
cv2.destroyAllWindows()
