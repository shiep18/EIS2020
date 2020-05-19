from mcpi.minecraft import Minecraft
import mcpi.block as block
import mcpi.block as block
import cv2
import math
import numpy as np
import time
import os
import csv
mc=Minecraft.create()
pos=mc.player.getTilePos()
#打开build.csv，获取房子大小
x=pos.x
y=pos.y
z=pos.z
def ReadCsv():
    csv_reader=csv.reader(open('build.csv',encoding='utf-8'))
    L=[]
    for row in csv_reader:
        L.append(row)
    return L

def CsvToNum(L=[]):
    num=0
    for i in L:
        num=num*10+int(i)
    return num
with open('build.csv', "r+") as f:
        read_data = f.read()
        f.seek(0)
        f.truncate()   #清空文件
K=[]
while True:
    L=ReadCsv()
    if L != []:
        print(L)
        for i in L:
            K.append(CsvToNum(i))
            print(CsvToNum(i))
        print(K)
        break
#用setblocks造房子
mc.setBlocks(x,y,z,x+K[0],y++K[1],z++K[2],41)
mc.setBlocks(x+1,y+1,x++K[0]-1,y++K[1]-1,z++K[2]-1,0)
