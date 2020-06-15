from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from conver import conver

driver = webdriver.Chrome()
driver.maximize_window()  # 窗口最大化显示

driver.get('http://jw.shiep.edu.cn/eams/index.action')

login = driver.find_element_by_xpath('//*[@id="loginForm"]/table[2]/tbody/tr[2]/td[2]/a')
login.click()

time.sleep(2)
username = driver.find_element_by_xpath('//*[@id="username"]')
username.send_keys(!secret username)
password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys(!secret password)


login_button = driver.find_element_by_xpath('//*[@id="casLoginForm"]/p[5]/button')
login_button.click()

myTable = driver.find_element_by_link_text('我的课表')
myTable.click()
time.sleep(10)

term = driver.find_element_by_xpath('//*[@title="学年学期"]')
term.click()

time.sleep(10)
term2 = driver.find_element_by_xpath('//*[@id="semesterCalendar_yearTb"]/tbody/tr[2]/td[3]')
term2.click()

time.sleep(10)
term3 = driver.find_element_by_xpath('//*[@id="courseTableForm"]/div[2]/input[2]')
term3.click()

time.sleep(2)
# courses = driver.find_elements_by_xpath('//*[contains(@id,"TD")]')
# courses = driver.find_elements_by_xpath('//*[@id="manualArrangeCourseTable"]/tbody/tr[*]')
courses = driver.find_elements_by_xpath('//*[@class="infoTitle"]')

dic = {i.get_attribute('id'):(i.text,i.get_attribute('rowspan'))for i in courses}

time.sleep(5)

conver(dic)

