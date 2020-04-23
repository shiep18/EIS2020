import pyautogui as pg
import numpy as np
import time
import cv2
import binvox_rw
from mcpi.minecraft import Minecraft
import mcpi.block as block

time.sleep(2)
pic=pg.screenshot()
img = cv2.cvtColor(np.array(pic),cv2.COLOR_RGB2BGR)
template = cv2.imread('mc.PNG')
(h, w )= template.shape[:2]

res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8

loc = np.where( res >= threshold)
pos=[0,0]
for pt in zip(*loc[::-1]):
    pos[0]=pt[0]
    pos[1]=pt[1]

time.sleep(1)

#回到游戏 
back = cv2.imread('fanhui.PNG')
(h, w )= back.shape[:2]
res1 = cv2.matchTemplate(img,back,cv2.TM_CCOEFF_NORMED)

locc1 = np.where( res1 >= threshold)
pos2=[0,0]
for ptt in zip(*locc1[::-1]):
    pos2[0]=ptt[0]
    pos2[1]=ptt[1]
    pg.moveTo(ptt[0],ptt[1])  # 移动鼠标
    time.sleep(1)
    pg.click()

#打开服务器
serve = cv2.imread('fuwuqi.PNG')
(h, w )= serve.shape[:2]
res2 = cv2.matchTemplate(img,serve,cv2.TM_CCOEFF_NORMED)

locc2 = np.where( res2 >= threshold)
for ptt in zip(*locc2[::-1]):
    pg.moveTo(ptt[0]+45,ptt[1]+30)  # 移动鼠标
    time.sleep(1)
    pg.click()
def build():
    mc=Minecraft.create()
    pos=mc.player.getTilePos()

    with open('caochang.binvox', 'rb') as f:
        model = binvox_rw.read_as_3d_array(f)

    #print(model.data)

    for y in range(model.dims[1]):
        #print("layer y=",y)
        layer_data=model.data[y]
        stringlayer=""
        for x in range(model.dims[0]):
            stringlayer=stringlayer+"\n"
            for z in range(model.dims[2]):
                if model.data[x][y][z] == True:
                    stringlayer=stringlayer+'1'
                    mc.setBlock(pos.x+x,pos.y+y,pos.z+z,block.STONE.id)
                else:
                    stringlayer=stringlayer+'0'
                    mc.setBlock(pos.x+x,pos.y+y,pos.z+z,block.AIR.id)

                
while True:
    pic= pg.screenshot("my_screenshot.png",region=(pos[0],pos[1], 850, 525))
    image = cv2.cvtColor(np.array(pic), cv2.COLOR_RGB2BGR)

    cv2.imshow("screenshot",image)
    key = cv2.waitKey(1) & 0xFF
    # 按'q'健退出循环
    if key == ord('q'):
        break
    if key == ord('a'):
        pg.moveTo(pos2[0],pos2[1])  # 移动鼠标
        time.sleep(1)
        pg.click()
    if key == ord('b'):
        build()
cv2.destroyAllWindows()
