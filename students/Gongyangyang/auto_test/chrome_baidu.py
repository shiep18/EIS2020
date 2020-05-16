import pyautogui

import time

#定义图像识别双击事件
def mouseDoubleClick(image):
    x,y=pyautogui.locateCenterOnScreen(image,confidence=0.9)
    pyautogui.click(x,y,clicks=2,interval=0.2,duration=0.2,button='left')

#定义单击事件
def mouseClick(image):
    x,y=pyautogui.locateCenterOnScreen(image,confidence=0.9)
    pyautogui.click(x,y,clicks=1,interval=0.2,duration=0.2,button='left')


pyautogui.press("win")
time.sleep(1)

mouseClick("./imgs/chrome.png")
time.sleep(1)

mouseClick("./imgs/maxmun.png")
time.sleep(1)

pyautogui.write("baidu.com")
time.sleep(1)

pyautogui.press("enter")
time.sleep(2)

mouseClick("./imgs/search.png")
time.sleep(1)

pyautogui.write("cnmbhbdm")
time.sleep(1)

pyautogui.press("enter")