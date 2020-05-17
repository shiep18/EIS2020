import pyautogui
if pyautogui.confirm(text='是否保留截图？', title='Screenshot', buttons=['YES', 'NO'])=='YES':
    im = pyautogui.screenshot('my_screenshot.png')
