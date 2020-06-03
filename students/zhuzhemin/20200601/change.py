import time
import speech_recognition as sr
import logging
from aip import AipSpeech
import cv2
face_cascade = cv2.CascadeClassifier(r'E:\zhu\face\haarcascade_frontalface_default.xml')
img = cv2.imread("kobe's_head.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    pass
head=img[y:(y+h),x:(x+w)]
head=cv2.resize(head,(130,130),interpolation=cv2.INTER_CUBIC)
pd = cv2.imread('clothe1.jpg')
pd1 = cv2.imread('clothe2.jpg')
cv2.imshow('result',pd)
cv2.namedWindow('result')
pd[187:317,312:442]=head[0:130,0:130]
pd1[187:317,312:442]=head[0:130,0:130]
BAIDU_APP_ID = '19165941'
BAIDU_API_KEY = 'XUqFyxlgEllBGh5qqRMfTh4x'
BAIDU_SECRET_KEY = 'S6GPVANUOEH4NFYxyfkd9f3lQPXfkx3N'
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
        end_time = time.time()
    else:
        print(" ")
    if cv2.waitKey(10)&0xFF==27:
        break
cv2.destroyAllWindows()
