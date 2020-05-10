from mcpi.minecraft import Minecraft
import mcpi.block as block
import cv2
import math
import numpy as np
import time
import os

mc=Minecraft.create()

pos=mc.player.getTilePos()


while True:
    i=20
    pos=mc.player.getTilePos()
    if os.path.isfile("move.txt"):
        f = open("move.txt")
        a =f.read()
        f.close()
        if a =='w':
            while i!=0:
                i=i-1
                pos=mc.player.getTilePos()
                mc.player.setTilePos(pos.x+1,pos.y,pos.z)
                
            
            while True:
                
                f = open("move.txt")
                a =f.read()
                if a !='w':
                    break
                else:
                    f.close()
        if a =='s':
            while i!=0:
                i=i-1
                pos=mc.player.getTilePos()
                mc.player.setTilePos(pos.x-1,pos.y,pos.z)                
            
            while True:
                
                f = open("move.txt")
                a =f.read()
                if a !='s':
                    break
                else:
                    f.close()
        if a =='a':
            while i!=0:
                i=i-1
                pos=mc.player.getTilePos()
                mc.player.setTilePos(pos.x,pos.y,pos.z+1)
                
            
            while True:
                
                f = open("move.txt")
                a =f.read()
                if a !='a':
                    break
                else:
                    f.close()
        if a =='d':
            while i!=0:
                i=i-1
                pos=mc.player.getTilePos()
                mc.player.setTilePos(pos.x,pos.y,pos.z-1)
                
            
            while True:
               
                f = open("move.txt")
                a =f.read()
                if a !='d':
                    break
                else:
                    f.close()
           
