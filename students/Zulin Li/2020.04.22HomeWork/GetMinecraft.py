import win32api,win32con,win32gui,time
import cv2
import numpy as np
import pyautogui as pg
from GetPlayground import *
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
def getMinecraft(name):
    name=name
    handle = win32gui.FindWindow(0,name)
    if handle == 0:
        return None
    else:
        return win32gui.GetWindowRect(handle)

x1,y1,x2,y2 = getMinecraft('Minecraft 1.12')
print(x1,y1,x2,y2)
pic=pg.screenshot(region=(x1,y1,x2-x1,y2-y1))
img = cv2.cvtColor(np.array(pic),cv2.COLOR_RGB2BGR)

while True:
    try:
        box=pg.locateOnScreen('Game.PNG')
    except:
      print("sss")
      continue
    if box is None:
        print("searching")
    else:
        print(box)
        break
pg.moveTo(box[0]+10,box[1]+10)
pg.leftClick()

while True:
    try:
        box=pg.locateOnScreen('Pin3.PNG')
    except:
      print("sss")
      continue
    if box is None:
        print("searching")
    else:
        print(box)
        break
pg.moveTo(box[0]+10,box[1]+10)
pg.leftClick()

while True:
    try:
        box=pg.locateOnScreen('SignIn.PNG')
    except:
      print("sss")
      continue
    if box is None:
        print("searching")
    else:
        print(box)
        break
pg.moveTo(box[0]+10,box[1]+10)
pg.leftClick()

mc.player.setTilePos([535, 8, 505])
for i in range(10):
    for j in range(10):
        mc.setBlock(530 + i, -1, 500 + j, 41)  # 底部
time.sleep(1)
mc.postToChat('Playground is building ......')
time.sleep(3)
GetPlayground()

cv2.imshow("OpenCV",img)
cv2.waitKey()
cv2.destroyAllWindows()