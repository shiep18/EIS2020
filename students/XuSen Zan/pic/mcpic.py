from mcpi.minecraft import Minecraft
import mcpi.block as block
import numpy as np
import cv2
import time

mc = Minecraft.create()
pos = mc.player.getTilePos()
a = 117
b = 175

img = cv2.imread("call.jpg")
img = ~img   #让图片的灰色与黑色取反值，可以更便于观察图案
GrayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh1 = cv2.threshold(GrayImage,100,255,cv2.THRESH_BINARY)
resized_image = cv2.resize(thresh1,(b,a))

for x0 in range (a):
    for y0 in range(b):
        mc.setBlock(pos.x+a-x0-1,pos.y,pos.z+y0,173)
for x0 in range(a):
    for y0 in range(b):
        if resized_image[x0][y0] == 0:
            mc.setBlock(pos.x+a-x0-1,pos.y,pos.z+y0,43.7)
