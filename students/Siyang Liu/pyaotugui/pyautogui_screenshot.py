import pyautogui

choice = pyautogui.confirm(text='screenshot ready', title='confirm', buttons=['Done', 'Cancel'])
if choice is 'Done':
    save = pyautogui.prompt(text='name：', title='prompt')
    im = pyautogui.screenshot(save + '.png')
    pyautogui.alert(text='Finished.', title='alert', button='OK')
else :
    pyautogui.alert(text='Error.', title='alert', button='OK')
