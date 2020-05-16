import pyautogui as pg
import time as t

def mousedoubleclick(image):
    x, y=pg.locateCenterOnScreen(image)
    pg.doubleClick(x, y)
def mouseclick(image):
    x, y=pg.locateCenterOnScreen(image)
    pg.click(x, y)
   
mousedoubleclick(image='goole.png')
t.sleep(2)
mouseclick(image='search.png')
t.sleep(1)
pg.typewrite('pyautogui')
t.sleep(1)
pg.press('enter')
t.sleep(1)
pg.press('enter')

if pg.alert(text='12345', title='none', button='OK')=='OK':
    im=pg.screenshot('my_screenshot.png')





