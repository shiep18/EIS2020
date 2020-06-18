from MXMqtt import MXMqtt
import time

MQTTHOST = "mqtt.16302.com"
MQTTPORT = 1883
mqtt = MXMqtt(MQTTHOST,MQTTPORT)

def one():
    mqtt.PUB("EIS1",0)
    mqtt.PUB("EIS2",0)
    mqtt.PUB("EIS3",0)
    mqtt.PUB("EIS4",1)
    mqtt.PUB("EIS5",0)
    time.sleep(1)
def four():
    mqtt.PUB("EIS1",1)
    mqtt.PUB("EIS2",1)
    mqtt.PUB("EIS3",1)
    mqtt.PUB("EIS4",1)
    mqtt.PUB("EIS5",0)
    time.sleep(1)
def three():
    mqtt.PUB("EIS1",0)
    mqtt.PUB("EIS2",1)
    mqtt.PUB("EIS3",1)
    mqtt.PUB("EIS4",1)
    mqtt.PUB("EIS5",0)
    time.sleep(1)
while True:
    #mqtt.PUB("A14306416",input("输入："))
    #mqtt.PUB("gch",input("输入："))
    #mqtt.PUB("20171581",input("输入："))
    #mqtt.PUB("EIS2",input("输入："))
    one()
    four()
    three()
