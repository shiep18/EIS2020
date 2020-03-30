
from mcpi.minecraft import Minecraft
import mcpi.block as block
import numpy as np
import cv2
import time

mc = Minecraft.create()
pos = mc.player.getTilePos()
a = 75
b = 62

img = cv2.imread("emotion.jpg")
img = ~img   #图片的灰色与黑色取反值
GrayImage = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh1 = cv2.threshold(GrayImage,100,255,cv2.THRESH_BINARY)
resized_image = cv2.resize(thresh1,(b,a))

for x in range (a):
    for y in range(b):
        mc.setBlock(pos.x+a-x-1,pos.y+30,pos.z+y,173)
for x in range(a):
    for y in range(b):
        if resized_image[x][y] == 0:
            mc.setBlock(pos.x+a-x-1,pos.y+30,pos.z+y,43)
