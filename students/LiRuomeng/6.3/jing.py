import cv2
import numpy as np
import speech_recognition as sr
import logging
from aip import AipSpeech
import time

BAIDU_APP_ID = '19455583'
BAIDU_API_KEY = '1GpE2BPDV8MgpgA00s1SvrmH'
BAIDU_SECRET_KEY = 'VUIOGVAXBQ3cucuVsIW049TnAvEQA3jq'
aip_speech = AipSpeech(BAIDU_APP_ID, BAIDU_API_KEY, BAIDU_SECRET_KEY)
r = sr.Recognizer()
mic = sr.Microphone(sample_rate=16000)

win = [0,0,0,0,0,0,0,0]
win1 = [0,0,0,0,0,0,0,0]
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
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
        if "白色AA" in result:
            print("白棋:第一行第一列")
            cv2.circle(img, (180, 180), 50, (255, 255, 255), -1)
            win[0]+=1
            win[3]+=1
            win[6]+=1
        if "白色AB" in result:
            print("白棋:第一行第二列")
            cv2.circle(img, (300, 180), 50, (255, 255, 255), -1)
            win[0]+=1
            win[4]+=1
        if "白色AC" in result:
            print("白棋:第一行第三列")
            cv2.circle(img, (420, 180), 50, (255, 255, 255), -1)
            win[0]+=1
            win[5]+=1
            win[7]+=1
        if "白色BA" in result:
            print("白棋:第二行第一列")
            cv2.circle(img, (180, 300), 50, (255, 255, 255), -1)
            win[1]+=1
            win[3]+=1
        if "白色BB" in result:
            print("白棋:第二行第二列")
            cv2.circle(img, (300, 300), 50, (255, 255, 255), -1)
            win[1]+=1
            win[4]+=1
            win[6]+=1
            win[7]+=1
        if "白色BC" in result:
            print("白棋:第二行第三列")
            cv2.circle(img, (420, 300), 50, (255, 255, 255), -1)
            win[1]+=1
            win[5]+=1
        if "白色CA" in result:
            print("白棋:第三行第一列")
            cv2.circle(img, (180, 420), 50, (255, 255, 255), -1)
            win[2]+=1
            win[3]+=1
            win[7]+=1
        if "白色cb" in result:
            print("白棋:第三行第二列")
            cv2.circle(img, (300, 420), 50, (255, 255, 255), -1)
            win[2]+=1
            win[4]+=1
        if "白色CC" in result:
            print("白棋:第三行第三列")
            cv2.circle(img, (420, 420), 50, (255, 255, 255), -1)
            win[2]+=1
            win[5]+=1
            win[6]+=1
        if "黑色AA" in result:
            print("黑棋:第一行第一列")
            cv2.circle(img, (180, 180), 50, (0,0,0), -1)
            win1[0]+=1
            win1[3]+=1
            win1[6]+=1
        if "黑色AB" in result:
            print("黑棋:第一行第二列")
            cv2.circle(img, (300, 180), 50, (0,0,0), -1)
            win1[0]+=1
            win1[4]+=1
        if "黑色AC" in result:
            print("黑棋:第一行第三列")
            cv2.circle(img, (420, 180), 50, (0,0,0), -1)
            win1[0]+=1
            win1[5]+=1
            win1[7]+=1
        if "黑色BA" in result:
            print("黑棋:第二行第一列")
            cv2.circle(img, (180, 300), 50, (0,0,0), -1)
            win1[1]+=1
            win1[3]+=1
        if "黑色BB" in result:
            print("黑棋:第二行第二列")
            cv2.circle(img, (300, 300), 50, (0,0,0), -1)
            win1[1]+=1
            win1[4]+=1
            win1[6]+=1
            win1[7]+=1
        if "黑色BC" in result:
            print("黑棋:第二行第三列")
            cv2.circle(img, (420, 300), 50, (0,0,0), -1)
            win1[1]+=1
            win1[5]+=1
        if "黑色CA" in result:
            print("黑棋:第三行第一列")
            cv2.circle(img, (180, 420), 50, (0,0,0), -1)
            win1[2]+=1
            win1[3]+=1
            win1[7]+=1
        if "黑色cb" in result:
            print("黑棋:第三行第二列")
            cv2.circle(img, (300, 420), 50, (0,0,0), -1)
            win1[2]+=1
            win1[4]+=1
        if "黑色CC" in result:
            print("黑棋:第三行第三列")
            cv2.circle(img, (420, 420), 50, (0,0,0), -1)
            win1[2]+=1
            win1[5]+=1
            win1[6]+=1
        if "重新开始" in result:
            img = np.zeros((512, 512, 3), np.uint8)
            cv2.namedWindow('image', cv2.WINDOW_NORMAL)
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
        #break
    elif win1[0]==3 or win1[1]==3 or win1[2]==3 or win1[3]==3 or win1[4]==3 or win1[5]==3 or win1[6]==3 or win1[7]==3 :
        print("黑棋win!")
        #break
cv2.destroyAllWindows()
