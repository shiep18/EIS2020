import requests
import base64
import cv2
from  threading import Thread
from datetime import datetime
import time
from pygame import mixer
import tkinter
import pickle
import pymysql
import pyzbar.pyzbar as pyzbar
import numpy
from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageDraw, ImageFont,ImageTk
from tkinter import ttk
from twilio.rest import Client
from MXMqtt import MXMqtt
import time
import os
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
MQTTMOST = "mqtt.16302.com"
MQTTPORT = 1883
mqtt = MXMqtt(MQTTMOST,MQTTPORT)

topic = "sp"
mqtt.SUB(topic)
c=[('6928820071755', '欧莱雅男士洁面乳', 37.05, 1, '2020-07-01 14:42'), ('6921168509256', '农夫山泉', 1.9, 1, '2020-07-01 14:42')]


isbn=['6928820071755','6933211451924','6921168509256','7208061645','7302275491','6920487503808','9787506366649','6902088113143']
name=['欧莱雅男士洁面乳','九制陈皮','农夫山泉550ml','《追风筝的人》','《阿波罗是如何飞到月球的》','德生牌收音机PL-380','《生死疲劳》','清扬洗发露200g']
price=[39,29,2,29,69,399,39,28]
number=[1,1,1,1,1,1,1,1]
dic=dict(i6928820071755=0,i6933811788338=1,i6921168509256=2,i9787208061644=3,i9787302275497=4,i6920487503808=5,i9787506366649=6,i6902088113143=7)

cap=cv2.VideoCapture(0)

def play1():
    mixer.init()
    mixer.music.load('iphone.mp3')
    mixer.music.play()
def play():
    mixer.init()
    mixer.music.load('11750.mp3')
    mixer.music.play()

def normal(i):
    d=(isbn[i],name[i],price[i],number[i],datetime.now().strftime('%Y-%m-%d %H:%M'))
    return d
def normal_loacl(i):
    d=(name[i],price[i],number[i])
    return d
def member(i):
    d=(isbn[i],name[i],0.95*price[i],number[i],datetime.now().strftime('%Y-%m-%d %H:%M'))
    return d
def member_loacl(i):
    d=(name[i],round(0.95*price[i],2),number[i])
    return d
def note(i):
    d=name[i]+'—'+str(number[i])+'—'+str(round(0.95*price[i],2))+'元\n'
    return d
def HA_send(i):
    d=[name[i],str(number[i])]
    return d
def mq(bill_HA):
    m=''
    for i in bill_HA:
        m = m+i+','
    return m

def message(x):
    account_sid = "ACa349b9fa5e92483e512cb6f9ca284134"
    auth_token  = "c8e6f0c54286167e12fc62b094d1c47b"
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="+8618217148825", 
        from_="+12058528426",
        body=x)
    print(x)
    print(type(x))
def decodeDisplay(imagex1):
    gray = cv2.cvtColor(imagex1, cv2.COLOR_BGR2GRAY)
    barcodes = pyzbar.decode(gray)
    global barcodeData
    global ii
    global bill,bill_HA,bill_note,sign_up_pay
    global judge
    global pay
    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(imagex1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        #更换为：
        img_PIL = Image.fromarray(cv2.cvtColor(imagex1, cv2.COLOR_BGR2RGB))        
        imagex1 = cv2.cvtColor(numpy.asarray(img_PIL), cv2.COLOR_RGB2BGR)
        print(barcodeData)
        print(type(barcodeData))
        
        if barcodeData=='莉俶ｬｾ' or barcodeData=='蜿冶ｴｧ':
         #   play1()
            break
        elif len(barcodeData)>2 and judge==0:
            play()
            ii+=1
            a=dic.get('i'+barcodeData)
            bill+=[normal(a)]
            bill_HA+=HA_send(a)
            pay+=price[a]
            bill_note+=(note(a))
            tkinter.Label(sign_up_pay, text=('总额:'+str(round(pay,1))), font=('黑体', 15),bg='white').place(x=379, y=617)
            print(bill)
            insert(normal_loacl(a))
            time.sleep(1)
        elif len(barcodeData)>2 and judge==1:
            play()
            ii+=1
            a=dic.get('i'+barcodeData)
            bill+=[member(a)]
            bill_HA+=HA_send(a)
            pay+=round(0.95*price[a],2)
            bill_note+=note(a)
            tkinter.Label(sign_up_pay, text=('总额:'+str(round(pay,1))), font=('黑体', 15),bg='white').place(x=373, y=617)
            print(mq(bill_HA))
            print('------')
            insert(member_loacl(a))
            time.sleep(1)
    cv2.imshow("camera", imagex1)
def insert(x):
    print('aa')
    print(x)
    print('aa')
    global tree
    tree.insert('',0,values=(x))
def detect():
    cv2.namedWindow("camera",cv2.WINDOW_NORMAL)
    camera = cv2.VideoCapture(0)
    global barcodeData
    global bill,bill_HA,bill_note
    global ii,pay
    bill=[]
    ii=0
    bill_HA=[]
    barcodeData=0
    pay=0
    bill_note='\n'
    while True:
        ret, frame = camera.read()
        #print(ret.shape)
        decodeDisplay(frame)
        if(cv2.waitKey(5)==27):
            break
        elif barcodeData=='莉俶ｬｾ':
            play1()
            #bill_note+=('总额'+str(round((pay),2))+'元')
            time=datetime.now().strftime('%Y-%m-%d %H:%M')
            bill_note='亲爱的顾客：\n        本次到店消费总额'+str(round((pay),2))+'元，祝您生活愉快。\n'+str(time)
            print(bill_note)
            print(type(bill_note))
            info(ii)
            def finish():
                sign_up_finish= tkinter.Toplevel(top)
                global sign_up_count,w6,h6,background_image6,aaa
                #sign_up_finish = tkinter.Toplevel(top)
                sign_up_finish.geometry('%dx%d+526+0' % (w6,h6))
                background_label = tkinter.Label(sign_up_finish, image=background_image6)
                background_label.place(x=0, y=0, relwidth=1, relheight=1)
                tkinter.Label(sign_up_finish, text='成支\n功付' ,font=('隶书', 32),bg='lavenderblush').place(x=217, y=200)
                aaa=('本次消费'+str(round((pay),1))+'元')
                tkinter.Label(sign_up_finish, text=(aaa) ,font=('隶书', 18),bg='lavenderblush').place(x=187, y=430)
                tkinter.Label(sign_up_finish, text=('消费满100元，可免费停车2小时') ,font=('隶书', 18),bg='lavenderblush').place(x=95, y=460)
            finish()
            def bye():
                global aaa
                speaker.Speak((aaa+',祝您生活愉快'))
            Thread(target=bye).start()
            mqtt.PUB(topic,mq(bill_HA))
          #  message(bill_note)
            print(len(bill_note))
            break
        elif barcodeData=='蜿冶ｴｧ':
            global sign_up_out
            def bye_out():
                speaker.Speak('这是你的外卖,路上注意安全')
            Thread(target=bye_out).start()
            tkinter.Label(sign_up_out, text='成取\n功货' ,font=('隶书', 32),bg='lavenderblush').place(x=217, y=200)
            play1()
            break
    camera.release()
    cv2.destroyAllWindows()
def finish():
    sign_up_finish= tkinter.Toplevel(top)
    global sign_up_count,w6,h6,background_image6
    #sign_up_finish = tkinter.Toplevel(top)
    sign_up_finish.geometry('%dx%d+0+0' % (w6,h6))
    background_label = tkinter.Label(sign_up_finish, image=background_image6)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    tkinter.Label(sign_up_finish, text='出示付款码即可付款  折扣95%' ,font=('黑体', 16),bg='white').place(x=47, y=617)

        
def info(i):
    global bill
    conn = pymysql.connect('localhost', 'root', '', '无人超市')
    cursor = conn.cursor()
    sql = "INSERT INTO 收银(ISBN,商品名,价格,数量,时间) VALUES (%s,%s,%s,%s,%s)"
    try:
        for x in range(0,i):
            print(x)
            cursor.execute(sql,bill[x])
        print('done')
        conn.commit()
    except:
        conn.rollback()
        conn.close()
def info_count():
    conn = pymysql.connect('localhost', 'root', '', '无人超市')
    cursor = conn.cursor()
    sql = 'SELECT * FROM 收银'
    global results
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            id = row[0]
            name = row[1]
            age = row[2]
            address = row[3]
            create_time = row[4]
    except:
        conn.rollback()
        conn.close()

def local():
    global sign_up_pay
    global tree
    style = ttk.Style()
    style.configure("Treeview",font=(None, 12,'bold'))
    style.configure("Treeview.Heading",font=('楷体', 13))
    columns = ('商品名','价格','数量')
    tree = ttk.Treeview(sign_up_pay,show = "headings",columns = columns)
    tree.column("商品名",width=160,anchor='center')
    tree.column("价格",width=40,anchor='center')
    tree.column("数量",width=20,anchor='center')
    tree.heading("商品名",text="商品名")
    tree.heading("价格",text="价格")
    tree.heading("数量",text="数量")
    tree.pack(expand='y',ipadx=105,ipady=109)
    tree.quit

def local_count():
    global sign_up_count
    global tree_count,results
    count=0
    info_count()
    style = ttk.Style()
    style.configure("Treeview",font=(None, 10))
    style.configure("Treeview.Heading",font=(None, 12,'bold'))
    columns = ('ISBN','商品名','价格','数量','消费时间')
    tree_count = ttk.Treeview(sign_up_count, show = "headings", columns = columns)
    tree_count.column("ISBN",width=90)
    tree_count.column("商品名",width=120)
    tree_count.column("价格",width=50,anchor='center')
    tree_count.column("数量",width=25,anchor='center')
    tree_count.column("消费时间",width=100)
    tree_count.heading("ISBN",text="ISBN")
    tree_count.heading("商品名",text="商品名")
    tree_count.heading("价格",text="价格")
    tree_count.heading("数量",text="数量")
    tree_count.heading("消费时间",text="消费时间")
    for row in results:
        a = row[0]
        b = row[1]
        c = row[2]
        d = row[3]
        e = row[4]
        count+=c
        tree_count.insert('',0,values=(a,b,c,d,e))
    time=datetime.now().strftime('%m-%d %H:%M')
    tkinter.Label(sign_up_count, text=('销售总额：'+str(round(count,2))+'元' ),font=('黑体', 17),bg='white').place(x=18, y=637)
    tkinter.Label(sign_up_count, text=('更新时间：'+str(time)) ,font=('黑体', 17),bg='white').place(x=18, y=666)

    print(count)
    print('cccc')
    tree_count.pack(expand='y',ipadx=57,ipady=129)
    tree_count.quit
def enter():
    global sign_up_pay,w1,h1,background_image1
    sign_up_pay = tkinter.Toplevel(top)
    sign_up_pay.geometry('%dx%d+0+0' % (w1,h1))
    background_label = tkinter.Label(sign_up_pay, image=background_image1)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    tkinter.Label(sign_up_pay, text='出示付款码即可付款  折扣95%' ,font=('黑体', 16),bg='white').place(x=47, y=617)

    local()
    global judge
    judge=1
    Thread(target=detect).start()

def feedback():
    sign_up = tkinter.Toplevel(top)  
    global w0,h0,background_image0,ww,hh,background_imagee,w3,h3,background_image3,over
    over=0
    image0 =Image.open('logo1.gif')
    background_image0 = ImageTk.PhotoImage(image0)
    w0 = background_image0.width()
    h0 = background_image0.height() 
    def no():
        global judge,sign_up_pay,w0,h0,background_image0
        sign_up_pay = tkinter.Toplevel(top)
        sign_up_pay.geometry('%dx%d+0+0' % (w0,h0))
        background_labe0 = tkinter.Label(sign_up_pay, image=background_image0)
        background_labe0.place(x=0, y=0, relwidth=1, relheight=1)
        tkinter.Label(sign_up_pay, text='出示付款码即可付款' ,font=('黑体', 16),bg='white').place(x=47, y=617)
        local()
        judge=0
        Thread(target=detect).start()
       # finish()
    def yes():
        sign_up = tkinter.Toplevel(top)
        global w3,h3,background_image3
        sign_up.geometry('%dx%d+0+0' % (w3,h3))
        background_label3 = tkinter.Label(sign_up, image=background_image3)
        background_label3.place(x=0, y=0, relwidth=1, relheight=1)
        var_usr_name = tkinter.StringVar()
        entry_usr_name = tkinter.Entry(sign_up, textvariable=var_usr_name, font=('Arial', 18),width=13)
        entry_usr_name.place(x=172,y=410)
        tkinter.Label(sign_up, text='请输入会员号' ,font=('隶书', 20),bg='white',fg='darkgoldenrod').place(x=165, y=350)
        def login():                 
            if entry_usr_name.get()=='18217148825':
                enter()
      #  login = tkinter.Button(sign_up, text='确定',font=('Times', 20,'bold'), command=login)
        login = tkinter.Button(sign_up, text='确定',font=('楷体', 23,'bold'),bg='orange',fg='white', command=login)
        login.place(x=210, y=510)
    print('我在这里')
    sign_up.geometry('%dx%d+0+0' % (ww,hh))
    background_labell = tkinter.Label(sign_up, image=background_imagee)
    background_labell.place(x=0, y=0, relwidth=1, relheight=1)
    login = tkinter.Button(sign_up, text='会员用户',font=('楷体', 23,'bold'),bg='orange',fg='white', command=yes)
    login.place(x=180, y=350)
    login = tkinter.Button(sign_up, text='普通用户',font=('楷体', 23,'bold'),bg='orange',fg='white', command=no)
    login.place(x=180, y=470)
    tkinter.Label(sign_up, text='会员用户享9.5折优惠！' ,font=('隶书', 19),bg='white',fg='red').place(x=133, y=570)
    if over==1:
        finish()
def admin():
    login=tkinter.Toplevel(top)
    global w3,h3,background_image3
    login.geometry('%dx%d+0+0' % (w3,h3))
    background_label3 = tkinter.Label(login, image=background_image3)
    background_label3.place(x=0, y=0, relwidth=1, relheight=1)
    var_usr_name = tkinter.StringVar()
    
##    canvas=tkinter.Canvas(login)
##    imagefile=tkinter.PhotoImage(file='logo.gif')
##    image=canvas.create_image(0,0,anchor='nw',image=imagefile)
##    canvas.pack(side='top')
    password = StringVar()
    name = tkinter.Entry(login, font=('Times', 18,'bold'),width=12)
    name.place(x=200,y=385)
    password = StringVar()
    e = tkinter.Entry(login,font=('Times', 18,'bold'), width=12,textvariable=password, show='*')
    e.place(x=200,y=460)
    tkinter.Label(login, text='用户名:' ,font=('黑体', 17),bg='white',fg='olive').place(x=105, y=385)
    tkinter.Label(login, text='密码:' ,font=('黑体', 17),bg='white',fg='olive').place(x=128, y=460)

    def yes():
        if e.get()=='11111111'and name.get()=='caojiayang':     
            global sign_up_count,w1,h1,background_image1
            sign_up_count = tkinter.Toplevel(top)
            sign_up_count.geometry('%dx%d+0+0' % (w1,h1))
            background_label = tkinter.Label(sign_up_count, image=background_image1)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)
            tkinter.Label(sign_up_count, text='收银记录:' ,font=('黑体', 18),bg='white').place(x=20, y=123)
            local_count()
    login = tkinter.Button(login, text='登陆',font=('楷体', 21,'bold'),bg='orange',fg='white', command=yes)
    login.place(x=225, y=530)
def take_out():
    global w6,h6,background_image6,sign_up_out
    sign_up_out= tkinter.Toplevel(top)
    sign_up_out.geometry('%dx%d+522+0' % (w6,h6))
    background_label = tkinter.Label(sign_up_out, image=background_image6)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    tkinter.Label(sign_up_out, text=('请出示外卖平台取货码') ,font=('隶书', 18),bg='lavenderblush').place(x=140, y=460)
    def bye_out():
        speaker.Speak('请出示取货码')
    Thread(target=bye_out).start()
    Thread(target=detect).start()
top = tkinter.Tk()
top.title('自助收银机')
global ww,hh,background_imagee,w3,h3,background_image3,w1,h1,background_image1,w6,h6,background_image6
image6 =Image.open('logo6.gif')
background_image6 = ImageTk.PhotoImage(image6)
w6 = background_image6.width()
h6 = background_image6.height()
image1 =Image.open('logo1.gif')
background_image1 = ImageTk.PhotoImage(image1)
w1 = background_image1.width()
h1 = background_image1.height()
image3 =Image.open('logo3.gif')
background_image3 = ImageTk.PhotoImage(image3)
w3 = background_image3.width()
h3 = background_image3.height()
imagee =image3
background_imagee = background_image3
ww = w3
hh = h3
image =Image.open('logo5.gif')
background_image = ImageTk.PhotoImage(image)
w = background_image.width()
h = background_image.height()
top.geometry('%dx%d+0+0' % (w,h))
background_label = Label(top, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
tkinter.Label(top, text='欢迎使用\n多功能收银机' ,font=('隶书', 26),bg='whitesmoke',fg='darkgoldenrod').place(x=150, y=210)
btn_login = tkinter.Button(top, text='自助收银',font=('楷体', 23,'bold'),bg='lightslategray',fg='white',cursor='clock',command=feedback)
btn_login.place(x=180, y=340)
btn_login = tkinter.Button(top, text='我是骑手',font=('楷体', 23,'bold'),bg='tomato',fg='white',command=take_out)
btn_login.place(x=180, y=440)
btn_login = tkinter.Button(top, text='我是员工',font=('楷体', 23,'bold'),bg='darkorange',fg='white',command=admin)
btn_login.place(x=180, y=540)
def welcome():
    speaker.Speak('欢迎使用多功能收银机')
Thread(target=welcome).start()
top.mainloop()
