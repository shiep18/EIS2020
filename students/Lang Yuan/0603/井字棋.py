
import cv2
import numpy as np
win = [0,0,0,0,0,0,0,0]
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
       print('mouse coords:',x,y)
       if 120<x<240 and 120<y<240:
            cv2.circle(img,(180,180),(50),(255,255,255),-1)
            win[0]+=1
            win[3]+=1
            win[6]+=1
            cv2.imshow('image',img)
       elif 120<x<240 and 240<y<360:
            cv2.circle(img,(180,300),(50),(255,255,255),-1)
            win[1]+=1
            win[3]+=1
            cv2.imshow('image',img)
       elif 120<x<240 and 360<y<480:
            cv2.circle(img,(180,420),(50),(255,255,255),-1)
            win[2]+=1
            win[3]+=1
            win[7]+=1
            cv2.imshow('image',img)
       elif 240<x<360 and 120<y<240:
            cv2.circle(img,(300,180),(50),(255,255,255),-1)
            win[0]+=1
            win[4]+=1
            cv2.imshow('image',img)
       elif 240<x<360 and 240<y<360:
            cv2.circle(img,(300,300),(50),(255,255,255),-1)
            win[1]+=1
            win[4]+=1
            win[6]+=1
            win[7]+=1
            cv2.imshow('image',img)
       elif 240<x<360 and 360<y<480:
            cv2.circle(img,(300,420),(50),(255,255,255),-1)
            win[2]+=1
            win[4]+=1
            cv2.imshow('image',img)
       elif 360<x<480 and 120<y<240:
            cv2.circle(img,(420,180),(50),(255,255,255),-1)
            win[0]+=1
            win[5]+=1
       elif 360<x<600 and 400<y<550:
            cv2.circle(img,(420,420),(50),(255,255,255),-1)
            win[0]+=1
            win[5]+=1
       elif 360<x<600 and 200<y<480:
            cv2.circle(img,(420,300),(50),(255,255,255),-1)
            win[0]+=1
            win[5]+=1       

    elif event == cv2.EVENT_RBUTTONDOWN:
       if 120<x<240 and 120<y<240:
            cv2.circle(img,(180,180),(50),(0,0,0),-1)
            win[0]+=1
            win[3]+=1
            win[6]+=1
            cv2.imshow('image',img)
       elif 120<x<240 and 240<y<360:
            cv2.circle(img,(180,300),(50),(0,0,0),-1)
            win[1]+=1
            win[3]+=1
            cv2.imshow('image',img)
       elif 120<x<240 and 360<y<480:
            cv2.circle(img,(180,420),(50),(0,0,0),-1)
            win[2]+=1
            win[3]+=1
            win[7]+=1
            cv2.imshow('image',img)
       elif 240<x<360 and 120<y<240:
            cv2.circle(img,(300,180),(50),(0,0,0),-1)
            win[0]+=1
            win[4]+=1
            cv2.imshow('image',img)
       elif 240<x<360 and 240<y<360:
            cv2.circle(img,(300,300),(50),(0,0,0),-1)
            win[1]+=1
            win[4]+=1
            win[6]+=1
            win[7]+=1
            cv2.imshow('image',img)
       elif 240<x<360 and 360<y<480:
            cv2.circle(img,(300,420),(50),(0,0,0),-1)
            win[2]+=1
            win[4]+=1
            cv2.imshow('image',img)
       elif 360<x<480 and 120<y<240:
            cv2.circle(img,(420,180),(50),(0,0,0),-1)
            win[0]+=1
            win[5]+=1
       elif 360<x<600 and 400<y<550:
            cv2.circle(img,(420,420),(50),(0,0,0),-1)
            win[0]+=1
            win[5]+=1
       elif 360<x<600 and 200<y<480:
            cv2.circle(img,(420,300),(50),(0,0,0),-1)
            win[0]+=1
            win[5]+=1       
 
 
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
 
cv2.setMouseCallback('image', draw_circle)

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
cv2.circle(img,(180,180),(50),(0,0,0),-1)

while True:
    cv2.imshow('image',img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cv2.destroyAllWindows()


