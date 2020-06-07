from MXMqtt import MXMqtt
import time as t

MQTTHOST = "mqtt.16302.com"
MQTTPORT = 1883
mqtt = MXMqtt(MQTTHOST,MQTTPORT)

topic = "test123"
mqtt.SUB(topic)
while True:
    mqtt.PUB(topic,'team4jsj：'+input("输入："))

'''
#topic = "jsj"
#mqtt.SUB(topic)
s=[['0','0','0','1','0'],
   ['0','0','1','1','0'],
   ['1','1','1','0','0'],
   ['1','1','1','1','0'],
   ['1','1','1','1','1'],
   ['1','0','0','0','1'],
   ['0','0','0','1','0'],#7
   ['0','0','0','1','1']
   ]
while True:
    c=input('输入：')
    for i in c:
        mqtt.PUB('EIS1',s[int(i)-1][0])
        mqtt.PUB('EIS2',s[int(i)-1][1])
        mqtt.PUB('EIS3',s[int(i)-1][2])
        mqtt.PUB('EIS4',s[int(i)-1][3])
        mqtt.PUB('EIS5',s[int(i)-1][4])
        t.sleep(1)
'''
