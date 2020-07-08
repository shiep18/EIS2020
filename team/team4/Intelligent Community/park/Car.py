import os
import threading
from hyperlpr import *
import re
import cv2
from aip import AipSpeech
from mutagen.mp3 import MP3
from playsound import playsound
from park import licenseplate
import time
from mcpi.minecraft import Minecraft

#变量定义与初始化，直接复制使用
mc=Minecraft.create("47.100.46.95",4784)
entityId= mc.getPlayerEntityId("W")
#Capture = cv2.VideoCapture(0)
CarMatchObj=re.compile(r'^[京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼使领A-Z]{1}[A-Z]{1}[A-Z0-9]{4}[A-Z0-9挂学警港澳]{1}$')
PLATE=""
NormalPark=[]
PersonalPark=[]

#整理
def NorMass(L):
    N=[0 for _ in range(1,10)]
    for i in L:
        if i!=0:
            N[i-1]= i
    return N
#根据给定字符串合成语音
def Str2Sound(yuyin):
    APP_ID = '17980615'
    API_KEY = 'pIQlVZYLO4aPDLM55GGMGe5L'
    SECRET_KEY = '0Pba78PqkEch32ozc4IbvMFmjN7kaejw'

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    result = client.synthesis(yuyin, 'zh', 1, {'vol': 5, })

    if not isinstance(result, dict):
        with open('auido.mp3', 'wb') as f:
            f.write(result)

    playsound("auido.mp3")
#延时函数:调用时给定坐标
def detectpos(x,y,z):
    pos=mc.entity.getTilePos(entityId)
    if pos.x==x and pos.y==y and pos.z==z:
        for i in range(5):
            mc.postToChat(str(i+1))
            time.sleep(1)
        pos=mc.entity.getTilePos(entityId)
        if pos.x==x and pos.y==y and pos.z==z:
            return 1
        else:
            return 0
#扫描车牌并执行进场操作：私家车位返回1，外来车返回0，并且将外来车车牌导入数据库
def CarPlateIn():
    global PLATE
    car=0
    Capture = cv2.VideoCapture(0)
    while True:
        ret,frame = Capture.read()
        cv2.imshow('Video',frame)
        a=HyperLPR_PlateRecogntion(frame)
        a=str(a)
        if a!='[]':
            Plate = str(a[3:10])
            if CarMatchObj.match(Plate):
                p=licenseplate.user_info(Plate)
                if p is not None:
                    car=1   #住户
                else:
                    info, i, state=licenseplate.car_num()
                    if Plate in info:
                        p=1
                        PLATE=Plate
                    else:
                        p=0
                break
        #请勿删除！否则会出现摄像头无法打开的情况！
        if cv2.waitKey(1) &0xFF==ord("q"):
            break
    if car==0 and p==0:
        Str2Sound("非法侵入车辆。请迅速去小区门口登记")
    else:
        Str2Sound("欢迎光临，" + Plate)
    Init()
    cv2.destroyAllWindows()
    Capture.release()
    return car,p
#扫描车牌并执行出场操作：将外来车车牌在数据库内删除
def CarPlateOut():
    car=0
    Capture = cv2.VideoCapture(0)
    while True:
        ret,frame = Capture.read()
        cv2.imshow('Video',frame)
        a=HyperLPR_PlateRecogntion(frame)
        a=str(a)
        if a!='[]':
            Plate = str(a[3:10])
            if CarMatchObj.match(Plate):
                p=licenseplate.user_info(Plate)
                if p is not None:
                    pass
                else:
                    print(licenseplate.car_num())
                    licenseplate.Park_add(0,Plate)
                    print(licenseplate.car_num())
                break
        if cv2.waitKey(1) &0xFF==ord("q"):
            break
    Str2Sound(Plate + "，一路顺风")
    Init()
    cv2.destroyAllWindows()
    Capture.release()
#铁柱 车位，材质
def Iron(num,p):#42
    for i in range(1296-(num-1)*7,1302-(num-1)*7):
        for k in range(4,6):
            mc.setBlock(i,k,1200,p)
#铁栏杆
def Railing(num,p):#101
    Num=1234
    if num%2==0:
        Num=1239
    for i in range(5):
        if num<=2*i:
            num=i
            break
    for i in range(1305-num*6,1308-num*6):
            mc.setBlock(i,4,Num,p)
# 初始化
def Init():
    global PersonalPark, NormalPark
    PersonalPark,iron = licenseplate.car_Per()
    info, i, nor = licenseplate.car_num()
    for i in range(0,9):
        if i<len(nor):
            NormalPark.append(int(nor[i]))
        else:
            NormalPark.append(0)
    NormalPark=NorMass(NormalPark)
    n=0

    for i in iron:
        if PersonalPark[n] == '0':
            Iron(int(i),42)
        else:
            Iron(int(i),0)
        n += 1
    for i in range(1,len(NormalPark)+1):
        if NormalPark[i-1]!=0:
            Railing(int(i),0)
        else:
            Railing(int(i),101)

#私家车操作
def PersonalCarSet(P):
    global PersonalPark,Per
    print(P)
    p=int(P[2])
    Iron(p,0)
    while True:
        pos=mc.entity.getTilePos(entityId)
        if pos.x == (1305-7*p) and pos.y == 4 and pos.z == 1197 and PersonalPark[p-1] == '0':
            if detectpos((1305-7*p), 4, 1197):
                mc.postToChat('The Car is Setted')  
                licenseplate.Per_update(1,P[2])
                break
    while True:
        pos = mc.entity.getTilePos(entityId)
        if pos.z>1200:
            Per=1
            mc.postToChat('The People is Left')
            break
    Init()

def PersonalCarGet():
    print("PersonalCarGet() is Running")
    global num,Per
    num=0
    T=False
    while True:
        pos = mc.entity.getTilePos(entityId)
        for p in range(1,4):
            if pos.x == (1306 - 7 * p) and pos.y == 4 and pos.z == 1196 and PersonalPark[p-1] == '1':
                print(p)
                if detectpos((1306 - 7 * p), 4, 1196) and PersonalPark[p-1] == '1':
                    mc.postToChat('The Car is Getted')
                    
                    PersonalPark[p - 1] = 0
                    licenseplate.Per_update(0, p)
                    print(PersonalPark)
                    num=p
                    T=True
                    break
        if T:
            break



    while True:
        pos = mc.entity.getTilePos(entityId)
        if pos.z>1200:
            Iron(num,42)
            mc.postToChat('The Car is Left')
            Per = 0
            break

    Init()

#大众车操作
def NormalCarSet(num):
    global NormalPark,PLATE,Nor
    Num=0
    if num <= 8:
        Str2Sound("请到序号为"+str(num)+"的车位停车" )
        licenseplate.Park_add(num,PLATE)
        Railing(num,0)
        for i in range(5):
            if num <= 2*i:
                Num=i
                break
        while True:
            pos=mc.entity.getTilePos(entityId)
            if pos.x == (1306-6*Num) and pos.y == 4 and (pos.z == 1232 or pos.z == 1241):
                if num%2 == 0:
                    if detectpos((1306 - 6 * Num), 4, 1241):
                        mc.postToChat('The Car is Setted')
                        NormalPark[num - 1] = 1
                        print(NormalPark)
                        break
                else:
                    if detectpos((1306 - 6 * Num), 4, 1232):
                        mc.postToChat('The Car is Setted')
                        NormalPark[num - 1] = 1
                        print(NormalPark)
                        break
        while True:
            pos = mc.entity.getTilePos(entityId)
            if 1234 < pos.z<1239:
                Nor=1
                print(Nor)
                mc.postToChat('The People is Left')
                break
    else:
        Str2Sound("车位已满，十分抱歉")
    Init()

def NormalCarGet():
    print("NormalCarGet() is Running")
    global NormalPark
    num = 0
    T = False
    while True:
        pos = mc.entity.getTilePos(entityId)
        for num in range(1,9):
            for i in range(5):
                if num <= 2 * i:
                    Num = i
                    break
            if pos.x == (1306-6*Num) and pos.y == 4 and (pos.z == 1230 or pos.z == 1243) and NormalPark[num-1] != 0:
                if num%2 == 0:
                    if detectpos((1306 - 6 * Num), 4, 1243):
                        mc.postToChat('The Car is Getted')
                        NormalPark[num - 1] = 0
                        T = True
                        print(NormalPark)
                        break
                else:
                    if detectpos((1306 - 6 * Num), 4, 1230):
                        mc.postToChat('The Car is Getted')
                        NormalPark[num - 1] = 0
                        T=True
                        print(NormalPark)
                        break
        if T:
            break
    NormalPark[num-1]=0
    print(num)
    while True:
        pos = mc.entity.getTilePos(entityId)
        if 1234 < pos.z<1239:
            Railing(num,101)
            mc.postToChat('The Car is Left')
            Nor = 0
            break

#线程一：监视与停车
def Thread_1():
    print("Thread_1 is Running......")
    global PersonalPark,NormalPark
    while True:
        pos = mc.entity.getTilePos(entityId)
        if pos.x == 1306 and pos.y == 4 and pos.z == 1223:
            if detectpos(1306,4,1223):
                car,p = CarPlateIn()
                print(p)
                if car == 1 and PersonalPark[int(p[2])-1] == '0':
                    PersonalCarSet(p)
                elif car == 0 and p==1:
                    for num in range(len(NormalPark)):
                        if NormalPark[num] == 0:
                            NormalCarSet(num+1)
                            break
        elif pos.x == 1302 and pos.y == 4 and pos.z == 1223:
            if detectpos(1302, 4, 1223):
                CarPlateOut()

#线程二：取车一
def Thread_2():
    global Per
    print("Thread_2 is Running......")
    while True:
        PersonalCarGet()
#线程三：取车二
def Thread_3():
    print("Thread_3 is Running......")
    global Nor
    while True:
        NormalCarGet()

def main():
    Init()
    thread_1=threading.Thread(target=Thread_1,name='C1')
    thread_1.start()
    thread_2 = threading.Thread(target=Thread_2,name='C2')
    thread_2.start()
    thread_3 = threading.Thread(target=Thread_3,name='C3')
    thread_3.start()


if __name__ == "__main__":
    main()


