import time
import speech_recognition as sr
import logging
from aip import AipSpeech
import cv2
pd = cv2.imread('usa.jpg')
pd1 = cv2.imread('white.jpg')
cv2.imshow('result',pd)
cv2.namedWindow('result')
APP_ID = '18980660'
API_KEY = 'hwoVnCcUV1VoizMZzHU7ayu6'
SECRET_KEY = 'Z1ynGkPNF1GBoYnnMPBdxt4lY8mm48QS'
aip_speech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
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
