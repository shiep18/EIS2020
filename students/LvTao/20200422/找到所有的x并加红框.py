import cv2
import numpy as np
import pyautogui as pg
import time

pic=pg.screenshot()
img = cv2.cvtColor(np.array(pic),cv2.COLOR_RGB2BGR)
template = cv2.imread('xb.PNG')
print("img",img.shape)
print("template",template.shape)
(h, w )= template.shape[:2]

start=time.time()
res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
#print(len(res))

end=time.time()
print("mach{:.2f}seconds".format(end - start))

loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    
resimg=cv2.resize(img,(600,400))
cv2.imshow("img",resimg)
cv2.waitKey()
cv2.destroyAllWindows()
