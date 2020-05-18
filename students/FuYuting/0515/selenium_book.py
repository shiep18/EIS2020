import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://accounts.douban.com/passport/login")#进入豆瓣

search=driver.find_element_by_xpath('//*[@id="account"]/div[2]/div[2]/div/div[1]/ul[1]/li[2]').click() #密码登陆


search=driver.find_element_by_id('username')#输入账号和密码
search.send_keys("18930688887")
search=driver.find_element_by_id('password')
search.send_keys("  ")

search=driver.find_element_by_xpath('//*[@id="account"]/div[2]/div[2]/div/div[2]/div[1]/div[4]/a').click() #登陆
time.sleep(2)
all_h = driver.window_handles #切换到新的窗口
driver.switch_to.window(all_h[-1])

search=driver.find_element_by_id('inp-query')#点击右上角搜索框
search.send_keys("selenium")
search.submit()
time.sleep(1)
search_book=driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[2]/ul/li[3]/a').click() #书籍



time.sleep(2)
names =driver.find_elements_by_xpath('//*[@id="content"]/div/div[1]/div[3]/div[2]/div[*]/div[2]/div/h3/a')
print("Found " + str(len(names)) + ":")
for i in names:
    a = i.text
    print(a)


