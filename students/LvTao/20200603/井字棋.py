import cv2
import numpy as np

global a
a = np.zeros((3,3))
print(a)

img=np.zeros((600,600,3),np.uint8)
img[:]=[200,5,100]
chess=np.zeros((3,3),np.int8)
cv2.line(img,(120,120),(480,120),(250,230,200),3)
cv2.line(img,(120,240),(480,240),(250,230,200),3)
cv2.line(img,(120,360),(480,360),(250,230,200),3)
cv2.line(img,(120,480),(480,480),(250,230,200),3)
cv2.line(img,(120,120),(120,480),(250,230,200),3)
cv2.line(img,(240,120),(240,480),(250,230,200),3)
cv2.line(img,(360,120),(360,480),(250,230,200),3)
cv2.line(img,(480,120),(480,480),(250,230,200),3)

#cv2.circle(img,(180,180),(50),(0,0,0),-1)
#cv2.circle(img,(300,180),(50),(255,255,255),-1)

cv2.imshow("img",img,)
def click(event,x,y,flags,param):
    global a
    if event==cv2.EVENT_RBUTTONDOWN:
        print('mouse coords:',x,y)
        for i in range(0,3):
            for i1 in range(0,3):
                if (i+1)*120<x<(i+1)*120+120 and (i1+1)*120<y<(i1+1)*120+120 and a[i][i1]==0:
                    cv2.circle(img,((i+1)*120+60,(i1+1)*120+60),(50),(255,255,255),-1)
                    a[i][i1]=-1
    if event==cv2.EVENT_LBUTTONDOWN:
        print('mouse coords:',x,y)
        for i in range(0,3):
            for i1 in range(0,3):
                if (i+1)*120<x<(i+1)*120+120 and (i1+1)*120<y<(i1+1)*120+120 and a[i][i1]==0:
                    cv2.circle(img,((i+1)*120+60,(i1+1)*120+60),(50),(0,0,0),-1)
                    a[i][i1]=1
    cv2.imshow("img",img,)
cv2.namedWindow('img')
cv2.setMouseCallback('img',click)
while True:
    if cv2.waitKey(10)&0xFF==27:
            break
cv2.destroyAllWindows()
