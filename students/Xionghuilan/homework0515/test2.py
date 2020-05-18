import pyautogui
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()  # 窗口最大化显示
driver.get("https://www.baidu.com")

search=driver.find_element_by_id('kw')
search.send_keys("上海电力大学")

pyautogui.keyDown('enter')
