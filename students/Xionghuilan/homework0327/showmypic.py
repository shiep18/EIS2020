from mcpi.minecraft import Minecraft
import mcpi.block as block
import numpy as np
import cv2
import time
mc=Minecraft.create()
pos=mc.player.getTilePos()
##mc.player.setTilePos([0,0,0])
def show():
    
    a=50
    b=50
    img=cv2.imread("mypic.jpg")
    img=cv2.resize(img,None,fx=0.6,fy=0.6,interpolation=cv2.INTER_AREA)


    GrayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,thresh1=cv2.threshold(GrayImage,127,255,cv2.THRESH_TOZERO)
    resized_image=~cv2.resize(thresh1,(b,a))

    for x in range(a):
        for y in range(b):
            mc.setBlock(pos.x+a-x-1,pos.y+10,pos.z-b+y,35,15)
    for x in range(a):
        for y in range(b):
            if resized_image[x][y]==0:
                mc.setBlock((pos.x+a-x-1,pos.y+10,pos.z-b+y,35,0))

