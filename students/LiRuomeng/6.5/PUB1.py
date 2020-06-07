from MXMqtt import MXMqtt
MQTTHOST = "mqtt.16302.com"
MQTTPORT = 1883
mqtt = MXMqtt(MQTTHOST,MQTTPORT)

mqtt.SUB("lrm1")
mqtt.SUB("zkx")
mqtt.SUB("oys1552")
mqtt.SUB("gch")
mqtt.SUB("wzy")
mqtt.SUB("mooc12345")

while True:
    
    msg = mqtt.returnMsg()
    if msg != None:
        print(msg)
  
