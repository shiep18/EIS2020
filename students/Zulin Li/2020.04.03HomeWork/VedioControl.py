#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Autor:ZLL
import cv2
from KeyBoardMove import *
from HouseClass import *
from CsvToHouse import *
import numpy as np
from pykeyboard import PyKeyboard
mc = minecraft.Minecraft.create()
k=PyKeyboard()
auto.PAUSE=1

def MoveIt(dx,dy,X,Y):
    if X / 4 < dx < X*3/4 and dy < Y/4:
        k.press_key("w")
    else:
        k.release_key("w")

    if X / 4 < dx < X*3/4 and dy > Y*3/4:
        k.press_key("s")
    else:
        k.release_key("s")

    if Y / 4 < dy < Y*3/4 and dx < X / 4:
        k.press_key("a")
    else:
        k.release_key("a")

    if Y / 4 < dy < Y*3/4 and dx > X*3/4:
        k.press_key("d")
    else:
        k.release_key("d")



cap=cv2.VideoCapture(0)
mc.player.setTilePos([500,0,500])
house = ReadCsv()
# 设定蓝色阈值
lower_blue = np.array([100, 90, 55])
upper_blue = np.array([255, 255, 95])

def Cammer():
    while True:
        ret,img=cap.read()
        ymax,xmax,l=img.shape
        #转换到HSV
        hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        # 根据阈值构建掩模
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        #对原图像和掩模进行位运算:将原图像img先与mask重合(筛去不在阈值区间的部分)
        #再将图二hsv与相重合，得到一幅只显示阈值内色块的图像a
        #res=cv2.bitwise_and(img,img,mask=mask)
        #寻找与圈定轮廓
        conts, hrc = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        #DST = cv2.drawContours(img, conts, -3, (0, 255, 0), 3)
        big=[]
        for i in conts:
            area=cv2.contourArea(i)
            if area > 1200:
                big.append(i)

        cx = int(xmax / 2)
        cy = int(ymax / 2)

        for cnt in big:
            M=cv2.moments(cnt)
            cx=int(M['m10']/M['m00'])
            cy = int(M['m01'] / M['m00'])
            cv2.circle(img,(cx,cy),50,(150,250,50),4)
            break

        MoveIt(cx, cy, xmax, ymax)
        for i in range(0, len(house)):
            pos = mc.player.getTilePos()
            flag = house[i][0].InsideHouse(pos.x, pos.y, pos.z)
            house[i][0].SetLight(flag)

        cv2.imshow('img',img)
        #按q退出
        key=cv2.waitKey(100)&0xFF
        if key==ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

for i in range(0, len(house)):
    house[i][0] = House(house[i][0], house[i][1], house[i][2], house[i][3], house[i][4], house[i][5], house[i][6])
    house[i][0].SetHouse()
    house[i][0].getHouseMessage()

Cammer()