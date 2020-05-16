import pyautogui
import time


# 定义图像识别双击事件
def mouseDoubleClick(image, confidence):
    x, y = pyautogui.locateCenterOnScreen(image, confidence=confidence)
    pyautogui.click(x, y, clicks=2, interval=0.2, duration=0.2, button='left')


# 定义单击事件
def mouseClick(a, image):
    x, y = pyautogui.locateCenterOnScreen(image, confidence=a)
    pyautogui.click(x, y, clicks=1, interval=0.2, duration=0.2, button='left')


mouseClick(0.8, image='chrome.png')
mouseClick(0.8, image='add_new_page.png')
pyautogui.write('www.baidu.com', interval=0.25)
pyautogui.press('enter', presses=2, interval=0.25)
time.sleep(2)
