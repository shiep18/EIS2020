import win32api
import win32con
import cv2 as cv
import 爬取天气
from aip import AipSpeech
from xpinyin import Pinyin
import paho.mqtt.client as mqtt
from mcpi.minecraft import Minecraft
import mcpi.block as block
import pyaudio
import wave
import time

mc=Minecraft.create()
pos=mc.player.getTilePos()

APP_ID='19165237'
API_KEY='xNGyPcYDtr0sMRU5pW31sbyF'
SECRET_KEY='6rGHY9XqOGuPtLybBLCDpcWCUh6lgGyi'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 8000
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "myworld.wav"

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
    result = client.asr(readFile('myworld.wav'), 'wav', 16000, {
        'dev_pid': 1537,
    })
    if result["err_no"] == 0:
        for t in result["result"]:
            return t
    else:
        print("没有识别到语音\n")
        return ""

def getPinYin(result):
    pin = Pinyin()
    return pin.get_pinyin(result)

def go(a):
    if a == 1:
        win32api.keybd_event(87, 0, 0, 0)  # w键位码是87
        time.sleep(0.3)
        win32api.keybd_event(87, 0, win32con.KEYEVENTF_KEYUP,0)
    elif a == 2:
        win32api.keybd_event(83, 0, 0, 0)  # s键位码是83
        time.sleep(0.3)
        win32api.keybd_event(83, 0, win32con.KEYEVENTF_KEYUP, 0)
    elif a == 3:
        win32api.keybd_event(65, 0, 0, 0)  # a键位码是65
        time.sleep(0.3)
        win32api.keybd_event(65, 0, win32con.KEYEVENTF_KEYUP, 0)
    elif a == 4:
        win32api.keybd_event(68, 0, 0, 0)  # d键位码是68
        time.sleep(0.3)
        win32api.keybd_event(68, 0, win32con.KEYEVENTF_KEYUP, 0)
    else : pass

def put_weather():
    a = 爬取天气.gettemp()
    a = int(a)
    gewei = a%10
    shiwei = a//10
    getpic(pos.x,pos.y,pos.z,shiwei)
    getpic(pos.x+16, pos.y, pos.z, gewei)
    for i in range(a):
        mc.setBlock(pos.x-5, pos.y + i, pos.z, 214)


def getpic(x0,y0,z0,zhi):
    a = 16
    b = 16

    img =cv.imread("D:/pythoncharm/unbeded/minecraft_m3_all/minecraft_m3_all/py/num/%s.jpg"%zhi)
    gray =cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret,thresh1 = cv.threshold(gray,127,255,cv.THRESH_BINARY)
    #re_img = cv.resize(thresh1,(b,a))
    for x in range(a):
        for y in range(b):
            mc.setBlock(x0+a-x-1,y0+y,z0,80)
    for x in range(a):
        for y in range(b):
            if thresh1[x][y] == 0:
                mc.setBlock(x0 +y,y0  + a - x - 1, z0, 49)

def wakeUp(result, pinyin):
    if getPinYin("小明同学") in pinyin:
        if getPinYin("前") in pinyin:
            go(1)
        elif getPinYin("后") in pinyin:
            go(2)
        elif getPinYin("左") in pinyin:
            go(3)
        elif getPinYin("右") in pinyin:
            go(4)
        elif getPinYin("天气") in pinyin:
            put_weather()
    else :
        print("我在")

while True:
    result = getBaiduText()
    pinyin = getPinYin(result)
    print("等待唤醒")
    print(result)
    wakeUp(result, pinyin)