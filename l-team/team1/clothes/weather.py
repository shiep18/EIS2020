import urllib.request
import gzip
import json
import time
import cv2
import speech_recognition as sr
import logging
from aip import AipSpeech
import win32com.client


BAIDU_APP_ID = '19455583'
BAIDU_API_KEY = '1GpE2BPDV8MgpgA00s1SvrmH'
BAIDU_SECRET_KEY = 'VUIOGVAXBQ3cucuVsIW049TnAvEQA3jq'
aip_speech = AipSpeech(BAIDU_APP_ID, BAIDU_API_KEY, BAIDU_SECRET_KEY)
r = sr.Recognizer()
mic = sr.Microphone(sample_rate=16000)

speaker = win32com.client.Dispatch("SAPI.SpVoice")

img=cv2.imread('clo1.jpg')
img1=cv2.imread('clo2.jpg')
#判断是否满意
def user_content():
    speaker.Speak("这是为您选择的衣服，请问是否满意")
    print('>>>>>>录音中...')
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    print('>>>>>>识别中...')
 
    start_time = time.time()
    audio_data = audio.get_wav_data()
    ret = aip_speech.asr(audio_data, 'wav', 16000, {'dev_pid': 1537, })
    if ret and ret['err_no'] == 0:
        result = ret['result'][0]
        print(result)
        if "不满意" in result:
            print("好吧sorry")
            speaker.Speak("重新为您推荐")
            show2()
            user_content()#重新推荐
        elif "满意" in result:
            
            print("感谢认可，欢迎下次使用")
            speaker.Speak("感谢认可，欢迎下次使用")
        else:#回答未被识别重新问
            speaker.Speak("对不起 我没有听懂您的意思")
            speaker.Speak("请您重新回答")
            user_content()#重新推荐
    else:
        print(" ")

#温度热的穿搭
def weather_hot():
    print("为您选择的衣服")
    #cv2.namedWindow('input_image', cv2.WINDOW_AUTOSIZE)
    show1()
    print("请回答满意or不满意")
    user_content()

#第一套

def show1():
    cv2.namedWindow('Recommendation 1')
    cv2.moveWindow('Recommendation 1',1,50)
    cv2.imshow('Recommendation 1', img)
    key = cv2.waitKey(10)
#第二套
def show2():
    cv2.namedWindow('Recommendation 2')
    cv2.moveWindow('Recommendation 2', 200, 50)
    cv2.imshow('Recommendation 2',img1)
    cv2.waitKey(10)
        
cv2.destroyAllWindows()

#天气冷的穿搭
def weather_cold():
    print("为您选择的衣服")
    print("请回答满意or不满意")
    user_content()

#爬取天气
def all_weather():
    print('------智能搭配系统------')
    def get_weather_data() :
        speaker.Speak("欢迎来到搭配系统")
        speaker.Speak("请输入所在或即将前往城市的名称")
        city_name = input('请输入城市名称：')
        
        url1 = 'http://wthrcdn.etouch.cn/weather_mini?city='+urllib.parse.quote(city_name)
        #需要输入城市名 urllib.parse解析成各个组件
        weather_data = urllib.request.urlopen(url1).read()
        #读取网页数据 这里读取的数据是经过gzip压缩的
        weather_data = gzip.decompress(weather_data).decode('utf-8')
        #解压网页数据
        weather_dict = json.loads(weather_data)
        #将json数据转换为dict数据
        return weather_dict

    def show_weather(weather_data):
        weather_dict = weather_data
        #将json数据转换为dict数据
        if weather_dict.get('desc') == 'invilad-citykey':
            print('你输入的城市名有误，或者天气中心未收录你所在城市')
        elif weather_dict.get('desc') =='OK':
            forecast = weather_dict.get('data').get('forecast')
            print('城市:',weather_dict.get('data').get('city'))
            print('日期:',forecast[0].get('date'))
            print('当前温度:',weather_dict.get('data').get('wendu')+"℃")
            
            print(forecast[0].get('high'))
            print(forecast[0].get('low'))
            print('天气:',forecast[0].get('type'))
            speaker.Speak("今天是"+forecast[0].get('date'))
            speaker.Speak("当前温度是"+weather_dict.get('data').get('wendu')+"℃")
            speaker.Speak(forecast[0].get('low')+forecast[0].get('high')+"天气"+forecast[0].get('type'))
            temp = int(weather_dict.get('data').get('wendu'))

            #gewei = temp%10
            #shiwei = temp//10

            print('温馨提示：',weather_dict.get('data').get('ganmao'))
            speaker.Speak("温馨提示"+weather_dict.get('data').get('ganmao'))


            #判读温度
            if temp>20:
                
                speaker.Speak("今天很热")
                weather_hot()
            else:
                speaker.Speak("天气较凉爽")
                weather_cold()
                
            print('*******************************')
    show_weather(get_weather_data())



