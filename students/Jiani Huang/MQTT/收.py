from MXMqtt import MXMqtt

MQTTMOST = "mqtt.16302.com"
MQTTPORT = 1883
mqtt = MXMqtt(MQTTMOST,MQTTPORT)

mqtt.SUB("jia")
mqtt.SUB("yi")

while True:
    msg = mqtt.returnMsg()
    if msg != None:
        print(msg[1]+": "+msg[0])
