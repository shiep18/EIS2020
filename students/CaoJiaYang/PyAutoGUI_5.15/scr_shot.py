import pyautogui
if pyautogui.confirm(text='Full screen capture?',buttons=['Yes', 'No'])=='Yes':
    im = pyautogui.screenshot('screenshot.jpg')
