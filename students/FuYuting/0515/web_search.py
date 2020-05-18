import time
from selenium import webdriver

#百度搜索并清空再搜索
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")

search=driver.find_element_by_id('kw')
search.send_keys("jay")
search.submit()
time.sleep(2)

search.clear()
search=driver.find_element_by_xpath("//*[@id='kw']")
search.send_keys("哪吒闹海")
search.submit()
