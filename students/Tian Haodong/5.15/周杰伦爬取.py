import time
from selenium import webdriver
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://accounts.douban.com/login")

driver.find_element_by_xpath('//*[@id="account"]/div[2]/div[2]/div/div[1]/ul[1]/li[2]').click()

login=driver.find_element_by_xpath('//*[@id="username"]')
login.send_keys('13679338393')
password=driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys('qweasd991035')

driver.find_element_by_xpath('//*[@id="account"]/div[2]/div[2]/div/div[2]/div[1]/div[4]/a').click()

time.sleep(2)

search=driver.find_element_by_xpath('//*[@id="inp-query"]')
search.send_keys("周杰伦")
search.submit()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[2]/ul/li[4]/a').click()
time.sleep(3)
names=driver.find_elements_by_xpath('//*[@id="content"]/div/div[1]/div[3]/div[2]/div[*]/div[2]/div/h3')

time.sleep(3)
print("Found"+str(len(names))+":")
for i in names:
    a=i.text
    print(a)

#driver.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]').click()
