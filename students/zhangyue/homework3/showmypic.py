import mcpi.minecraft as minecraft
import mcpi.block as block
import numpy as np
import cv2
import time
print("showmypic has been include")
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()


def showMyPic(name, a, b):
    print("We are working")
    img = cv2.imread(name)
    GrayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(GrayImage, 170, 255, cv2.THRESH_BINARY)
    resized_image = cv2.resize(thresh1, (b, a))
    for x in range(a):
        for y in range(b):
            mc.setBlock(pos.x + a - x - 1, pos.y, pos.z + y, 35, 0)
    for x in range(a):
        for y in range(b):
            if resized_image[x][y] == 0:
                mc.setBlock(pos.x + a - x - 1, pos.y, pos.z + y, 35, 15)
    print("Finish")


def clearPic(a, b):
    for x in range(a):
        for y in range(b):
            mc.setBlock(pos.x + a - x - 1, pos.y, pos.z + y, 0)
    print("Finish")

