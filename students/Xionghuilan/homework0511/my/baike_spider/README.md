# baike_spider 
[![DUB](https://img.shields.io/dub/l/vibe-d.svg)]()
![](https://img.shields.io/badge/language-python3.5-orange.svg)
[![](https://travis-ci.org/jerryhanjj/baike_spider.svg?branch=master)](https://travis-ci.org/jerryhanjj/baike_spider)
![](https://img.shields.io/badge/platform-win-green.svg)
![](https://img.shields.io/badge/release-v1.0.0-519dd9.svg)
<div>&nbsp;一个简单爬虫开发</div><div>&nbsp;语言版本：python3.5.1</div><div>&nbsp;功能说明：爬取百度百科词条和词条简介内容并输出到网页中</div><div>&nbsp;注：面向对象编程 全部采用对象来调用方法</div><div>&nbsp;</div><div>&nbsp;程序执行流程：</div><div>&nbsp; &nbsp; 1.将 入口URL（root_url） 添加到 URL管理器</div><div>&nbsp; &nbsp; 2.启动爬虫的循环</div><div>&nbsp; &nbsp; 3.获取 URL管理器 待爬取列表 中的一个URL并将其移出待爬取列表，添加到已爬取列表</div><div>&nbsp; &nbsp; 4.使用HTML下载器下载这个页面</div><div>&nbsp; &nbsp; 5.使用解析器解析下载的页面,得到新的URL和数据</div><div>&nbsp; &nbsp; 6.将得到的新的URL批量添加到URL管理器中,在过程中判断得到的URL是否是已经爬取过的URL,采取舍去或者保留</div><div>&nbsp; &nbsp; 7.收集得到的页面内容,存入输出器，解析后输出</div><div>&nbsp; &nbsp; 8.循环3-7</div><div>&nbsp; &nbsp; 9.循环条件不符合退出循环时,将结果输出到html文件中</div><div><br></div><div>&nbsp;模块设计：</div><div>&nbsp;URL管理器：UrlManager</div><div>&nbsp;HTML下载器：HTMLDownloader</div><div>&nbsp;网页解析器：HtmlParser</div><div>&nbsp;结果输出器：HtmlOutputer</div>
