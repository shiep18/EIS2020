from mcpi.minecraft import Minecraft
import mcpi.block as block
import cv2
import math
import numpy as np
import time
import os
mc=Minecraft.create()

pos=mc.player.getTilePos()
mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
i=0
j=0
while True:
    pos=mc.player.getTilePos()
    if os.path.isfile("move.csv"):
        if i==0:
            tm=time.ctime(os.stat("move.csv").st_mtime) #文件的修改时间
            i=i+1
            print(tm)
        if i>0:
            tm1=time.ctime(os.stat("move.csv").st_mtime)
            if tm1 != tm:
                f = open("move.csv")
                a =f.read()
                if a =='w':
                    mc.player.setTilePos(pos.x+1,pos.y,pos.z)
                if a =='s':
                    mc.player.setTilePos(pos.x-1,pos.y,pos.z)
                if a =='a':
                    mc.player.setTilePos(pos.x,pos.y,pos.z+1)
                if a =='d':
                    mc.player.setTilePos(pos.x,pos.y,pos.z-1)
                if a ==' ':
                    mc.player.setTilePos(pos.x,pos.y+1,pos.z)
                if a =='j':
                    mc.player.setTilePos(pos.x,pos.y-1,pos.z)
                if a =='q':
                    break
                tm=tm1
    if os.path.isfile("house.csv"):
        if j==0:
            tms=time.ctime(os.stat("house.csv").st_mtime) #文件的修改时间
            j=i+1
            print(tms)
        if j>0:
            tms1=time.ctime(os.stat("house.csv").st_mtime)
            if tms1 != tms:
                f = open("house.csv",'r')
                n=f.readlines()
                b=np.array(n)
                print(b)
                s=b[0]
                a=s.split(',')
                print(a[0])
                print(a[1])
                print(a[2])
                for x in range(10):
                    for z in range(10):
                        mc.setBlock(int(a[0])+x,int(a[1]),int(a[2])+z,41)
                for y in range(10):
                    for x in range(10):
                        mc.setBlock(int(a[0])+x,int(a[1])+y,int(a[2]),41)
                        mc.setBlock(int(a[0])+x,int(a[1])+y,int(a[2])+9,41)
                    for z in range(10):
                        mc.setBlock(int(a[0]),int(a[1])+y,int(a[2])+z,41)
                        mc.setBlock(int(a[0])+9,int(a[1])+y,int(a[2])+z,41)
                for x in range(10):
                    for z in range(10):
                        mc.setBlock(int(a[0])+x,int(a[1])+9,int(a[2])+z,41)

                mc.setBlock(int(a[0])+5,int(a[1])+1,int(a[2]),0)
                mc.setBlock(int(a[0])+5,int(a[1])+2,int(a[2]),0)

                for z in range(2):
                    for y in range(2):
                        mc.setBlock(int(a[0]),int(a[1])+4+y,int(a[2])+4+z,20)
                tms=tms1

        
            
