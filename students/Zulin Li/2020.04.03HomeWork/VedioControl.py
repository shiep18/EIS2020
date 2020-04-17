#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Autor:ZLL
import cv2
from KeyBoardMove import *
import numpy as np

cap=cv2.VideoCapture(0)

def Cammer():
    while True:
        ret,img=cap.read()
        ymax,xmax,len=img.shape
        #转换到HSV
        hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        #设定蓝色阈值
        lower_blue = np.array([98, 137, 75])
        upper_blue = np.array([255, 255, 255])
        # 根据阈值构建掩模
        mask=cv2.inRange(hsv,lower_blue,upper_blue)
        #对原图像和掩模进行位运算:将原图像img先与mask重合(筛去不在阈值区间的部分)
        #再将图二hsv与相重合，得到一幅只显示阈值内色块的图像
        res=cv2.bitwise_and(img,img,mask=mask)
        #寻找与圈定轮廓
        conts, hrc = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        DST = cv2.drawContours(img, conts, -3, (0, 255, 0), 3)
        big=[]
        for i in conts:
            area=cv2.contourArea(i)
            if area > 800:
                big.append(i)
            for cnt in big:
                M=cv2.moments(cnt)
                cx=int(M['m10']/M['m00'])
                cy = int(M['m01'] / M['m00'])
                cv2.circle(img,(cx,cy),50,(150,250,50),4)
                MoveIt(cx, cy, xmax, ymax)

        cv2.imshow('img',img)
        #cv2.imshow('hsv',hsv)
        #cv2.imshow('mask',mask)
        #cv2.imshow('DST',DST)
        #cv2.imshow('res',res)
        #按q退出
        key=cv2.waitKey(100)&0xFF
        if key==ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

Cammer()