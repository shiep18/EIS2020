import cv2
import numpy as np
from pymouse import PyMouse
from pykeyboard import PyKeyboard
cap = cv2.VideoCapture(0)
m = PyMouse()
k = PyKeyboard()
def key_con(cx,cy,xmax,ymax,k):  
    case1=int(xmax*1/4)
    case2=int(xmax*3/4)
    case3=int(ymax*1/4)
    case4=int(ymax*3/4)
    if (cx<case1)and(case4>cy>case3):#left
        k.press_key("a")
        print("left")
    else:
        k.release_key("a")
    # if (cx<case1)and(cy<case3):#left-forward
    #     k.press_key("a")
    #     k.press_key("w")
    #     print("left-forward")
    # else:
    #     k.release_key("a")
    #     k.release_key("w")
    # if (cx<case1)and(cy>case4):#left-back
    #     k.press_key("a")
    #     k.press_key("s")
    #     print("left-back")
    # else:
    #     k.release_key("a")
    #     k.release_key("s")
    if (cx>case2)and(case4>cy>case3):#right
        k.press_key("d")
        print("right")
    else:
        k.release_key("d")
    # if (cx>case2)and(cy<case3):#right-forward
    #     k.press_key("d")
    #     k.press_key("w")
    #     print("right-forward")
    # else:
    #     k.release_key("d")
    #     k.release_key("w")
    # if (cx>case2)and(cy>case4):#right-back
    #     k.press_key("d")
    #     k.press_key("s")
    #     print("right-back")
    # else:
    #     k.release_key("d")
    #     k.release_key("s")
    if(case1<cx<case2)and(cy<case3):#forward
        k.press_key("w")
        print("forward")
    else:
        k.release_key("w")
    if(case1<cx<case2)and(cy>case4):#back
        k.press_key("s")
        print("back")
    else:
        k.release_key("s")

while True:

    ret, img= cap.read()
    ymax,xmax,leni = img.shape
    imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    # print(imghsv[0:30,0:30])
    lower_red=np.array([0,130,120])
    upper_red=np.array([55,255,255])
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
cv2.waitKey(0)
cv2.destroyAllWindows()