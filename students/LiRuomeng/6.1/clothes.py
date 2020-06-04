import time
import speech_recognition as sr
import logging
from aip import AipSpeech
import cv2
pd1 = cv2.imread('yellow.jpg')
pd2 = cv2.imread('white.jpg')
pd3 = cv2.imread('black.jpg')
pdface = cv2.imread('face.jpg')
pdface = cv2.resize(pdface,(59,59),interpolation=cv2.INTER_CUBIC)
pd3[103:162,172:231]=pdface[0:59,0:59]
pd1[103:162,172:231]=pdface[0:59,0:59]
pd2[103:162,172:231]=pdface[0:59,0:59]
global p
F=0
T=1
p=F
cv2.imshow('result',pd1)
BAIDU_APP_ID = '19455583'
BAIDU_API_KEY = '1GpE2BPDV8MgpgA00s1SvrmH'
BAIDU_SECRET_KEY = 'VUIOGVAXBQ3cucuVsIW049TnAvEQA3jq'
aip_speech = AipSpeech(BAIDU_APP_ID, BAIDU_API_KEY, BAIDU_SECRET_KEY)
r = sr.Recognizer()
mic = sr.Microphone(sample_rate=16000)

cv2.namedWindow('result')


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
        if "白色" in result:
            print("正在换白色衣服")
            cv2.imshow('result',pd2)
        if "黑色" in result:
            print("正在换黑色衣服")
            cv2.imshow('result',pd3)
        if "黄色" in result:
            print("正在换黄色衣服")
            cv2.imshow('result',pd1)
    else:
        print(" ")

    if cv2.waitKey(10)&0xFF==27:
        break


cv2.destroyAllWindows()
