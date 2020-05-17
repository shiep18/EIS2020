import pyautogui
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()  # 窗口最大化显示

driver.get('https://accounts.douban.com/login')

s=driver.find_element_by_xpath('//*[@id="account"]/div[2]/div[2]/div/div[1]/ul[1]/li[2]').click()
s=driver.find_element_by_xpath('//*[@id="username"]')
s.send_keys('18217148825')
s=driver.find_element_by_xpath('//*[@id="password"]')
s.send_keys('50344807a')
s=driver.find_element_by_xpath('//*[@id="account"]/div[2]/div[2]/div/div[2]/div[1]/div[4]/a').click()
time.sleep(2)
all_h = driver.window_handles

driver.switch_to.window(all_h[-1])
s=driver.find_element_by_xpath('//*[@id="inp-query"]')
s.send_keys('selenium')
s=driver.find_element_by_xpath('//*[@id="db-nav-sns"]/div/div/div[2]/form/fieldset/div[2]/input').click()
time.sleep(2)
all_h = driver.window_handles

driver.switch_to.window(all_h[-1])
s=driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[2]/ul/li[3]/a').click()

names = driver.find_elements_by_xpath('//*[@id="content"]/div/div[1]/div[3]/div[2]/div[*]/div[2]/div/h3/a')
print("Found " + str(len(names)) + ":")
for i in names:
    a = i.text
    print(a)
