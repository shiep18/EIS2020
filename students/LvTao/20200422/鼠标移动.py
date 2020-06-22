import pyautogui as pg
import time
pg.moveTo(100, 100) # 移动鼠标
time.sleep(5)
W, H = pg.size()
pg.moveTo(W/2, H/2)
