import MXMqtt as MXMqtt
import time

MQTTHOST = "mqtt.16302.com"
MQTTPORT = 1883
mqtt = MXMqtt.MXMqtt(MQTTHOST,MQTTPORT)

print("HA")
a=0
mqtt.SUB("HA")
A = 'DoorClose'
while True:
     #mqtt.PUB(topic,input("输入："))
   msg = mqtt.returnMsg()
   f=open("D:\\Users\\ouyes\\Desktop\\QRS\\work\\face\\face1\\index4.html", "w")#Apache要一直更新，否则数据消失
   if msg:                                          #防None时出错
       f.write(str(msg[0]))
       A = str(msg[0])
       print(A)      
   else:
       f.write(A)

   f.close()      
   
