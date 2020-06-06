from MXMqtt import MXMqtt
import time
MQTTHOST="mqtt.16302.com"
MQTTPORT=1883
mqtt=MXMqtt(MQTTHOST,MQTTPORT)


topic="test123"
mqtt.SUB(topic)
while True:
    #mqtt.PUB("EIS1",input("输入:"))
    msg=mqtt.returnMsg()
    if msg!=None:
        print(msg[0])

# def jiandao():
#     mqtt.PUB("EIS1","0")
#     mqtt.PUB("EIS2","0")
#     mqtt.PUB("EIS3","1")
#     mqtt.PUB("EIS4","1")
#     mqtt.PUB("EIS5","0")
# def shitou():
#     mqtt.PUB("EIS1","0")
#     mqtt.PUB("EIS2","0")
#     mqtt.PUB("EIS3","0")
#     mqtt.PUB("EIS4","0")
#     mqtt.PUB("EIS5","0")
# def bu():
#     mqtt.PUB("EIS1","1")
#     mqtt.PUB("EIS2","1")
#     mqtt.PUB("EIS3","1")
#     mqtt.PUB("EIS4","1")
#     mqtt.PUB("EIS5","1")


# jiandao()
# time.sleep(0.1)
# shitou()
# time.sleep(0.1)
# bu()
