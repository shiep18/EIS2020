from MXMqtt import MXMqtt
import time

MQTTHOST = "mqtt.16302.com"
MQTTPORT = 1883
mqtt = MXMqtt(MQTTHOST,MQTTPORT)



while True:
         mqtt.PUB("sjc",input("输入："))

