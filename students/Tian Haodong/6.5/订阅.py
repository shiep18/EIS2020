from MXMqtt import MXMqtt

MQTTHOST = "mqtt.16302.com"
MQTTPORT = 1883
mqtt = MXMqtt(MQTTHOST,MQTTPORT)


mqtt.SUB("test123")
while True:
    
    msg = mqtt.returnMsg()
    if msg != None:
        print(msg[0])