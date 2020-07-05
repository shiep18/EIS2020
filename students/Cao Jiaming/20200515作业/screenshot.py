import pyautogui
if pyautogui.confirm(text='Make a screenshot? ', title='test', buttons=['OK', 'Cancel'])=='OK':
    img = pyautogui.screenshot('cjmscreenshot.png')
