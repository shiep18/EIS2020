from newTest19.MXMqtt import MXMqtt
import time

MQTTHOST = "mqtt.16302.com"
MQTTPORT= 1883
mqtt = MXMqtt(MQTTHOST, MQTTPORT)
topic1 = "EIS1"
topic2 = "EIS2"
topic3 = "EIS3"
topic4 = "EIS4"
topic5 = "EIS5"
arr = [0, 0, 0, 0, 0]

while True:
    mqtt.PUB('nM5wrxSb0VUIxAYq', input("input:"))
