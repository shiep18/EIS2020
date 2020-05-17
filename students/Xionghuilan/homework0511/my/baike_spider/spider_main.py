# !/usr/bin/env pyton3
# -*- coding:utf-8 -*-

# baike_spider 一个简单爬虫开发
# 语言版本：python3.5.1
# 功能说明：爬取百度百科词条和词条简介内容并输出到网页中
# 注：面向对象编程 全部采用对象来调用方法
'''
  程序执行流程：
    1.将 入口URL（root_url） 添加到 URL管理器
    2.启动爬虫的循环
    3.获取 URL管理器 待爬取列表 中的一个URL并将其移出待爬取列表，添加到已爬取列表
    4.使用HTML下载器下载这个页面
    5.使用解析器解析下载的页面,得到新的URL和数据
    6.将得到的新的URL批量添加到URL管理器中,在过程中判断得到的URL是否是已经爬取过的URL,采取舍去或者保留
    7.收集得到的页面内容,存入输出器，解析后输出
    8.循环3-7
    9.循环条件不符合退出循环时,将结果输出到html文件中
'''
# 模块设计
# URL管理器：UrlManager
# HTML下载器：HTMLDownloader
# 网页解析器：HtmlParser
# 结果输出器：HtmlOutputer

import html_downloader
import html_outputer
import html_parser
import url_manager

class SpiderMain(object):
    # 默认构造,创建对象时自动执行
    # 初始化所需的各个对象：下载器、解析器、URL管理器、输出器
    def __init__(self):
        self.urls = url_manager.UrlManager()                # URL管理器
        self.downloader = html_downloader.HtmlDownloader()  # HTML下载器
        self.parser = html_parser.HtmlParser()              # 网页解析器
        self.outputer = html_outputer.HtmlOutputer()        # 输出器

    # 爬虫 功能代码
    def craw(self, root_url):
        # 计数器
        count = 1
        # 将 root_url 添加到 URL管理器 中的 待爬取列表
        self.urls.add_new_url(root_url)
        # 启动 爬虫 循环流程
        while self.urls.has_new_url():                      # has_new_url() 判断URL管理器中是否还有待爬取URL
            # 还有待爬取URL,进入循环，获取待爬取URL
            new_url = self.urls.get_new_url()
            # 启动HTML下载器,下载网页
            html_content = self.downloader.download(new_url)
            # 启动网页解析器,获取网页中的 URL列表(多个URL) 和数据
            new_urls, new_data = self.parser.parse(new_url, html_content)
            # 将得到的 URL列表 批量 添加到URL管理器
            self.urls.add_new_urls(new_urls)
            # 收集得到的页面内容,存入输出器
            self.outputer.collect_data(new_data)
            # 打印爬取页面的信息
            print("crawle %d:%s\n" % (count, new_url))
            # 循环条件
            if count == 100:
                break
            count += 1
        # 输出器 将需要内容输出到 output.html 文件中
        self.outputer.output_html()

# 判断这个文件是不是独立执行而没有被作为模块来使用
# 如果是独立执行 则 __name__ == "__main__" 成立,执行程序
# 如果不是独立执行，则 条件 不成立,程序不执行
if __name__ == "__main__":
    # 入口URL
    root_url = "http://baike.baidu.com/view/21087.htm"
    # spider总调度程序,创建一个爬虫
    obj_spider = SpiderMain()
    # 启动爬虫，传入 入口URL
    obj_spider.craw(root_url)