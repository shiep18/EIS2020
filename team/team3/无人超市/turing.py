import speech_recognition as sr
from aip import AipSpeech
import requests
import json
import threading
from mcpi.minecraft import Minecraft
mc=Minecraft.create("47.100.46.95",4783)
entityId= mc.getPlayerEntityId("fhz")
entityId1= mc.getPlayerEntityId("cjy")
pos=mc.entity.getTilePos(entityId)
pos1=mc.entity.getTilePos(entityId1)
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
#百度API
APP_ID = '16847874'
API_KEY = '6XATdS1rGo2NV27jHGemaada'
SECRET_KEY = '0SINmEBfvotQXl1itzrMcwedaxuBaw4h'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
# 图灵机器人的API_KEY、API_URL
turing_api_key = "55c3d84baaa843e3832770d66a712a75"
api_url = "http://openapi.tuling123.com/openapi/api/v2"  # 图灵机器人api网址
headers = {'Content-Type': 'application/json;charset=UTF-8'}
path = 'voices/myvoices.wav'

def translate(word):
    # 有道词典 api
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
    # 传输的参数，其中 i 为需要翻译的内容
    key = {
        'type': "AUTO",
        'i': word,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_CLICKBUTTON",
        "typoResult": "true"
    }
    # key 这个字典为发送给有道词典服务器的内容
    response = requests.post(url, data=key)
    # 判断服务器是否相应成功
    if response.status_code == 200:
        # 然后相应的结果
        return response.text
    else:
        print("有道词典调用失败")
        # 相应失败就返回空
        return None

def get_reuslt(repsonse):
    # 通过 json.loads 把返回的结果加载成 json 格式
    result = json.loads(repsonse)
    print (result['translateResult'][0][0]['tgt'])
    mc.postToChat(result['translateResult'][0][0]['tgt'])

def translate_word(text):
    word = text
    list_trans = translate(word)
    get_reuslt(list_trans)

def my_record():
    rate = 16000   #录音参数必须满足 16k 采样率
    r = sr.Recognizer()  #实例化一个识别器r
    with sr.Microphone(sample_rate=rate) as source:   # 打开麦克风  句柄 source
        print("please say something")
        audio = r.listen(source)    #通过麦克风进行录音
    with open("voices/myvoices.wav", "wb") as f:  #设置文件名，类型
        f.write(audio.get_wav_data())             #将录音数据转换成wav格式写入文件
    print("录音完成！")

def listen():
    # 读取录音文件
    with open(path, 'rb') as fp:
        voices = fp.read()
    try:
        # 参数dev_pid：1536普通话(支持简单的英文识别)、1537普通话(纯中文识别)、1737英语、1637粤语、1837四川话、1936普通话远场
        result = client.asr(voices, 'wav', 16000, {'dev_pid': 1537, })
        result_text = result["result"][0]
        #print("you said: " + result_text)
        return result_text
    except KeyError:
        print("KeyError")

def turing(text_words=""):
    #请求
    if "天气" in text_words:
        a = "上海"
        url = 'http://wthrcdn.etouch.cn/weather_mini?city='+a
        response = requests.get(url)
        wearher_json = json.loads(response.text)
        a = wearher_json['data']
        result = a['city']+"今天气温"+a['wendu']+'摄氏度'+"天气"+a["forecast"][1]['type']
        print("AI Robot said: "+result)
    else:
        req = {
            "reqType": 0,       # 输入类型 为文本
            "perception": {
                "inputText": {
                    "text": text_words    # 输入文本信息
                },

                "selfInfo": {             # 客户端属性
                    "location": {
                        "city": "新干县",
                        "province": "江西省",
                        "street": "善政二路"
                    }
                }
            },
            #用户参数
            "userInfo": {
                "apiKey": turing_api_key,  # 你的图灵机器人apiKey
                "userId": "cheney007"  # 用户唯一标识(随便填, 非密钥)
            }
        }

        req["perception"]["inputText"]["text"] = text_words  #给json串赋值
        response = requests.request("post", api_url, json=req, headers=headers) #向接口网站发送请求
        response_dict = json.loads(response.text)

        result = response_dict["results"][0]["values"]["text"]  #得到接口的回复进行解析
        print("AI Robot said: " + result)
    return result

def speak(workText):
    speaker.Speak(workText)

def chat():
    mc.postToChat("Welcome,What can i do for you?")
    #speaker.Speak("欢迎光临，有什么需要我帮忙的吗？")
    a=True
    while a:
        my_record()
        text=listen()
        print("you said: " + text)
        translate_word(text)
        if "谢谢" in text:
            a=False
        elif "再见" in text:
            a=False
            #mc.player.setTilePos(83,-1,89)
        respondText=turing(text)
        translate_word(respondText)
        speak(respondText)

def follow():
    a=True
    while a:
        text=listen()
        if "谢谢" in text:
            a=False
            mc.player.setTilePos(83,-1,89)
            with open("voices/voices.wav", 'rb') as fp:
                voices = fp.read()
            with open("voices/myvoices.wav", "wb") as f:
                f.write(voices) 
        elif "再见" in text:
            a=False
            mc.player.setTilePos(83,-1,89)
            with open("voices/voices.wav", 'rb') as fp:
                voices = fp.read()
            with open("voices/myvoices.wav", "wb") as f:
                f.write(voices) 

        else:
            pos1=mc.entity.getTilePos(entityId1)
            pos=mc.entity.getTilePos(entityId)
            z=abs(pos1.z-pos.z)
            x=abs(pos1.x-pos.x)
            if x!=1 and z!=1:   
                mc.player.setTilePos(pos1.x-1,pos1.y,pos1.z-1)



def main():
    threads = []  # 用来存放执行read函数线程的列表

    t = threading.Thread(target=chat) # 执行的函数如果需要传递参数，threading.Thread(target=函数名,args=(参数，逗号隔开))
    threads.append(t)

    t1 = threading.Thread(target=follow) # 执行的函数如果需要传递参数，threading.Thread(target=函数名,args=(参数，逗号隔开)
    threads.append(t1)
    
    if __name__=='__main__':
        for t in threads:
            t.start()
        for t in threads:
            t.join()

#main()
#chat()
