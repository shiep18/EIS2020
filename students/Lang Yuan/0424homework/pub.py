
from MXMqtt import MXMqtt
import time

MQTTHOST = "mqtt.16302.com"
MQTTPORT = 1883
mqtt = MXMqtt(MQTTHOST,MQTTPORT)

topic = "langyuan"

mqtt.SUB(topic)

mqtt.SUB("mooc12345")





while True:
    mqtt.PUB("EIS1",0)
    mqtt.PUB("EIS2",0)
    mqtt.PUB("EIS3",0)
    mqtt.PUB("EIS4",0)
    mqtt.PUB("EIS5",0)
    delay(10)

    mqtt.PUB("EIS1",0)
    mqtt.PUB("EIS2",0)
    mqtt.PUB("EIS3",1)
    mqtt.PUB("EIS4",1)
    mqtt.PUB("EIS5",0)
    delay(10)

    mqtt.PUB("EIS1",1)
    mqtt.PUB("EIS2",1)
    mqtt.PUB("EIS3",1)
    mqtt.PUB("EIS4",1)
    mqtt.PUB("EIS5",1)
    delay(10)



