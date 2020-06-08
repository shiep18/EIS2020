from newTest19.MXMqtt import MXMqtt

MQTTHOST = "mqtt.16302.com"
MQTTPORT= 1883
mqtt = MXMqtt(MQTTHOST, MQTTPORT)

mqtt.SUB("zzm")
mqtt.SUB("langyuan")
mqtt.SUB("fyt")
mqtt.SUB("cjm")
mqtt.SUB("moocyue")
mqtt.SUB("EIS1")
mqtt.SUB("EIS2")
mqtt.SUB("EIS3")
mqtt.SUB("EIS4")
mqtt.SUB("EIS5")

while True:
    msg = mqtt.returnMsg()
    if msg is not None:
        print(msg)
