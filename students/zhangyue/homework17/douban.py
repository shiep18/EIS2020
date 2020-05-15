import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'd:\\'}
options.add_experimental_option('prefs', prefs)

driver.get("https://www.douban.com/")

driver.switch_to.frame(driver.find_elements_by_tag_name('iframe')[0])
driver.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]').click()
driver.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]').click()

driver.find_element_by_id("username").send_keys('')  # 账号
driver.find_element_by_id("password").send_keys('')  # 密码
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[5]/a').click()

time.sleep(1)

driver.find_element_by_id('inp-query').send_keys('selenium')
driver.find_element_by_xpath('//*[@id="db-nav-sns"]/div/div/div[2]/form/fieldset/div[2]/input').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[2]/ul/li[3]/a').click()
while True:
    try:
        driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[3]/div[2]/div[*]/a').click()
    except:
        break
    else:
        time.sleep(0.2)

names = driver.find_elements_by_xpath('//*[@id="content"]/div/div[1]/div[3]/div[2]/div[*]/div[2]/div/h3/a')
print("Found " + str(len(names)) + ":")
for i in names:
    a = i.text
    print(a)
