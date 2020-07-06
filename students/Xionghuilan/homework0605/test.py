from MXMqtt import MXMqtt

MQTTMOST = "mqtt.16302.com"
MQTTPORT = 1883
mqtt = MXMqtt(MQTTMOST,MQTTPORT)

topic = "mqtt0605"
mqtt.SUB(topic)

while True:
    mqtt.PUB(topic,input("输入："))
    msg = mqtt.returnMsg()
    print(msg[1]+":"+msg[0])