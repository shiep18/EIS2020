import time
from selenium import webdriver

question = input("请输入想搜索的内容：\n")
driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.baidu.com/')

search = driver.find_element_by_id('kw')
search.send_keys(question)
search.submit()
