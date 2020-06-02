import cv2
pd = cv2.imread('1.jpg')
pd1 = cv2.imread('2.jpg')
pd2 = cv2.imread('3.jpg')
global p
F=0
T=1
p=F
pdon= cv2.imshow('result',pd1)
pdon= cv2.resize(pdon,(140,300),interpolation=cv2.INTER_CUBIC)
pd[300:400,400:500] = pdon[0:90,0:140]
# pdoff = cv2.imread('tou.jpg')
def click(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print('mouse coords:',x,y)
        if 90 < x < 430 and 15 < y < 390:

            if 240<x<310 and 120<y<350:
                # f = open('C:\\Apache24\\htdocs\\index1.html', 'w')
                # f.write("<meta http-equiv=\"refresh\" content=\"1\">\n")
                # f.write("LOCK")
                # f.close()
                cv2.imshow('result',pd2)
            else:
                cv2.imshow('result', pd)

                # f = open('C:\\Apache24\\htdocs\\index1.html', 'w')
                # f.write("<meta http-equiv=\"refresh\" content=\"1\">\n")
                # f.write("ON")
                # f.close()
        else:
            cv2.imshow('result', pd1)
            # f = open('C:\\Apache24\\htdocs\\index1.html', 'w')
            # f.write("<meta http-equiv=\"refresh\" content=\"1\">\n")
            # f.write("OFF")
            # f.close()
            cv2.setMouseCallback('result',click)

# mouse coords: 381 139
# mouse coords: 378 318
# mouse coords: 317 194
# mouse coords: 440 190
cv2.namedWindow('result')

cv2.setMouseCallback('result',click)
while True:
    if cv2.waitKey(10)&0xFF==27:
            break
cv2.destroyAllWindows()
