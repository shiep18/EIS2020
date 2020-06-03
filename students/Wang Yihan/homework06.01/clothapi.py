import time
import speech_recognition as sr
import logging
from aip import AipSpeech
import cv2
pd = cv2.imread('white.jpg')
pd1 = cv2.imread('pink.jpg')
cv2.imshow('result',pd)
cv2.namedWindow('result')
BAIDU_APP_ID = '19540945'
BAIDU_API_KEY = 'ElACzP3fgBKEGZb3ZCtiusVr'
BAIDU_SECRET_KEY = 'Uj2XAnjeDFdPm487tHdpdDuErWE0MGUE'
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
        if "粉" in result:
            print("好的，换粉色衣服。")
            cv2.imshow('result',pd1)
        if "白" in result:
            print("好的，换白色衣服。")
            cv2.imshow('result',pd)
        end_time = time.time()
    else:
        print(" ")
    if cv2.waitKey(10)&0xFF==27:
        break
cv2.destroyAllWindows()
