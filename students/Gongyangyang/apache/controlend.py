from mcpi.minecraft import Minecraft
import mcpi.block as block
import cv2
import math
import numpy as np
import time
import os

mc=Minecraft.create()

def buildhouse(x0,y0,z0,L=10,W=10,H=6,M=1):
    for y in range(H):
        for x in range(L):
            mc.setBlock(x0+x,y0+y,z0,M)
            mc.setBlock(x0+x,y0+y,z0+W-1,M)
        for z in range(W):
            mc.setBlock(x0,y0+y,z0+z,M)
            mc.setBlock(x0+L-1,y0+y,z0+z,M)
    for x in range(L):
        for z in range(W):
            mc.setBlock(x0+x, y0+H-1, z0+z,1)
            mc.setBlock(x0+x, y0, z0+z,1)   #建地板

    mc.setBlock(x0+int(L/2), y0+1, z0,block.DOOR_WOOD.id) #门
    mc.setBlock(x0+int(L/2), y0+2, z0,block.DOOR_WOOD.id)

    for z in range(2):
        for y in range(2): 
            mc.setBlock(x0+L-1,y0+y+2,z0+z+4,20) #窗

def controlend():
    

    pos=mc.player.getTilePos()


# while True:
    pos=mc.player.getTilePos()
    if os.path.isfile("move.txt"):
        f = open("move.txt")
        a =f.read()
        f.close()
        try:
            p = eval(a[1:])
        except:
            pass
        if a[0] =='w':
                mc.player.setTilePos(pos.x+p,pos.y,pos.z)
        if a[0] =='s':
                mc.player.setTilePos(pos.x-p,pos.y,pos.z)
        if a[0] =='d':
                mc.player.setTilePos(pos.x,pos.y,pos.z+p)        
        if a[0] =='a':
                mc.player.setTilePos(pos.x,pos.y,pos.z-p)
        if a =='b':
                mc.player.setTilePos(399,75,-247)
        os.remove("move.txt")
    
    if os.path.isfile("home.txt"):
        f = open("home.txt")
        b =(f.read()).split(",")
        f.close()
        buildhouse(pos.x+int(b[0]),pos.y+int(b[1]),pos.z+int(b[2]))
        print("done")
        os.remove("home.txt")

        
