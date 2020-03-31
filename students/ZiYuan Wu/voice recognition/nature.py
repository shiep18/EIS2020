import requests


def getCity(text):
   # try:
      #  url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=19171403&client_id=98gXfS8CgOe0fIkLbm9Rrp4W&client_secret=AGn7c8tltmmdT84Omdpl7Phlz2EytyYI&" + text
      ##  res = requests.post(url)
      #  print(res)
      #  info = dict(res.json())
      #  print(info)
      #  info = dict(info)
       
   # except:
      #   print("problem")
         return ""
    
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
            

