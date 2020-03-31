import requests
import os


def getMusicInfo(keyword):
    url = "https://api.apiopen.top/searchMusic?name=" + keyword
    res = requests.post(url)
    info = dict(res.json())
    info = dict(info)
    return info

def getMusicRankings():
    url = "https://api.apiopen.top/musicRankings"
    res = requests.post(url)
    info = dict(res.json())
    info = dict(info)
    result = info["result"][0]["content"][0]["title"]
    return result

def getMusicUrl(keyword):
    info = getMusicInfo(keyword)
    musicUrl = info["result"][0]["url"]
    print("keyword=%s"%keyword)
    print("歌名：%s"%(info["result"][0]["title"]))
    return musicUrl

def downMusic(keyword):
    try:
        if keyword == "":
            keyword = getMusicRankings()
        musicUrl = getMusicUrl(keyword)
    except:
        keyword = getMusicRankings()
        musicUrl = getMusicUrl(keyword)
    
    print(musicUrl)
    os.system("wget "+ musicUrl + " -O back.mp3")
    playVoice("back.mp3")

def playVoice(fileName):
    # os.system("madplay -v " + fileName)
    os.system(fileName)
    

#downMusic("bad guy")
