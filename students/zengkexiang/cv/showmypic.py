from mcpi.minecraft import Minecraft
import mcpi.block as block
import cv2 as cv
import numpy as np
import time

mc=Minecraft.create()
pos=mc.player.getTilePos()

def getpic():
    a = 32
    b = 32

    img =cv.imread("mypic.jpg")
    gray =cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret,thresh1 = cv.threshold(gray,127,255,cv.THRESH_BINARY)
    #re_img = cv.resize(thresh1,(b,a))
    for x in range(a):
        for y in range(b):
            mc.setBlock(pos.x+a-x-1,pos.y,pos.z+y,80)
    for x in range(a):
        for y in range(b):
            if thresh1[x][y] == 0:
                mc.setBlock(pos.x + a - x - 1, pos.y, pos.z + y, 49)

