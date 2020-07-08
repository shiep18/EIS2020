from moocxing import MOOCXING
from robot.Brain import Brain
from threading import Thread
import time

mx = MOOCXING()

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
mc = mx.initMinecraft("47.100.46.95",4781)
entityId= mc.getPlayerEntityId("ZKX")
pos=mc.entity.getTilePos(entityId)
mc.setBlock(pos.x - 2, pos.y, pos.z, 84)

follow_flag = False
stop_flag = False
wake_flag = False
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

def follow(entityId):

    while follow_flag:
        pos = mc.entity.getTilePos(entityId)
        x1 = pos.x
        y1 = pos.y
        z1 = pos.z
        mc.setBlock(x1 - 2, y1, z1, 84)
        time.sleep(1)
        mc.setBlock(x1 - 2, y1, z1, 0)
        time.sleep(0.1)
        if stop_flag:
            mc.setBlock(x1 - 2, y1, z1, 84)

def turnOn():
    mc.setBlock(-491, 1, -399, 169)
    mc.setBlock(-495, 1, -399, 169)
    for t in range(12):
        mc.setBlock(-499, 1, -401 - 3 * t, 169)

def turnOff():
    mc.setBlock(-491, 1, -399, 155)
    mc.setBlock(-495, 1, -399, 155)
    for t in range(12):
        mc.setBlock(-499, 1, -401 - 3 * t, 155)

def curtain():
    mc.setBlock(-494, 1, -428, 0)
    mc.setBlock(-495, 1, -428, 0)
    mc.setBlock(-496, 1, -428, 0)
    mc.setBlock(-497, 1, -428, 0)

while True:
    if not wake_flag:
        TTSplay('主人天亮了，该起床去上班了')
    result = recordSTT()
    print(result)
    if '小白' in result:
        wake_flag = True
        TTSplay('我在')
        order = recordSTT()
        if '暂停' in order:
            media.isPause = True
        if '继续' in order:
            media.isPause = False
        if '停下' in order:
            TTSplay('好的')
            stop_flag = True
            follow_flag = False
        if '跟着我' in order:
            TTSplay('好的')
            follow_flag = True
            fl = Thread(target=follow, args=(entityId,)).start()
        if '开个灯' in order:
            turnOn()
            TTSplay('灯已打开')
        if '关灯'in order:
            turnOff()
            TTSplay('灯已关闭')
        if '窗帘'in order:
            curtain()
            TTSplay('窗帘已打开')
        Thread(target=brain.query,args=(order,)).start()