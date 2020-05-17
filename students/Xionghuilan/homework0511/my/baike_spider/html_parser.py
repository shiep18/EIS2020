from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

# 解析器实现
# BeautifulSoup html.parse
class HtmlParser(object):
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # 获取格式匹配的URL 如 http://baike.baidu.com/view/21087.htm
        links = soup.find_all('a', href=re.compile(r'/view/\d+\.htm'))          # 正则表达式 \d+\ 表示数字
        for link in links:
            new_url = link['href']
            # 将两个URL自动匹配成完整的URL page_url new_url
            new_full_url = urljoin(page_url, new_url)
            # 添加到集合中
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        # 创建一个字典
        res_data = {}
        res_data['url'] = page_url
        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
        res_data['title'] = title_node.get_text()

        # 获取 词条简介的内容
        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_='lemma-summary')
        if summary_node is None:
            res_data['summary'] = "None summary!"
        else:
            res_data['summary'] = summary_node.get_text()

        return res_data
