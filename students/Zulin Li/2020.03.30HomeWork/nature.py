import requests
from xpinyin import Pinyin
def getPinYin(result):
    pin = Pinyin()
    return pin.get_pinyin(result)
def getCity(text):
    if getPinYin('上海') in getPinYin(text):
        return '上海'
    elif getPinYin('北京') in getPinYin(text):
        return '北京'
    elif getPinYin('广州') in getPinYin(text):
        return '广州'
    elif getPinYin('深圳') in getPinYin(text):
        return '深圳'
    elif getPinYin('成都') in getPinYin(text):
        return '成都'
def getMusicName(text):
    url = "https://api.shenjian.io/nlp/lexer?appid=07e8d355ba0a44f0d9580b669eb2bfc3&text=" + text
    res = requests.post(url)
    info = dict(res.json())
    info = dict(info)
    infoItems = info["data"]["items"]
    #print(infoItems)
    result = ""
    for num in range(len(infoItems)):
        if infoItems[num]["item"] == "听" or infoItems[num]["item"] == "想听" or infoItems[num]["item"] == "要听" or infoItems[num]["item"] == "首" or infoItems[num]["item"] == "一首":
            num += 1
            for j in range(len(infoItems) - num):
                result += infoItems[num+j]["item"]
            break
    print()
    return result   
            

#print(getMusicName(""))
