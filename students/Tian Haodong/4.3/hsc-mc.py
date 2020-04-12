import cv2
import numpy as np
import mcpi.minecraft as minecraft
import mcpi.block as block
from time import *

cap=cv2.VideoCapture(0)#打开摄像头
lower_red=np.array([1,150,100])
upper_red=np.array([8,255,255])
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

def  move(mx,my):
    if mx<210 and 160<my<320:#左
        mc.player.setPos(pos.x+1,pos.y,pos.z)
    elif 430<mx<640 and 160<my<320:#右
        mc.player.setPos(pos.x-1,pos.y,pos.z)
    elif 210<mx<430 and my<160:#前
        mc.player.setPos(pos.x,pos.y,pos.z+1)
    elif 210<mx<430 and 320<my<480:#后
        mc.player.setPos(pos.x,pos.y,pos.z-1)
    elif mx<210 and my<160:#左前方
        mc.player.setPos(pos.x+1,pos.y,pos.z+1)
           # sleep(0.1)
    elif 430<mx<640 and my<160:#右前方
        mc.player.setPos(pos.x-1,pos.y,pos.z+11)
    elif mx<210 and 320<my<480:#左后方
        mc.player.setPos(pos.x+1,pos.y,pos.z-1)
    elif 430<mx<640 and 320<my<480:#右后方
        mc.player.setPos(pos.x-1,pos.y,pos.z-1)
    else:
        mc.player.setPos(pos.x,pos.y+1,pos.z)

while True:
    ret,pic=cap.read()#截取一帧图片
    y,x,l=pic.shape
    #print(x,y)
    pichsv=cv2.cvtColor(pic,cv2.COLOR_BGR2HSV)#选择相应的截取图片转换为hsv格式
    red=cv2.inRange(pichsv,lower_red,upper_red)#将选择的图片进行设阈值，去除背景部分
    #cv2.imshow("red",red)
    conter,hierarchy=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)#找轮廓
    pic=cv2.drawContours(pic,conter,-1,(0,255,0),3)#画轮廓

    
    pos = mc.player.getTilePos()
    biggest=[]
    for i in conter:
        area = cv2.contourArea(i)#计算轮廓面积
        if area>500:
            biggest.append(i)
        for cnt in biggest:
            M=cv2.moments(cnt)
            cx=int(M['m10']/M['m00'])
            cy=int(M['m01']/M['m00'])
            print(cx,cy)
            move(cx,cy)
            cv2.circle(pic,(cx,cy),50,(0,0,255),5)

    
    cv2.imshow('drawimg',pic)
    key=cv2.waitKey(1)&0xFF
    if key ==ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        breakcamera()
        
