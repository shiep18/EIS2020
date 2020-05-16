import time
from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://accounts.douban.com/login")

driver.find_element_by_xpath('//*[@id="account"]/div[2]/div[2]/div/div[1]/ul[1]/li[2]').click()

user=driver.find_element_by_id('username')
user.send_keys("17621776825")
passw=driver.find_element_by_id('password')
passw.send_keys("123456123")

driver.find_element_by_xpath('//*[@id="account"]/div[2]/div[2]/div/div[2]/div[1]/div[4]/a').click()

time.sleep(3)
search=driver.find_element_by_id('inp-query')
search.send_keys("selenium")
driver.find_element_by_xpath('//*[@id="db-nav-sns"]/div/div/div[2]/form/fieldset/div[2]/input').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[2]/ul/li[3]/a').click()
time.sleep(3)
name=driver.find_elements_by_xpath('//*[@id="content"]/div/div[1]/div[3]/div[2]/div[*]/div[2]/div/h3/a')
print("Found " + str(len(name)) + ":")
for i in name:
    print(i.text)
