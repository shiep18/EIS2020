import cv2
pd = cv2.imread('close.jpg')
pd1 = cv2.imread('open.jpg')
pd2 = cv2.imread('lock.jpg')
cv2.imshow('result',pd)

def click(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print('mouse coords:',x,y)    
        if 175<x<225 and 300<y<350:
            print ('open')
            cv2.imshow('result',pd1)
            f=open("C:\\Apache24\\htdocs\\index.html", "w")
            f.write("<meta http-equiv=\"refresh\" content=\"1\">\n")
            f.write("open")

        elif 340<x<390 and 275<y<325:
            cv2.imshow('result',pd2)
            f=open("C:\\Apache24\\htdocs\\index.html", "w") 
            f.write("<meta http-equiv=\"refresh\" content=\"1\">\n")
            f.write("lock")
        else :
            cv2.imshow('result',pd)
            f=open("C:\\Apache24\\htdocs\\index.html", "w") 
            f.write("<meta http-equiv=\"refresh\" content=\"1\">\n")
            f.write("close")
cv2.namedWindow('result')
cv2.setMouseCallback('result',click)
while True:
    if cv2.waitKey(10)&0xFF==27:
            break
cv2.destroyAllWindows()

