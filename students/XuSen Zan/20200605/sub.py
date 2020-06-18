from MXMqtt import MXMqtt

MQTTHOST = "mqtt.16302.com"
MQTTPORT = 1883
mqtt = MXMqtt(MQTTHOST,MQTTPORT)

topic = "A14306416"
topic = "gch"
topic = "20171581"
mqtt.SUB(topic)

while True:
    msg = mqtt.returnMsg()
    if msg != None:
        print(msg)
