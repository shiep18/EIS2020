from MXMqtt import MXMqtt

MQTTHOST="mqtt.16302.com"
MQTTPORT=1883
mqtt=MXMqtt(MQTTHOST,MQTTPORT)



while True:
    mqtt.PUB("test123","team4wyb:"+input("输入："))
##mqtt.SUB("wyb1")
##mqtt.SUB("wyb2")
##mqtt.SUB("wyb3")
##mqtt.SUB("wyb4")
##mqtt.SUB("wyb5")
##
##while True:
##    msg=mqtt.returnMsg()
##    if msg!=None:
##        print(msg[1]+":"+msg[0])
