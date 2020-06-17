import os
from hyperlpr import *
from aip import AipOcr
import cv2
import time
import pyaudio
import wave
from aip import AipSpeech
from xpinyin import Pinyin
import requests
from os import system
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

#军旗 司令 军长
#师长 旅长 团长 营长 炸弹
#连长 排长 工兵 地雷

APP_ID = '20359943'
API_KEY = 'qnLBpWaNcl8mEORZRRCcKzZ2'
SECRET_KEY = 'BoKRYbe64dAVFTPWxMz7YOl4F7G8jtL2'
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
cap = cv2.VideoCapture(0)
aaa=2
temp=0
temp1=0
w1=''
w=''
b=0

filePath = "test.png"
#filePath = "all.png"

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


options = {
    'detect_direction': 'true',
    'language_type': 'CHN_ENG',
}
print("请输入要分辨多少颗棋子")
speaker.Speak("请输入要分辨多少颗棋子")
aaa=int(input(":"))
while True:
    if b==2:
        break
    if b==1:
        print("请输入要分辨多少颗棋子")
        speaker.Speak("请输入要分辨多少颗棋子")
        aaa=input(":")
        aaa=int(aaa)
    b=0
    if temp<20:
        ret, frame = cap.read()
        cv2.imshow('Video', frame)
        cv2.imwrite('test.png',frame)
        result = aipOcr.basicGeneral(get_file_content(filePath), options)
        words_result=result['words_result']
        #print(words_result)
        temp+=1
        for i in range(len(words_result)):
            #print(words_result[i]['words'])
            if len(words_result)==aaa:
                if (words_result[i]['words'] == "军旗" or words_result[i]['words'] == "司令"
                    or words_result[i]['words'] == "军长" or words_result[i]['words'] == "师长"
                    or words_result[i]['words'] == "旅长" or words_result[i]['words'] == "团长"
                    or words_result[i]['words'] == "营长" or words_result[i]['words'] == "炸弹"
                    or words_result[i]['words'] == "连长" or words_result[i]['words'] == "排长"
                    or words_result[i]['words'] == "工兵" or words_result[i]['words'] == "地雷"):
                    print("第"+str(i+1)+"个棋子为"+words_result[i]['words'])
                    temp1+=1
        if temp1==aaa:
            for i in range(0,aaa):
                w+=("第"+str(i+1)+"个棋子为"+words_result[i]['words']+"\n")
            speaker.Speak(w)
            w=""
            temp=0
            print("继续识别输入1,退出输入2")
            speaker.Speak("继续识别输入1,退出输入2")
            while b==0:
                b=int(input(":"))
                if b==2:
                    break
                elif b==1:
                    break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        temp1=0
        
        if b==0:
            print(str(temp)+"秒")
        else:
            temp=0
        #print('\n')
    else:
        print("没有识别到相应数量的棋子，请重新输入要分辨多少颗棋子")
        speaker.Speak("没有识别到相应数量的棋子，请重新输入要分辨多少颗棋子")
        aaa=input(":")
        aaa=int(aaa)
        temp=0
    w1=""
cap.release()

cv2.destroyAllWindows()

