from aip import AipSpeech
from xpinyin import Pinyin
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import re
import pyaudio
import wave
import mcpi.minecraft as minecraft
import mcpi.block as block

pp=Pinyin()
APP_ID = '17527531'
API_KEY = 'sGeHlRhneatUOLZAGpu0G3ef'
SECRET_KEY = 'jM4iRjwpKkgVqclQlTxnc26daZTdXist'
client=AipSpeech(APP_ID,API_KEY,SECRET_KEY)
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
x=pos.x
y=pos.y
z=pos.z

def readFile(fileName):
    with open(fileName,'rb') as fp:
        return fp.read()

def record():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 8000
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "audio.wav"

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
    wf.close()
#APP_ID='17980615'
#API_KEY='plQlVZYLO4aPDLM55GGMGe5L'
#SECRET_KEY='0Pba78PqkEch32ozc4lbvMFmjN7kaejw'
def listen():
    global pp
    global pos,x,y,z

    SWITCH={
        "yi":1,
        "er":2,
        "san":3,
        "si":4,
        "wu":5,
        "liu":6,
        "qi":7,
        "ba":8,
        "jiu":9,
        "shi":10,
    }
    
    print("* 正在识别......")
    result=client.asr(readFile("audio.wav"),'wav',16000,{'dev_pid':1537})
    #print(result)
    jieguo=pp.get_pinyin(result["result"][0][0:2])
    jieguo1=pp.get_pinyin(result["result"][0][2])
    print(jieguo)
    if result["err_no"]==0:
        #for t in result["result"]:
        #    print(t)
        print(result["result"][0][0:3])
        if jieguo1 in SWITCH:
            if (result["result"][0][0:2]=="前进")|(jieguo=="qian-qin"):
                print("ok")
                x=x+SWITCH[jieguo1]
                #print("ok")
                mc.player.setTilePos(x,y,z)
            elif (result["result"][0][0:2]=="后退")|(jieguo=="hou-tui"):
                print("ok1")
                x=x-SWITCH[jieguo1]
                mc.player.setTilePos(x,y,z)
            elif (result["result"][0][0:2]=="向左")|(jieguo=="xiang-zuo"):
                print("ok2")
                z=z-SWITCH[jieguo1]
                mc.player.setTilePos(x,y,z)
            elif (result["result"][0][0:2]=="向右")|(jieguo=="xiang-you"):
                print("ok3")
                z=z+SWITCH[jieguo1]
                mc.player.setTilePos(x,y,z)   
            elif (result["result"][0][0:2]=="向上")|(jieguo=="xiang-shang"):
                print("ok4")
                y=y+SWITCH[jieguo1]
                mc.player.setTilePos(x,y,z) 
            elif (result["result"][0][0:2]=="向下")|(jieguo=="xiang-xia"):
                print("ok5")
                y=y-SWITCH[jieguo1]
                mc.player.setTilePos(x,y,z) 
            else:
                print("no") 
        else:
            print("没有识别到语音\n",result["err_no"])
    else:
        print("没有识别到语音1\n",result["err_no"])

while True:
    kongzhi=""
    kongzhi=input("有什么可以帮助你的吗：")
    if kongzhi=="1":
        record()
        listen()
        kongzhi=""
    elif kongzhi=="3":
        kongzhi=""
        break
    