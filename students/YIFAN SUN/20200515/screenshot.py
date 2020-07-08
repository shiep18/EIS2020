import pyautogui
if pyautogui.confirm(text='screenshot?', title='homework1', buttons=['OK', 'Cancel'])=='OK':
    im = pyautogui.screenshot('my_screenshot.png')
