from selenium import webdriver
import time

def switch():
    # 切换到新窗口句柄
    driver.implicitly_wait(3)
    all_h = driver.window_handles
    driver.switch_to.window(all_h[-1])
    
driver = webdriver.Chrome()
driver.maximize_window()  # 窗口最大化显示
driver.get("https://accounts.douban.com/login")

#登陆
driver.find_element_by_xpath('//*[@id="account"]/div[2]/div[2]/div/div[1]/ul[1]/li[2]').click()
driver.find_element_by_id('username').send_keys("13917730292")
driver.find_element_by_id('password').send_keys("19981127@hjn")
driver.find_element_by_xpath('//*[@id="account"]/div[2]/div[2]/div/div[2]/div[1]/div[4]/a').click()
switch()

#搜索
search=driver.find_element_by_xpath('//*[@id="inp-query"]')
search.send_keys("selenium")
search.submit()
switch()
driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[2]/ul/li[3]/a').click()
switch()
names = driver.find_elements_by_xpath('//*[@id="content"]/div/div[1]/div[3]/div[2]/div[*]/div[2]/div/h3/a')
print("Found "+str(len(names))+":")
for i in names:
    a=i.text
    print(a)
