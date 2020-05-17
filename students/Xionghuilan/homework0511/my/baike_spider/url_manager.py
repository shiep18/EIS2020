# URL管理器实现
class UrlManager(object):
    # 初始化URL管理器 中 待爬取列表 和 已爬取列表
    def __init__(self):
        # 初始化 待爬取列表 集合
        self.new_urls = set()
        # 初始化 已爬取列表 集合
        self.old_urls = set()

    # 添加单个URL到管理器中
    def add_new_url(self, url):
        if url is None:
            return
        # 如果当前URL既不在待爬取列表中，也不再未爬取列表中，则是一个全新的URL，添加到待爬取列表集合中
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)                                  # .add(url) 直接添加到列表中

    # 判断URL管理器中是否还有待爬取URL
    def has_new_url(self):
        # 将 len(self.new_urls)!=0 判断结果返回 （True or False）
        return len(self.new_urls) != 0

    # 从 待爬取列表 获取一条URL
    def get_new_url(self):
        # pop() 获取一条记录 并 移出 new_urls 列表
        new_url = self.new_urls.pop()
        # 添加到 old_urls 已爬取列表
        self.old_urls.add(new_url)
        return new_url

    # 批量添加新的URL 循环调用add_new_url
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)