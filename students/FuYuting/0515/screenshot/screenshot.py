import pyautogui


text=pyautogui.confirm(text="确定要截图吗？",title="提示",buttons=["Yes","No"])
if(text=="Yes"):
    im1 = pyautogui.screenshot('my_screenshot.png')
    pyautogui.alert(text="截图成功",title="提示",button="OK")
else:
    pyautogui.alert(text="取消截图",title="提示",button="OK")
