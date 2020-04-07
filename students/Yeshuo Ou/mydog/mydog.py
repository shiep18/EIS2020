import pyaudio
import wave
from aip import AipSpeech
from xpinyin import Pinyin
import paho.mqtt.client as mqtt
import requests
from weather import *
from nature import *
from music import *
import mcpi.minecraft as minecraft
import mcpi.block as block
from pykeyboard import PyKeyboard
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


APP_ID = '19166551'
API_KEY = 'hBCgzHQN7EI9OXAepXrkx7e1'
SECRET_KEY = 'tv9Xrsnp6eO5N7pifDmv6FFy01McQx5B'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

STATE = 0
TIME_START = 0
TIME_END = 0

num = 0

mc = minecraft.Minecraft.create()  
k = PyKeyboard()

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
    mc.postToChat("Start Record......")

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
    mc.postToChat("Analysising......")
    result = client.asr(readFile('audio.wav'), 'wav', 16000, {
    'dev_pid': 1537,
})
    if result["err_no"] == 0:
        for t in result["result"]:
            return t
    else:
        print("没有识别到语音\n")
        mc.postToChat("Did't find the sound")
        return ""


def getBaiduVoice(text):
    result  = client.synthesis(text, 'zh', 6, {'vol': 5, 'per':4,'spd':5})
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
            # getBaiduVoice(getWeatherInfo(getCity(result)))
            temp = getWeatherInfo(get_address(get_url(),result))
            print(temp[0])
            mc.postToChat(rep(getPinYin(temp[1]))+"'s temporary:"+temp[2]+"C")
            pos = mc.player.getTilePos()
            for i in range(eval(temp[2])):
                mc.setBlock(pos.x+20,pos.y+i,pos.z,1)



        elif getPinYin("听") in pinyin:
            # downMusic(getMusicName(result))
            downMusic(getMusicName(result))
        elif getPinYin("首") in pinyin:
            downMusic(getMusicName(result))

        elif getPinYin("前") in pinyin:
            mc.postToChat('Forward')
            k.press_key('W')
            time.sleep(2)
            k.release_key('W')      

        elif getPinYin("后") in pinyin:
            mc.postToChat('Back')
            k.press_key('S')
            time.sleep(2)
            k.release_key('S')          

        elif getPinYin("左") in pinyin:
            mc.postToChat('Left')
            k.press_key('A')
            time.sleep(2)
            k.release_key('A')          

        elif getPinYin("右") in pinyin:
            mc.postToChat('Right')
            k.press_key('D')
            time.sleep(2)
            k.release_key('D')          
        
        else:
            print("我在")
    

def main():
    onMqttConnect()
    while True:
        result = getBaiduText()
        pinyin = getPinYin(result)
        print("等待唤醒")
        mc.postToChat("Waiting for calling")
        print(result)
        mc.postToChat(rep(pinyin))
        wakeUp(result,pinyin)
            

            
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        os.system("del back.mp3")
        os.system("del audio.wav")
        os.system("rmdir /s/q __pycache__")
