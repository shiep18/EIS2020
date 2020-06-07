from MXMqtt import MXMqtt

MQTTHOST = "mqtt.16302.com"
MQTTPORT = 1883
mqtt = MXMqtt(MQTTHOST,MQTTPORT)


mqtt.SUB('test123')
mqtt.SUB('EIS4')

while True:
    #mqtt.PUB(topic,input("输入："))
    msg = mqtt.returnMsg()
    if msg != None :
        print(msg[1]+": "+msg[0])
