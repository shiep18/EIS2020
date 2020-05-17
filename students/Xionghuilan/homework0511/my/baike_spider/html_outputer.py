class HtmlOutputer(object):
    def __init__(self):
        # 创建一个空列表来存放数据
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)     # data 数据类型是字典 datas是列表 列表里面每个元素都是字典

    def output_html(self):
        with open("Output.html", encoding='utf-8', errors='ignore')as fp:
            fp.write("<html>")
            fp.write('<head><meta http-equiv="content-type" content="text/html;charset=utf-8"></head>')
            fp.write("<body>")
            fp.write("<table>")

            for data in self.datas:
                fp.write("<tr>")
                fp.write("<td>%s</td>" % data['url'])
                fp.write("<td>%s</td>" % data['title'])
                fp.write("<td>%s</td>" % data['summary'])
                fp.write("</tr>")

            fp.write("</table>")
            fp.write("</body>")
            fp.write("</html>")