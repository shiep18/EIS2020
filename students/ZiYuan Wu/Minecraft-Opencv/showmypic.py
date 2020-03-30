from mcpi.minecraft import Minecraft
import mcpi.block as block
import numpy as np
import cv2
import time
#mc = minecraft.Minecraft.create()
#pos = mc.player.getTilePos()
blockcolor = [[254, 0],[240, 4], [170, 8],[150, 3],[145, 2],[139, 8],[125, 1],[111, 10],[107, 5],[89, 11],[67, 7],[22, 15]] #[240, 4], [170, 8],[150, 3],[145, 2],[139, 8],[125, 1],[111, 10],[107, 5],[89, 11],[67, 7],[22, 15]
a = 200
b = 200

mc=Minecraft.create()
pos=mc.player.getTilePos()
a=32
b=32

def draw(i):
    img=cv2.imread("e:/2020class/QianRuShi/Opencv/new/1.png")
    GrayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,thresh1=cv2.threshold(GrayImage,blockcolor[i][0],255,cv2.THRESH_BINARY)
    median = cv2.medianBlur(thresh1,7)  #中值滤波
    resized_image=~cv2.resize(median,(32,32))
    return resized_image

for x in range(a):
    for y in range(b):
        mc.setBlock(pos.x,pos.y+a-x-1,pos.z+y,219)
for i in range(12):
    resized_image=draw(i)
    for x in range(a):
        for y in range(b):
            if (resized_image[x][y] != 0):
                mc.setBlock(pos.x,pos.y+a-x-1,pos.z+y,35,blockcolor[i][1])
                time.sleep(0.01)
    i += 1