from MXMqtt import MXMqtt

MQTTMOST = "mqtt.16302.com"
MQTTPORT = 1883
mqtt = MXMqtt(MQTTMOST,MQTTPORT)

# mqtt.SUB("nM5wrxSb0VUIxAYq")
mqtt.SUB("mqtt0605")
# mqtt.SUB("hjn")
# mqtt.SUB("caojiayang")
# mqtt.SUB("wyh1560")
# mqtt.SUB("20171581")
# mqtt.SUB("mooc12345")

while True:
    msg = mqtt.returnMsg()
    if msg !=None:
        print(msg)