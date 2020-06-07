from MXMqtt import MXMqtt
import time
MQTTHOST = "mqtt.16302.com"
MQTTPORT = 1883
mqtt = MXMqtt(MQTTHOST,MQTTPORT)

topic="test123"
mqtt.SUB(topic)
while True:
    mqtt.PUB(topic,"team4THD:"+input("请输入："))
            
    msg = mqtt.returnMsg()
    print(msg[1]+":"+msg[0])