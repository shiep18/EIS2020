import pyautogui
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()  # 窗口最大化显示

#driver.get("https://www.taobao.com")
driver.get('http://www.baidu.com')
#s=driver.find_element_by_xpath('//*[@id="db-global-nav"]/div/div[4]/ul/li[3]/a').click()
s=driver.find_element_by_xpath('//*[@id="kw"]')

s.send_keys('曹嘉扬 上海电力大学')
s=driver.find_element_by_xpath('//*[@id="su"]').click()
