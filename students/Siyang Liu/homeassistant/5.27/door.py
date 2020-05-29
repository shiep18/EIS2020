import cv2

filepath = "C://Apache24//htdocs//door.html"
on = cv2.imread("./door_on.png")
off = cv2.imread("./door_off.png")
locked = cv2.imread("./door_locked.png")

rehead = '<meta http-equiv="refresh" content="1">\n'

cv2.imshow('result',on)

def click(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('mouse coords:',x,y)        
        if 316<x<480 and 52<y<480:
            print ('pd')
            #p=T
            cv2.imshow('result',on)
            with open(filepath, "w") as f:
                f.write(rehead + "on")
            #pass
        elif 250<x<295 and 230<y<278:   
            cv2.imshow('result',locked)
            with open(filepath, "w") as f:
                f.write(rehead + "locked")
            cv2.setMouseCallback('result',click)

        else:
            cv2.imshow('result',off)
            with open(filepath, "w") as f:
                f.write(rehead + "off")
            cv2.setMouseCallback('result',click)
            
cv2.namedWindow('result')
cv2.setMouseCallback('result',click)
while True:
    if cv2.waitKey(10)&0xFF==27:
            break
cv2.destroyAllWindows()
