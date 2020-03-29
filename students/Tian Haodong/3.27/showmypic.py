from mcpi.minecraft import Minecraft
import mcpi.block as block
import numpy as np
import cv2
import time
mc=Minecraft.create()
pos=mc.player.getTilePos()

a=160
b=160

img=cv2.imread("logo2.jpg")


#print(len(img[0]))
#print(len(img))
GrayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh1=cv2.threshold(GrayImage,0,255,cv2.THRESH_BINARY)
resized_image=~cv2.resize(thresh1,(b,a))
for i in range(a):
    for j in range(b):
        mc.setBlock(pos.x+a-i-1,pos.y,pos.z+j,173)
        #time.sleep(0.1)
        #print("1")
for i in range(a):
    for j in range(b):
        if resized_image[i][j]==0:
            mc.setBlock(pos.x+a-i-1,pos.y,pos.z+j,35)
            #print("2")
       
