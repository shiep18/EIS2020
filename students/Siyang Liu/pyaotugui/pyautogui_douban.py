from selenium import webdriver
import pyautogui
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://accounts.douban.com/passport/login')

#使用账号密码进行登录
driver.find_element_by_class_name('account-tab-account').click()
time.sleep(1)
driver.find_element_by_class_name('account-form-input').click()
pyautogui.typewrite('18018596064')
pyautogui.press('tab')
pyautogui.typewrite('Arthas0917')
pyautogui.press('enter')
time.sleep(2)

driver.find_element_by_xpath('//*[@id="db-global-nav"]/div/div[4]/ul/li[4]/a').click()
time.sleep(3)

driver.find_element_by_id('inp-query').click()
pyautogui.typewrite('David Garrett')
pyautogui.press('enter')
time.sleep(1)

name = driver.find_elements_by_xpath('//*[@id="content"]/div/div[1]/div[3]/div[2]/div[*]/div[2]/div/h3/a')

print("Music" + str(len(name)) + ":")
for i in name:
    print(i.text)
