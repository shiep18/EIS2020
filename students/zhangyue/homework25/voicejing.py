import cv2
import numpy as np
import wave
from aip import AipSpeech
from xpinyin import Pinyin
import pyaudio


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

ti = 0
num = 0
pix = []
piz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
img = np.zeros((600, 600, 3), np.uint8)
img[:] = [200, 5, 100]
chess = np.zeros((3, 3), np.int8)
cv2.line(img, (480, 120), (480, 480), (250, 230, 200), 3)
cv2.line(img, (360, 120), (360, 480), (250, 230, 200), 3)
cv2.line(img, (240, 120), (240, 480), (250, 230, 200), 3)
cv2.line(img, (120, 120), (120, 480), (250, 230, 200), 3)
cv2.line(img, (120, 120), (480, 120), (250, 230, 200), 3)
cv2.line(img, (120, 240), (480, 240), (250, 230, 200), 3)
cv2.line(img, (120, 360), (480, 360), (250, 230, 200), 3)
cv2.line(img, (120, 480), (480, 480), (250, 230, 200), 3)


def click(event, x, y, flag, flags=0, param=0):
    global ti
    global pix
    if event == cv2.EVENT_LBUTTONDOWN:
        for i in range(3):
            for j in range(3):
                if (i + 1) * 120 < x < (i + 2) * 120 and (j + 1) * 120 < y < (j + 2) * 120 and piz[i][j] == 0:
                    if flag == 1:
                        cv2.circle(img, ((i + 1) * 120 + 60, (j + 1) * 120 + 60), 50, (0, 0, 0), -1)
                        cv2.imshow('cheese', img)
                        piz[i][j] = 1
                    else:
                        cv2.circle(img, ((i + 1) * 120 + 60, (j + 1) * 120 + 60), 50, (255, 255, 255), -1)
                        cv2.imshow('cheese', img)
                        piz[i][j] = -1
                        cv2.setMouseCallback('cheese', click)
                    pix = sum(piz, [])
                    ti = ti + 1


def readFile(fileName):
    with open(fileName, 'rb') as fp:
        return fp.read()


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
    result_wav = client.asr(readFile('audio.wav'), 'wav', 16000, {
        'dev_pid': 1537,
    })
    if result_wav["err_no"] == 0:
        for t in result_wav["result"]:
            return t
    else:
        print("没有识别到语音\n")
        return ""


def getPinYin(result_get):
    pin = Pinyin()
    return pin.get_pinyin(result_get)


def wakeUp(pin_yin):
    if getPinYin("小爱同学") in pin_yin:
        if getPinYin("白") in pin_yin:
            color = 2
            if getPinYin("一一") in pin_yin:
                click(1, 180, 180, color)
            elif getPinYin("一二") in pin_yin:
                click(1, 180, 300, color)
            elif getPinYin("一三") in pin_yin:
                click(1, 180, 420, color)
            elif getPinYin("二一") in pin_yin:
                click(1, 300, 180, color)
            elif getPinYin("二二") in pin_yin:
                click(1, 300, 300, color)
            elif getPinYin("二三") in pin_yin:
                click(1, 300, 420, color)
            elif getPinYin("三一") in pin_yin:
                click(1, 420, 180, color)
            elif getPinYin("三二") in pin_yin:
                click(1, 420, 300, color)
            elif getPinYin("三三") in pin_yin:
                click(1, 420, 420, color)
        elif getPinYin("黑") in pin_yin:
            color = 1
            if getPinYin("一一") in pin_yin:
                click(1, 180, 180, color)
            elif getPinYin("一二") in pin_yin:
                click(1, 180, 300, color)
            elif getPinYin("一三") in pin_yin:
                click(1, 180, 420, color)
            elif getPinYin("二一") in pin_yin:
                click(1, 300, 180, color)
            elif getPinYin("二二") in pin_yin:
                click(1, 300, 300, color)
            elif getPinYin("二三") in pin_yin:
                click(1, 300, 420, color)
            elif getPinYin("三一") in pin_yin:
                click(1, 420, 180, color)
            elif getPinYin("三二") in pin_yin:
                click(1, 420, 300, color)
            elif getPinYin("三三") in pin_yin:
                click(1, 420, 420, color)


def win_or_lost():
    lines = [pix[0:3], pix[3:6], pix[6:9], pix[0::3], pix[1::3], pix[2::3], pix[0::4], pix[2:7:2]]
    if [1] * 3 in lines:
        return 0
    elif [-1] * 3 in lines:
        return 1
    else:
        return 2


cv2.imshow('cheese', img)
cv2.namedWindow('cheese')
cv2.setMouseCallback('cheese', click)
while True:
    if cv2.waitKey(10) & 0xFF == 27:
        break
    elif win_or_lost() != 2:
        if win_or_lost() == 0:
            print('black wins,white lost!')
            print('the game finish!')
            break
        elif win_or_lost() == 1:
            print('black lost,white wins!')
            print('the game finish!')
            break
    elif win_or_lost() == 2 and ti == 9:
        print('draw!')
        print('the game finish!')
        break
    result = getBaiduText()
    pinyin = getPinYin(result)
    print("等待唤醒")
    print(result)
    wakeUp(pinyin)

cv2.destroyAllWindows()
