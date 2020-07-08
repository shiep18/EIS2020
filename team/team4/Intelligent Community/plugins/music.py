import requests
import os
import random
from threading import Thread
import time

from robot.sdk.AbstractPlugin import AbstractPlugin


class Plugin(AbstractPlugin):
    SLUG = "music"

    def getMusicInfo(self,keyword):
        url = "http://127.0.0.1:3000/search?keywords={}".format(keyword)
        res = requests.get(url)
        return res.json()["result"]["songs"][0]

    def getMusicRankings(self):
        url = "http://127.0.0.1:3000/personalized/newsong"
        res = requests.get(url)
        return res.json()["result"][random.randint(0, 9)]["song"]

    def getMusicUrl(self, musicID):
        url = "http://127.0.0.1:3000/song/url?id={}".format(musicID)
        res = requests.get(url)
        return res.json()["data"][0]["url"]

    def downMusic(self, keyword):
        try:
            info = self.getMusicInfo(keyword)
        except:
            info = self.getMusicRankings()

        musicUrl = self.getMusicUrl(info["id"])
        
        os.system("wget " + musicUrl + " -O back.mp3")
        os.system("ffmpeg -i back.mp3 -y back.wav")

        print(f'\n{info["artists"][0]["name"]}———{info["name"]}')

    def handle(self, query):
        #self.say("正在为你准备歌曲！")
        keyword = self.getMusicName(query)
        self.downMusic(keyword)
        self.play("back.wav")
        return None

    def isValid(self, query):
        return any(word in query for word in ["听", "放", "首", "歌"])
