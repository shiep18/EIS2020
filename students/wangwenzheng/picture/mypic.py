from mcpi.minecraft import Minecraft
import mcpi.block as block
import numpy as np
import cv2
import time
mc=Minecraft.create()
pos=mc.player.getTilePos()

def showpic(a=50,b=50):
    img=cv2.imread('jj.jpg')
    img=~img
    GrayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,thresh1=cv2.threshold(GrayImage,100,255,cv2.THRESH_BINARY)
    resized_image=cv2.resize(thresh1,(b,a))
    
    for x in range(a):
        for y in range(b):
            mc.setBlock(pos.x+a-x-1,pos.y+5,pos.z+y,35,15)
    for x in range(a):
        for y in range(b):
            if resized_image[x][y]==0:
                mc.setBlock(pos.x+a-x-1,pos.y+5,pos.z+y,35,0)


    
