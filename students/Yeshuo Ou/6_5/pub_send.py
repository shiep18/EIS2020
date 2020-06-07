from MXMqtt import MXMqtt

MQTTHOST = "mqtt.16302.com"
MQTTPORT = 1883
mqtt = MXMqtt(MQTTHOST,MQTTPORT)



while True:
    mqtt.PUB("TalkRoom","oys:"+input("输入："))
    
    
