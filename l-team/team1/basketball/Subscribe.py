
import MXMqtt as MXMqtt
import time

MQTTHOST = "mqtt.16302.com"
MQTTPORT = 1883
mqtt = MXMqtt.MXMqtt(MQTTHOST,MQTTPORT)
a=0
mqtt.SUB("WZY123")
A = ''
while True:
     #mqtt.PUB(topic,input("输入："))
   msg = mqtt.returnMsg()
   f=open("C:\\Apache24\\htdocs\\index1.html", "w")#Apache要一直更新，否则数据消失
   if msg:                                          #防None时出错
       f.write(str(msg[0]))
       A = str(msg[0])
       print(msg[0][1])
   else:
       f.write(A)

   f.close()      
   
