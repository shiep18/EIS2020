import cv2
import numpy as np
import pyautogui as pg
import time

time.sleep(5)
W, H = pg.size()
print(W,H)

#首先确定mc窗口位置，此处使用画矩形的程序
pic=pg.screenshot()#截图函数
img = cv2.cvtColor(np.array(pic),cv2.COLOR_RGB2BGR)#数组，RGB
template = cv2.imread('mc.PNG')#读取图片
(h, w )= template.shape[:2]#读出图片长宽

res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.9

loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)#画出矩形位置
pic= pg.screenshot("my_screenshot.png",region=(pt[0],pt[1], (pt[0]+820),(pt[1]+435)))
image = cv2.cvtColor(np.array(pic), cv2.COLOR_RGB2BGR)
#确定多人游戏按键的位置，并点击
picn=pg.screenshot()
imgn = cv2.cvtColor(np.array(picn),cv2.COLOR_RGB2BGR)#数组，RGB
button = cv2.imread('button.PNG')#读取图片
(hn, wn )= button.shape[:2]#读出图片长宽
res = cv2.matchTemplate(imgn,button,cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
left_top = max_loc  # 左上角
click = (left_top[0] + wn/2, left_top[1] + hn/2)  #中心点
pg.click(click[0], y=click[1], button='left')
#因服务器有延时，这里休眠等待五秒用来连接服务器
time.sleep(1)
print("请稍等")
time.sleep(1)
print("请稍等.")
time.sleep(1)
print("请稍等..")
time.sleep(1)
print("请稍等...")
time.sleep(1)
print("请稍等....")
#确定localhost服务区按键的位置，并双击
picm=pg.screenshot()
imgm = cv2.cvtColor(np.array(picm),cv2.COLOR_RGB2BGR)#数组，RGB
localhost = cv2.imread('localhost.PNG')#读取图片
(hm, wm )= localhost.shape[:2]#读出图片长宽
res = cv2.matchTemplate(imgm,localhost,cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
left_top = max_loc  # 左上角
click = (left_top[0] + wm/2, left_top[1] + hm/2)  #中心点
pg.click(click[0], y=click[1], button='left')
pg.click(click[0], y=click[1], button='left')

#创建窗口监视游戏情况
while True:
    pic= pg.screenshot("my_screenshot.png",region=(pt[0],pt[1], (pt[0]+820),(pt[1]+435)))
    image = cv2.cvtColor(np.array(pic), cv2.COLOR_RGB2BGR)
    cv2.imshow("screenshot",image)
    cv2.waitKey(100)


#cv2.waitKey()
cv2.destroyAllWindows()
