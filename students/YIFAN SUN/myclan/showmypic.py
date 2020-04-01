from mcpi.minecraft import Minecraft
import mcpi.block as block
import numpy as np
import cv2
import time

mc=Minecraft.create()
pos=mc.player.getTilePos()
a=32
b=32

def show():
    img=cv2.imread("mypic.png")
    GrayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,thresh1=cv2.threshold(GrayImage,127,255,cv2.THRESH_BINARY)
    median = cv2.medianBlur(thresh1,7) 
    resized_image=~cv2.resize(median,(32,32))

    for x in range(a):
        for z in range(b):
            mc.setBlock(pos.x+a-x-1,pos.y,pos.z+z,35)
        for x in range(a):
            for z in range(b):
                if (resized_image[x][z] != 0):
                    mc.setBlock(pos.x+a-x-1,pos.y,pos.z+z,173)

show()
