import cv2
import numpy as np
import time
import speech_recognition as sr
import logging
from aip import AipSpeech
import win32api,win32con
from xpinyin import Pinyin


img  = np.zeros((600,600,3),np.uint8)
win = [0,0,0,0,0,0,0,0]
num = [0]
def draw():
    img[:]=[200,5,100]
    cv2.line(img,(120,120),(480,120),(255,255,255),3)
    cv2.line(img,(120,240),(480,240),(255,255,255),3)
    cv2.line(img,(120,360),(480,360),(255,255,255),3)
    cv2.line(img,(120,480),(480,480),(255,255,255),3)
    cv2.line(img,(120,120),(120,480),(255,255,255),3)
    cv2.line(img,(240,120),(240,480),(255,255,255),3)
    cv2.line(img,(360,120),(360,480),(255,255,255),3)
    cv2.line(img,(480,120),(480,480),(255,255,255),3)
    win = [0,0,0,0,0,0,0,0]
    cv2.imshow('result',img)
draw()

def getPinYin(result):
    pin = Pinyin()
    return pin.get_pinyin(result)
    
def click(x,y,color):
    
    if color==1:
        num[0]=num[0]+1
        #print('mouse coords:',x,y)
        if 120<x<240 and 120<y<240:
            cv2.circle(img,(180,180),(50),(255,255,255),-1)
            win[0]+=1
            win[3]+=1
            win[6]+=1
            cv2.imshow('result',img)
        elif 120<x<240 and 240<y<360:
            cv2.circle(img,(180,300),(50),(255,255,255),-1)
            win[1]+=1
            win[3]+=1
            cv2.imshow('result',img)
        elif 120<x<240 and 360<y<480:
            cv2.circle(img,(180,420),(50),(255,255,255),-1)
            win[2]+=1
            win[3]+=1
            win[7]+=1
            cv2.imshow('result',img)
        elif 240<x<360 and 120<y<240:
            cv2.circle(img,(300,180),(50),(255,255,255),-1)
            win[0]+=1
            win[4]+=1
            cv2.imshow('result',img)
        elif 240<x<360 and 240<y<360:
            cv2.circle(img,(300,300),(50),(255,255,255),-1)
            win[1]+=1
            win[4]+=1
            win[6]+=1
            win[7]+=1
            cv2.imshow('result',img)
        elif 240<x<360 and 360<y<480:
            cv2.circle(img,(300,420),(50),(255,255,255),-1)
            win[2]+=1
            win[4]+=1
            cv2.imshow('result',img)
        elif 360<x<480 and 120<y<240:
            cv2.circle(img,(420,180),(50),(255,255,255),-1)
            win[0]+=1
            win[5]+=1
            win[7]+=1
            cv2.imshow('result',img)
        elif 360<x<480 and 240<y<360:
            cv2.circle(img,(420,300),(50),(255,255,255),-1)
            win[1]+=1
            win[5]+=1
            cv2.imshow('result',img)
        elif 360<x<480 and 360<y<480:
            cv2.circle(img,(420,420),(50),(255,255,255),-1)
            win[2]+=1
            win[5]+=1
            win[6]+=1
            cv2.imshow('result',img)
    elif color==2:
        num[0]=num[0]+1
        #print('mouse coords:',x,y)
        if 120<x<240 and 120<y<240:
            cv2.circle(img,(180,180),(50),(0,0,0),-1)
            win[0]-=1
            win[3]-=1
            win[6]-=1
            cv2.imshow('result',img)
        elif 120<x<240 and 240<y<360:
            cv2.circle(img,(180,300),(50),(0,0,0),-1)
            win[1]-=1
            win[3]-=1
            cv2.imshow('result',img)
        elif 120<x<240 and 360<y<480:
            cv2.circle(img,(180,420),(50),(0,0,0),-1)
            win[2]-=1
            win[3]-=1
            win[7]-=1
            cv2.imshow('result',img)
        elif 240<x<360 and 120<y<240:
            cv2.circle(img,(300,180),(50),(0,0,0),-1)
            win[0]-=1
            win[4]-=1
            cv2.imshow('result',img)
        elif 240<x<360 and 240<y<360:
            cv2.circle(img,(300,300),(50),(0,0,0),-1)
            win[1]-=1
            win[4]-=1
            win[6]-=1
            win[7]-=1
            cv2.imshow('result',img)
        elif 240<x<360 and 360<y<480:
            cv2.circle(img,(300,420),(50),(0,0,0),-1)
            win[2]-=1
            win[4]-=1
            cv2.imshow('result',img)
        elif 360<x<480 and 120<y<240:
            cv2.circle(img,(420,180),(50),(0,0,0),-1)
            win[0]-=1
            win[5]-=1
            win[7]-=1
            cv2.imshow('result',img)
        elif 360<x<480 and 240<y<360:
            cv2.circle(img,(420,300),(50),(0,0,0),-1)
            win[1]-=1
            win[5]-=1
            cv2.imshow('result',img)
        elif 360<x<480 and 360<y<480:
            cv2.circle(img,(420,420),(50),(0,0,0),-1)
            win[2]-=1
            win[5]-=1
            win[6]-=1
            cv2.imshow('result',img)
cv2.namedWindow('result')
cv2.setMouseCallback('result',click)

BAIDU_APP_ID = '19165151'
BAIDU_API_KEY = 'ih6wgeKUaRrubYOBykp2kNZe'
BAIDU_SECRET_KEY = 'e0H9uyxuBxI1RRZSoN25vcDb4gPCUyDK'
aip_speech = AipSpeech(BAIDU_APP_ID, BAIDU_API_KEY, BAIDU_SECRET_KEY)
r = sr.Recognizer()
mic = sr.Microphone(sample_rate=16000)
while True:
    x=0
    y=0
    color=0
    for m in win:
        if m == 3:
            print("白棋获胜!\n")
            win = [0,0,0,0,0,0,0,0]
            time.sleep(1)
            draw()
            check=win32api.MessageBox(0, "请问要重新开局吗？", "提醒",win32con.MB_YESNO)
            if check==6:
                check=0
                continue
            else:
                break
        elif m == -3:
            print("黑棋获胜！\n")
            win = [0,0,0,0,0,0,0,0]
            time.sleep(1)
            check=win32api.MessageBox(0, "请问要重新开局吗？", "提醒",win32con.MB_YESNO)
            if check==6:
                check=0
                continue
            else:
                break
        elif num[0]==9:
            print("平局\n")
            num[0]=0
            win = [0,0,0,0,0,0,0,0]
            time.sleep(1)
            check=win32api.MessageBox(0, "请问要重新开局吗？", "提醒",win32con.MB_YESNO)
            if check==6:
                check=0
                continue
            else:
                break
    print('>>>>>>录音中...')
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    print('>>>>>>识别中...')
    start_time = time.time()
    audio_data = audio.get_wav_data()
    ret = aip_speech.asr(audio_data, 'wav', 16000, {'dev_pid': 1537, })
    if ret and ret['err_no'] == 0:
        result = getPinYin(ret['result'][0])

        print(result)
        if getPinYin("白") in result:
            color=1
        elif getPinYin("黑") in result:
            color=2

        if getPinYin("一") in result:
                x=180
                y=180
                click(x,y,color)
                time.sleep(0.5)
        elif getPinYin("二") in result:
                x=300
                y=180
                click(x,y,color)
                time.sleep(0.5)
        elif getPinYin("三") in result:
                x=420
                y=180
                click(x,y,color)
                time.sleep(0.5)
        elif getPinYin("四") in result:
                x=180
                y=300
                click(x,y,color)
                time.sleep(0.5)
        elif getPinYin("五") in result:
                x=300
                y=300
                click(x,y,color)
                time.sleep(0.5)
        elif getPinYin("六") in result:
                x=420
                y=300
                click(x,y,color)
                time.sleep(0.5)
        elif getPinYin("七") in result:
                x=180
                y=420
                click(x,y,color)
                time.sleep(0.5)
        elif getPinYin("八") in result:
                x=300
                y=420
                click(x,y,color)
                time.sleep(0.5)
        elif getPinYin("九") in result:
                x=420
                y=420
                click(x,y,color)
                time.sleep(0.5)
        end_time = time.time()
    else:
        print(" ")     
    if cv2.waitKey(10)&0xFF==27:
        break
cv2.destroyAllWindows()