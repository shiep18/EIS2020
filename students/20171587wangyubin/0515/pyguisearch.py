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
pyautogui.typewrite('test')
#打开浏览器默认中文，所以回车两次。第一次输入test，第二次搜索
pyautogui.press('enter')
pyautogui.press('enter')