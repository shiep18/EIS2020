import mcpi.minecraft as minecraft
import mcpi.block as block
import cv2
import numpy as np
import pyautogui as pg
import time

def click(x,y):
    pg.moveTo(x, y) 
    time.sleep(0.1)
    pg.click()

pic=pg.screenshot()
img = cv2.cvtColor(np.array(pic),cv2.COLOR_RGB2BGR)
template = cv2.imread('logo.PNG')
(h, w )= template.shape[:2]
res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.9
loc = np.where( res >= threshold)
a=list(zip(*loc[::-1]))
click(a[0][0]+400,a[0][1]+295)
click(a[0][0]+400,a[0][1]+100)
click(a[0][0]+200,a[0][1]+410)
click(a[0][0]+400,a[0][1]+165)

mc = minecraft.Minecraft.create()
pos=mc.player.getTilePos()
a=50
b=50
img=cv2.imread('circle.jpg')
GrayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh1=cv2.threshold(GrayImage,130,255,cv2.THRESH_BINARY)
resized_image= cv2.resize(thresh1,(b,a))
cv2.imshow('1',resized_image)
for x in range(a):
    for y in range(b):
        if resized_image[x][y]!=0:
            mc.setBlock(pos.x-x-1,pos.y-10,pos.z+y,173)
            time.sleep(0.05)
cv2.waitKey()
cv2.destroyAllWindows()
