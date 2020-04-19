from mcpi.minecraft import Minecraft
from pykeyboard import PyKeyboard
import mcpi.block as block
import cv2
import math
import numpy as np
import time
import os
mc=Minecraft.create()
k = PyKeyboard()
pos=mc.player.getTilePos()
def move():
    k.press_key(t)
    time.sleep(2)
    k.release_key(t)
def house(t):
    M=1
    x0=pos.x+int(t)/10000
    y0=pos.y+int(t)%10000/100
    z0=pos.z+int(t)%100
    for y in range(6):                                    
        for a in range(9):
            mc.setBlock(x0+a, y0+y, z0, M)
            mc.setBlock(x0+a, y0+y, z0+8,M)
        for a in range(8):
            mc.setBlock(x0, y0+y, z0+1+a, M)
            mc.setBlock(x0+8, y0+y, z0+1+a,M)
    for z in range(3):
        for y in range(3):
            mc.setBlock(x0+8, y0+y+2, z0+z+3, 102)
    for x in range(9):
        for z in range(9):
            mc.setBlock(x0+x,y0+6,z+z0, M)

while True:
    if os.path.isfile("move.txt"):
        f = open("move.txt")
        t=f.read()
        f.close()
        time.sleep(3)
        if t=='w' or t=='s' or t=='d' or t=='a':
            move()
            pos=mc.player.getTilePos()
        else:
            house(t)
      
