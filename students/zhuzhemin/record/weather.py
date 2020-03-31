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
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
pp=Pinyin()
resp=urlopen("http://www.weather.com.cn/weather/101020100.shtml")#上海的7日温度
#print(resp)
soup=BeautifulSoup(resp,"html.parser")
#print(soup)
today=soup.find("p",class_="tem") #第一个包含class="tem"的p标签即为存放今天天气数据的标签
#print(today)
#tem=today.find_next("p",class_="tem").span.string
try:
    temHigh=today.span.string  #晚上的时候，最高温度是不显示的，此时利用第二天的最高温度代替。
except AttributeError as e:
    temHigh=today.find_next('p',class_="tem").span.string  #获取第二天的最高温度代替
    print("替代")
temLow=today.i.string#获取最低温度
weather=soup.find('p',class_="wea").string #获取天气

APP_ID = '17527531'
API_KEY = 'sGeHlRhneatUOLZAGpu0G3ef'
SECRET_KEY = 'jM4iRjwpKkgVqclQlTxnc26daZTdXist'
client=AipSpeech(APP_ID,API_KEY,SECRET_KEY)
x=pos.x
y=pos.y
z=pos.z

def readFile(fileName):
    with open(fileName,'rb') as fp:
        return fp.read()

def record():
    global pos
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
    x=pos.x
    y=pos.y
    z=pos.z
    print("* 正在识别......")
    result=client.asr(readFile("audio.wav"),'wav',16000,{'dev_pid':1537})
    #print(result)
    if result["err_no"]==0:
        for t in result["result"]:
            print(t)
            return t
    else:     
        print("没有识别到语音2\n")
        return ""

def writeFile(fileName,result):
    with open(fileName,"wb") as fp:
        fp.write(result)

def playVoice(fileName):
    os.system(fileName)

def getBaiduVoice(text):
    result=client.synthesis(text,"zh",6,{"vol":15,"per":4,"spd":3})
    if not isinstance(result,dict):
        writeFile("back.mp3",result)
    playVoice("back.mp3")

text=pp.get_pinyin(record())
temHigh=temHigh[0:-1]
temLow=temLow[0:-1]
tem1=("最高气温："+temHigh+"摄氏度\n最低气温："+temLow+"摄氏度")
#print(tem1)
if pp.get_pinyin("天气") in text:
    getBaiduVoice(tem1) 
    print('最高温度:' + temHigh)
    print('最低温度:' + temLow)
    print('天气:' + weather)
    for i in range(int(temHigh)):
        mc.setBlock(x+2,y+i,z,block.GOLD_BLOCK.id)
    for i in range(int(temLow)):
        mc.setBlock(x+2,y+i,z+2,block.DIAMOND_BLOCK.id)