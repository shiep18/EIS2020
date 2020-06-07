from MXMqtt import MXMqtt
import time
MQTTHOST = "mqtt.16302.com"
MQTTPORT = 1883
mqtt = MXMqtt(MQTTHOST,MQTTPORT)
'''
topic = "lrm1"
mqtt.SUB(topic)
topic = "lrm2"
mqtt.SUB(topic)
topic = "lrm3"
mqtt.SUB(topic)
topic = "lrm4"
mqtt.SUB(topic)
topic = "lrm5"
mqtt.SUB(topic)
'''

while True:
    mqtt.PUB("mooc12345","meng:"+input("请输入："))
