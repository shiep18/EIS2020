import cv2
pd = cv2.imread('door_open.jpg')
pd1 = cv2.imread('door_close.jpg')
pd2 = cv2.imread('door_lock.jpg')
global p
F=0
T=1
p=F
cv2.imshow('result',pd)

def click(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print('mouse coords:',x,y)    
        if 1<x<133 and 1<y<200:
            print ('open')
            cv2.imshow('result',pd)
            f=open("C:\\Apache24\\htdocs\\index4.html", "r+")
            #f.write("<meta http-equiv=\"refresh\" content=\"1\">\n")
            f.truncate()
            f.write("open")

        elif 134<x<267 and 1<y<200:
            print ('lock')
            cv2.imshow('result',pd2)
            f=open("C:\\Apache24\\htdocs\\index4.html", "r+") 
            #f.write("<meta http-equiv=\"refresh\" content=\"1\">\n")
            f.truncate()
            f.write("lock")
        else :
            print ('close')
            cv2.imshow('result',pd1)
            f=open("C:\\Apache24\\htdocs\\index4.html", "r+") 
            #f.write("<meta http-equiv=\"refresh\" content=\"1\">\n")
            f.write("close")
cv2.namedWindow('result')
cv2.setMouseCallback('result',click)
while True:
    if cv2.waitKey(10)&0xFF==27:
            break
cv2.destroyAllWindows()
