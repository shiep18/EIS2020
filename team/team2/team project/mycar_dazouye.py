import time
import mcpi.minecraft as minecraft
import mcpi.block as block
from pykeyboard import PyKeyboard
import math as m
from pymouse import PyMouse
import pymysql
from aip import AipSpeech
import speech_recognition as sr
import cv2
from MXMqtt import MXMqtt
from mc_control import *
import win32com.client as win


k = PyKeyboard()
mouse = PyMouse()
mc = minecraft.Minecraft.create("47.100.46.95",4782)

BAIDU_APP_ID='19165943'
BAIDU_API_KEY='YZvt651qpTG8Sm0MmocMW9oz'
BAIDU_SECRET_KEY='GD5y6RcPciVdp05S6TWT9YHaQv3YGpbb'
aip_speech = AipSpeech(BAIDU_APP_ID, BAIDU_API_KEY, BAIDU_SECRET_KEY)
r = sr.Recognizer()
mic = sr.Microphone(sample_rate=16000)

button = [[273,195],[273,202],[273,210],[273,219],[258,227],[243.216],[243,204],[258,187]]
roadx = [77,63,92]
roadz = [81,51,66]
houseposition = [[92,97],[63,81],[63,66],[63,51],[92,51],[92,66],[92,81]]

entityId=mc.getPlayerEntityId("sjc")
pos = mc.entity.getTilePos(entityId)
print('x:'+str(pos.x)+'y:'+str(pos.y)+'z:'+str(pos.z))


MQTTHOST = "mqtt.16302.com"
MQTTPORT = 1883
mqtt = MXMqtt(MQTTHOST,MQTTPORT)

topic = "mccar"

def movex(x):
    while True:
        entityId=mc.getPlayerEntityId("sjc")
        pos = mc.entity.getTilePos(entityId)
        
        X = x - pos.x
        k.press_key("w")
        
        
        if X == 0:
            k.release_key("w")
            k.release_key("s")
            break

def movez(z):
    while True:
        entityId=mc.getPlayerEntityId("sjc")
        pos = mc.entity.getTilePos(entityId)

        Z = z - pos.z
        k.press_key("w")
        
        
        if Z == 0:
            k.release_key("w")
            k.release_key("s")
            break
    print('over')

def moveto(x,z):
    entityId=mc.getPlayerEntityId("sjc")
    pos = mc.entity.getTilePos(entityId)


    if pos.x == 63:
        rotate("left")
        movex(77)
        if z - pos.z > 0 :
            rotate("right")
            movez(z)
            if x - pos.x > 0 :
                rotate("left")
                movex(x)
                rotate("right")
            else:
                rotate("right")
                movex(x)
                rotate("left")
        elif z - pos.z == 0:
            movex(x)
            rotate("right")
        else:
            rotate("left")
            movez(z)
            if x - pos.x > 0 :
                rotate("right")
                movex(x)
                rotate("right")
            else:
                rotate("left")
                movex(x)
                rotate("left")
            
    elif pos.x == 92:

        if pos.z > 90:
            rotate("left")
            movex(77)
            rotate("right")
            movez(z)
            if x - pos.x < 0:
                rotate("left")
                movex(x)
                rotate("left")
            else:
                rotate("right")
                movex(x)
                rotate("right")
            
        else:
            rotate("right")
            movex(77)
            if z - pos.z > 0 :
                rotate("left")
                movez(z)
                if x - pos.x < 0 :
                    rotate("right")
                    movex(x)
                    rotate("left")
                else:
                    rotate("left")
                    movex(x)
                    rotate("right")
            elif z - pos.z == 0:
                movex(x)
                rotate("left")
            else:
                rotate("right")
                movez(z)
                if x - pos.x < 0 :
                    rotate("left")
                    movex(x)
                    rotate("left")
                else:
                    rotate("right")
                    movex(x)
                    rotate("right")
            

def rotate(a):
    if a == "left":
        for j in range(50):
            
            time.sleep(0.1)
            mouse.move(770-10, 457)
    if a == "right":
        for j in range(46):
            
            time.sleep(0.1)
            mouse.move(770+10, 457)
    if a == "down":
        for j in range(30):
            
            time.sleep(0.1)
            mouse.move(770, 457+10)
    if a == "on":
        for j in range(30):
            
            time.sleep(0.1)
            mouse.move(770, 457-10)
    

def tans(x,y,angle):
    x1 = x*m.cos(angle) + y*m.sin(angle)
    y1 = (-x)*m.sin(angle) + y*m.cos(angle)
    return [x1,y1]

def schooltohouse():
    mqtt.PUB(topic, "-10,-10")# 前
    #mqtt.PUB("chat" , 0) # 小车前
    movex(92)
    mqtt.PUB(topic, "-10,0")# 右
    #mqtt.PUB("chat" , 2) # 小车右
    rotate("right")
    mqtt.PUB(topic, "-10,-10")# 前
    #mqtt.PUB("chat" , 0) # 小车前
    movez(96)
    mqtt.PUB(topic, "0,0")# 停
    #mqtt.PUB("chat" , 4) # 小车停
def housetoschool():
    mqtt.PUB(topic, "-10,-10")# 前
    mqtt.PUB("chat" , 0) # 小车前
    movez(220)
    mqtt.PUB(topic, "0,-10")# 左
    mqtt.PUB("chat" , 1) # 小车左
    rotate("left")
    mqtt.PUB(topic, "-10,-10")# 前
    #mqtt.PUB("chat" , 0) # 小车前
    movex(180)
    mqtt.PUB(topic, "0,0")# 停
    #mqtt.PUB("chat" , 4) # 小车停

def main():
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
        if "去学校" in result:
            mouse.move(862, 845)
            time.sleep(0.5)
            mouse.click(862, 845, 1)
            time.sleep(0.5)
            mouse.move(770, 390)
            time.sleep(0.5)
            mouse.click(770, 390, 1)
            housetoschool()
            speak = win.Dispatch("SAPI.SpVoice")
            speak.Speak("已到达学校")            

        if "回村庄" in result:
            mouse.move(862, 845)
            time.sleep(0.5)
            mouse.click(862, 845, 1)
            time.sleep(0.5)
            mouse.move(770, 390)
            time.sleep(0.5)
            mouse.click(770, 390, 1)
            schooltohouse()
            speak = win.Dispatch("SAPI.SpVoice")
            speak.Speak("已到达村庄")
           
        if "去一号房" in result:
            moveto(houseposition[1][0],houseposition[1][1])

        if "去二号房" in result:
            moveto(houseposition[2][0],houseposition[2][1])

        if "去三号房" in result:
            moveto(houseposition[3][0],houseposition[3][1])

        if "去四号房" in result:
            moveto(houseposition[4][0],houseposition[4][1])

        if "去五号房" in result:
            moveto(houseposition[5][0],houseposition[5][1])

        if "去六号房" in result:
            moveto(houseposition[6][0],houseposition[6][1])

if __name__ == "__main__":
    while True:
        main()
        windows()
        doors()
