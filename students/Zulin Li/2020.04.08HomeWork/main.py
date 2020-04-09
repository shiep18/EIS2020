#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Autor:ZLL
import mcpi.minecraft as minecraft
import mcpi.block as block
from HouseClass import *
import serial
import serial.tools.list_ports
import time

def run():
    action = "empty"
    while True:
        pos = mc.player.getTilePos()
        flag = house1.InsideHouse(pos.x, pos.y, pos.z)
        house1.SetLight(flag)
        if flag:
            action = '01234567'
            print('LightOn')
        else:
            action = '8'
            print('LightOff')
        ser.write(action.encode())
        time.sleep(1)

mc = minecraft.Minecraft.create()
mc.setBlock(25, 19, 15, 1)
mc.player.setTilePos([25, 20, 15])
house1 = House('BigHouse1', 20, 20, 20, 10, 10, 10)
house1.SetHouse()

print('hello')
ports = list(serial.tools.list_ports.comports())
print(ports)

for p in ports:
    print(p[1])
    if "SERIAL" in p[1]:
        ser=serial.Serial(port=p[0])
    else:
        print ("No Arduino Device was found connected to the computer")
ser=serial.Serial(port='COM12')
#ser=serial.Serial(port='/dev/ttymodem542')
#wait 2 seconds for arduino board restart
time.sleep(2)

run()












