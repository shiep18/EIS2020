from mcpi.minecraft import Minecraft
from pykeyboard import PyKeyboard
import mcpi.block as block
import cv2
import math
import numpy as np
import time
import os
import csv

def MoveIt(wasd):
    if wasd == 'w':
        k.press_key("w")
    else:
        k.release_key("w")

    if wasd == 's':
        k.press_key("s")
    else:
        k.release_key("s")

    if wasd == 'a':
        k.press_key("a")
    else:
        k.release_key("a")

    if wasd == 'd':
        k.press_key("d")
    else:
        k.release_key("d")
        

def ReadCsv():
    csv_reader=csv.reader(open('move.csv',encoding='utf-8'))
    L=[]
    for row in csv_reader:
        L.append(row)
    return L

with open('move.csv', "r+") as f:
        read_data = f.read()
        f.seek(0)
        f.truncate()   #清空文件
k=PyKeyboard()
mc=Minecraft.create()
pos=mc.player.setTilePos([535,0,505])

print('The code is running......')

while True:
    L=ReadCsv()
    if L != []:
        print(L)
        break
    
print('Got it !')
time.sleep(5)
for i in L:
    num=int(i[1])
    while num:
        MoveIt(i[0])
        time.sleep(0.5)
        num-=1
k.release_key(L[len(L)-1][0])







