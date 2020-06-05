import time
import speech_recognition as sr
import logging
from aip import AipSpeech
import cv2
import numpy as np
img  = np.zeros((600,600,3),np.uint8)
win = [0,0,0,0,0,0,0,0]
add = 0
def clear():
    img[:] = [255,127,0]
    cv2.line(img,(120,120),(480,120),(250,230,200),3)
    cv2.line(img,(120,240),(480,240),(250,230,200),3)
    cv2.line(img,(120,360),(480,360),(250,230,200),3)
    cv2.line(img,(120,480),(480,480),(250,230,200),3)
    cv2.line(img,(120,120),(120,480),(250,230,200),3)
    cv2.line(img,(240,120),(240,480),(250,230,200),3)
    cv2.line(img,(360,120),(360,480),(250,230,200),3)
    cv2.line(img,(480,120),(480,480),(250,230,200),3)
    #img[0:100,0:100] = re[0:100,0:100]
    cv2.imshow('result',img)
clear()

cv2.namedWindow('result')
BAIDU_APP_ID = '19165941'
BAIDU_API_KEY = 'XUqFyxlgEllBGh5qqRMfTh4x'
BAIDU_SECRET_KEY = 'S6GPVANUOEH4NFYxyfkd9f3lQPXfkx3N'
aip_speech = AipSpeech(BAIDU_APP_ID, BAIDU_API_KEY, BAIDU_SECRET_KEY)
r = sr.Recognizer()
mic = sr.Microphone(sample_rate=16000)
while True:
    cv2.imshow('result',img)
    print('>>>>>>录音中...')
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    print('>>>>>>识别中...')
    start_time = time.time()

    audio_data = audio.get_wav_data()
  
    ret = aip_speech.asr(audio_data, 'wav', 16000, {'dev_pid': 1537, })

    if ret and ret['err_no'] == 0:
        result = ret['result'][0]
        print(result)
        if "白" or "百" in result:
            color = (255,255,255)
            add = 1
        if "黑" in result:
            color = (0,0,0)
            add = -1
        if "一" in result:
            cv2.circle(img,(180,180),(50),color,-1)
            win[0]+=add
            win[3]+=add
            win[6]+=add
            cv2.imshow('result',img)
        if "四" in result:
            cv2.circle(img,(180,300),(50),color,-1)
            win[1]+=add
            win[3]+=add
            cv2.imshow('result',img)
        if "七" in result:
            cv2.circle(img,(180,420),(50),color,-1)
            win[2]+=add
            win[3]+=add
            win[7]+=add
            cv2.imshow('result',img)
        if "二" in result:
            cv2.circle(img,(300,180),(50),color,-1)
            win[0]+=add
            win[4]+=add
            cv2.imshow('result',img)
        if "五" in result:
            cv2.circle(img,(300,300),(50),color,-1)
            win[1]+=add
            win[4]+=add
            win[6]+=add
            win[7]+=add
            cv2.imshow('result',img)
        if "八" in result:
            cv2.circle(img,(300,420),(50),color,-1)
            win[2]+=add
            win[4]+=add
            cv2.imshow('result',img)
        if "三" in result:
            cv2.circle(img,(420,180),(50),color,-1)
            win[0]+=add
            win[5]+=add
            win[7]+=add
            cv2.imshow('result',img)
        if "六" in result:
            cv2.circle(img,(420,300),(50),color,-1)
            win[1]+=add
            win[5]+=add
            cv2.imshow('result',img)
        if "九" in result:
            cv2.circle(img,(420,420),(50),color,-1)
            win[2]+=add
            win[5]+=add
            win[6]+=add
            cv2.imshow('result',img)
        if "清空" in result:
            clear()
        end_time = time.time()
    else:
        print(" ")
    for x in win:
        if x == 3:
            print("white win!")
            win = [0,0,0,0,0,0,0,0]
            
        elif x == -3:
            print("black win!")
            win = [0,0,0,0,0,0,0,0]

    if 0 not in win:
        print("no one win!")
        win = [0,0,0,0,0,0,0,0]

    if cv2.waitKey(10)&0xFF==27:
        break
cv2.destroyAllWindows()
