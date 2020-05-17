import pyautogui
import time
from selenium import webdriver

#定义图像识别双击事件
def mouseDoubleClick(image):
    x,y=pyautogui.locateCenterOnScreen(image,confidence=0.9)
    pyautogui.click(x,y,clicks=2,interval=0.2,duration=0.2,button='left')

#定义单击事件
def mouseClick(image):
    x,y=pyautogui.locateCenterOnScreen(image,confidence=0.9)
    pyautogui.click(x,y,clicks=1,interval=0.2,duration=0.2,button='left')

mouseDoubleClick(image = 'chorm.png')

pyautogui.write("www.baidu.com")
time.sleep(1)
pyautogui.press("enter")
time.sleep(3)

pyautogui.write("Detroit: Become Human")
time.sleep(2)
pyautogui.press("enter")
