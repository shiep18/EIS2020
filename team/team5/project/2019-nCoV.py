from urllib.parse import unquote
from httputils import gehtml
import matplotlib.pyplot as plt
import json
import re
from pycharts_utils import getmaps

url_code_name = "\u963f\u8054\u914b"
text = unquote(url_code_name, 'utf-8')
print(text)

text = gehtml('https://voice.baidu.com/act/newpneumonia/newpneumonia')
if text is not 'error':
    re_str = r'caseList(.*?),"dataSource'
    informations = re.findall(re_str, text, re.S | re.M)
    json_str = '{"caseList' + informations[0] + '}'
    json_str = json.loads(json_str)

    area = []
    confirmed = []
    died = []
    crued = []

    for detail in json_str["caseList"]:
        area.append(unquote(detail["area"], 'utf-8'))
        confirmed.append(int(detail["confirmed"]))
        map = getmaps(area, confirmed)
        map.render(path='china.html')
        if detail["died"] is not "":
            died.append(int(detail["died"]))
        else:
            died.append(0)
        if detail["crued"] is not "":
            crued.append(int(detail["crued"]))
        else:
            crued.append(0)
  
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    plt.figure(figsize=(15, 15))
    plt.subplot(131)
    plt.barh(area, confirmed)
    plt.ylabel(u'地区')
    plt.xlabel(u'感染人数')
    plt.title('各省感染人数')
    for i in range(33):
        plt.text(confirmed[i], area[i], confirmed[i])

    plt.subplot(132)
    plt.barh(area, died)
    plt.ylabel(u'地区')
    plt.xlabel(u'死亡人数')
    plt.title('各省死亡人数')
    for i in range(33):
        if died[i] is not 0:
            plt.text(died[i], area[i], died[i])

    plt.subplot(133)
    plt.barh(area, crued)
    plt.ylabel(u'地区')
    plt.xlabel(u'治愈人数')
    plt.title('各省治愈人数')
    for i in range(33):
        if crued[i] is not 0:
            plt.text(crued[i], area[i], crued[i])

    plt.show()
