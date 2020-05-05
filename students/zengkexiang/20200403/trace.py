import cv2
import numpy as np
from pykeyboard import PyKeyboard


k = PyKeyboard()
lower_yellow=np.array([20,80,90])
upper_yellow=np.array([40,255,255])

def drawcircle(img,lower,upper):
    imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #print(imghsv)
    redobj=cv2.inRange(imghsv,lower,upper)
    a,conts,hrc=cv2.findContours(redobj,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #img = cv2.drawContours(img, conts, -1, (0,255,0), 3)

    bigconts=[]
    for cont in conts:
        area = cv2.contourArea(cont)
        if area >200:
            bigconts.append(cont)

    if len(bigconts) > 0:
        area = []
        # 找到最大的轮廓
        for k in range(len(bigconts)):
            area.append(cv2.contourArea(bigconts[k]))
        max_idx = np.argmax(np.array(area))
        #img = cv2.drawContours(img, bigconts,max_idx, (255,0,0), 10)
        #img = cv2.drawContours(img, bigconts, -1, (255, 0, 0), 10)

        #算出轮廓质心再画圆
        M = cv2.moments(bigconts[max_idx])
        cx, cy = M['m10'] / M['m00'], M['m01'] / M['m00']
        cv2.circle(img,(int(cx),int(cy)),50,(0,0,255),5)
        return cx,cy
    else :
        return 0,0

def control(x1,y1,x2,y2,x,y):
    if x+y != 0:
        if x < x1:
            k.press_key("d")
        else:
            k.release_key("d")

        if x > x2:
            k.press_key("a")
        else:
            k.release_key("a")

        if y < y1:
            k.press_key("w")
            print("up")
        else:
            k.release_key("w")

        if y > y2:
            k.press_key("s")
            print("down")
        else:
            k.release_key("s")
    else :
        pass

cv2.namedWindow('abc')
cap = cv2.VideoCapture(0)
ret,img = cap.read()
y,x,l = img.shape
my = int(y/2)

mx = int(x/2)
while ret:

    ret,img = cap.read()
    xx,yy = drawcircle(img,lower_yellow,upper_yellow)
    img = cv2.rectangle(img,(mx-70,my-70),(mx+70,my+70),(255,255,0),2)
    cv2.imshow("abc",img)
    control(mx-70,my-70,mx+70,my+70,xx,yy)
    key = cv2.waitKey(1)&0xff
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()