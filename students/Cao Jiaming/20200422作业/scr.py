import cv2
import numpy as np
import pyautogui as pg
#rgb
pic=pg.screenshot()
img = cv2.cvtColor(np.array(pic),cv2.COLOR_RGB2BGR)
template = cv2.imread('1.PNG')
backworld = cv2.imread('2.PNG')
(h, w )= template.shape[:2]

threshold = 0.5
res2 = cv2.matchTemplate(img,backworld,cv2.TM_CCOEFF_NORMED)
loc_back = np.where( res2 >= threshold)

pg.moveTo(loc_back[1],loc_back[0])
pg.click()


#窗体面积计算
res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
loc = np.where( res >= threshold)
print("窗体的面积：",1027-int(loc[0]),"*",int(loc[1])+w+6) #高*宽
while True:
    pic= pg.screenshot("my_screenshot.png",region=(0,int(loc[0]),int(loc[1])+w+6,539)) #region的含义？
    image = cv2.cvtColor(np.array(pic), cv2.COLOR_RGB2BGR)

    cv2.imshow("screenshot",image)
    cv2.waitKey(300)

#cv2.imshow("img",img[int(loc[0]):1027,0:int(loc[1])+w+6])


cv2.destroyAllWindows()
