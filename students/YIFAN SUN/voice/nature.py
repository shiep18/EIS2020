import requests
import json

APIKey='LuUwUnqxmZYd1pCuwmn1WyTL'
SecretKey='ZBsM5DV0IFAmYAQ1sAvOSYCGpqbgMqi2'

#得到请求url
def get_url():
    url=0
    #通过API Key和Secret Key获取access_token
    AccessToken_url='https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(APIKey,SecretKey)
    res = requests.get(AccessToken_url)
    json_data = json.loads(res.text)
    if not json_data or 'access_token' not in json_data:
        print("获取AccessToken的json数据失败")
    else:
        accessToken=json_data['access_token']
        #将得到的access_token加到请求url中
        url='https://aip.baidubce.com/rpc/2.0/nlp/v1/lexer?charset=UTF-8&access_token={}'.format(accessToken)
    return url

#创建请求，获取数据
def get_address(url,text):
    address=''#存储得到的地址
    body={
        "text": text,
    }
    body2 = json.dumps(body)#将字典形式的数据转化为字符串,否则报错
    #创建Header请求
    header={
        'content-type': 'application/json'
    }
    res = requests.post(url,headers=header,data=body2)# 推荐使用post
    json_data = json.loads(res.text)
    if not json_data or 'error_code' in json_data:
        # print(json.dumps(json_data, indent=4, ensure_ascii=False))
        print("获取关键词的Json数据失败")
    else:
        for item in json_data['items']:
            if item['ne'] == "LOC" :
                # print(item['item'])
                address = item['item']
        return address


def getCity(text):
    # url = "https://api.shenjian.io/nlp/lexer?appid=07e8d355ba0a44f0d9580b669eb2bfc3&text=" + text
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
    result = ""
    for num in range(len(infoItems)):
        if infoItems[num]["item"] == "听" or infoItems[num]["item"] == "想听" or infoItems[num]["item"] == "要听" or infoItems[num]["item"] == "首" or infoItems[num]["item"] == "一首":
            num += 1
            for j in range(len(infoItems) - num):
                result += infoItems[num+j]["item"]
            break
    print()
    return result   
