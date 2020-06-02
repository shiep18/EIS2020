import time
import os
import speech_recognition as sr
import logging
from aip import AipSpeech
import cv2

x = 0
y = 0
w = 0
h = 0

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
pd = cv2.imread('1.jpg')
pd1 = cv2.imread('2.jpg')
pd2 = cv2.imread('3.jpg')

img = cv2.imread('tou.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    pass
head = img[y:(y + h), x:(x + w)]
head = cv2.resize(head, (130, 130), interpolation=cv2.INTER_CUBIC)
cv2.namedWindow('result')

BAIDU_APP_ID = '19165595'
BAIDU_API_KEY = '94C64NI6tR0Glm60d0wA3GUD'
BAIDU_SECRET_KEY = 'qFzfyeF2inDryNd28QD3hzSSi9SfG5v8'
aip_speech = AipSpeech(BAIDU_APP_ID, BAIDU_API_KEY, BAIDU_SECRET_KEY)

r = sr.Recognizer()
mic = sr.Microphone(sample_rate=16000)

def writeFile(fileName,result):
    with open(fileName, 'wb') as fp:
        fp.write(result)

def playVoice(fileName):
    os.system(fileName)

def getBaiduVoice(text):
    result  = aip_speech.synthesis(text, 'zh', 6, {'vol': 5, 'per':4,'spd':5})
    if not isinstance(result, dict):
        writeFile("back.mp3",result)
    playVoice("back.mp3")

def pic(pd4):
    cv2.destroyWindow('result')
    pd4[185:315, 315:445] = head[0:130, 0:130]
    cv2.imshow('result', pd4)

while True:
# def yuyin():
    print('>>>>>>录音中...')
    print("您需要什么呢？")
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
        # if (result == "白色"):
        if "白色" in result:
            print("白色衣服已备好")
            getBaiduVoice("白色衣服已备好")
            # cv2.imshow('result', pd1)
            pic(pd1)
        elif "黑色" in result:
            print("黑色衣服已备好")
            getBaiduVoice("黑色衣服已备好")
            # cv2.imshow('result', pd)
            pic(pd)
        elif "黄色" in result:
            print("黄色衣服已备好")
            getBaiduVoice("黄色衣服已备好")
            # cv2.imshow('result', pd2)
            pic(pd2)
        else:
            print("请再讲一遍")
        end_time = time.time()

    else:
        print(" ")
    if cv2.waitKey(10)&0xFF==27:
        break
cv2.destroyAllWindows()