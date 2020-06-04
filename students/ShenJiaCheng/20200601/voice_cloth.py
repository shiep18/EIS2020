import time
import speech_recognition as sr
import logging
from aip import AipSpeech
import cv2
img = cv2.imread('1.jpg')
img1 = cv2.imread('2.jpg')
#face = cv2.imread('face.jpg')
#face = cv2.resize(face,(125,125),interpolation=cv2.INTER_CUBIC)
#pd[188:313,316:441] = face[0:125,0:125]
#pd1[188:313,316:441] = face[0:125,0:125]
#pd2[188:313,316:441] = face[0:125,0:125]
cv2.imshow('result',img)
cv2.namedWindow('result',0)

BAIDU_APP_ID = '19165943'
BAIDU_API_KEY = 'YZvt651qpTG8Sm0MmocMW9oz'
BAIDU_SECRET_KEY = 'GD5y6RcPciVdp05S6TWT9YHaQv3YGpbb'
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
            cv2.imshow('result',img1)
        if "黑" in result:
            print("好的，换黑色衣服。")
            cv2.imshow('result',img)
        end_time = time.time()
    else:
        print(" ")

cv2.destroyAllWindows()
