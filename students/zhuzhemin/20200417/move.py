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
    pos=mc.player.getTilePos()
    if os.path.isfile("move.txt"):
        f = open("move.txt")
        a =f.read()
        if a=="w":
            mc.player.setTilePos(pos.x+1,pos.y,pos.z)
        elif a=="s":
            mc.player.setTilePos(pos.x-1,pos.y,pos.z)
        elif a=="a":
            mc.player.setTilePos(pos.x,pos.y,pos.z-1)
        elif a=="d":
            mc.player.setTilePos(pos.x,pos.y,pos.z+1)
        pos=mc.player.getTilePos()
        with open('move.txt', 'w+') as f:
            f.write(f'0')
           
