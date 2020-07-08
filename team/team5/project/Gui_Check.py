import sys
import re
import tkinter as tk
import tkinter.messagebox
import numpy as np
import urllib
import pickle
import pymysql
import cv2
import random
import requests
import threading
import json
import re
import datetime
import os
import webbrowser
import win32com.client
import zxing
import time
import vtk
import pyaudio
import wave
import win32com.client
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation
import pandas as pd
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from hyperlpr import *
from aip import AipSpeech
from xpinyin import Pinyin

from os import system
from bs4 import BeautifulSoup
from pyecharts import GeoLines, Style    #地理轨迹图的类就是Geolines
from urllib.parse import unquote
from httputils import gehtml
from pycharts_utils import getmaps
from IPython.display import HTML
from os import system
from threading import Thread
from selenium import webdriver
from moocxing import MOOCXING
from robot.Brain import Brain
from PIL import ImageGrab,Image,ImageTk
data2 = pd.read_excel('全国身份证号对应省市区.xls', header=None, names=['身份证前六位', '所属地区'])
speaker = win32com.client.Dispatch("SAPI.SpVoice")
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 8000
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "audio1.wav"
fg=0
mx = MOOCXING()
lock=0
flag3=2
ptt=0
s=100
be=100
m=5
r=0
ooo=-1
oo=1
flagg=1
actors=[]
f = 1 
# 初始化串口
#serial = mx.initSerial(mx.getComPorts(-1),9600)
# 初始化播放器和录音
media = mx.initMedia()

# 初始化语音识别+语音合成
APP_ID = '16901888'
API_KEY = 'qUcr9z2IVvREkyjDtlfbhsuv'
SECRET_KEY = 'preDe7g0C4ubTQ9XOir1afybwhD3jnAn'
speech = mx.initSpeech(APP_ID, API_KEY, SECRET_KEY)
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 初始化NLP
APP_ID = '19745053'
API_KEY = 'UnBq5gNtiZnReCKts31GiPlS'
SECRET_KEY = 'Ip2YLBAkGgbCp4xSv7TXjXojihipjFku'
nlp = mx.initNLP(APP_ID, API_KEY, SECRET_KEY)

# 初始化MQTT
MQTTHOST = "mqtt.16302.com"
MQTTPORT = 1883
mqtt = mx.initMqtt(MQTTHOST, MQTTPORT)

# 初始化我的世界
mc = mx.initMinecraft("47.100.46.95", 4785)
entityId = mc.getPlayerEntityId("zhuzhe")
print("********初始化完成********\n")

# 技能插件
SKILL = {"media": media, "speech": speech, "nlp": nlp}
brain = Brain(SKILL)
print("********技能插件加载完成********\n")

def control1():
    class Window(QWidget):
    
        def __init__(self, parent=None):
            super().__init__(parent)
            self.setWindowTitle("疫情期间通行身份校验系统")
            self.layout = QGridLayout()
            self.setLayout(self.layout)  # 局部布局

            self.titleText = QTextBrowser()
            self.titleText.setText('疫情期间通行身份校验系统')
            self.titleText.setStyleSheet(
                "font-size:24px;font-weight:700;background-color: rgba(255,255,255,180);border: none;color:#0000CD")
             #   "font-size:24px;font-weight:700;background:white;background-color: rgba(255,255,255,255);border: none;color:#0000CD")
            self.titleText.setAlignment(Qt.AlignCenter)
            self.titleText.setFixedSize(500, 40)
            self.layout.addWidget(self.titleText, 0, 0, 1, 3 , Qt.AlignRight)
            self.Text = QTextBrowser()
            self.Text.setText('请输入身份证号码：')
            self.Text.setAlignment(Qt.AlignRight)
            self.Text.setStyleSheet(
                "font-size:18px;font-weight:700;background-color: rgba(255,255,255,180);border: none;color:#0000CD")
            self.Text.setFixedSize(180, 30)
            self.layout.addWidget(self.Text, 1, 0, Qt.AlignRight)

            self.idcardText = QLineEdit(self)
            self.idcardText.setFixedSize(210, 30)
            self.idcardText.setStyleSheet("font-size:16px;font-weight:500;background-color: rgba(255,255,255,180);border: none;color:#55007f")
            self.layout.addWidget(self.idcardText, 1, 1, Qt.AlignLeft)

            self.Text = QTextBrowser()
            self.Text.setText('查询结果：')
            self.Text.setAlignment(Qt.AlignRight)
            self.Text.setStyleSheet(
                "font-size:18px;font-weight:700;background-color: rgba(255,255,255,180);border: none;color:#0000CD")
            self.Text.setFixedSize(105, 30)
            self.layout.addWidget(self.Text, 2, 0, Qt.AlignRight)

            self.resultText = QLineEdit(self)
            self.resultText.setFixedSize(210, 25)
            self.resultText.setStyleSheet(
                "font-size:16px;font-weight:500;background-color: rgba(255,255,255,180);border: none;color:#55007f")
            self.layout.addWidget(self.resultText, 2, 1, Qt.AlignLeft)

            self.Text = QTextBrowser()
            self.Text.setText('性别：')
            self.Text.setAlignment(Qt.AlignRight)
            self.Text.setStyleSheet(
                "font-size:18px;font-weight:700;background-color: rgba(255,255,255,180);border: none;color:#0000CD")
            self.Text.setFixedSize(65, 30)
            self.layout.addWidget(self.Text, 3, 0, Qt.AlignRight)

            self.genderText = QLineEdit(self)
            self.genderText.setFixedSize(210, 25)
            self.genderText.setStyleSheet(
                "font-size:16px;font-weight:500;background-color: rgba(255,255,255,180);border: none;color:#55007f")
            self.layout.addWidget(self.genderText, 3, 1, Qt.AlignLeft)

            self.Text = QTextBrowser()
            self.Text.setText('年龄：')
            self.Text.setAlignment(Qt.AlignRight)
            self.Text.setStyleSheet(
                "font-size:18px;font-weight:700;background-color: rgba(255,255,255,180);border: none;color:#0000CD")
            self.Text.setFixedSize(65, 30)
            self.layout.addWidget(self.Text, 4, 0, Qt.AlignRight)

            self.ageText = QLineEdit(self)
            self.ageText.setFixedSize(210, 25)
            self.ageText.setStyleSheet(
                "font-size:16px;font-weight:500;background-color: rgba(255,255,255,180);border: none;color:#55007f")
            self.layout.addWidget(self.ageText, 4, 1, Qt.AlignLeft)

            self.Text = QTextBrowser()
            self.Text.setText('发证地：')
            self.Text.setAlignment(Qt.AlignRight)
            self.Text.setStyleSheet(
                "font-size:18px;font-weight:700;background-color: rgba(255,255,255,180);border: none;color:#0000CD")
            self.Text.setFixedSize(85, 30)
            self.layout.addWidget(self.Text, 5, 0, Qt.AlignRight)

            self.addressText = QLineEdit(self)
            self.addressText.setFixedSize(210, 25)
            self.addressText.setStyleSheet(
                "font-size:16px;font-weight:500;background-color: rgba(255,255,255,180);border: none;color:#55007f")
            self.layout.addWidget(self.addressText, 5, 1, Qt.AlignLeft)

            self.startPushButton = QPushButton("开始查询")
            #self.startPushButton.setStyleSheet("background-color: red");
            self.startPushButton.setFixedSize(200, 50)
            self.startPushButton.clicked.connect(self.check)
            self.layout.addWidget(self.startPushButton, 1, 2, 2, 2, Qt.AlignRight)
            
            self.startPushButton1 = QPushButton("查看路线")
            #self.startPushButton1.setStyleSheet("background-color: green");
            self.startPushButton1.setFixedSize(200, 50)
            
            self.startPushButton1.clicked.connect(self.route)
            self.layout.addWidget(self.startPushButton1, 2, 2, 2, 2, Qt.AlignRight)

            self.startPushButton1 = QPushButton("国内数据")
            #self.startPushButton1.setStyleSheet("background-color: yellow");
            self.startPushButton1.setFixedSize(200, 50)
            self.startPushButton1.clicked.connect(self.ly)
            self.layout.addWidget(self.startPushButton1, 3, 2, 2, 2, Qt.AlignRight)

            self.startPushButton1 = QPushButton("海外数据")
            #self.startPushButton1.setStyleSheet("background-color: pink");
            self.startPushButton1.setFixedSize(200, 50)
            self.startPushButton1.clicked.connect(self.dongtai)
            self.layout.addWidget(self.startPushButton1, 4, 2, 2, 2, Qt.AlignRight)
            

            
       
        def check(self):
            global data2
            idcard = self.idcardText.text()
            verification = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
            sum = 0
            for i, j in zip(list(idcard)[0:18], verification):
                sum += int(i) * j
            final_dic = {0: 1, 1: 0, 2: 'X', 3: 9, 4: 8, 5: 7, 6: 6, 7: 5, 8: 4, 9: 3, 10: 2}
            if str(final_dic[sum % 11]) == str(idcard[17]):
                self.resultText.setText('Successfull')
                speaker.Speak("查询成功")
            else:
                self.resultText.setText('fail ')
                speaker.Speak("抱歉，您输入的身份证号码有误请从新输入")
    ##            os._exit(0)
                app = QApplication(sys.argv)
                show = Window()  #主窗口的类
                palette = QPalette()
                palette.setBrush(QPalette.Background, QBrush(QPixmap("a.jpg")))
                show.setFixedSize(700,434 )
                
                show.setPalette(palette)
                show.show()
                sys.exit(app.exec_())
                
            gender_id = {'0': '女', '1': '男'}
                
            gender = gender_id[str(int(idcard[16]) % 2)]
            age = int(datetime.datetime.now().year) - int(idcard[6:10])
            global address
            address = data2[data2['身份证前六位'].eq(idcard[:6])]['所属地区']

            self.genderText.setText(gender)
            speaker.Speak("欢迎您来自"+address.values[0]+"的"+gender+"士"+",请确认您的身份证后四位为"+idcard[14]+"杠"+idcard[15]+"杠"+idcard[16]+"杠"+idcard[17]+",语音播报完毕后查询结果会显示在屏幕上")
            self.ageText.setText(str(age))
            self.addressText.setText(str(address.values[0]))
            #print(address.values[0])
            speaker.Speak("更多功能请点击相应按钮")

        def closeEvent(self, event):
            reply = QMessageBox.question(self, 'Message',
                                         "Are you sure to quit?", QMessageBox.Yes |
                                         QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()

        def route(self):
            speaker.Speak("即将进入路线查询板块请稍等"+"即将为您查询路线信息")
            url0 = "https://www.fastmock.site/mock/62e89c64391d93ce581798b816d8edec/smartbuild/base/python"
            
            res0 = requests.get(url0)
            city0 = res0
            city00=city0.text[20:30]
            rciry0=re.sub('\W', '', city00,)
            #rcity2="保定市"
            #print(address.values[0][0:5])
            print('此人在疫情期间途径以下五个城市:')
            
            print(rciry0)
            #print(rcity2)
            
            speaker.Speak(city0.text)
             
            url1 = "https://www.fastmock.site/mock/62e89c64391d93ce581798b816d8edec/smartbuild/base/python1"
            
            res1 = requests.get(url1)
            city1 = res1
            city11=city1.text[6:20]
            rciry1=re.sub('\W', '', city11,)
            #rcity2="保定市"
            #print(address.values[0][0:5])
            print(rciry1)
            #print(rcity2)
            
            speaker.Speak(city1.text)

            url2 = "https://www.fastmock.site/mock/62e89c64391d93ce581798b816d8edec/smartbuild/base/python2"
            
            res2 = requests.get(url2)
            city2 = res2
            city22=city2.text[6:20]
            rciry2=re.sub('\W', '', city22,)
            #rcity2="保定市"
            #print(address.values[0][0:5])
            print(rciry2)
            #print(rcity2)
            
            speaker.Speak(city2.text)

            url3 = "https://www.fastmock.site/mock/62e89c64391d93ce581798b816d8edec/smartbuild/base/python3"
            
            res3 = requests.get(url3)
            city3 = res3
            city33=city3.text[6:20]
            rciry3=re.sub('\W', '', city33,)
            #rcity2="保定市"
            #print(address.values[0][0:5])
            print(rciry3)
            #print(rcity2)
            
            speaker.Speak(city3.text)

            url4 = "https://www.fastmock.site/mock/62e89c64391d93ce581798b816d8edec/smartbuild/base/python4"
            
            res4 = requests.get(url4)
            city4 = res4
            city44=city4.text[7:20]
            rciry4=re.sub('\W', '', city44,)
            #rcity2="保定市"
            #print(address.values[0][0:5])
            print(rciry4)
            #print(rcity2)
            
            speaker.Speak(city4.text)


            number = []
            for i in range(0,100):
                num = random.randint(0,100)
                number.append(num)
            if number[5] > 90:
                speaker.Speak('查询结束，正在生成可视化动态路线图')
                speaker.Speak('即将自动打开动态路线图，请稍候')
            else:
                speaker.Speak('查询结束，正在生成可视化动态路线图')
                speaker.Speak('抱歉，因查询人数较多系统繁忙')
                if number[5] > 50:
                    speaker.Speak('等待期间，给你讲个笑话吧。叔叔问外甥：小猪几条腿？答：四条腿。问：跑起来呢？答：那乱七八糟的我哪数的清。')
                else:    
                    speaker.Speak('等待期间，给你来段吴亦凡的rap吧， 碍，碍，碍，泥砍着歌晚，塌，油打，油院。泥刊着歌棉、塌，油场、油款。尼闷，莱着理，池反。嚼的犯，恨浩痴。哎，卧砍姓。逆闷，莱着理，池反。就、像、卧给逆闷、腊、棉、姨、羊恨开信，哎！')
                speaker.Speak('查询结束，正在生成可视化动态路线图')
                speaker.Speak('即将自动打开动态路线图，请稍候')
                
            
            idcard = self.idcardText.text()
            data1 = pd.read_excel('1.xlsx', header=None, names=['city', 'lad', 'long'])
            city = list(data1['city'])
            lad_list = list(data1['lad'])
            long_list = list(data1['long'])
            result = pd.DataFrame({'地点': city, '经度': lad_list, '纬度': long_list})

            geo_cities_coords = {result.iloc[i]['地点']: [result.iloc[i]['经度'], result.iloc[i]['纬度']]
                                 for i in range(len(result))}
            # 设置画布的格式
            style = Style(title_pos="center",
                          width=1000,
                          height=800)

            # 部分地理轨迹图的格式
            style_geolines = style.add(is_label_show=True,#标签的有无
                                       line_curve=0.3,  # 轨迹线的弯曲度，0-1
                                       line_opacity=0.6,  # 轨迹线的透明度，0-1
                                       geo_effect_symbol='plane',  # 特效的图形，有circle,plane,pin等等
                                       geo_effect_symbolsize=10,  # 特效图形的大小
                                       geo_effect_color='#7FFFD4',  # 特效的颜色
                                       geo_effect_traillength=0.1,  # 特效图形的拖尾效果，0-1
                                       label_color=['#FFA500', '#FFF68F'],  # 轨迹线的颜色，标签点的颜色，
                                       border_color='#97FFFF',  # 边界的颜色
                                       geo_normal_color='#36648B',  # 地图的颜色
                                       label_formatter='{b}',  # 标签格式
                                       legend_pos='left')

            # 作图
            # !pip install echarts-countries-pypkg
            # !pip install echarts-china-provinces-pypkg
            # !pip install echarts-china-cities-pypkg
            # !pip install echarts-china-counties-pypkg
            # !pip install echarts-china-misc-pypkg

            geolines = GeoLines('身份证号码为', idcard,  **style.init_style)
            geolines.add(address.values[0],
                         [(rciry4, rciry1), (rciry1, rciry2), (rciry2, rciry3), (rciry3,rciry4)
                             , (rciry4, rciry0), (rciry0, '舟山'),],
                         maptype='china',
                         geo_cities_coords=geo_cities_coords,
                         **style_geolines)

            # 发布，得到图形的html文件
            geolines.render()
            webbrowser.open_new_tab('render.html')
        def ly(self):
            speaker.Speak("欢迎进入国内疫情数据可视化板块，正在联网获取实时数据。数据获取成功系统将自动为您弹出")
            url_code_name = "\u963f\u8054\u914b"
            text = unquote(url_code_name, 'utf-8')
            print(text)

            text = gehtml('https://voice.baidu.com/act/newpneumonia/newpneumonia')
            if text is not 'error':
                re_str = r'caseList(.*?),"dataSource'
                informations = re.findall(re_str, text, re.S | re.M)
                json_str = '{"caseList' + informations[0] + '}'
                json_str = json.loads(json_str)

                area = []
                confirmed = []
                died = []
                crued = []

                for detail in json_str["caseList"]:
                    area.append(unquote(detail["area"], 'utf-8'))
                    confirmed.append(int(detail["confirmed"]))
                    map = getmaps(area, confirmed)
                    map.render(path='china.html')
                    if detail["died"] is not "":
                        died.append(int(detail["died"]))
                    else:
                        died.append(0)
                    if detail["crued"] is not "":
                        crued.append(int(detail["crued"]))
                    else:
                        crued.append(0)
              
                plt.rcParams['font.sans-serif'] = ['SimHei']
                plt.rcParams['axes.unicode_minus'] = False

                plt.figure(figsize=(15, 15))
                plt.subplot(131)
                plt.barh(area, confirmed)
                plt.ylabel(u'地区')
                plt.xlabel(u'感染人数')
                plt.title('各省感染人数')
                for i in range(33):
                    plt.text(confirmed[i], area[i], confirmed[i])

                plt.subplot(132)
                plt.barh(area, died)
                plt.ylabel(u'地区')
                plt.xlabel(u'死亡人数')
                plt.title('各省死亡人数')
                for i in range(33):
                    if died[i] is not 0:
                        plt.text(died[i], area[i], died[i])

                plt.subplot(133)
                plt.barh(area, crued)
                plt.ylabel(u'地区')
                plt.xlabel(u'治愈人数')
                plt.title('各省治愈人数')
                for i in range(33):
                    if crued[i] is not 0:
                        plt.text(crued[i], area[i], crued[i])
                        
                webbrowser.open_new_tab('china.html')
                plt.show()
                        

        def dongtai(self):
            speaker.Speak("欢迎进入海外疫情数据可视化板块，正在联网获取实时数据。数据获取成功系统将自动为您弹出")
            plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
            df = pd.read_excel('1.xls', encoding='gbk', usecols=['country', 'date', 'confirm']) #cjm注释用pandas读取表格中的数据，设置图形窗口大小
            fig, ax = plt.subplots(figsize=(15, 8))
            def sortTime(list1):
                list2 = []
                for i in list1:
                    if i in list2:
                        pass
                    else:
                        list2.append(str(i))
                return list2
            def start(date):
    ##            date = '2020年3月20日'
                dff = df[df['date'].eq(date)].sort_values(by='confirm', ascending=False).head(10)#cjm注释
    ##            dff = dff[::-1]    #反转数据
                ax.clear()
                colors = ['#abd0ff', '#ffb3ff', '#90d595', '#e48381', '#aafbff', '#f7bb5f', '#eafb50', '#00BFFF', '#ADD8E6',
                          '#32CD32']
                ax.barh(dff['country'], dff['confirm'], color=[colors[i] for i in range(len(dff['country']))])
                dx = dff['confirm'].max()/200
                for i, (num, country) in enumerate(zip(dff['confirm'], dff['country'])):
                    print(num, country)
                    #ax.text(dx, i, country, size=15)
                    ax.text(num+dx, i, num, size=20, color='#444444')
                ax.set_title('海外疫情动态变化展示图', fontsize=30, color='y')
                ax.text(0.83, 1.05, date, transform=ax.transAxes, color='b', size=30)  #将时间戳放到右上角
                ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))  # 给x轴坐标数据科学计数
                ax.xaxis.set_ticks_position('top')  # 将x轴坐标放到上端
                ax.tick_params(axis='x', colors='#777777', labelsize=12)
                ax.margins(0, 0.01)  # 缩放坐标轴
                ax.grid(which='major', axis='x', linestyle='-')  # 画网格虚线
            animator = animation.FuncAnimation(fig, start, frames=sortTime(df['date']), interval=500)
            plt.show()
    class vtkTimerCallback1():
        def __init__(self):
            pass
                 
        def execute(self,obj,event):
            global ptt,s,be,renderer,renderWindowInteractor,actors,f,ooo
            #Vtk=vtkTimerCallback1()
            if ptt==3:
                if f == 1:
                    actors[0+ooo*3].RotateX(-50)
                    #actors[1+ooo*3].RotateX(-50)
                    f = -f
                    time.sleep(0.4)
                elif f == -1:
                    actors[0+ooo*3].RotateX(50)
                    #actors[1+ooo*3].RotateX(50)
                    f = -f
                    time.sleep(0.4)
            elif ptt==1:
                if f == 1:
                    actors[0+ooo*3].RotateX(-50)
                    actors[1+ooo*3].RotateX(-50)
                    f = -f
                    time.sleep(0.2)
                elif f == -1:
                    actors[0+ooo*3].RotateX(50)
                    actors[1+ooo*3].RotateX(50)
                    f = -f
                    time.sleep(0.2)
            elif ptt==2:
                if f == 1:
                    actors[0+ooo*3].RotateX(-50)
                    actors[1+ooo*3].RotateX(-50)
                    f = -f
                    time.sleep(0.1)
                elif f == -1:
                    actors[0+ooo*3].RotateX(50)
                    actors[1+ooo*3].RotateX(50)
                    f = -f
                    time.sleep(0.1)
            iren = obj
            if (flagg):
                renderWindow.Render()
            else:
                pass
                #renderWindowInteractor.GetRenderWindow().Finalize()
                #self.timer_count += 1
                #del renderer, renderWindowInteractor
                #self.timer_count += 1
                #print('1')
        def fun_timer(self):
            global ptt,s,m,flag3,flagg
            if (flagg):   
                #Vtk=vtkTimerCallback1()
                print('hello timer')   #打印输出
                global timer  #定义变量
                timer = threading.Timer(30,Vtk.fun_timer)   #60秒调用一次函数
                if ptt == 1:
                    Vtk.putong()
                    print('普通模式')
                elif ptt==2 :
                    Vtk.kuangpen()
                    print('疯狂模式')
                elif ptt == 3:
                    Vtk.jianyi()
                    print('简易模式')
                ##    s=s-3
                ##    be=be-1
                m=m-1
                
                print('消毒液余量：'+str(s))
                print('电量：'+str(be))
                print('剩余时间：'+str(m)+'min')
                if s == 5 :
                    speaker.Speak("系统自动检测到消毒液余量为百分之五，停止消毒")
                    flagg=0
                    if flag3==0:
                        print('你可以进入学校了。')
                    
                #   os._exit(0)
                if m == 0 and flag3!=1:
                    #flag3=0
                    flagg=0
                    speaker.Speak("消毒完成。")
                    if flag3==0:
                        print('你可以进入学校了。')    
                #定时器构造函数主要有2个参数，第一个参数为时间，第二个参数为函数名
                timer.start()    #启用定时器
                result = Vtk.getBaiduText()
                pinyin = Vtk.getPinYin(result)
                print(result)
                Vtk.wakeUp(result,pinyin)
            else:
                pass
        def jianyi(self):
            global s,be
            s=s-1
            be=be-0.5
        def  putong(self):
            global s,be
            s=s-3
            be=be-1

        def  kuangpen(self):
            global s,be
            s=s-5
            be=be-2 
          
        def playVoice(self,fileName):
            os.system("madplay -v " + fileName)
        

        def readFile(self,fileName):
            with open(fileName, 'rb') as fp:
                return fp.read()
           
        def writeFile(self,fileName,result):
            with open(fileName, 'wb') as fp:
                fp.write(result)
               
        def getBaiduText(self):
            global r
            Vtk=vtkTimerCallback1()
            p = pyaudio.PyAudio()

            stream = p.open(format=FORMAT,
                          channels=CHANNELS,
                          rate=RATE,
                          input=True,
                          frames_per_buffer=CHUNK)

            stream.start_stream()
            if r==0:
                speaker.Speak("开始消毒。")
                r=1
            else:
             #speaker.Speak("正在消毒，目前消毒液充足 ，请随时说出暂停将暂停消毒")
                r=1
            print("请随时说出停止将停止消毒")
            print("说出消毒液余量，将为您检查消毒液余量")
            print("说出电量余量，将为您检查电量液余量")
            print("说出机器人状态，将为您检查机器人状态参数")
            print("您也可以随时说出指令简易模式普通模式或狂喷模式改变消毒强度")
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
            result = client.asr(Vtk.readFile('audio1.wav'), 'wav', 16000, {
            'dev_pid': 1537,
            })
            if result["err_no"] == 0:
                for t in result["result"]:
                    return t
            else:
                print("没有识别到语音\n")
                return ""

        def getBaiduVoice(self,text):
            result  = client.synthesis(text, 'zh', 6, {'vol': 5, 'per':4,'spd':5})
            if not isinstance(result, dict):
                Vtk.writeFile("back.mp3",result)
            os.system("back.mp3")
            #playVoice("back.mp3")


        def getVoiceResult(self):
            return baiduVoice()

        def getPinYin(self,result):
            pin = Pinyin()
            return pin.get_pinyin(result)
        def wakeUp(self,result,pinyin):
            global ptt,s,be,m,renderWindowInteractor,renderer,flagg,flag3
            Vtk=vtkTimerCallback1()
            if Vtk.getPinYin("停止") in pinyin or Vtk.getPinYin("再见") in pinyin or Vtk.getPinYin("不需要") in pinyin :
                print("谢谢你的使用，感谢下次光临！")
                speaker.Speak("谢谢你的使用，感谢下次光临！")
                flagg=0 
            elif  Vtk.getPinYin("完成") in pinyin or Vtk.getPinYin("完全") in pinyin:
                if flag3!=1:
                    flag3=0
                flagg=0
                print("手动结束，消毒完成，谢谢你的使用！")
                speaker.Speak("手动结束，消毒完成，谢谢你的使用！")
            elif  Vtk.getPinYin("消毒液") in pinyin :
                speaker.Speak("消毒液余量为百分之"+str(s))
            elif  Vtk.getPinYin("简易") in pinyin :
                ptt=3
                speaker.Speak("正在切换简易模式，请稍后，切换成功，目前模式为简易模式")
            elif  Vtk.getPinYin("普通") in pinyin :
                ptt=1
                speaker.Speak("正在切换普通模式，请稍后，切换成功，目前模式为普通模式")
            elif  Vtk.getPinYin("疯狂") in pinyin :
                ptt=2
                speaker.Speak("正在切换疯狂消毒模式，请稍后，切换成功，目前模式为疯狂消毒模式，请注意此模式下消毒液使用量及耗电量将增加")
            elif  Vtk.getPinYin("电量") in pinyin : 
                speaker.Speak("电量余量为百分之"+str(be))
            elif Vtk.getPinYin("状态") in pinyin :
                if ptt == 0:
                    speaker.Speak("机器人自检中请稍后，机器状态良好，目前模式为简易模式")
                elif ptt == 1:
                    speaker.Speak("机器人自检中请稍后，机器状态良好，目前模式为普通模式")
                elif ptt==2 :
                    speaker.Speak("机器人自检中请稍后，机器状态良好，目前模式为疯狂模式")
                speaker.Speak("消毒液余量为百分之"+str(s))
                speaker.Speak("电量余量为百分之"+str(be))
                speaker.Speak("预计消毒结束还有"+str(m)+"分钟")
                speaker.Speak("感谢查询，我将继续为您消毒哦主人")
            else:
                print("无法识别，请重新操作")
        def close_window(self,renderWindowInteractor1):
            global renderWindowInteractor
            render_window = renderWindowInteractor.GetRenderWindow()
            render_window.Finalize()
        def main(self):
            global renderWindowInteractor,renderer,flagg,m,r,ptt,ooo,actors,renderWindow,f,oo
            ooo+=1
            flagg=1
            m=5
            r=0
            f=1          
            #Read STL            
            reader1 = vtk.vtkSTLReader()
            reader1.SetFileName("arml.stl")
            reader2 = vtk.vtkSTLReader()
            reader2.SetFileName("armr.stl")
            reader5 = vtk.vtkSTLReader()
            reader5.SetFileName("body.stl")
            #Create a mapper and actor
            mapper1 = vtk.vtkPolyDataMapper()
            mapper1.SetInputConnection(reader1.GetOutputPort())
            mapper2 = vtk.vtkPolyDataMapper()
            mapper2.SetInputConnection(reader2.GetOutputPort())
            mapper5 = vtk.vtkPolyDataMapper()
            mapper5.SetInputConnection(reader5.GetOutputPort())
            actor1 = vtk.vtkActor()
            actor1.SetMapper(mapper1)
            actor2 = vtk.vtkActor()
            actor2.SetMapper(mapper2)
            actor5 = vtk.vtkActor()
            actor5.SetMapper(mapper5)
            # Setup a renderer, render window, and interactor
            renderer = vtk.vtkRenderer()
            renderWindow = vtk.vtkRenderWindow()
            renderWindow.AddRenderer(renderer);
            renderWindowInteractor = vtk.vtkRenderWindowInteractor()
            renderWindowInteractor.SetRenderWindow(renderWindow)
            #renderWindow.SetWindowName("Test")
            renderWindow.AddRenderer(renderer);
            renderWindowInteractor = vtk.vtkRenderWindowInteractor()
            renderWindowInteractor.SetRenderWindow(renderWindow)

            #Add the actor to the scene
            renderer.AddActor(actor1)
            renderer.AddActor(actor2)
            renderer.AddActor(actor5)
            renderer.SetBackground(0,0,0.8) # RGB 0~1
            actor1.SetOrigin(-75.98744583129883, 55.179789543151855+10, 28.96554946899414)
            actor2.SetOrigin(-16.002686738967896, 54.13501167297363+10, 28.966289520263672)
            actor5.SetOrigin(actor5.GetCenter())

            #Render and interact
            renderWindow.Render()

            # Initialize must be called prior to creating timer events.
            renderWindowInteractor.Initialize()          
        
            # Sign up to receive TimerEvent
            actors.append(actor1)
            actors.append(actor2)
            actors.append(actor5)
            renderWindowInteractor.AddObserver('TimerEvent', Vtk.execute)
            timerId = renderWindowInteractor.CreateRepeatingTimer(100);
            if (oo):
                #oo=0
                timer = threading.Timer(1,Vtk.fun_timer)  #首次启动
                timer.start()      
        
            #start the interaction and timer
            renderWindowInteractor.Start()
    def user_yiqing():
        cap = cv2.VideoCapture(0)
        speaker.Speak("欢迎光临疫情期间通行身份校验系统"+"请输入您的身份证号码"+"并点击开始查询按钮")
        data2 = pd.read_excel('全国身份证号对应省市区.xls', header=None, names=['身份证前六位', '所属地区'])
        gender_id = {'0': '女', '1': '男'}
        app = QApplication(sys.argv)
        show = Window()  #主窗口的类
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("a.png")))
        show.setFixedSize(700,434 )
        show.setPalette(palette)
        show.show()
        sys.exit(app.exec_())
    def mod():
        global ptt
        ptt=int(input('输入模式：'))
        if ptt==3:
            speaker.Speak('简易模式。')
            print('简易模式。')
        elif ptt==1:
            speaker.Speak('普通模式。')
            print('普通模式。')
        elif ptt==2:
            speaker.Speak('疯狂模式。')
            print('疯狂模式。')
    def chongdian():
        global s,be
        ppp=int(input('是否要充电：'))
        if (ppp):
            be=100
            speaker.Speak("充电完成。")
            print('充电完成。')
        else:
            pass
        ppp1=int(input('是否要加入消毒液：'))
        if (ppp):
            s=100
            speaker.Speak("消毒液加入完成。")
            print('消毒液加入完成。')
        else:
            pass
    #############脸部识别##############
    def user_face_recognition():
        speaker.Speak('正在加载人脸识别，请稍等。')
        print('正在加载人脸识别，请稍等。')
        #准备好识别方法
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        #使用之前训练好的模型
        recognizer.read('trainner/trainner.yml')
        #再次调用人脸分类器
        cascade_path = "E:\zhu/face/haarcascade_frontalface_default.xml"#脸部识别
        face_cascade = cv2.CascadeClassifier(cascade_path)
        #加载一个字体，用于识别后，在图片上标注出对象的名字
        font = cv2.FONT_HERSHEY_SIMPLEX
        idnum = 0
        #设置好与ID号码对应的用户名，如下，如0对应的就是初始
        names = ['Yuhao','Zhuzhemin','Daxiangge','unknown']
        #调用摄像头
        cam = cv2.VideoCapture(0)
        minW = 0.1*cam.get(3)
        minH = 0.1*cam.get(4)
        flag=[0,0,0,0]
        flag1=0
        while True:
            ret,img = cam.read()
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            #识别人脸
            faces = face_cascade.detectMultiScale(
                    gray,
                    scaleFactor = 1.2,
                    minNeighbors = 5,
                    minSize = (int(minW),int(minH))
                    )
            #进行校验

            for(x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                idnum,confidence = recognizer.predict(gray[y:y+h,x:x+w])
                #计算出一个检验结果
                if confidence < 50:
                    print(idnum)
                    print(confidence)
                    if 1<=idnum<=800:
                        idnum=0
                        #ser.write("0".encode())
                        print("0 send")
                        flag[0]+=1
                        if flag[0]==3:
                            speaker.Speak("俞澔，是否为你本人，是输入1，不是输入2:")
                            flag1=int(input("俞澔，是否为你本人，是输入1，不是输入2:"))
                            if flag1==1:
                                speaker.Speak('请点击“学生体温录入”，输入姓名和体温。')
                                print('请点击“学生体温录入”，输入姓名和体温。')
                                break
                            else:
                                flag=[0,0,0,0]
                                flag1=0
                        #mc.setBlock(-22,20,-33,0)
                        #mc.setBlock(-22,19,-33,0)
                    elif 801<=idnum<=1600:
                        idnum=1
                        #ser.write("1".encode())
                        print("1 send")
                        flag[1]+=1
                        if flag[1]==3:
                            speaker.Speak("朱哲敏，是否为你本人，是输入1，不是输入2:")
                            flag1=int(input("朱哲敏，是否为你本人，是输入1，不是输入2:"))
                            if flag1==1:
                                speaker.Speak('请点击“学生体温录入”，输入姓名和体温。')
                                print('请点击“学生体温录入”，输入姓名和体温。')
                                break
                            else:
                                flag=[0,0,0,0]
                                flag1=0
                        #mc.setBlock(-22,20,-33,0)
                        #mc.setBlock(-22,19,-33,0)
                    elif 1601<=idnum<=2400:
                        idnum=2
                        #ser.write("2".encode())
                        print("2 send")
                        flag[2]+=1
                        if flag[2]==3:
                            speaker.Speak("大翔哥，是否为你本人，是输入1，不是输入2:")
                            flag1=int(input("大翔哥，是否为你本人，是输入1，不是输入2:"))
                            if flag1==1:
                                speaker.Speak('请点击“学生体温录入”，输入姓名和体温。')
                                print('请点击“学生体温录入”，输入姓名和体温。')
                                break
                            else:
                                flag=[0,0,0,0]
                                flag1=0
                        #mc.setBlock(-22,20,-33,20)
                        #mc.setBlock(-22,19,-33,20)
                    idum = names[idnum]
                    confidence = "{0}%",format(round(100-confidence))
                else:
                    idnum=3
                    print(idnum)
                    print(confidence)
                    
                    idum = names[idnum]
                    flag[3]+=1
                    if flag[3]==3:
                        speaker.Speak("你不是学校内部成员，不是输入1，是输入2:")
                        flag1=int(input("你不是学校内部成员，不是输入1，是输入2:"))
                        if flag1==1:
                            speaker.Speak('1. 请出示健康码。2. 请点击“外部人员登记”，输入各项信息。')
                            print('1. 请出示健康码。')
                            print('2. 请点击“外部人员登记”，输入各项信息。')
                            break
                        else:
                            flag=[0,0,0,0]
                            flag1=0
                    confidence = "{0}%",format(round(100-confidence))

                #输出检验结果以及用户名
                cv2.putText(img,str(idum),(x+5,y-5),font,1,(0,0,255),1)
                cv2.putText(img,str(confidence),(x+5,y+h-5),font,1,(0,0,0),1)

                #展示结果
                cv2.imshow('camera',img)
            if flag1==1:
                key=27
            else:
                key = cv2.waitKey(10) & 0xFF
            if key == 27:#ord('q')
                break

        #释放资源
        cam.release()
        cv2.destroyAllWindows()
    ###########健康码##########################
    def health():
        speaker.Speak('正在加载健康码识别，请稍等。')
        print('正在加载健康码识别，请稍等。')
        driver = webdriver.Chrome()
        driver.minimize_window()
        reader = zxing.BarCodeReader()
        bbox = (960, 0, 1920, 1080)
        cap = cv2.VideoCapture(0 + cv2.CAP_DSHOW)
        width = 640  # 定义摄像头获取图像宽度
        height = 480  # 定义摄像头获取图像长度
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)  # 设置宽度
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)  # 设置长度
        def aa():
            global fg
            while cap is not None:
                # 读获取每一帧
                if fg==1:
                    speaker.Speak('扫描成功，请稍等！')
                    print('扫描成功，请稍等！')
                    cap.release()
                    cv2.destroyAllWindows()
                    break
                elif fg==0:
                    ret, frame = cap.read()
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    cv2.imwrite("code1.png", frame)
                    cv2.imshow('frame', frame)
                    cv2.waitKey(200)
                    a = ''
                    b = ''
                    im = ImageGrab.grab(bbox)
                    im.save('code1.jpg')
        def find():
            try:
                barcode = reader.decode("code1.jpg")
                #print(barcode.parsed)
                driver.get(barcode.parsed)
                time.sleep(0.5)
                color = driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[2]')
                for i in color:
                    a = i.text
                time_get = driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[3]')
                for i in time_get:
                    b = i.text
                return a,b
            except:
                pass
        def bb():
            global fg
            while True:
                if find()!=None:
                    fg=1
                    find1=find()[0]
                    find2=find()[1]
                    print(find1+find2)
                    speaker.Speak('扫描结果为：'+find1+'。此码更新于：'+find2[7:12]+'年'+find2[13:15]+'月'+find2[16:18]+'日'+find2[19:21]+'时'+find2[22:24]+'分'+find2[25:27]+'秒。')
                    print('扫描结果为：'+find1+'。此码更新于：'+find2[7:12]+'年'+find2[13:15]+'月'+find2[16:18]+'日'+find2[19:21]+'时'+find2[22:24]+'分'+find2[25:27]+'秒。')
                    #cap.release()
                    #cv2.destroyAllWindows()
                    break
        if __name__=="__main__":
            Thread(target=aa).start()
            bb()
    ##############外部人员登记##################        
    def user_sign_up():
        global flag3
        speaker.Speak('正在加载外部人员登记，请稍等。')
        print('正在加载外部人员登记，请稍等。')
        window_sign_up = tk.Toplevel(window)
        bkimg2=Image.open('backp2.jpg')
        bkimg2 = bkimg.resize((400, 450),Image.ANTIALIAS)
        photo2 = ImageTk.PhotoImage(bkimg2)
        label_img2 = tk.Label(window_sign_up,image = photo2,compound=tk.CENTER)
        label_img2.pack()
        

        window_sign_up.title('人员登记')
        window_sign_up.geometry('%dx%d' %(400,450))
        cap = cv2.VideoCapture(0)
        conn = pymysql.connect('localhost', 'basketball','basketball', 'external_personnel')
        cursor = conn.cursor()
        tk.Label(window_sign_up, text='日期', font=('msyh', 14)).place(x=10, y=90)
        tk.Label(window_sign_up, text='时间', font=('msyh', 14)).place(x=10, y=130)
        tk.Label(window_sign_up, text='姓名', font=('msyh', 14)).place(x=10, y=170)
        tk.Label(window_sign_up, text='电话', font=('msyh', 14)).place(x=10, y=210)
        tk.Label(window_sign_up, text='体温', font=('msyh', 14)).place(x=10, y=250)
        tk.Label(window_sign_up, text='目的', font=('msyh', 14)).place(x=10, y=290)
        var_usr_name = tk.StringVar()
        entry_usr_name1 = tk.Entry(window_sign_up, textvariable=var_usr_name, font=('msyh', 14))
        entry_usr_name1.place(x=120,y=90)
        var_usr_name = tk.StringVar()
        entry_usr_name2 = tk.Entry(window_sign_up, textvariable=var_usr_name, font=('msyh', 14))
        entry_usr_name2.place(x=120,y=130)
        var_usr_name = tk.StringVar()
        entry_usr_name3 = tk.Entry(window_sign_up, textvariable=var_usr_name, font=('msyh', 14))
        entry_usr_name3.place(x=120,y=170)
        var_usr_name = tk.StringVar()
        entry_usr_name4 = tk.Entry(window_sign_up, textvariable=var_usr_name, font=('msyh', 14))
        entry_usr_name4.place(x=120,y=210)
        var_usr_name = tk.StringVar()
        entry_usr_name5 = tk.Entry(window_sign_up, textvariable=var_usr_name, font=('msyh', 14))
        entry_usr_name5.place(x=120,y=250)
        var_usr_name = tk.StringVar()
        entry_usr_name6 = tk.Entry(window_sign_up, textvariable=var_usr_name, font=('msyh', 14))
        entry_usr_name6.place(x=120,y=290)
        def usr_login():
            a=entry_usr_name1.get()
            b=entry_usr_name2.get()
            c=entry_usr_name3.get()
            d=entry_usr_name4.get()
            e=entry_usr_name5.get()
            f=entry_usr_name6.get()
            g=a + "-" + c + "-" + d + ".bin"
            i=a + "-" + c + "-" + d + ".jpg"
            h=a + "," + b + ",'" + c + "'," + d + "," + e + ",'" + f + "'"
            while True:
                ret, frame = cap.read()
                cv2.imshow("frame",frame)
                if cv2.waitKey(1) & 0xFF == 27:
                    cv2.imencode('.jpg',frame)[1].tofile('./pic/'+i)
                    cv2.imencode('.jpg',frame)[1].tofile('./bin/'+g)
                    break
                    os.exit()      
            sql = "INSERT INTO `external_personnel`.`external_personnel`(日期,时间,姓名,电话,体温,目的) VALUES (" + h + ")"
            try:
                cursor.execute(sql)
                conn.commit()
                speaker.Speak('录入完成。')
                print('录入完成。')               
            except:
                print('error')
                conn.rollback()
                conn.close()
            if float(e)>=37.3:
                msg="11111"
                mqtt.PUB("EIS1",msg[0])
                mqtt.PUB("EIS2",msg[1])
                mqtt.PUB("EIS3",msg[2])
                mqtt.PUB("EIS4",msg[3])
                mqtt.PUB("EIS5",msg[4])
                speaker.Speak('您发烧了，不得进入学校，需要疯狂消毒。')
                print('您发烧了，不得进入学校，需要疯狂消毒。')
                flag3=1
            else:
                flag1=0
                flag3=2
                speaker.Speak('正在查询您的过往入校记录，请稍等。')
                print('正在查询您的过往入校记录，请稍等。')
                sql="SELECT * FROM `external_personnel`.`external_personnel` WHERE `external_personnel`.`姓名` > '%d'" % (0)
                cursor.execute(sql)
                results=cursor.fetchall()
                for row in results:
                    if row[2]==c: 
                        #print(row)
                        print(row[2]+'于'+row[0][0:4]+'年'+row[0][4:6]+'月'+row[0][6:8]+'日'+row[1][0:2]+'点'+row[1][2:4]+'分曾进入学校，目的是：'+row[5]+'，电话是：'+ row[3]+'，体温是：'+row[4]+'。\n')
            
                        if float(row[4])>=37.3:
                            flag1+=1
                if flag1>0:
                    msg="00001"
                    mqtt.PUB("EIS1",msg[0])
                    mqtt.PUB("EIS2",msg[1])
                    mqtt.PUB("EIS3",msg[2])
                    mqtt.PUB("EIS4",msg[3])
                    mqtt.PUB("EIS5",msg[4])
                    speaker.Speak('过往共'+str(flag1)+'次体温超标,需要普通消毒!')
                    print('过往共'+str(flag1)+'次体温超标,需要普通消毒!')
                else:
                    msg="11100"
                    mqtt.PUB("EIS1",msg[0])
                    mqtt.PUB("EIS2",msg[1])
                    mqtt.PUB("EIS3",msg[2])
                    mqtt.PUB("EIS4",msg[3])
                    mqtt.PUB("EIS5",msg[4])
                    speaker.Speak('过往无体温超标,需要简易消毒。')
                    print('过往无体温超标,需要简易消毒。')
                
            cap.release()
            cv2.destroyAllWindows()   
            window_sign_up.destroy()     
        login = tk.Button(window_sign_up, text='确定', command=usr_login)
        login.place(x=150, y=350)
        window.mainloop()
    ##############内部人员登记##################
    def student_sign_up():
        global flag3
        speaker.Speak('正在加载学生体温录入，请稍等。')
        print('正在加载学生体温录入，请稍等。')
        student_sign_up = tk.Toplevel(window)
        bkimg3=Image.open('backp3.jpg')
        bkimg3 = bkimg.resize((400, 350),Image.ANTIALIAS)
        photo3 = ImageTk.PhotoImage(bkimg3)
        label_img2 = tk.Label(student_sign_up,image = photo3,compound=tk.CENTER)
        label_img2.pack()
        student_sign_up.title('人员登记')
        student_sign_up.geometry('%dx%d' %(400,350))
        cap = cv2.VideoCapture(0)
        conn = pymysql.connect('localhost', 'basketball','basketball', 'internal_personnel')
        cursor = conn.cursor()
        tk.Label(student_sign_up, text='日期', font=('msyh', 14)).place(x=10, y=90)
        tk.Label(student_sign_up, text='时间', font=('msyh', 14)).place(x=10, y=130)
        tk.Label(student_sign_up, text='姓名', font=('msyh', 14)).place(x=10, y=170)
        tk.Label(student_sign_up, text='体温', font=('msyh', 14)).place(x=10, y=210)
        var_usr_name = tk.StringVar()
        entry_usr_name1 = tk.Entry(student_sign_up, textvariable=var_usr_name, font=('msyh', 14))
        entry_usr_name1.place(x=120,y=90)
        var_usr_name = tk.StringVar()
        entry_usr_name2 = tk.Entry(student_sign_up, textvariable=var_usr_name, font=('msyh', 14))
        entry_usr_name2.place(x=120,y=130)
        var_usr_name = tk.StringVar()
        entry_usr_name3 = tk.Entry(student_sign_up, textvariable=var_usr_name, font=('msyh', 14))
        entry_usr_name3.place(x=120,y=170)
        var_usr_name = tk.StringVar()
        entry_usr_name5 = tk.Entry(student_sign_up, textvariable=var_usr_name, font=('msyh', 14))
        entry_usr_name5.place(x=120,y=210)
        def student_login():
            a=entry_usr_name1.get()
            b=entry_usr_name2.get()
            c=entry_usr_name3.get()
            e=entry_usr_name5.get()
            h=a + "," + b + ",'" + c + "',"  + e
            sql = "INSERT INTO `internal_personnel`.`internal_personnel`(日期,时间,姓名,体温) VALUES (" + h + ")"
            try:
                cursor.execute(sql)
                conn.commit()
                speaker.Speak('录入完成。')
                print('录入完成。')
            except:
                print('error')
                conn.rollback()
                conn.close()
            if float(e)>=37.3:
                flag3=1
                msg="11111"
                mqtt.PUB("EIS1",msg[0])
                mqtt.PUB("EIS2",msg[1])
                mqtt.PUB("EIS3",msg[2])
                mqtt.PUB("EIS4",msg[3])
                mqtt.PUB("EIS5",msg[4])
                speaker.Speak('您发烧了，不得进入学校，需要疯狂消毒。')
                print('您发烧了，不得进入学校，需要疯狂消毒。')
                
            else:
                flag2=0
                flag3=2
                speaker.Speak('正在查询您的过往入校记录，请稍等。')
                print('正在查询您的过往入校记录，请稍等。')
                sql="SELECT * FROM `internal_personnel`.`internal_personnel` WHERE `internal_personnel`.`姓名` > '%d'" % (0)
                cursor.execute(sql)
                results=cursor.fetchall()
                for row in results:
                    if row[2]==c: 
                        #print(row)
                        print(row[2]+'于'+row[0][0:4]+'年'+row[0][4:6]+'月'+row[0][6:8]+'日'+row[1][0:2]+'点'+row[1][2:4]+'分曾进入学校，体温是：'+row[3]+'。\n')
                        if float(row[3])>=37.3:
                            flag2+=1
                if flag2>0:
                    msg="00001"
                    mqtt.PUB("EIS1",msg[0])
                    mqtt.PUB("EIS2",msg[1])
                    mqtt.PUB("EIS3",msg[2])
                    mqtt.PUB("EIS4",msg[3])
                    mqtt.PUB("EIS5",msg[4])
                    speaker.Speak('过往共'+str(flag2)+'次体温超标,需要普通消毒!')
                    print('过往共'+str(flag2)+'次体温超标,需要普通消毒!')
                    
                else:
                    msg="11100"
                    mqtt.PUB("EIS1",msg[0])
                    mqtt.PUB("EIS2",msg[1])
                    mqtt.PUB("EIS3",msg[2])
                    mqtt.PUB("EIS4",msg[3])
                    mqtt.PUB("EIS5",msg[4])
                    speaker.Speak('过往无体温超标,需要简易消毒。')
                    print('过往无体温超标,需要简易消毒。')
                     
            cap.release()
            cv2.destroyAllWindows()
            
            student_sign_up.destroy()
            
        login = tk.Button(student_sign_up, text='确定', command=student_login)
        login.place(x=150, y=250)
        window.mainloop()
    ##############外部人员进入情况查询##################
    def external_personnel_query():
        speaker.Speak('正在加载外部人员进入情况查询，请稍等。')
        print('正在加载外部人员进入情况查询，请稍等。')
        external_personnel_query = tk.Toplevel(window)
        bkimg2=Image.open('backp2.jpg')
        bkimg2 = bkimg.resize((400, 200),Image.ANTIALIAS)
        photo2 = ImageTk.PhotoImage(bkimg2)
        label_img2 = tk.Label(external_personnel_query,image = photo2,compound=tk.CENTER)
        label_img2.pack()
        external_personnel_query.title('人员登记')
        external_personnel_query.geometry('%dx%d' %(400,200))
        cap = cv2.VideoCapture(0)
        conn = pymysql.connect('localhost', 'basketball','basketball', 'external_personnel')
        cursor = conn.cursor()
        tk.Label(external_personnel_query, text='姓名', font=('msyh', 14)).place(x=10, y=100)
        var_usr_name = tk.StringVar()
        entry_usr_name3 = tk.Entry(external_personnel_query, textvariable=var_usr_name, font=('msyh', 14))
        entry_usr_name3.place(x=100,y=100)
        def external_query():
            c=entry_usr_name3.get()
            flag4=0
            flag5=0
            speaker.Speak('正在查询'+c+'的过往入校记录，请稍等。')
            print('正在查询'+c+'的过往入校记录，请稍等。')
            sql="SELECT * FROM `external_personnel`.`external_personnel` WHERE `external_personnel`.`姓名` > '%d'" % (0)
            cursor.execute(sql)
            results=cursor.fetchall()
            for row in results:
                if row[2]==c: 
                    #print(row)
                    print(row[2]+'于'+row[0][0:4]+'年'+row[0][4:6]+'月'+row[0][6:8]+'日'+row[1][0:2]+'点'+row[1][2:4]+'分曾进入学校，目的是：'+row[5]+'，电话是：'+ row[3]+'，体温是：'+row[4]+'。\n')
                    flag5+=1
                    if float(row[4])>=37.3:
                        flag4+=1
            speaker.Speak(c+'一共进入学校'+str(flag5)+'次。')
            print(c+'一共进入学校'+str(flag5)+'次。')
            if flag4>0:
                speaker.Speak('过往共'+str(flag4)+'次体温超标!')
                print('过往共'+str(flag4)+'次体温超标!')
            else:
                speaker.Speak('过往无体温超标。')
                print('过往无体温超标。')
            cap.release()
            cv2.destroyAllWindows()
            
            external_personnel_query.destroy()
            
        login = tk.Button(external_personnel_query, text='确定', command=external_query)
        login.place(x=150, y=140)
        window.mainloop()
        ##############内部人员进入情况查询##################
    def internal_personnel_query():
        speaker.Speak('正在加载内部人员进入情况查询，请稍等。')
        print('正在加载内部人员进入情况查询，请稍等。')
        internal_personnel_query = tk.Toplevel(window)
        bkimg3=Image.open('backp3.jpg')
        bkimg3 = bkimg.resize((400, 200),Image.ANTIALIAS)
        photo3 = ImageTk.PhotoImage(bkimg3)
        label_img2 = tk.Label(internal_personnel_query,image = photo3,compound=tk.CENTER)
        label_img2.pack()
        internal_personnel_query.title('人员登记')
        internal_personnel_query.geometry('%dx%d' %(400,200))
        cap = cv2.VideoCapture(0)
        conn = pymysql.connect('localhost', 'basketball','basketball', 'internal_personnel')
        cursor = conn.cursor()
        tk.Label(internal_personnel_query, text='姓名', font=('msyh', 14)).place(x=10, y=100)
        var_usr_name = tk.StringVar()
        entry_usr_name3 = tk.Entry(internal_personnel_query, textvariable=var_usr_name, font=('msyh', 14))
        entry_usr_name3.place(x=100,y=100)
        def internal_query():
            c=entry_usr_name3.get()
            flag4=0
            flag5=0
            speaker.Speak('正在查询'+c+'的过往入校记录，请稍等。')
            print('正在查询'+c+'的过往入校记录，请稍等。')
            sql="SELECT * FROM `internal_personnel`.`internal_personnel` WHERE `internal_personnel`.`姓名` > '%d'" % (0)
            cursor.execute(sql)
            results=cursor.fetchall()
            for row in results:
                if row[2]==c: 
                    #print(row)
                    print(row[2]+'于'+row[0][0:4]+'年'+row[0][4:6]+'月'+row[0][6:8]+'日'+row[1][0:2]+'点'+row[1][2:4]+'分曾进入学校。\n')
                    flag5+=1
                    if float(row[3])>=37.3:
                        flag4+=1
            speaker.Speak(c+'一共进入学校'+str(flag5)+'次。')
            print(c+'一共进入学校'+str(flag5)+'次。')
            if flag4>0:
                speaker.Speak('过往共'+str(flag4)+'次体温超标!')
                print('过往共'+str(flag4)+'次体温超标!')
            else:
                speaker.Speak('过往无体温超标。')
                print('过往无体温超标。')
            cap.release()
            cv2.destroyAllWindows()
            
            internal_personnel_query.destroy()
            
        login = tk.Button(internal_personnel_query, text='确定', command=internal_query)
        login.place(x=150, y=140)
        window.mainloop()
    ##############内部人员信息上传##################
    def information_upload():
        speaker.Speak('正在加载内部人员信息上传，请稍等。')
        print('正在加载内部人员信息上传，请稍等。')
        information_upload = tk.Toplevel(window)
        bkimg2=Image.open('backp.jpg')
        bkimg2 = bkimg.resize((400,600),Image.ANTIALIAS)
        photo2 = ImageTk.PhotoImage(bkimg2)
        label_img2 = tk.Label(information_upload,image = photo2,compound=tk.CENTER)
        label_img2.pack()
        information_upload.title('内部人员信息上传')
        information_upload.geometry('%dx%d' %(400,600))
        cap = cv2.VideoCapture(0)
        conn = pymysql.connect('localhost', 'basketball','basketball', 'internal_personnel')
        cursor = conn.cursor()
        tk.Label(information_upload, text='姓名', font=('msyh', 14)).place(x=10, y=90)
        tk.Label(information_upload, text='学院', font=('msyh', 14)).place(x=10, y=130)
        tk.Label(information_upload, text='专业', font=('msyh', 14)).place(x=10, y=170)
        tk.Label(information_upload, text='班级', font=('msyh', 14)).place(x=10, y=210)
        tk.Label(information_upload, text='学号', font=('msyh', 14)).place(x=10, y=250)
        tk.Label(information_upload, text='性别', font=('msyh', 14)).place(x=10, y=290)
        tk.Label(information_upload, text='电话', font=('msyh', 14)).place(x=10, y=330)
        tk.Label(information_upload, text='年龄', font=('msyh', 14)).place(x=10, y=370)
        tk.Label(information_upload, text='政治面貌', font=('msyh', 14)).place(x=10, y=410)
        tk.Label(information_upload, text='出生年月日', font=('msyh', 14)).place(x=10, y=450)
        
        var_usr_name = tk.StringVar()
        entry_usr_name1 = tk.Entry(information_upload, textvariable=var_usr_name, font=('msyh', 14))
        entry_usr_name1.place(x=120,y=90)
        var_usr_name = tk.StringVar()
        entry_usr_name2 = tk.Entry(information_upload, textvariable=var_usr_name, font=('msyh', 14))
        entry_usr_name2.place(x=120,y=130)
        var_usr_name = tk.StringVar()
        entry_usr_name3 = tk.Entry(information_upload, textvariable=var_usr_name, font=('msyh', 14))
        entry_usr_name3.place(x=120,y=170)
        var_usr_name = tk.StringVar()
        entry_usr_name4 = tk.Entry(information_upload, textvariable=var_usr_name, font=('msyh', 14))
        entry_usr_name4.place(x=120,y=210)
        var_usr_name = tk.StringVar()
        entry_usr_name5 = tk.Entry(information_upload, textvariable=var_usr_name, font=('msyh', 14))
        entry_usr_name5.place(x=120,y=250)
        var_usr_name = tk.StringVar()
        entry_usr_name6 = tk.Entry(information_upload, textvariable=var_usr_name, font=('msyh', 14))
        entry_usr_name6.place(x=120,y=290)
        var_usr_name = tk.StringVar()
        entry_usr_name7 = tk.Entry(information_upload, textvariable=var_usr_name, font=('msyh', 14))
        entry_usr_name7.place(x=120,y=330)
        var_usr_name = tk.StringVar()
        entry_usr_name8 = tk.Entry(information_upload, textvariable=var_usr_name, font=('msyh', 14))
        entry_usr_name8.place(x=120,y=370)
        var_usr_name = tk.StringVar()
        entry_usr_name9 = tk.Entry(information_upload, textvariable=var_usr_name, font=('msyh', 14))
        entry_usr_name9.place(x=120,y=410)
        var_usr_name = tk.StringVar()
        entry_usr_name10 = tk.Entry(information_upload, textvariable=var_usr_name, font=('msyh', 14))
        entry_usr_name10.place(x=120,y=450)
        def user_upload():
            a=entry_usr_name1.get()
            b=entry_usr_name2.get()
            c=entry_usr_name3.get()
            d=entry_usr_name4.get()
            e=entry_usr_name5.get()
            f=entry_usr_name6.get()
            j=entry_usr_name7.get()
            k=entry_usr_name8.get()
            m=entry_usr_name9.get()
            o=entry_usr_name10.get()
            
            g=a + "-" + b + "-" + c + "-" + d + "-" + e + "-" + j + "-" + ".bin"
            i=a + "-" + b + "-" + c + "-" + d + "-" + e + "-" + j + "-" + ".jpg"
            h="'" + a + "','" + b + "','" + c + "'," + d + "," + e + ",'" + f + "'," + j + "," + k + ",'" + m + "'," + o
            while True:
                ret, frame = cap.read()
                cv2.imshow("frame",frame)
                if cv2.waitKey(1) & 0xFF == 27:
                    cv2.imencode('.jpg',frame)[1].tofile('./information/pic/'+i)
                    cv2.imencode('.jpg',frame)[1].tofile('./information/bin/'+g)
                    break
                    os.exit()
            
            sql = "INSERT INTO `internal_personnel`.`information_upload`(姓名,学院,专业,班级,学号,性别,电话,年龄,政治面貌,出生年月日) VALUES (" + h + ")"
            try:
                cursor.execute(sql)
                conn.commit()
                speaker.Speak('信息上传成功。')
                print('信息上传成功。')
            except:
                print('error')
                conn.rollback()
                conn.close()
            cap.release()
            cv2.destroyAllWindows()
            
            information_upload.destroy()
            
        login = tk.Button(information_upload, text='确定', command=user_upload)
        login.place(x=150, y=500)
        window.mainloop()
    ##############内部人员信息查询##################
    def internal_personnel_information_query():
        speaker.Speak('正在加载内部人员信息查询，请稍等。')
        print('正在加载内部人员信息查询，请稍等。')
        internal_personnel_information_query = tk.Toplevel(window)
        bkimg2=Image.open('backp.jpg')
        bkimg2 = bkimg.resize((400, 200),Image.ANTIALIAS)
        photo2 = ImageTk.PhotoImage(bkimg2)
        label_img2 = tk.Label(internal_personnel_information_query,image = photo2,compound=tk.CENTER)
        label_img2.pack()
        internal_personnel_information_query.title('内部人员信息查询')
        internal_personnel_information_query.geometry('%dx%d' %(400,200))
        cap = cv2.VideoCapture(0)
        conn = pymysql.connect('localhost', 'basketball','basketball', 'internal_personnel')
        cursor = conn.cursor()
        tk.Label(internal_personnel_information_query, text='姓名', font=('msyh', 14)).place(x=10, y=100)
        var_usr_name = tk.StringVar()
        entry_usr_name1 = tk.Entry(internal_personnel_information_query, textvariable=var_usr_name, font=('msyh', 14))
        entry_usr_name1.place(x=100,y=100)
        def internal_information_query():
            a=entry_usr_name1.get()
            try:
                sql="SELECT * FROM `internal_personnel`.`information_upload` WHERE `information_upload`.`姓名` > '%d'" % (0)
                cursor.execute(sql)
                results=cursor.fetchall()
                for row in results:
                    if row[0]==a: 
                        #print(row)
                        speaker.Speak(row[0]+'的个人信息如下：学院：'+row[1]+'。专业：'+row[2]+'。班级：'+row[3]+'。电话：'+row[6]+'。年龄：'+row[7]+'。政治面貌：'+row[8]+'。出生年月日：'+row[9][0:4]+'年'+row[9][4:6]+'月'+row[9][6:8]+'日。')
                        print(row[0]+'的个人信息如下：\n学院：'+row[1])
                        print('专业：'+row[2]+'\n班级：'+row[3])
                        print('学号：'+row[4]+'\n性别：'+row[5])
                        print('电话：'+row[6]+'\n年龄：'+row[7])
                        print('政治面貌：'+row[8]+'\n出生年月日：'+row[9][0:4]+'年'+row[9][4:6]+'月'+row[9][6:8]+'日')
            except:
                print('error')
                conn.rollback()
                conn.close()
            cap.release()
            cv2.destroyAllWindows()        
            internal_personnel_information_query.destroy()      
        login = tk.Button(internal_personnel_information_query, text='确定', command=internal_information_query)
        login.place(x=150, y=140)
        window.mainloop()
    def TTSplay(text):
        speech.TTS(text)
        media.play()
    def recordSTT():
        media.record(fname='record.wav')
        return speech.STT(fname='record.wav')
    
    #print('1')
    #time.sleep(1)
    #print('1')
    #closewindow()
    #print('1')
    #def mcc():
    global entityId,lock,flag3
    Vtk=vtkTimerCallback1()
    while True:
        pos=mc.entity.getTilePos(entityId)
        #print(pos)
        blockId=mc.getBlock(pos.x,pos.y-1,pos.z)
        if blockId==41 and lock==0:
            lock=1
            flag3=2
            window = tk.Tk()
            bkimg=Image.open('backp1.gif')
            bkimg = bkimg.resize((1200, 600),Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(bkimg)
            label_img = tk.Label(window, image = photo)
            label_img.pack()
            window.title('管理界面')
            window.geometry("%dx%d" %(1200,600))
            botton = tk.Button(window, text='人脸识别', command=user_face_recognition , font=('msyh', 20))
            botton.place(x=100, y=100)
            botton = tk.Button(window, text='身份校验', command=user_yiqing , font=('msyh', 20))
            botton.place(x=500, y=100)
            botton = tk.Button(window, text='健康码识别', command=health , font=('msyh', 20))
            botton.place(x=900, y=100)
            botton = tk.Button(window, text='外部人员登记', command=user_sign_up , font=('msyh', 20))
            botton.place(x=100, y=200)
            botton = tk.Button(window, text='学生体温录入', command=student_sign_up , font=('msyh', 20))
            botton.place(x=500, y=200)
            botton = tk.Button(window, text='外部人员进入情况查询', command=external_personnel_query , font=('msyh', 20))
            botton.place(x=100, y=400)
            botton = tk.Button(window, text='内部人员进入情况查询', command=internal_personnel_query , font=('msyh', 20))
            botton.place(x=500, y=400)
            botton = tk.Button(window, text='内部人员信息上传', command=information_upload , font=('msyh', 20))
            botton.place(x=100, y=300)
            botton = tk.Button(window, text='内部人员信息查询', command=internal_personnel_information_query , font=('msyh', 20))
            botton.place(x=500, y=300)
            botton = tk.Button(window, text='机器人消毒', command=Vtk.main, font=('msyh', 20))
            botton.place(x=900, y=200)
            botton = tk.Button(window, text='消毒模式选择', command=mod, font=('msyh', 20))
            botton.place(x=900, y=300)
            botton = tk.Button(window, text='机器人充电', command=chongdian, font=('msyh', 20))
            botton.place(x=900, y=400)
            window.mainloop()
            #
            
        elif blockId==1 and lock==1 and flag3==0:
            print('k'+str(flag3))
            lock=0
            #mc.setBlock(-76,-21,-126,0)
            mc.setBlock(-73,-21,-125,0)
            mc.setBlock(-73,-20,-125,0)
            mc.setBlock(-74,-21,-125,0)
            mc.setBlock(-74,-20,-125,0)
        elif blockId==1 and lock==1 and flag3==2:
            lock=0
            speaker.Speak('请您先消毒，消毒完成后才能进入学校。')
            print('请您先消毒，消毒完成后才能进入学校。')
        elif pos.x==-72 and pos.y==-21 and pos.z==-125:
            speaker.Speak('欢迎来到上海电力大学。')
            print('欢迎来到上海电力大学。')
            mc.postToChat("欢迎来到上海电力大学。")
            mc.setBlock(-73,-21,-125,20)
            mc.setBlock(-73,-20,-125,20)
            mc.setBlock(-74,-21,-125,20)
            mc.setBlock(-74,-20,-125,20)
    
    
if __name__=="__main__":
    control1()
    #Thread(target=control1).start()
