import os
import hyperlpr
import cv2
import speech_recognition as sr
import logging
from xpinyin import Pinyin
import expressdata as ex
import baidusound as bs

def detect(dir):   
    cap = cv2.VideoCapture(0) 
    while True:
        ret,frame = cap.read()
        cv2.imshow('Video',frame)
        cv2.waitKey(5)
        a=hyperlpr.HyperLPR_PlateRecogntion(frame)
        a=str(a)
        if a!="[]":
            break        
    cap.release()
    cv2.destroyAllWindows()  
    info=ex.user_info(a[3:10])
    if dir==1:
        if info!=None:
            bs.speak("欢迎，"+info[1])
        else:
            ex.car_add(a[3:10])
            bs.speak("欢迎访客，进门请左转走到头再右转，进入停车场停车")
    elif dir==2:
        if info!=None:
            bs.speak(info[1]+"祝您一路平安")        
        else:
            ex.delate(a[3:10])
            bs.speak("欢迎您的来访，祝您一路顺风")





    

