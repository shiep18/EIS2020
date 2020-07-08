import tkinter as tk
import time
from MXMqtt import MXMqtt
import mcpi.minecraft as minecraft
import mcpi.block as block
import threading

global state
state=0
mc=minecraft.Minecraft.create('47.100.46.95',4784)
entityId= mc.getPlayerEntityId("W")

MQTTHOST="mqtt.16302.com"
MQTTPORT=1883
mqtt=MXMqtt(MQTTHOST,MQTTPORT)

topic="chat"
mqtt.SUB(topic)

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

def stop():
    #mc.postToChat("stop")
    print("stop")
    mqtt.PUB(topic,"4")
def go():
    mc.postToChat("go")
    print("go")
    mqtt.PUB(topic,"0")
def back():
    mc.postToChat("back")
    print("back")
    mqtt.PUB(topic,"3")
def left():
    mc.postToChat("left")
    print("left")
    mqtt.PUB(topic,"1")
def right():
    mc.postToChat("right")
    print("right")
    mqtt.PUB(topic,"2")

def mccardetect():
    global state
    while True:
        if detectpos(1252,4,1147)==1:
            state=1
            time.sleep(120)
        else:
            state=0

def start():
    global state
    while True:
        if state:
            pos2=mc.entity.getTilePos(entityId)
            time.sleep(1)
            pos1=mc.entity.getTilePos(entityId)
            if pos2.x-pos1.x>3:
                right()
            elif pos2.x-pos1.x<-3:
                left()
            elif pos2.z-pos1.z>3:
                back()
            elif pos2.z-pos1.z<-3:
                go()
            else:
                stop()
        
def main():
    thread_1=threading.Thread(target=mccardetect)
    thread_1.start()
    thread_2=threading.Thread(target=start)
    thread_2.start()
if __name__=='__main__':
    main()