import cv2
import mcpi.minecraft as minecraft
import mcpi.block as block
import numpy as np
from matplotlib import pyplot as plt

def SetPic(X,Y,Z):
    img=cv2.imread('Shock.jpg',0)
    ret,thresh1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    L=len(thresh1)
    W=len(thresh1[0])
    if W>L:
        R=L
        L=W
        W=R
    for x in range(0,L):
        for z in range(0,W):
            if thresh1[x][z]==0:
                mc.setBlock(X+x, Y, Z+W-z,49)
            else:
                mc.setBlock(X+x, Y, Z+W-z,35)

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()#玩家位置，联机


