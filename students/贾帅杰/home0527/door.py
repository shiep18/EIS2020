import cv2
pd = cv2.imread('ON.jpg')
pd1 = cv2.imread('OFF.jpg')
pd2 = cv2.imread('LOCK.jpg')
global p
F=0
T=1
p=F
cv2.imshow('result',pd)

def click(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print('mouse coords:',x,y)        
        if 173<x<232 and 277<y<326:
            print ('pd')
            #p=T
            cv2.imshow('result',pd)
            f=open("C:\\Apache24\\htdocs\\index.html", "w")
            f.write("<meta http-equiv=\"refresh\" content=\"1\">\n  ")
            f.write('ON')
            #pass
        elif 332<x<390 and 268<y<330:
            print ('pd2')
            #p=T
            cv2.imshow('result',pd2)
            f=open("C:\\Apache24\\htdocs\\index.html", "w")
            f.write("<meta http-equiv=\"refresh\" content=\"1\">\n  ")
            f.write('LOCK')
        elif 16<x<73 and 222<y<306:
            cv2.imshow('result',pd1)
            cv2.setMouseCallback('result',click)
            f=open("C:\\Apache24\\htdocs\\index.html", "w")
            f.write("<meta http-equiv=\"refresh\" content=\"1\">\n  ")
            f.write('OFF')
cv2.namedWindow('result')
cv2.setMouseCallback('result',click)
while True:
    if cv2.waitKey(10)&0xFF==27:
            break
cv2.destroyAllWindows()
