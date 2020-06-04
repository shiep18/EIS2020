import time
import speech_recognition as sr
import logging
from aip import AipSpeech
import cv2
import numpy as np

BAIDU_APP_ID = '19455322'
BAIDU_API_KEY = 'Mf483gm9St29BDeUGLUrPGnI'
BAIDU_SECRET_KEY = 'fxuawYvBZAtAK8ipcP7a5vfPxOieU9BE'
aip_speech = AipSpeech(BAIDU_APP_ID, BAIDU_API_KEY, BAIDU_SECRET_KEY)
r = sr.Recognizer()
mic = sr.Microphone(sample_rate=16000)

white = cv2.imread('T2.jpg')
black = cv2.imread('T1.jpg')
cv2.namedWindow('result',0)
cv2.imshow('result',white)
cv2.waitKey(1)

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
        if "白" in result:
            cv2.namedWindow('result',0)
            cv2.imshow('result',white)
            cv2.waitKey(1)
        if "黑" in result:
            cv2.namedWindow('result',0)
            cv2.imshow('result',black)
            cv2.waitKey(1)

        end_time = time.time()
    else:
        print(" ")
cv2.destroyAllWindows()
