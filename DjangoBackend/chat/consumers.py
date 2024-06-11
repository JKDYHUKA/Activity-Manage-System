import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer

# CONN_LIST=[]
class ChatConsumer(WebsocketConsumer):
    def websocket_connect(self, message):
        # 将这个客户端的连接对象加入到某个地方（内存 or redis）1314 是群号这里写死了
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = self.room_name
        print('arrive')

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name)
        print(self.room_group_name)
        # 接收这个客户端的连接
        self.accept()

    def websocket_receive(self, message):
        # 浏览器基于websocket向后端发送数据，自动触发接收消息
        print('222', message)
        data = json.loads(message['text'])
        chat_type = data.get('chat_type')
        chat_id = data.get('chat_id')
        print(chat_id)
        chat_content = data.get('message')
        print('chat_type', chat_type)
        # if chat_type == 'add_chat':
        #     async_to_sync(self.channel_layer.group_add)(
        #         chat_id, self.channel_name)
        # 通知组内的所有客户端，执行 chat_message 方法，在此方法中自己可以去定义任意的功能。
        async_to_sync(self.channel_layer.group_send)(
            chat_id, {"type": 'chat_message', 'message': message})

    # 这个方法对应上面的type，意为向1314组中的所有对象发送信息
    # 回调的方法
    def chat_message(self, event):
        text = event['message']['text']
        self.send(text)

    def websocket_disconnect(self, message):
        print('3333', message)
        data = json.loads(message['text', '{}'])
        chat_id = data.get('chat_id')
        # 断开链接要将这个对象从 channel_layer 中移除
        async_to_sync(self.channel_layer.group_discard)(
            chat_id, self.channel_name)
        raise StopConsumer()

    # def websocket_connect(self, message):
    #     print("WebSocket connected")
    #     self.accept()
    #     CONN_LIST.append(self)
    #
    # def websocket_receive(self, message):
    #     print("message receive",message)
    #     text = message["text"]
    #     print("text receice",text)
    #     res = {'result': 'ok'}
    #     for conn in CONN_LIST:
    #         conn.send(json.dumps(res))
    #     # text_data_json = json.loads(message)
    #     # self.send(text_data=json.dumps({"message":text_data_json}))       # 返回给客户端的消息
    #
    # def websocket_disconnect(self, message):
    #     CONN_LIST.remove(self)
    #     raise StopConsumer()

