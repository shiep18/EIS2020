import cv2
pd = cv2.imread('on.jpg')
pd1 = cv2.imread('off.jpg')
pd2 = cv2.imread('lock.jpg')
global p
F=0
T=1
p=F
cv2.imshow('result',pd1)
def click(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print('mouse coords:',x,y)
        if 90 < x < 430 and 15 < y < 390:

            if 240<x<310 and 120<y<350:
                f = open('C:\\Apache24\\htdocs\\index1.html', 'w')
                f.write("<meta http-equiv=\"refresh\" content=\"1\">\n")
                f.write("LOCK")
                f.close()
                cv2.imshow('result',pd2)
            else:
                cv2.imshow('result', pd)
                f = open('C:\\Apache24\\htdocs\\index1.html', 'w')
                f.write("<meta http-equiv=\"refresh\" content=\"1\">\n")
                f.write("ON")
                f.close()
        else:
            cv2.imshow('result', pd1)
            f = open('C:\\Apache24\\htdocs\\index1.html', 'w')
            f.write("<meta http-equiv=\"refresh\" content=\"1\">\n")
            f.write("OFF")
            f.close()
            cv2.setMouseCallback('result',click)


cv2.namedWindow('result')
cv2.setMouseCallback('result',click)
while True:
    if cv2.waitKey(10)&0xFF==27:
            break
cv2.destroyAllWindows()
