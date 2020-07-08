import time
import paho.mqtt.client as mqtt
print("MXMqtt")

class MXMqtt():
    def __init__(self, host, post):
        self.host = host
        self.post = post
        self.mqttClient = mqtt.Client()
        self.message = None
        self.flag = False
        self._connect()

    def _connect(self):
        self.mqttClient.connect(self.host, self.post, 60)
        self.mqttClient.loop_start()

    def _messageBack(self, client, userdata, msg):
        self.message = msg
        self.flag = True

    def PUB(self, topic, payload, qos = 1):
        """发布信息"""
        self.mqttClient.publish(topic, payload, qos)
        time.sleep(0.5)
    
    def SUB(self, topic, qos = 1):
        """订阅频道"""
        self.mqttClient.subscribe(topic, qos)
        self.mqttClient.on_message = self._messageBack

    def returnMsg(self):
        """获取返回的消息"""
        if self.flag == True:
            self.flag = False
            return self.message.payload.decode("utf-8"), self.message.topic
              

