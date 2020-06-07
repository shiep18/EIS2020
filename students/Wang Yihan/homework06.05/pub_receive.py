from MXMqtt import MXMqtt
MQTTHOST = "mqtt.16302.com"
MQTTPORT = 1883
mqtt = MXMqtt(MQTTHOST,MQTTPORT)

mqtt.SUB("wyh1560")
#mqtt.SUB("hjn")
#mqtt.SUB("caojiayang")
#mqtt.SUB("fhz")
#mqtt.SUB("xhl")
#mqtt.SUB("20171581")
#mqtt.SUB("EIS3")

while True:
    
    msg = mqtt.returnMsg()
    if msg != None:
        print(msg[0])
     
