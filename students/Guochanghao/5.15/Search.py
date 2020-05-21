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

mouseDoubleClick(image='chorme.PNG')
time.sleep(3)
pyautogui.typewrite('https://www.baidu.com')
pyautogui.press('enter')
