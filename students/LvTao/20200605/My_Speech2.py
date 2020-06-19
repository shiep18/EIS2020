
import pyaudio
import wave
from aip import AipSpeech
from xpinyin import Pinyin
import requests
#from weather import *
#from nature import *
#from music import *
import os
from os import system
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 8000
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "audio.wav"


APP_ID = '18980660'
API_KEY = 'hwoVnCcUV1VoizMZzHU7ayu6'
SECRET_KEY = 'Z1ynGkPNF1GBoYnnMPBdxt4lY8mm48QS'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

STATE = 0
TIME_START = 0
TIME_END = 0

num = 0
balls = 20    

def playVoice(fileName):
    os.system("madplay -v " + fileName)
 

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

    speaker.Speak("请说出你想要租赁的球类？")
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
    
    print("正在识别......")
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
    if not isinstance(result, dict):
        writeFile("back.mp3",result)
    playVoice("back.mp3")


def getVoiceResult():
    return baiduVoice()

def getPinYin(result):
    pin = Pinyin()
    return pin.get_pinyin(result)


def wakeUp(result,pinyin):

    if getPinYin("几个") in pinyin or getPinYin("多少") in pinyin:
        speaker.Speak("现在有"+str(balls)+"个球")
        print("现在有"+str(balls)+"个球")
    elif getPinYin("篮球") in pinyin:
        print("你好,这是你的篮球")
        #getBaiduVoice("你好,这是你的篮球")
        speaker.Speak("你好,这是你的篮球")
    elif getPinYin("足球") in pinyin:
        print("你好,这是你的足球")
        speaker.Speak("你好,这是你的足球")
    elif getPinYin("排球") in pinyin:
        print("你好,这是你的排球")
        speaker.Speak("你好,这是你的排球")
    else:
        print("我在")
        speaker.Speak("我在")
        #playVoice("im.mp3")

def main():
    result = getBaiduText()
    pinyin = getPinYin(result)
    print(result)
    wakeUp(result,pinyin)
            

            
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        os.system("del back.mp3")
        os.system("del audio.wav")
        os.system("rmdir /s/q __pycache__")
   

