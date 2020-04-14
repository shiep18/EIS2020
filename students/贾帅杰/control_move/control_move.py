'''
import cv2

img = cv2.imread('ren.jpg')

print(img.shape)
cv2.rectangle(img,(60,50),(60+100,50+100),(0,255,0),3)
cv2.imwrite('myhead.jpg',img[50:150,60:160])
cv2.imshow('fasdlfadsf',img)

imghead = cv2.imread('myhead.jpg')
cv2.imshow('head',imghead)

def mycircle(event,x,y,flag,pa):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        print('i got a mouse')
        cv2.circle(img,(x,y),20,(255,0,0),3)
        

cv2.setMouseCallback('fasdlfadsf',mycircle)

while True:
    cv2.waitKey(1000)
    cv2.imshow('fasdlfadsf',img)


cv2.destroyAllWindows()
'''
import numpy as np
import cv2
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
i=0

cap=cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
while True:
    pos = mc.player.getTilePos()
    ret,img=cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        #记录初始位置
        if i<1:
            xs=x
            zs=y
        #得到需要移动的距离
        if i>=1:
            xs1=x
            zs1=y
            if -3<=xs1-xs<=3 and -3<=zs1-zs<=3:
                cv2.waitKey(1)
            else:
                mc.player.setTilePos([pos.x+(xs1-xs),pos.y,pos.z+(zs1-zs)])
            xs=xs1
            zs=zs1
        i=i+1
        
        #cv2.imwrite('face'+str(i)+'.jpg',img[y+2:y+h-2,x+2:x+w-2])
            
    cv2.imshow('img',img)
    key = cv2.waitKey(1) & 0xFF
    # 按'q'健退出循环
    if key == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
