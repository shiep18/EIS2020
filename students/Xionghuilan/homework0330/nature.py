import requests


def getCity(text):
    url = "https://api.shenjian.io/nlp/lexer?appid=07e8d355ba0a44f0d9580b669eb2bfc3&text=" + text
    res = requests.post(url)
    info = dict(res.json())
    info = dict(info)
    infoItems = info["data"]["items"]

    result = ""
    for num in range(len(infoItems)):
        if infoItems[num]["ne"] == "LOC":
            result = infoItems[num]["item"]
            break

    if result == "":
        return ""
    else:
        print()
        print("城市：%s"%result)
        return result


def getMusicName(text):
    url = "https://api.shenjian.io/nlp/lexer?appid=07e8d355ba0a44f0d9580b669eb2bfc3&text=" + text
    res = requests.post(url)
    info = dict(res.json())
    info = dict(info)
    infoItems = info["data"]["items"]
##    print(infoItems)
    result = ""
    for num in range(len(infoItems)):
        if infoItems[num]["item"] == "听" or infoItems[num]["item"] == "想听" or infoItems[num]["item"] == "要听" or infoItems[num]["item"] == "首" or infoItems[num]["item"] == "一首":
            num += 1
            for j in range(len(infoItems) - num):
                result += infoItems[num+j]["item"]
            break
    print()
    return result


##print(getMusicName(""))
