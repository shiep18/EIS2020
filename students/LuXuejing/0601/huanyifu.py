import pyaudio
from aip import AipSpeech
from xpinyin import Pinyin
import cv2
import time as t

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

pd = cv2.imread('b.jpg')
pd1 = cv2.imread('w.jpg')
pd2 = cv2.imread('y.jpg')

def RecodeSound():
    import wave
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 8000
    RECORD_SECONDS = 3
    WAVE_OUTPUT_FILENAME = "audio.wav"

    APP_ID='19518465'
    API_KEY='UF4ODqCLzdI4beDM35xgqBUZ'
    SECRET_KEY='7GgZSfL4M621duaMtEfhQAwgzGX0kkhb'
    client =AipSpeech(APP_ID,API_KEY,SECRET_KEY)

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

    stream.start_stream()
    print("* 开始录音......")
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    stream.stop_stream()
    #录音结束

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    with open('audio.wav', 'rb') as fp:
        wave=fp.read()

    print("*正在识别......",len(wave))
    result=client.asr(wave,'wav',16000,{'dev_pid':1537})
    #print(result['result'])
    if '。' in result['result'][0]:
        result['result'][0]=result['result'][0].replace('。','')
    
    if result["err_no"]==0:
        print(result['result'][0])
        return result['result'][0]
    else:
        print("没有识别到语音\n",result["err_no"])
        return 'Err'

def click(event,x,y,flags,param):
    p = Pinyin()
    #print('mouse coords:',x,y)
    txt=RecodeSound()
    ptxt = p.get_pinyin(txt)
    if p.get_pinyin('黑色') in ptxt:
        img=pd.copy()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imshow('result',img)

    elif p.get_pinyin('白色') in ptxt:
        img = pd1.copy()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imshow('result', img)

    elif p.get_pinyin('黄色') in ptxt:
        img = pd2.copy()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imshow('result', img)
            
cv2.namedWindow('result')
cv2.setMouseCallback('result',click)
while True:
    if cv2.waitKey(10)&0xFF==27:
            break
cv2.destroyAllWindows()

