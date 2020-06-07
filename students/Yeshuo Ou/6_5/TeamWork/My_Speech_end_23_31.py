
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

num_basketball = 10

def str_num(str_num):
    # 传入中文数字
    #str_num = "二十一"
    # 一、定义转换字典
    num_dict = {"一": "1","两":"2","二": "2", "三": "3", "四": "4", "五": "5", "六": "6", "七": "7", "八": "8", "九": "9","十":"10"}
    # 将中文的数字替换成阿拉伯数字
    # 针对不同的情况进行判断和字典的更改
    if str_num[0] == "十" and len(str_num) > 1:
        num_dict["十"] = "1"
    if str_num[0] == "十" and len(str_num) == 1:
        num_dict["十"] = "10"
    if str_num[1] == "十" and len(str_num) == 2:
        num_dict["十"] = "0"
        
    num = ""
    # 遍历字典并对中文数字进行替换
    for str in str_num:
        for key in num_dict:
            if key == str:
                num += num_dict[key]
                break
    return num

    
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
    
    print("您好！现在有"+str(num_basketball)+"个篮球，有什么能帮助您的吗？")
    speaker.Speak("您好！现在有"+str(num_basketball)+"个篮球,有什么能帮助您的吗？")
    
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
    os.system("back.mp3")
    #playVoice("back.mp3")


def getVoiceResult():
    return baiduVoice()

def getPinYin(result):
    pin = Pinyin()

    return pin.get_pinyin(result)


def wakeUp(result,pinyin):
    global num_basketball
    global num_basketball_else
    if (getPinYin("几个") in pinyin or getPinYin("多少") in pinyin or getPinYin("的数量")in pinyin ) and getPinYin("球") in pinyin :
        print("现在有"+str(num_basketball)+"个篮球，您需要什么？")
        speaker.Speak("现在有"+str(num_basketball)+"个篮球，您需要什么？")
    elif (getPinYin("需要")in pinyin or getPinYin("想要")in pinyin or getPinYin("要")in pinyin or getPinYin("借")in pinyin )and getPinYin("个篮球") in pinyin:
        if 0 < num_basketball <= 10:
            num_basketball_else = str_num(result)
            num_basketball = int(num_basketball) - int(num_basketball_else)
            print("你好,这是你的"+str(num_basketball_else)+"个篮球")
            speaker.Speak("你好,这是你的"+str(num_basketball_else)+"个篮球")
            
        else:
            print("数量太大，无法操作，请您重新选择")
            speaker.Speak("数量太大，无法操作，请您重新选择")
    elif getPinYin("不用") in pinyin or getPinYin("谢谢") in pinyin or getPinYin("不需要") in pinyin :
        print("谢谢你的使用，感谢下次光临！")
        speaker.Speak("谢谢你的使用，感谢下次光临！")
        os._exit(0)
    else:
        print("无法识别，请重新操作")
        speaker.Speak("无法识别，请重新操作")
        

def main():

    while True:
        result = getBaiduText()
        pinyin = getPinYin(result)
        #print("请说出你借什么球类？")
        print(result)
        wakeUp(result,pinyin)
            

            
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        os.system("del back.mp3")
        os.system("del audio.wav")
        os.system("rmdir /s/q __pycache__")
#main()   

