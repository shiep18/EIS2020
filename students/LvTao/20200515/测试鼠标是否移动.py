import time
import pyautogui

def pos():
    pos_mouse=pyautogui.position()
    time.sleep(1)
    return pos_mouse

while True:
    if pos()==pyautogui.position():
        continue

    else:
        x,y=pyautogui.position()
        print('当前位置X{},Y{}'.format(x,y))
