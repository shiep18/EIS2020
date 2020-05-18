import pyautogui
if pyautogui.confirm(text='make a screenshot?', title='test', buttons=['OK', 'Cancel'])=='OK':
    im = pyautogui.screenshot('screenshot.png')