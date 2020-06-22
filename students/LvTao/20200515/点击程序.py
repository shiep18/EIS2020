import pyautogui
import time

#定义图像识别双击事件
def mouseDoubleClick(image):
    x,y=pyautogui.locateCenterOnScreen(image)
    pyautogui.click(x,y,clicks=2,interval=0.2,duration=0.2,button='left')

#定义单击事件
def mouseClick(image):
    x,y=pyautogui.locateCenterOnScreen(image)
    pyautogui.click(x,y,clicks=1,interval=0.2,duration=0.2,button='left')

mouseDoubleClick(image='wyy.png')
time.sleep(2)
