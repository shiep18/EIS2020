import pyautogui
import win32api,win32con

test=win32api.MessageBox(0, "是否确定截取全屏？", "提醒",win32con.MB_YESNO)
#print(test)
if test==6:
    im = pyautogui.screenshot('截屏.png')

    
