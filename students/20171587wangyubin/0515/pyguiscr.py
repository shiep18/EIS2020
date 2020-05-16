import pyautogui
if pyautogui.confirm(text='make a Scr?', title='test', buttons=['OK', 'Cancel'])=='OK':
    im = pyautogui.screenshot('my_screenshot.png')