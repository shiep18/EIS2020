from moocxing import MOOCXING
from robot.Brain import Brain
from threading import Thread

mx = MOOCXING()
# 初始化串口
#serial = mx.initSerial(mx.getComPorts(-1),9600)
# 初始化播放器和录音
media = mx.initMedia()

# 初始化语音识别+语音合成
APP_ID = '16901888'
API_KEY = 'qUcr9z2IVvREkyjDtlfbhsuv'
SECRET_KEY = 'preDe7g0C4ubTQ9XOir1afybwhD3jnAn'
speech = mx.initSpeech(APP_ID, API_KEY, SECRET_KEY)

# 初始化NLP
APP_ID = '19745053'
API_KEY = 'UnBq5gNtiZnReCKts31GiPlS'
SECRET_KEY = 'Ip2YLBAkGgbCp4xSv7TXjXojihipjFku'
nlp = mx.initNLP(APP_ID, API_KEY, SECRET_KEY)

# 初始化MQTT
MQTTHOST = "mqtt.16302.com"
MQTTPORT = 1883
mqtt = mx.initMqtt(MQTTHOST, MQTTPORT)

# 初始化我的世界
mc = mx.initMinecraft("47.100.46.95", 4785)
entityId = mc.getPlayerEntityId("zhuzhe")
print("********初始化完成********\n")

# 技能插件
SKILL = {"media": media, "speech": speech, "nlp": nlp}
brain = Brain(SKILL)
print("********技能插件加载完成********\n")
def TTSplay(text):
    speech.TTS(text)
    media.play()
def recordSTT():
    media.record(fname='record.wav')
    return speech.STT(fname='record.wav')
'''
TTSplay("你好,请问有什么可以帮您的？")
result = recordSTT()
print(result)
brain.query(result)
'''

lock=0
mqtt.SUB('设备状态/')


while True:
    pos=mc.entity.getTilePos(entityId)
    #pos=mc.player.getTilePos()
    print(pos)
    blockId=mc.getBlock(pos.x,pos.y-1,pos.z)
    if blockId==1 and lock==0:
        #mqtt.PUB('卧室/空调/',1)
        #msg=mqtt.returnMsg()
        #print(msg)
        #TTSplay('欢迎回家，'+msg[0])#
        #Thread(target=brain.query,args=('我要听歌',)).start()
        lock=1
    elif blockId==41 and lock==1:
        #media.isPlay=False
        #mqtt.PUB('卧室/空调/',0)
        #msg=mqtt.returnMsg()
        #print(msg)
        #TTSplay(msg[0]+',进入离家模式')#
        #brain.query('上海的天气')
        lock=0

'''
while True:
    order=recordSTT().replace('。',',')
    print(order)
    if '暂停' in order:
        media.isPause=True
    if '继续' in order:
        media.isPause=False
    if '停止' in order:
        media.isPlay=False
    Thread(target=brain.query,args=(order,)).start()
'''
#brain.query(recordSTT())
#brain.query('时间')
