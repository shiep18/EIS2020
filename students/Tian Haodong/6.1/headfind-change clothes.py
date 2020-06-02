import time
import speech_recognition as sr
import logging
from aip import AipSpeech
import cv2
import numpy as np


#面部识别
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
img = cv2.imread('1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imwrite('face.jpg',img[y:y+h,x:x+w])
    








BAIDU_APP_ID = '19165941'
BAIDU_API_KEY = 'XUqFyxlgEllBGh5qqRMfTh4x'
BAIDU_SECRET_KEY = 'S6GPVANUOEH4NFYxyfkd9f3lQPXfkx3N'
aip_speech = AipSpeech(BAIDU_APP_ID, BAIDU_API_KEY, BAIDU_SECRET_KEY)
r = sr.Recognizer()
mic = sr.Microphone(sample_rate=16000)

white = cv2.imread('yi1.jpg')
black = cv2.imread('yi2.jpg')
yellow = cv2.imread('yi3.jpg')
white[130:130+h,270:270+w]=img[y:y+h,x:x+w]
black[130:130+h,270:270+w]=img[y:y+h,x:x+w]
yellow[130:130+h,270:270+w]=img[y:y+h,x:x+w]
cv2.namedWindow('result',0)
cv2.imshow('result',white)
cv2.waitKey(1)
#cv2.destroyAllWindows()

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
        if "黄" in result:
            cv2.namedWindow('result',0)
            cv2.imshow('result',yellow)
            cv2.waitKey(1)
        end_time = time.time()
    else:
        print(" ")
cv2.destroyAllWindows()

