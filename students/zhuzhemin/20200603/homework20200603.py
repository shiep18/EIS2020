import time
import speech_recognition as sr
import logging
from aip import AipSpeech
import cv2
import numpy as np
BAIDU_APP_ID = '19165941'
BAIDU_API_KEY = 'XUqFyxlgEllBGh5qqRMfTh4x'
BAIDU_SECRET_KEY = 'S6GPVANUOEH4NFYxyfkd9f3lQPXfkx3N'
aip_speech = AipSpeech(BAIDU_APP_ID, BAIDU_API_KEY, BAIDU_SECRET_KEY)
r = sr.Recognizer()
mic = sr.Microphone(sample_rate=16000)
class chess1:
    def __init__(self):
        self.img=np.zeros((600,600,3),np.uint8)
        self.img[:]=[200,5,100]
        self.chess=np.zeros((3,3),np.int8)
        cv2.line(self.img,(120,120),(480,120),(250,230,200),3)
        cv2.line(self.img,(120,240),(480,240),(250,230,200),3)
        cv2.line(self.img,(120,360),(480,360),(250,230,200),3)
        cv2.line(self.img,(120,480),(480,480),(250,230,200),3)
        cv2.line(self.img,(120,120),(120,480),(250,230,200),3)
        cv2.line(self.img,(240,120),(240,480),(250,230,200),3)
        cv2.line(self.img,(360,120),(360,480),(250,230,200),3)
        cv2.line(self.img,(480,120),(480,480),(250,230,200),3)
        cv2.imshow('result',self.img)
        self.case=[0,255,0]
        self.flag=[0,0,0,0,0,0,0,0,0]
        self.flag1=0
        self.i=-1
        self.a=0
        self.b=0
        self.c=0
        self.d=0
        self.e=0
        self.f=0
        self.g=0
        self.h=0
    def start(self):
        img=self.img
        self.flag=[0,0,0,0,0,0,0,0,0]
        flag=self.flag
        case=self.case
        chess=self.chess
        img[:]=[200,5,100]
        cv2.line(img,(120,120),(480,120),(250,230,200),3)
        cv2.line(img,(120,240),(480,240),(250,230,200),3)
        cv2.line(img,(120,360),(480,360),(250,230,200),3)
        cv2.line(img,(120,480),(480,480),(250,230,200),3)
        cv2.line(img,(120,120),(120,480),(250,230,200),3)
        cv2.line(img,(240,120),(240,480),(250,230,200),3)
        cv2.line(img,(360,120),(360,480),(250,230,200),3)
        cv2.line(img,(480,120),(480,480),(250,230,200),3)
        cv2.imshow('result',img)
        self.flag1=0            
    def voice(self):
        if self.flag1==1:
            CHESS.start()
        flag=self.flag
        case=self.case
        img=self.img
        i=self.i
        a=self.a
        b=self.b
        c=self.c
        d=self.d
        e=self.e
        f=self.f
        g=self.g
        h=self.h       
        if "黑色一一" in result:
            print(黑色一一"")
            cv2.circle(img,(180,180),(50),(case[i],case[i],case[i]),-1)
            flag[0]=i
        elif "黑色一二" in result:
            print("黑色一二")
            cv2.circle(img,(180,300),(50),(case[i],case[i],case[i]),-1)
            flag[1]=i
        elif "黑色一三" in result:
            print("黑色一三")
            cv2.circle(img,(180,420),(50),(case[i],case[i],case[i]),-1)
            flag[2]=i
        elif "黑色二一" in result:
            print("黑色二一")
            cv2.circle(img,(300,180),(50),(case[i],case[i],case[i]),-1)
            flag[3]=i
        elif "黑色二二" in result:
            print("黑色二二")
            cv2.circle(img,(300,300),(50),(case[i],case[i],case[i]),-1)
            flag[4]=i
        elif "黑色二三" in result:
            print("黑色二三")
            cv2.circle(img,(300,420),(50),(case[i],case[i],case[i]),-1)
            flag[5]=i
        elif "黑色三一" in result:
            print("黑色三一")
            cv2.circle(img,(420,180),(50),(case[i],case[i],case[i]),-1)
            flag[6]=i
        elif "黑色三二" in result:
            print("黑色三二")
            cv2.circle(img,(420,300),(50),(case[i],case[i],case[i]),-1)
            flag[7]=i
        elif "黑色三三" in result:
            print("黑色三三")
            cv2.circle(img,(420,420),(50),(case[i],case[i],case[i]),-1)
            flag[8]=i  
        elif "白色一一" in result:
            print("白色一一")
            cv2.circle(img,(180,180),(50),(case[i+2],case[i+2],case[i+2]),-1)
            flag[0]=i+2
        elif "白色一二" in result:
            print("白色一二")
            cv2.circle(img,(180,300),(50),(case[i+2],case[i+2],case[i+2]),-1)
            flag[1]=i+2
        elif "白色一三" in result:
            print("白色一三")
            cv2.circle(img,(180,420),(50),(case[i+2],case[i+2],case[i+2]),-1)
            flag[2]=i+2
        elif "白色二一" in result:
            print("白色二一")
            cv2.circle(img,(300,180),(50),(case[i+2],case[i+2],case[i+2]),-1)
            flag[3]=i+2
        elif "白色二二" in result:
            print("白色二二")
            cv2.circle(img,(300,300),(50),(case[i+2],case[i+2],case[i+2]),-1)
            flag[4]=i+2
        elif "白色二三" in result:
            print("白色二三")
            cv2.circle(img,(300,420),(50),(case[i+2],case[i+2],case[i+2]),-1)
            flag[5]=i+2
        elif "白色三一" in result:
            print("白色三一")
            cv2.circle(img,(420,180),(50),(case[i+2],case[i+2],case[i+2]),-1)
            flag[6]=i+2
        elif "白色三二" in result:
            print("白色三二")
            cv2.circle(img,(420,300),(50),(case[i+2],case[i+2],case[i+2]),-1)
            flag[7]=i+2
        elif "白色三三" in result:
            print("白色三三")
            cv2.circle(img,(420,420),(50),(case[i+2],case[i+2],case[i+2]),-1)
            flag[8]=i+2
        cv2.imshow('result',img)
        a=flag[0]+flag[1]+flag[2]
        b=flag[3]+flag[4]+flag[5]
        c=flag[6]+flag[7]+flag[8]
        d=flag[0]+flag[3]+flag[6]
        e=flag[1]+flag[4]+flag[7]
        f=flag[2]+flag[5]+flag[8]
        g=flag[0]+flag[4]+flag[8]
        h=flag[2]+flag[4]+flag[6]
        if a==-3 or b==-3 or c==-3 or d==-3 or e==-3 or f==-3 or g==-3 or h==-3:
            print("Black WIN.")
            self.flag1=1
            #cv2.destroyAllWindows()
        elif a==3 or b==3 or c==3 or d==3 or e==3 or f==3 or g==3 or h==3:
            print("White WIN.")
            self.flag1=1
            #cv2.destroyAllWindows()
        elif (flag[0]==1 or flag[0]==-1)and(flag[1]==1 or flag[1]==-1)and(flag[2]==1 or flag[2]==-1)and(flag[3]==1 or flag[3]==-1)and(flag[4]==1 or flag[4]==-1)and(flag[5]==1 or flag[5]==-1)and(flag[6]==1 or flag[6]==-1)and(flag[7]==1 or flag[7]==-1)and(flag[8]==1 or flag[8]==-1):
            print("It's a draw.")
            self.flag1=1
CHESS=chess1()
cv2.namedWindow('result')
#cv2.setMouseCallback('result',CHESS.click)
while True:
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
        CHESS.voice()
        end_time = time.time()
    else:
        print(" ")
    if cv2.waitKey(10)&0xFF==27:
        break
cv2.destroyAllWindows()
