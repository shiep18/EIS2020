import numpy as np
import speech_recognition as sr
import logging
from aip import AipSpeech
import time
import cv2

#创建棋盘
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

#引入百度语音
BAIDU_APP_ID = '19165865'
BAIDU_API_KEY = 'W7N52MRGuGCyrrsm6aCRP4Y8'
BAIDU_SECRET_KEY = '8rzZd6FHqGnFPQloptdXGrHfLruy44QG'
aip_speech = AipSpeech(BAIDU_APP_ID, BAIDU_API_KEY, BAIDU_SECRET_KEY)
r = sr.Recognizer()
mic = sr.Microphone(sample_rate=16000)

#判定胜利条件
win = [0,0,0,0,0,0,0,0]
win1 = [0,0,0,0,0,0,0,0]


while True:
    
    #语音识别过程
    print('>>>>>>录音中...')
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    print('>>>>>>识别中...')
    start_time = time.time()
    audio_data = audio.get_wav_data()
    ret = aip_speech.asr(audio_data, 'wav', 16000, {'dev_pid': 1537, })

    #执行语音下棋程序，并将棋盘从上到下和从左到右各分为ABC三行
    if ret and ret['err_no'] == 0:
        result = ret['result'][0]
        print(result)
        if "白色AA" in result:
            print("白棋:1.1")
            cv2.circle(img, (180, 180), 50, (255, 255, 255), -1)
            win[0]+=1
            win[3]+=1
            win[6]+=1
        if "白色AB" in result:
            print("白棋:1.2")
            cv2.circle(img, (300, 180), 50, (255, 255, 255), -1)
            win[0]+=1
            win[4]+=1
        if "白色AC" in result:
            print("白棋:1.3")
            cv2.circle(img, (420, 180), 50, (255, 255, 255), -1)
            win[0]+=1
            win[5]+=1
            win[7]+=1
        if "白色BA" in result:
            print("白棋:2.1")
            cv2.circle(img, (180, 300), 50, (255, 255, 255), -1)
            win[1]+=1
            win[3]+=1
        if "白色BB" in result:
            print("白棋:2.2")
            cv2.circle(img, (300, 300), 50, (255, 255, 255), -1)
            win[1]+=1
            win[4]+=1
            win[6]+=1
            win[7]+=1
        if "白色BC" in result:
            print("白棋:2.3")
            cv2.circle(img, (420, 300), 50, (255, 255, 255), -1)
            win[1]+=1
            win[5]+=1
        if "白色CA" in result:
            print("白棋:3.1")
            cv2.circle(img, (180, 420), 50, (255, 255, 255), -1)
            win[2]+=1
            win[3]+=1
            win[7]+=1
        if "白色CB" in result:
            print("白棋:3.2")
            cv2.circle(img, (300, 420), 50, (255, 255, 255), -1)
            win[2]+=1
            win[4]+=1
        if "白色CC" in result:
            print("白棋:3.3")
            cv2.circle(img, (420, 420), 50, (255, 255, 255), -1)
            win[2]+=1
            win[5]+=1
            win[6]+=1
        if "黑色AA" in result:
            print("黑棋:1.1")
            cv2.circle(img, (180, 180), 50, (0,0,0), -1)
            win1[0]+=1
            win1[3]+=1
            win1[6]+=1
        if "黑色AB" in result:
            print("黑棋:1.2")
            cv2.circle(img, (300, 180), 50, (0,0,0), -1)
            win1[0]+=1
            win1[4]+=1
        if "黑色AC" in result:
            print("黑棋:1.3")
            cv2.circle(img, (420, 180), 50, (0,0,0), -1)
            win1[0]+=1
            win1[5]+=1
            win1[7]+=1
        if "黑色BA" in result:
            print("黑棋:2.1")
            cv2.circle(img, (180, 300), 50, (0,0,0), -1)
            win1[1]+=1
            win1[3]+=1
        if "黑色BB" in result:
            print("黑棋:2.2")
            cv2.circle(img, (300, 300), 50, (0,0,0), -1)
            win1[1]+=1
            win1[4]+=1
            win1[6]+=1
            win1[7]+=1
        if "黑色BC" in result:
            print("黑棋:2.3")
            cv2.circle(img, (420, 300), 50, (0,0,0), -1)
            win1[1]+=1
            win1[5]+=1
        if "黑色CA" in result:
            print("黑棋:3.1")
            cv2.circle(img, (180, 420), 50, (0,0,0), -1)
            win1[2]+=1
            win1[3]+=1
            win1[7]+=1
        if "黑色CB" in result:
            print("黑棋:3.2")
            cv2.circle(img, (300, 420), 50, (0,0,0), -1)
            win1[2]+=1
            win1[4]+=1
        if "黑色CC" in result:
            print("黑棋:3.3")
            cv2.circle(img, (420, 420), 50, (0,0,0), -1)
            win1[2]+=1
            win1[5]+=1
            win1[6]+=1
        if "重新开始" in result:
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
            win = [0,0,0,0,0,0,0,0]
            win1 = [0,0,0,0,0,0,0,0]

    else:
        print(" ")
    cv2.imshow('image', img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if win[0]==3 or win[1]==3 or win[2]==3 or win[3]==3 or win[4]==3 or win[5]==3 or win[6]==3 or win[7]==3 :
        print("白棋win!")
    elif win1[0]==3 or win1[1]==3 or win1[2]==3 or win1[3]==3 or win1[4]==3 or win1[5]==3 or win1[6]==3 or win1[7]==3 :
        print("黑棋win!")
cv2.destroyAllWindows()
