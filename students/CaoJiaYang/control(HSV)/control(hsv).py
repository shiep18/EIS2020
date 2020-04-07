import cv2
import numpy as np
from pymouse import PyMouse
from pykeyboard import PyKeyboard
cap = cv2.VideoCapture(0)
m = PyMouse()
k = PyKeyboard()
def key_con(cx,cy,xmax,ymax,k):  
    if cx < int(xmax/4) :
        k.press_key("a")
    else :
        k.release_key("a")
    if cx > int((xmax/4)*3) :
        k.press_key("d")
    else :
        k.release_key("d")
    if cy > int((ymax/4)*3) :
        k.press_key("s")
    else :
        k.release_key("s")
    if cy < int(ymax/4) :
        k.press_key("w")
    else :
        k.release_key("w")

while True:
    ret, img= cap.read()
    ymax,xmax,leni = img.shape
    imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    print(imghsv[0:30,0:30])
    lower_red=np.array([59,85,100])
    upper_red=np.array([80,255,255])
    redobj=cv2.inRange(imghsv,lower_red,upper_red)
    conts,hrc=cv2.findContours(redobj,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    bigconts=[]
    for cont in conts:
        area = cv2.contourArea(cont)
        if area >200:
            bigconts.append(cont)
    for bigcnt in bigconts:
      M=cv2.moments(bigcnt)
      cx=int(M['m10']/M['m00'])
      cy=int(M['m01']/M['m00'])
      cv2.circle(img,(cx,cy),30,(0,0,255),2)
      key_con(cx,cy,xmax,ymax,k)
    cv2.imshow("myshowwindwos",img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
   # k.tap_key('w')
cv2.waitKey(0)
cv2.destroyAllWindows()
