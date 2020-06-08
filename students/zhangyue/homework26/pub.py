from newTest19.MXMqtt import MXMqtt
import time

MQTTHOST = "mqtt.16302.com"
MQTTPORT= 1883
mqtt = MXMqtt(MQTTHOST, MQTTPORT)
topic1 = "EIS1"
topic2 = "EIS2"
topic3 = "EIS3"
topic4 = "EIS4"
topic5 = "EIS5"
arr = [0, 0, 0, 0, 0]


def arr_get(at):
    arr[0] = int(at / 10000)
    arr[1] = int(at / 1000) - int(at / 10000)*10
    arr[2] = int(at / 100) - int(at / 1000)*10
    arr[3] = int(at / 10) - int(at / 100)*10
    arr[4] = int(at / 1) - int(at / 10)*10
    return arr


while True:
    # a = int(input("input:"))
    a = 11111
    arr = arr_get(a)
    mqtt.PUB(topic1, arr[0])
    mqtt.PUB(topic2, arr[1])
    mqtt.PUB(topic3, arr[2])
    mqtt.PUB(topic4, arr[3])
    mqtt.PUB(topic5, arr[4])
    time.sleep(1)
    a = 11110
    arr = arr_get(a)
    mqtt.PUB(topic1, arr[0])
    mqtt.PUB(topic2, arr[1])
    mqtt.PUB(topic3, arr[2])
    mqtt.PUB(topic4, arr[3])
    mqtt.PUB(topic5, arr[4])
    time.sleep(1)
    a = 11100
    arr = arr_get(a)
    mqtt.PUB(topic1, arr[0])
    mqtt.PUB(topic2, arr[1])
    mqtt.PUB(topic3, arr[2])
    mqtt.PUB(topic4, arr[3])
    mqtt.PUB(topic5, arr[4])
    time.sleep(1)
    a = 110
    arr = arr_get(a)
    mqtt.PUB(topic1, arr[0])
    mqtt.PUB(topic2, arr[1])
    mqtt.PUB(topic3, arr[2])
    mqtt.PUB(topic4, arr[3])
    mqtt.PUB(topic5, arr[4])
    time.sleep(1)
    a = 10
    arr = arr_get(a)
    mqtt.PUB(topic1, arr[0])
    mqtt.PUB(topic2, arr[1])
    mqtt.PUB(topic3, arr[2])
    mqtt.PUB(topic4, arr[3])
    mqtt.PUB(topic5, arr[4])
    time.sleep(1)
    a = 0
    arr = arr_get(a)
    mqtt.PUB(topic1, arr[0])
    mqtt.PUB(topic2, arr[1])
    mqtt.PUB(topic3, arr[2])
    mqtt.PUB(topic4, arr[3])
    mqtt.PUB(topic5, arr[4])
    time.sleep(1)
