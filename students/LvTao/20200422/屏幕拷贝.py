import pyautogui as pg
import numpy as np
import time
import cv2

time.sleep(5)
W, H = pg.size()
print(W,H)
pg.moveTo(400,700)

while True:
    pic= pg.screenshot("my_screenshot.png",region=(0,400, 600, 400))
    image = cv2.cvtColor(np.array(pic), cv2.COLOR_RGB2BGR)

    cv2.imshow("screenshot",image)
    cv2.waitKey(50)
cv2.destroyAllWindows()
