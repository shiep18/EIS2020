#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Autor:ZLL
import cv2
import time
import pygame
import numpy as np

file = r'E:\PythonProject\Homework\20200401HomeWork\Vedio\m.mp3'
pygame.mixer.init()
track = pygame.mixer.music.load(file)

cap=cv2.VideoCapture(0)

PlayMusic=0
background = None
while True:
    ret,img=cap.read()
    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    if background is None:
        background=gray_img
        time.sleep(0.1)
        continue
    diff = cv2.absdiff(background,gray_img)
    diff = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]
    #寻找与圈定轮廓,TREE: ，EXTERNAL：
    conts, hrc = cv2.findContours(diff.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    GetMove = 0
    num=0
    for i in conts:
        num+=1
        if cv2.contourArea(i) > 1000:
            (x,y,w,h)=cv2.boundingRect(i)
            #被画图像，对角坐标1，对角坐标2，线色，线粗细
            cv2.rectangle(img,(x,y),(x+w,y+h),(127,127,127),4)
            GetMove=1
            num-=1

    if len(conts)<=num:
        GetMove=0
    elif len(conts)>num:
        GetMove=1

    if GetMove==1 and PlayMusic==0:
        pygame.mixer.music.play()
        PlayMusic = 1
        print('Playing....')
    if GetMove==0 and PlayMusic==1:
        pygame.mixer.music.pause()
        PlayMusic = 0
        print('Pause')


    cv2.imshow('img',img)
    cv2.imshow('dif',diff)
    #按q退出
    key=cv2.waitKey(100)&0xFF
    if key==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()