from mcpi.minecraft import Minecraft
import mcpi.block as block
import numpy as np
import cv2
import time
import threading
mc=Minecraft.create('47.100.46.95',4784)

def showmypic(name="",x=50,y=50):
    while True:
        a=x 
        b=y
        for i in range(1,11):
            img=cv2.imread('picture/'+str(i)+'.jpg')
            GrayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            ret,thresh1=cv2.threshold(GrayImage,50,255,cv2.THRESH_BINARY)
            resized_image=~cv2.resize(thresh1,(b,a))
            mc.setBlocks(1189,14,1207,1189,64,1256,41)
            for x in range(a):
                for y in range(b):
                    if resized_image[x][y]!=0:
                        mc.setBlock(1189,15+a-x-1,1207+y,169)
            
            # for x in range(a):
            #     for y in range(b):
            #         if resized_image[x][y]==0:
            #             mc.setBlock((1189,15+a-x-1,1207+y,41))
            time.sleep(2)
def main():
    first_thread=threading.Thread(target=showmypic)
    first_thread.start()
#mc.setBlocks(1189,14,1207,1189,64,1256,41)