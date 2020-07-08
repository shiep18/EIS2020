import cv2
#import os module for reading training data directories and paths
import os
#import numpy to convert python lists to numpy arrays as 
#it is needed by OpenCV face recognizers
import numpy as np
from mcpi.minecraft import Minecraft
import mcpi.block as block
import time
import matplotlib.pyplot as plt
import os
from hyperlpr import *
import win32com.client as win
import csv
from aip import AipSpeech
import speech_recognition as sr
import pykeyboard
import asyncio
import threading
from MXMqtt import MXMqtt
import pymysql
conn = pymysql.connect('localhost', 'root', '', 'mysql')
cursor = conn.cursor()

BAIDU_APP_ID = '19165943'
BAIDU_API_KEY = 'YZvt651qpTG8Sm0MmocMW9oz'
BAIDU_SECRET_KEY = 'GD5y6RcPciVdp05S6TWT9YHaQv3YGpbb'
aip_speech = AipSpeech(BAIDU_APP_ID, BAIDU_API_KEY, BAIDU_SECRET_KEY)
r = sr.Recognizer()
mic = sr.Microphone(sample_rate=16000)

subjects = ["", "Yang", "Beckham" ]

mc = Minecraft.create("47.100.46.95",4782)
entityId = mc.getPlayerEntityId("sjc")
pos = mc.entity.getTilePos(entityId)


MQTTHOST = "mqtt.16302.com"
MQTTPORT = 1883
mqtt = MXMqtt(MQTTHOST,MQTTPORT)

gesture_topics = ["EIS1-test","EIS2-test","EIS3-test","EIS4-test","EIS5-test"]

acts0 = ['0','0','0','0','0']
acts2 = ['0','0','1','1','0']
acts6 = ['1','0','0','0','1']
acts5 = ['1','1','1','1','1']

def gesture_control(acts):
    for topic ,act in zip(gesture_topics,acts):
        mqtt.PUB(topic, act)
        

def csv_read(name):
    with open (name, 'r') as f:
        reader = csv.reader(f)
        result = list(reader)
    return result

members = ['gyy','lsy','lxj','sjc','syf','zxs']
name_list = csv_read('./team2_clan.csv')
pos_dic = {}
for name in name_list:
    pos_dic[name[0]] = tuple(map(eval,name[1:]))

L = 10
W = 10
H = 6

areas = {}

for myname in members:
    posx = pos_dic[myname][0] + pos_dic['clancenter'][0]
    posy = pos_dic[myname][1] + pos_dic['clancenter'][1]
    posz = pos_dic[myname][2] + pos_dic['clancenter'][2]
    area = (posx,posx+L,posy,posy+H,posz,posz+W)
    areas[myname] = area
    
global flag,temp_name
flag = 0
flag1 = 0
temp_name = ""

def yuyin():
    global temp_name
    while True:
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
            if temp_name is not "":  # 在家的时候才触发开关灯
                area = areas[temp_name]
                x = area[0]+L//2
                y = area[2]+H-1
                z = area[4]+W//2
                if "开灯" in result:
                    mc.setBlocks(x,y,z,x,y,z+2,169)
                if "关灯" in result:
                    mc.setBlocks(x,y,z,x,y,z+2,0)
                if "打开空调" in result:
                    mc.setBlocks(x+3,y,z-3,x+3,y,z-1,0)
                    speak = win.Dispatch("SAPI.SpVoice")
                    speak.Speak("空调已打开，当前温度26℃")
                    sql = "UPDATE `mysql`.`house` SET `air-conditioner_state` = 'ON' WHERE `house`.`house` = '%s'"%temp_name
                    try:
                        cursor.execute(sql)
                        conn.commit()
                    except:
                        conn.rollback()
                        conn.close()
                    gesture_control(acts2)
                    time.sleep(1)
                    gesture_control(acts6)
                if "关闭空调" in result:
                    sql = "UPDATE `mysql`.`house` SET `air-conditioner_state` = 'OFF' WHERE `house`.`house` = '%s'"%temp_name
                    try:
                        cursor.execute(sql)
                        conn.commit()
                    except:
                        conn.rollback()
                        conn.close()
                    mc.setBlocks(x+3,y,z-3,x+3,y,z-1,102)
                    speak = win.Dispatch("SAPI.SpVoice")
                    speak.Speak("空调已关闭")
            if "结束" in result:
                print("感谢您的使用")
                break

def welcome(x,y,z):
    global flag,temp_name
    if flag == 0:
        for name,area in areas.items():
            if area[0]<=x<=area[1] and area[2]<=y<=area[3] and area[4]<=z<=area[5] :
                mc.postToChat(f"Welcome to {name}'s home")
                flag = 1
                temp_name = name

    else:
        area = areas[temp_name]
        if area[0]<=x<=area[1] and area[2]<=y<=area[3] and area[4]<=z<=area[5]:
            pass
        else :
            flag = 0
            temp_name = ""

def welcome1(x,y,z):
    entityId = mc.getPlayerEntityId("sjc")
    pos = mc.entity.getTilePos(entityId)
    global flag1
    if flag1 == 0:
        if 89<=pos.x<=95 and pos.y==-21 and pos.z==101:
            mc.postToChat("Welcome to team2's village ！")
            #gesture_control(acts5)
            #time.sleep(1)
            #gesture_control(acts0)
            #time.sleep(1)
            #gesture_control(acts5)
            #time.sleep(1)
            #gesture_control(acts0)
            flag1 = 1
    else:
        if 89<=pos.x<=95 and pos.y==-21 and pos.z==102:
            mc.postToChat("Wish you a good journey ！")
            #gesture_control(acts5)
            #time.sleep(1)
            #gesture_control(acts0)
            #time.sleep(1)
            #gesture_control(acts5)
            #time.sleep(1)
            #gesture_control(acts0)
            flag1 = 0

def door1(x1,y1,z1,L,act):
    if act:
        m = block.AIR.id
    else:
        m = block.GLASS.id
    mc.setBlock(x1+5,y1+1,z1,m)
    mc.setBlock(x1+5,y1+2,z1,m)

x1,y1,z1,L,W,H,M = (58,-21,83,10,10,6,5)

def door2(x2,y2,z2,L,act):
    if act:
        m = block.AIR.id
    else:
        m = block.GLASS.id
    mc.setBlock(x2+5,y2+1,z2,m)
    mc.setBlock(x2+5,y2+2,z2,m)

x2,y2,z2,L,W,H,M = (58,-21,68,10,10,6,5)

def door3(x3,y3,z3,L,act):
    if act:
        m = block.AIR.id
    else:
        m = block.GLASS.id
    mc.setBlock(x3+5,y3+1,z3,m)
    mc.setBlock(x3+5,y3+2,z3,m)

x3,y3,z3,L,W,H,M = (58,-21,53,10,10,6,5)
    
def door4(x4,y4,z4,L,act):
    if act:
        m = block.AIR.id
    else:
        m = block.GLASS.id
    mc.setBlock(x4+5,y4+1,z4,m)
    mc.setBlock(x4+5,y4+2,z4,m)

x4,y4,z4,L,W,H,M = (87,-21,53,10,10,6,5)

def door5(x5,y5,z5,L,act):
    if act:
        m = block.AIR.id
    else:
        m = block.GLASS.id
    mc.setBlock(x5+5,y5+1,z5,m)
    mc.setBlock(x5+5,y5+2,z5,m)

x5,y5,z5,L,W,H,M = (87,-21,68,10,10,6,5)

def door6(x6,y6,z6,L,act):
    if act:
        m = block.AIR.id
    else:
        m = block.GLASS.id
    mc.setBlock(x6+5,y6+1,z6,m)
    mc.setBlock(x6+5,y6+2,z6,m)

x6,y6,z6,L,W,H,M = (87,-21,83,10,10,6,5)

def detect_face(img):
    #convert the test image to gray image as opencv face detector expects gray images
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #load OpenCV face detector, I am using LBP which is fast
    #there is also a more accurate but slow Haar classifier
    face_cascade = cv2.CascadeClassifier('opencv-files/lbpcascade_frontalface.xml')

    #let's detect multiscale (some images may be closer to camera than others) images
    #result is a list of faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);
    
    #if no faces are detected then return original img
    if (len(faces) == 0):
        return None, None
    
    #under the assumption that there will be only one face,
    #extract the face area
    (x, y, w, h) = faces[0]
    
    #return only the face part of the image
    return gray[y:y+w, x:x+h], faces[0]


face_recognizer  = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('Training.yml')

#function to draw rectangle on image 
#according to given (x, y) coordinates and 
#given width and heigh
def draw_rectangle(img, rect):
    (x, y, w, h) = rect
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
#function to draw text on give image starting from
#passed (x, y) coordinates. 
def draw_text(img, text, x, y):
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)


# First function `draw_rectangle` draws a rectangle on image based on passed rectangle coordinates. It uses OpenCV's built in function `cv2.rectangle(img, topLeftPoint, bottomRightPoint, rgbColor, lineWidth)` to draw rectangle. We will use it to draw a rectangle around the face detected in test image.
# 
# Second function `draw_text` uses OpenCV's built in function `cv2.putText(img, text, startPoint, font, fontSize, rgbColor, lineWidth)` to draw text on image. 
# 
# Now that we have the drawing functions, we just need to call the face recognizer's `predict(face)` method to test our face recognizer on test images. Following function does the prediction for us.

# In[9]:

#this function recognizes the person in image passed
#and draws a rectangle around detected face with name of the 
#subject
def predict(test_img):
    #make a copy of the image as we don't want to chang original image
    img = test_img.copy()
    #detect face from the image
    face, rect = detect_face(img)
    label_text = ""
    try :
        # cv2.imshow("face",face)
        # cv2.waitKey(1000)
        # cv2.destroyAllWindows()
        cv2.imwrite("face.jpg",face)
        #predict the image using our face recognizer 
        label, confidence = face_recognizer.predict(face)
        print("label,confidence",label,confidence)
        #get name of respective label returned by face recognizer
        label_text = subjects[label]
        
        #draw a rectangle around face detected
        draw_rectangle(img, rect)
        #draw name of predicted person
        draw_text(img, label_text, rect[0], rect[1]-5)
    except :
        pass
    return img,label_text

# Now that we have the prediction function well defined, next step is to actually call this function on our test images and display those test images to see if our face recognizer correctly recognized them. So let's do it. This is what we have been waiting for. 

cap = cv2.VideoCapture(0)

# In[10]:
def main():
    while True :
        entityId = mc.getPlayerEntityId("sjc")
        pos = mc.entity.getTilePos(entityId)
    
        welcome(pos.x,pos.y,pos.z)
        
        welcome1(pos.x,pos.y,pos.z)
        
        # yuyin()
        
        ret, img = cap.read()
        test_img1 = img
    
        predicted_img1,sub = predict(test_img1)

        act1 = 0
        act2 = 0
        act3 = 0
        act4 = 0
        act5 = 0
        act6 = 0

        #display both images
        cv2.imshow("camera", cv2.resize(predicted_img1, (400, 500)))
        
        if pos.x == 180 and pos.y == -21 and pos.z == 220:
            a=HyperLPR_PlateRecogntion(img)
            a = str(a)
            if a[3:5] != "":
                if a[3:5] == "沪A" and a[5:10] == "88888":
                    pass
                else:
                    speak = win.Dispatch("SAPI.SpVoice")
                    speak.Speak("欢迎" + a[3:5] + a[5:10])
                for i in range(1,9):
                    mc.setBlock(183,-20,224-i,0)
                    mc.setBlock(183,-21,224-i,0)
                    time.sleep(1)
                time.sleep(5)   
                for i in range(1,9):
                    mc.setBlock(183,-20,224-9+i,101)
                    mc.setBlock(183,-21,224-9+i,101)
                    time.sleep(1)
                a[3:5] == ""
        if pos.x == 185 and pos.y==-21 and pos.z == 198:
            a = HyperLPR_PlateRecogntion(img)
            a = str(a)
            if a[3:5] != "":
                if a[3:5] == "沪A" and a[5:10] == "88888":
                    pass
                else:
                    speak = win.Dispatch("SAPI.SpVoice")
                    speak.Speak("再见"+a[3:5]+a[5:10])
                for i in range(1,9):
                    mc.setBlock(183,-20,194+i,0)
                    mc.setBlock(183,-21,194+i,0)
                    time.sleep(1)
                time.sleep(5)
                for i in range(1,9):
                    mc.setBlock(183,-20,194+9-i,101)
                    mc.setBlock(183,-21,194+9-i,101)
                    time.sleep(1)
                a[3:5] == ""

        if sub in [ "Beckham" ]:
            if pos.x == 92 and -21<=pos.y<=-20 and 51<=pos.z<=54:
                act4 = 1  
            elif pos.x == 92 and -21<=pos.y<=-20 and 66<=pos.z<=69:
                act5 = 1 
            elif pos.x == 92 and -21<=pos.y<=-20 and 81<=pos.z<=84:
                act6 = 1

        elif sub in [ "Yang" ]:
            if pos.x == 63 and -21<=pos.y<=-20 and 51<=pos.z<=54:
                act3 = 1
            elif pos.x == 63 and -21<=pos.y<=-20 and 66<=pos.z<=69:
                act2 = 1
            elif pos.x == 63 and -21<=pos.y<=-20 and 81<=pos.z<=84:
                act1 = 1

        door1(x1,y1,z1,L,act1)
        door2(x2,y2,z2,L,act2)
        door3(x3,y3,z3,L,act3)
        door4(x4,y4,z4,L,act4)
        door5(x5,y5,z5,L,act5)
        door6(x6,y6,z6,L,act6)

        key = cv2.waitKey(1) & 0xFF
        # 按'q'健退出循环
        if key == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break

if __name__ == "__main__":
    # main()
    threads = []
    
    thread1 = threading.Thread(target=main)
    threads.append(thread1)

    thread2 = threading.Thread(target=yuyin)
    threads.append(thread2)

    for t in threads:
        t.start()
    for t in threads:
        t.join()

