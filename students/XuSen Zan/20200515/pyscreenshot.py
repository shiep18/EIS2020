import pyautogui
if pyautogui.confirm(text='要截图吗?', title='测试', buttons=['OK', 'Cancel'])=='OK':
    im = pyautogui.screenshot('my_screenshot.png')
