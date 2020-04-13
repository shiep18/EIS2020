import cv2
import numpy as np
from pykeyboard import PyKeyboard

cap = cv2.VideoCapture(0)
k = PyKeyboard()
lower_blue = np.array([100,43,46])
upper_blue = np.array([124,255,255])   

def move(x,y,xmax,ymax,k):  # 控制移动
    if x < int(xmax/3) :
        k.press_key("a")
    else :
        k.release_key("a")

    if x > int(xmax/3)*2 :
        k.press_key("d")
    else :
        k.release_key("d")

    if y > int(ymax/3)*2 :
        k.press_key("s")
    else :
        k.release_key("s")

    if y < int(ymax/3) :
        k.press_key("w")
    else :
        k.release_key("w")
        
def camera():
    while True:
        ret,img= cap.read()
        ymax,xmax,leni = img.shape
        imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

        blueobj=cv2.inRange(imghsv,lower_blue,upper_blue)
        conts,hrc=cv2.findContours(blueobj,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        #img = cv2.drawContours(img, conts, -1, (0,255,0), 3)
        
        bigconts=[]
        for cont in conts:
            area = cv2.contourArea(cont)
            if area >200:
                bigconts.append(cont)
        img = cv2.drawContours(img, bigconts, -1, (255,0,0), 10)

        cx = int(xmax/2)
        cy = int(ymax/2)
        
        for bigycnt in bigconts:
            M=cv2.moments(bigycnt)
            cx=int(M['m10']/M['m00'])
            cy=int(M['m01']/M['m00'])
            cv2.circle(img,(cx,cy),50,(0,0,255),5)
            break

        move(cx,cy,xmax,ymax,k)
        
        #cv2.imshow("blueobj",blueobj)
        cv2.imshow("window",img)

        key = cv2.waitKey(1) & 0xFF
        # 按'q'健退出循环
        if key == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break
