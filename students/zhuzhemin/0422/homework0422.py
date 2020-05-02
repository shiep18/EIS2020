import cv2
import numpy as np
import pyautogui as pg
import time
pg.FAILSAFE=False
W,H=pg.size()
print(W,H)
pic=pg.screenshot("my_test_screenshot.png")
img = cv2.cvtColor(np.array(pic),cv2.COLOR_RGB2BGR)
def ready():
    global img
    pic=pg.screenshot("my_test_screenshot.png")
    img = cv2.cvtColor(np.array(pic),cv2.COLOR_RGB2BGR)
threshold = 0.9
loc3=[0,0]
loc4=[0,0]
# x号
x = cv2.imread('xb2.PNG')
(h,w)= x.shape[:2]
res = cv2.matchTemplate(img,x,cv2.TM_CCOEFF_NORMED)
locc = np.where(res >= threshold)
loc=[0,0]
for pt in zip(*locc[::-1]):
    loc[0]=pt[1]
    loc[1]=pt[0]
# 服务器图标
def server():
    global loc3
    server = cv2.imread('server.PNG')
    res3 = cv2.matchTemplate(img,server,cv2.TM_CCOEFF_NORMED)
    locc3 = np.where( res3 >= threshold-0.05)
    for pt in zip(*locc3[::-1]):
        loc3[0]=pt[1]
        loc3[1]=pt[0]
#回到游戏图标
def back():
    global loc4
    back = cv2.imread('back.PNG')
    res4 = cv2.matchTemplate(img,back,cv2.TM_CCOEFF_NORMED)
    locc4 = np.where( res4 >= threshold)
    loc4=[0,0]
    for pt in zip(*locc4[::-1]):
        loc4[0]=pt[1]
        loc4[1]=pt[0]   

#窗口高度是屏幕高度-坐标，此外还要再减去任务栏所占的60高度
print("inecraft窗口大小为",str(loc[1]+w),"*",str(1080-loc[0]-60))
while True:
    ready()
    server()
    back()
    if loc3[0] != 0 and loc3[1] != 0:
        pg.moveTo(loc3[1], loc3[0])
        pg.click()
        pg.click()
        print("server")
        time.sleep(3)
        loc3=[0,0]

    if loc4[0] != 0 and loc4[1] != 0:
        pg.moveTo(loc4[1], loc4[0])
        pg.click()
        print("back to the game")
        time.sleep(3)
        loc4=[0,0]       
    # pic= pg.screenshot("my_screenshot.png",region=(0,loc[0],loc[1]+w,1080-loc[0]))
    # image = cv2.cvtColor(np.array(pic), cv2.COLOR_RGB2BGR)
    # cv2.imshow("screenshot",image)
    cv2.waitKey(1000)
cv2.destroyAllWindows()    