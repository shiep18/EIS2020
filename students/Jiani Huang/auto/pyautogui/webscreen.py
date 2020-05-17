import pyautogui
import time

#定义图像识别双击事件
def mouseDoubleClick(image):
    x,y=pyautogui.locateCenterOnScreen(image,confidence=0.9)
    pyautogui.click(x,y,clicks=2,interval=0.2,duration=0.2,button='left')

#定义单击事件
def mouseClick(image):
    x,y=pyautogui.locateCenterOnScreen(image,confidence=0.8)
    pyautogui.click(x,y,clicks=1,interval=0.2,duration=0.2,button='left')


mouseDoubleClick('web.jpg')
time.sleep(1)
mouseClick('http.jpg')
pyautogui.typewrite('www.baidu.com')
pyautogui.press('enter')
pyautogui.press('enter')
time.sleep(1)
mouseClick('search.jpg')
time.sleep(1.5)
pyautogui.typewrite('pyautogui')
time.sleep(0.5)
pyautogui.press('enter')
pyautogui.press('enter')

if pyautogui.confirm(text='Do you want a screenshot?', title='screenshot', buttons=['YES', 'NO']):
    pyautogui.screenshot('screenshot.jpg')
