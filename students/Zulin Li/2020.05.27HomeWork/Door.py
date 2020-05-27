import cv2
op = cv2.imread('Opened.jpg')
cl = cv2.imread('Closed.jpg')
lk = cv2.imread('Locked.jpg')

p=1

addr=r'C:\Apache24\htdocs\Blank.html'
#cv2.rectangle(lk,(175,285),(225,340),(255,0,0),3) #lock
#cv2.rectangle(lk,(75,160),(330,400),(0,0,255),3) #door
cv2.imshow('result',op)

def OpenTheDoor():
    cv2.imshow('result', op)
    f = open(addr, 'w')
    # f.write("<meta http-equiv=\"refresh\" content=\"1\">\n")
    f.write("Opened")
    f.close()

def CloseTheDoor():
    cv2.imshow('result', cl)
    f = open(addr, 'w')
    # f.write("<meta http-equiv=\"refresh\" content=\"1\">\n")
    f.write("Unlocked and Closed")
    f.close()

def LockTheDoor():
    cv2.imshow('result', lk)
    f = open(addr, 'w')
    # f.write("<meta http-equiv=\"refresh\" content=\"1\">\n")
    f.write("Locked")
    f.close()

def ClickWarnning():
    f = open(addr, 'w')
    f.write("Click The Door Please !")
    f.close()

def ClickWarnning2():
    f = open(addr, 'w')
    f.write("Click The Lock Please !")
    f.close()

def click(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        global p
        if p==1:
            if (75<x<330) and (160<y<400):
                CloseTheDoor()
                p=2
            else:
                ClickWarnning()
        elif p==2:
            if 175 < x < 225 and 285 < y < 340:
                LockTheDoor()
                p = 3
            elif 75<x<330 and 160<y<400:
                OpenTheDoor()
                p=1
            else:
                ClickWarnning()
        else:
            if 175 < x < 225 and 285 < y < 340:
                CloseTheDoor()
                p = 2
            else:
                ClickWarnning2()
            
cv2.namedWindow('result')
cv2.setMouseCallback('result',click)
while True:
    if cv2.waitKey(10)&0xFF==27:
            break
cv2.destroyAllWindows()
