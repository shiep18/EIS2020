from MXMqtt import MXMqtt

MQTTHOST = "mqtt.16302.com"
MQTTPORT = 1883
mqtt = MXMqtt(MQTTHOST,MQTTPORT)

topic = "TalkRoom"

mqtt.SUB(topic)
mqtt.SUB("oys")

while True:
    msg = mqtt.returnMsg()
    if msg != None:
        print(msg)
    
