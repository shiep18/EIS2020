import pyautogui

if pyautogui.confirm(text='Do you want to make a ScreenShot?', title='test', buttons=['OK', 'Cancel'])=='OK':
    im = pyautogui.screenshot('my_ScreenShot.png')
