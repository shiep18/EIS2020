import json
from channels.generic.websocket import WebsocketConsumer

class Chatconsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, tesx_data):
        tesx_data_json = json.loads(tesx_data)
        message = tesx_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))