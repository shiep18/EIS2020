from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()  # 窗口最大化显示

driver.get('https://www.douban.com')
# driver.get('https://accounts.douban.com')
driver.switch_to.frame(driver.find_elements_by_tag_name('iframe')[0])

login = driver.find_element_by_class_name("account-tab-account")
login.click()

username = driver.find_element_by_xpath('//*[@id="username"]')
username.send_keys("12345678901")
password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys("******")

login_button = driver.find_element_by_link_text('登录豆瓣')
login_button.click()

driver.switch_to_default_content()
time.sleep(2)

search = driver.find_element_by_name('q')
search.send_keys("selenium")
search.submit()
driver.implicitly_wait(10) # seconds

label = driver.find_element_by_link_text('书籍')
label.click()

more = driver.find_element_by_link_text('显示更多')
more.click()

names = driver.find_elements_by_xpath('//*[@id="content"]/div/div[1]/div[3]/div[2]/div[*]/div[2]/div/h3/a')
print("Found " + str(len(names)) + ":")
for i in names:
    a = i.text
    print(a)

# 拼图验证
# time.sleep(2)
# driver.switch_to.frame("tcaptcha_popup")
# target_ele = driver.find_element_by_id("slideBlock")
# # 创建一个拖动对象
# action = ActionChains(driver)
# # 点击拖动对象并长按保持
# action.click_and_hold(target_ele)

# # 模拟拖动5次，每次拖动17个像素点
# for i in range(5):
#     # 执行拖动动作
#     action.move_by_offset(15, 0).perform()
#     # 每拖动17像素暂停5秒
#     time.sleep(2)

# # 释放拖动对象句柄
# action.release()

