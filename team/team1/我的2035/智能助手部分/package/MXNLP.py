import requests
import json
print("MXNLP")

class MXNLP():
    def __init__(self, APP_ID, API_KEY, SECRET_KEY):
        self.APP_ID = APP_ID
        self.API_KEY = API_KEY
        self.SECRET_KEY = SECRET_KEY

        self.token = self._getToken()

    def _getToken(self):
        """获取token"""
        url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + self.API_KEY + '&client_secret=' + self.SECRET_KEY
        response = requests.get(url)
        if response:
            return response.json()["access_token"]

    def getInfo(self, text):
        """获取词法分析结果"""
        url = "https://aip.baidubce.com/rpc/2.0/nlp/v1/lexer?charset=UTF-8&access_token=" + self.token
        header = {"Content-Type": "application/json"}
        data = json.dumps({"text": text})

        res = requests.post(url, headers=header, data=data)
        return res.json()["items"]

    def getCity(self, text):
        """获取城市名称"""
        for item in self.getInfo(text):
            if item["ne"] == "LOC":
                return item["item"]

    def getMusicName(self, text):
        """获取歌曲名称"""
        items = self.getInfo(text)
        result = ""
        for i,item in enumerate(items):
            if any(key in item["item"] for key in ["听", "放", "首"]):
                for it in items[i+1:]:
                    result += it["item"]
                return result


