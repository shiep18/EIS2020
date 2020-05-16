import pyautogui

choice = pyautogui.confirm(text='是否截取全屏', title='confirm', buttons=['OK', 'Cancel'])
if choice is 'OK':
    save = pyautogui.prompt(text='输入截图名称：', title='prompt')
    im = pyautogui.screenshot(save + '.png')
    pyautogui.alert(text='截图完毕', title='alert', button='OK')
else :
    pyautogui.alert(text='程序已结束', title='alert', button='OK')
    

