import time
from selenium import webdriver

class douban(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # 隐式等待
        self.driver.implicitly_wait(3)
        self.url = "https://accounts.douban.com/login"
        self.user_name = "18621833081"
        
        self.password = 'hello..com'

    def input(self):
        self.driver.get(self.url)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="account"]/div[2]/div[2]/div/div[1]/ul[1]/li[2]').click()
        #获取标签
        user_el=self.driver.find_element_by_id("username")
        #输入账号
        user_el.send_keys(self.user_name)
        #输入密码
        pwd_el=self.driver.find_element_by_id("password")
        pwd_el.send_keys(self.password)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[4]/a').click()
    def search(self):
        search_field=self.driver.find_element_by_name("q")
        search_field.send_keys("selenium")
        search_field.submit()
        #search_music = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div/h3/a').click()
    def album_name(self):
        b=[]
        names = self.driver.find_elements_by_xpath('//*[@id="content"]/div/div[1]/div[3]/div[2]/div[*]/div[2]/div/h3/a')
        span = self.driver.find_elements_by_xpath('//*[@id="content"]/div/div[1]/div[3]/div[2]/div[*]/div[2]/div/h3/span')
        for i in span:
            if i.text=='可试读' or i.text=='有电子版':
                continue
            else:
                b.append(i.text)
        print("Found " + str(i) + ":")
        for j in range(int(len(b))):
            if b[j]=='[书籍]':
                print(names[j].text)
    def tearDown(self):
        self.driver.close()
    def run(self):
        # 主逻辑
        self.input()
        time.sleep(3)
        self.search()
        self.album_name()
        #self.tearDown()
if __name__ == '__main__':
    Douban=douban()
    Douban.run()
