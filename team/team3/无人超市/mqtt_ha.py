import pymysql
import MXMqtt as MXMqtt
import time

MQTTHOST = "mqtt.16302.com"
MQTTPORT = 1883
mqtt = MXMqtt.MXMqtt(MQTTHOST,MQTTPORT)
mqtt.SUB("sp")

conn = pymysql.connect('localhost', 'root', '', 'goods')
cursor = conn.cursor()
names = ['欧莱雅男士洁面乳','九制陈皮','农夫山泉550ml','《追风筝的人》','《阿波罗是如何飞到月球的》','德生牌收音机PL-380','清扬洗发露200g','《生死疲劳》']
sell = [0,0,0,0,0,0,0,0]
rest = [80,150,200,50,40,50,80,50]
##sql = "INSERT INTO goods (`name`, `sell`, `rest`) VALUES  ('《生死疲劳》','0','50');"
##cursor.execute(sql)
##conn.commit()
def update():     
    for i in range(8):
        sql = "UPDATE `goods` SET `sell`="+str(sell[i])+" WHERE name='"+names[i]+"'"
        cursor.execute(sql)
        conn.commit()
        sql = "UPDATE `goods` SET `rest`="+str(rest[i])+" WHERE name='"+names[i]+"'"
        cursor.execute(sql)
        conn.commit()
def download():
    for i in range(8):
       sql = "SELECT * FROM goods WHERE name='"+names[i]+"'"
       cursor.execute(sql)
       results = cursor.fetchall()
       for row in results:
          sell[i]=row[1]
          rest[i]=row[2]
          conn.commit()
def ha():
    for i in range(8):
        f=open("C:\\Users\\11722\\AppData\\Roaming\\.homeassistant\\custom_components\\Goods\\Goods"+str(i+1)+".txt", "w")
        f.write(str(sell[i])+","+str(rest[i]))
        f.close()
while True:
    download()
    ha()
    msg = mqtt.returnMsg()
    if msg:
        count = -1
        a=str(msg[0])
        a=a.split(',')
        for i in a:
            count+=1
            if i in names:
                n=names.index(i)
                sell[n]+=int(a[count+1])
                rest[n]-=int(a[count+1])
        print(sell,rest)
        update()
        ha()
