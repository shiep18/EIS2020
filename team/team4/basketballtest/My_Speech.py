import pyaudio
import wave
from aip import AipSpeech
from xpinyin import Pinyin
import requests
import os
from os import system
import win32com.client
import user
speaker = win32com.client.Dispatch("SAPI.SpVoice")


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 8000
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "audio.wav"


APP_ID = '19165156'
API_KEY = 'WtdBurU6FFaQ1ZDfIqoxwm5l'
SECRET_KEY = '13k6LOB86dLS7QWsIIkSsYLYoIr3EhT9'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

STATE = 0
TIME_START = 0
TIME_END = 0
global num,lastnum

    



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
    #print("***录音中......")
    print("请说出你的要求？")
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






def getPinYin(result):
    pin = Pinyin()
    return pin.get_pinyin(result)


def wakeUp(result,pinyin):
    global num,lastnum
    if (getPinYin("几个") in pinyin or getPinYin("多少") in pinyin) and getPinYin("球") in pinyin:

        print("现在有"+str(num)+"个球")
        speaker.Speak("现在有"+str(num)+"个球")
    elif getPinYin("篮球") in pinyin:
        num=user.make()
        if num>10000:
            num=num-10000
            speaker.Speak("库存不足，现在还有"+str(num)+"个球")
        elif num-lastnum>0:
            speaker.Speak("谢谢使用，欢迎下次再来")
        elif num-lastnum<0:
            speaker.Speak("你好,这是你的篮球")    
        lastnum=num     
    elif getPinYin("你好") in pinyin:
        speaker.Speak("我在")

def main():
    global num,lastnum
    num=user.getnumber()
    lastnum=num
    while True:
        result = getBaiduText()
        pinyin = getPinYin(result)
        print(result)
        wakeUp(result,pinyin)
            

            
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        speaker.Speak("欢迎再次使用")
main()   

