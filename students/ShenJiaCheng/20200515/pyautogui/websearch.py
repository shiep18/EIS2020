import pyautogui
import time

#定义图像识别双击事件
def mouseDoubleClick(image):
    x,y=pyautogui.locateCenterOnScreen(image,confidence=0.8)
    pyautogui.click(x,y,clicks=2,interval=0.2,duration=0.2,button='left')

#定义单击事件
def mouseClick(image):
    x,y=pyautogui.locateCenterOnScreen(image,confidence=0.8)
    pyautogui.click(x,y,clicks=1,interval=0.2,duration=0.2,button='left')

mouseDoubleClick(image='Chorme.PNG')
time.sleep(1)
mouseClick(image='web.PNG')
time.sleep(2)
pyautogui.typewrite('www.baidu.com')
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
mouseClick(image='search.PNG')
time.sleep(2)
pyautogui.typewrite('manchesterunited')
time.sleep(2)
pyautogui.press('enter')
