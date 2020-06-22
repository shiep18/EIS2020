import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.baidu.com/')

driver.find_element_by_id("virus-2020").click()

all_h = driver.window_handles
# 切换到新窗口句柄
driver.switch_to.window(all_h[-1])
