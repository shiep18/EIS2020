from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()  # 窗口最大化显示


driver.get("https://www.baidu.com/")
search=driver.find_element_by_id('kw')
#search=driver.find_element_by_name('wd')
#search=driver.find_element_by_xpath('//*[@id="kw"]')
search.send_keys("jay")
search=driver.find_element_by_id('su').click()