import time
import speech_recognition as sr
import logging
from aip import AipSpeech
import cv2
import numpy as np


#面部识别
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
img = cv2.imread('face.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imwrite('face.jpg',img[y:y+h,x:x+w])
    

pd = cv2.imread('black.jpg')
pd1 = cv2.imread('white.jpg')
pd2 = cv2.imread('yellow.jpg')
pd1[150:150+h,280:280+w]=img[y:y+h,x:x+w]
pd[150:150+h,280:280+w]=img[y:y+h,x:x+w]
pd2[150:150+h,280:280+w]=img[y:y+h,x:x+w]
cv2.imshow('result',pd)
cv2.namedWindow('result')
BAIDU_APP_ID = '19165936'
BAIDU_API_KEY = 'ob71scZRxoenNj3EuzrjDir3'
BAIDU_SECRET_KEY = 'jx9sdsbo3ZlyH6aUfTyA242ee2u1U2E6'
aip_speech = AipSpeech(BAIDU_APP_ID, BAIDU_API_KEY, BAIDU_SECRET_KEY)
r = sr.Recognizer()
mic = sr.Microphone(sample_rate=16000)


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
            print("好的，换白色衣服。")
            cv2.imshow('result',pd1)
        if "黑" in result:
            print("好的，换黑色衣服。")
            cv2.imshow('result',pd)
        if "黄" in result:
            print("好的，换黄色衣服。")
            cv2.imshow('result',pd2)
        end_time = time.time()
    else:
        print(" ")
    if cv2.waitKey(10)&0xFF==27:
        break
cv2.destroyAllWindows()
