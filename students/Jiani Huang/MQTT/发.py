from MXMqtt import MXMqtt
import time
MQTTMOST = "mqtt.16302.com"
MQTTPORT = 1883
mqtt = MXMqtt(MQTTMOST,MQTTPORT)

mqtt.SUB("jia")
mqtt.SUB("yi")

while True:
    mqtt.PUB("jia",input("输入："))
    time.sleep(1)
    mqtt.PUB("yi",input("输入："))

