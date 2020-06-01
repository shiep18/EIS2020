import wave
from aip import AipSpeech
from xpinyin import Pinyin
import pyaudio
import os
import cv2

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 8000
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "audio.wav"

APP_ID = '19165395'
API_KEY = 'x4jPYDgmGDXNOuDwsQBoTGfv'
SECRET_KEY = 'OpDbxHBvf4XrTjYRRNb8dhyPOazFHwm9'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

STATE = 0
TIME_START = 0
TIME_END = 0

num = 0
x = 0
y = 0
w = 0
h = 0
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
pd = cv2.imread('white.jpg')
pd1 = cv2.imread('yellow.jpg')
pd2 = cv2.imread('black.jpg')
img = cv2.imread('6.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    pass
head = img[y:(y + h), x:(x + w)]
head = cv2.resize(head, (130, 130), interpolation=cv2.INTER_CUBIC)
cv2.namedWindow('result')


def readFile(fileName):
    with open(fileName, 'rb') as fp:
        return fp.read()


def writeFile(fileName, result):
    with open(fileName, 'wb') as fp:
        fp.write(result)


def getBaiduText():
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

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))

    print("* 正在识别......")
    result = client.asr(readFile('audio.wav'), 'wav', 16000, {
        'dev_pid': 1537,
    })
    if result["err_no"] == 0:
        for t in result["result"]:
            return t
    else:
        print("没有识别到语音\n")
        return ""


def getBaiduVoice(text):
    result = client.synthesis(text, 'zh', 6, {'vol': 5, 'per': 4, 'spd': 5})
    if not isinstance(result, dict):
        writeFile("back.mp3", result)
    os.system("back.mp3")


def getPinYin(result):
    pin = Pinyin()
    return pin.get_pinyin(result)


def pic(pd4):
    cv2.destroyWindow('result')
    pd4[185:315, 315:445] = head[0:130, 0:130]
    cv2.imshow('result', pd4)


def wakeUp(pinyin):
    if getPinYin("小爱同学") in pinyin:
        if getPinYin("你好") in pinyin:
            print("你好")
        elif getPinYin("白色衣服") in pinyin:
            print("好的，白色衣服")
            pic(pd)
        elif getPinYin("黄色衣服") in pinyin:
            print("好的，黄色衣服")
            pic(pd1)
        elif getPinYin("黑色衣服") in pinyin:
            print("好的，黑色衣服")
            pic(pd2)
        else:
            print("我在")


def main():
    pic(pd)
    if cv2.waitKey(10) & 0xFF == 'q':
        return
    while True:
        result = getBaiduText()
        pinyin = getPinYin(result)
        print("等待唤醒")
        print(result)
        wakeUp(pinyin)
        if cv2.waitKey(10) & 0xFF == 'q':
            break


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        os.system("back.mp3")
        os.system("audio.wav")
        os.system("rmdir /s/q __pycache__")
