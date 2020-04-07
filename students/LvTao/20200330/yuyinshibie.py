import pyaudio
import wave
from aip import AipSpeech
from xpinyin import Pinyin
import paho.mqtt.client as mqtt
import requests
from weather import *
from nature import *
from music import *
from move import *
import time 
 
MQTTHOST = "47.101.154.50"
MQTTPORT = 1883
mqttClient = mqtt.Client()


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "audio.wav"


APP_ID = '19165941'
API_KEY = 'XUqFyxlgEllBGh5qqRMfTh4x'
SECRET_KEY = 'S6GPVANUOEH4NFYxyfkd9f3lQPXfkx3N'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

STATE = 0
TIME_START = 0
TIME_END = 0

num = 0
    
def rep(a):
    for i in '，。；！？':
        a=a.replace(i,'')
    return a

def onMqttConnect():
    mqttClient.connect(MQTTHOST, MQTTPORT, 60)
    mqttClient.loop_start()
 
def onPublish(topic, payload, qos):
    mqttClient.publish(topic, payload, qos)

def readFile(fileName):
    with open(fileName, 'rb') as fp:
        return fp.read()
    
def writeFile(fileName,result):
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
    result  = client.synthesis(text, 'zh', 6, {'vol': 5, 'per':4,'spd':5})
    print("this")
    if not isinstance(result, dict):
        writeFile("back.mp3",result)
    playVoice("back.mp3")


def getVoiceResult():
    return baiduVoice()

def getPinYin(result):
    pin = Pinyin()
    return pin.get_pinyin(result)


def wakeUp(result,pinyin):
    if getPinYin("狗") in pinyin:
        if getPinYin("你好") in pinyin:
            print("你好")
            getBaiduVoice("你好")
        
        
        elif getPinYin("开灯") in pinyin:
            onPublish("chat", "1", 1)
            print("灯已打开")
            getBaiduVoice("灯已打开")
        elif getPinYin("关灯") in pinyin:
            onPublish("chat", "5", 1)
            print("灯已关闭")
            getBaiduVoice("灯已关闭")

            
        elif getPinYin("天气") in pinyin:
            getBaiduVoice(getWeatherInfo(getCity(result)))
            temp = getWeatherInfo(get_address(get_url(),result))
            print(temp[0])
            mc.postToChat(rep(getPinYin(temp[1]))+"'s temperature is:"+temp[2]+"C")
            pos = mc.player.getTilePos()
            mc.setBlocks(pos.x-2,pos.y,pos.z+8,pos.x+2,pos.y+30,pos.z+12,0)
            for i in range(eval(temp[2])):
                mc.setBlock(pos.x,pos.y+i,pos.z+10,86)

        elif getPinYin("听") in pinyin:
            downMusic(getMusicName(result))
        elif getPinYin("首") in pinyin:
            downMusic(getMusicName(result))
        elif getPinYin("向左走。") in pinyin:
            move("left")
            print("done")
        elif getPinYin("向右走。") in pinyin:
            move("right")
        elif getPinYin("向前走。") in pinyin:
            move("front")
        elif getPinYin("向后走。") in pinyin:
            move("back")
        elif getPinYin("向上。") in pinyin:
            move("up")
        elif getPinYin("向下。") in pinyin:
            move("down") 
        else:
            print("我在")
            playVoice("im.mp3")
    

def main():
    onMqttConnect()
    while True:
        result = getBaiduText()
        pinyin = getPinYin(result)
        print(pinyin)
        print("等待唤醒")
        print(result)
        wakeUp(result,pinyin)
            

            
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        #print("error")
        os.system("del back.mp3")
        os.system("del audio.wav")
        os.system("rmdir /s/q __pycache__")
