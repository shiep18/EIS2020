import time
from selenium import webdriver
class douban(object):
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.url="https://accounts.douban.com/login"
        self.user_name="18616043519"
        self.password="1999120GCH"

    def input(self):
        self.driver.get(self.url)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="account"]/div[2]/div[2]/div/div[1]/ul[1]/li[2]').click()
        #获取标签
        user_el=self.driver.find_element_by_id("username")
        #输入账号
        user_el.send_keys(self.user_name)
        #输入密码
        password_el=self.driver.find_element_by_id("password")
        password_el.send_keys(self.password)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[4]/a').click()

    def tearDown(self):
        self.driver.close()
    def search(self):
        search=self.driver.find_element_by_id("inp-query")
        search.send_keys("selenium")
        search.submit()
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[2]/ul/li[3]/a').click()
    def album_name(self):
        names = self.driver.find_elements_by_xpath('//*[@id="content"]/div/div[1]/div[3]/div[2]/div[*]/div[2]/div/h3/a')
        print("Found " + str(len(names)) + ":")
        for i in names:
            a = i.text
            print(a)

    def run(self):
        self.input()
        time.sleep(3)
        self.search()
        time.sleep(2)
        self.album_name()
        #self.tearDown()

if __name__=='__main__':
    Douban=douban()
    Douban.run()
