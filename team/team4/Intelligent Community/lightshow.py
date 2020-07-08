import mcpi.minecraft as minecraft
import time
import mcpi.block as block
import numpy as np
import cv2
import threading
mc = minecraft.Minecraft.create('47.100.46.95',4784)
entityId= mc.getPlayerEntityId("W")
def shoufig():
    while True:
        pos=mc.entity.getTilePos(entityId)
        if 1189<=pos.x<=1217 and 1218<=pos.z<=1248:
            lights=['3','2','1','go','spiral','diejia','quart','xx','A','boat','team4']
            
            for light in lights:
                mc.setBlocks(1189,37,1244,1189,15,1222,41)
                fname = "huawen\\"+light  + ".csv"
                f = open(fname, "r")
                x0=1189
                y0=38
                z0=1245
                i=0
                j=0
                for line in f.readlines():
                    data = line.split(",")
                    i=i+1
                    j=0
                    for cell in data:
                        j=j+1
                        if cell == "1" or cell == "1\n":
                            mc.setBlock(x0, y0-i, z0-j, 169)
                time.sleep(1)
def main():
    first_thread=threading.Thread(target=shoufig)
    first_thread.start()

