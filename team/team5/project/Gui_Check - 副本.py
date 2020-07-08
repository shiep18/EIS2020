import sys
import re

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import random
import requests
from bs4 import BeautifulSoup
import threading
import pandas as pd
import datetime
import os
import webbrowser
from pyecharts import GeoLines, Style    #地理轨迹图的类就是Geolines

from urllib.parse import unquote
from httputils import gehtml
import matplotlib.pyplot as plt
import json
import re
from pycharts_utils import getmaps

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation
from IPython.display import HTML

from hyperlpr import *
import cv2
from os import system
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
cap = cv2.VideoCapture(0)


speaker.Speak("欢迎光临疫情期间通行身份校验系统"+"请输入您的身份证号码"+"并点击开始查询按钮")
data = pd.read_excel('全国身份证号对应省市区.xls', header=None, names=['身份证前六位', '所属地区'])
gender_id = {'0': '女', '1': '男'}
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
        address = data[data['身份证前六位'].eq(idcard[:6])]['所属地区']

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
        style_geolines = style.add(is_label_show=True,
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
        
        geolines = GeoLines('身份证号码为', idcard,  **style.init_style)
        geolines.add(address.values[0],
                     [(rciry4, rciry1), (rciry1, rciry2), (rciry2, rciry3), (rciry3,rciry4)
                         , (rciry4, rciry0), (rciry0, '北京'),],
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
app = QApplication(sys.argv)
show = Window()  #主窗口的类
palette = QPalette()
palette.setBrush(QPalette.Background, QBrush(QPixmap("a.png")))
show.setFixedSize(700,434 )
show.setPalette(palette)
show.show()
sys.exit(app.exec_())
