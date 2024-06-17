import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
from channels.exceptions import StopConsumer
from .chat_utils import ask_openai
import redis
from activity_feedback.models import *


class ChatConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.redis = redis.Redis(host='localhost', port=6379, db=0)
        self.gpt_role = {
            'role': 'system',
            'content': '你是一个在群聊中的聊天机器人，每句话开头的用户名表示说这句话的人的名字，你需要结合上下文语境给出回答'
        }

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

        history = self.get_history_messages(self.room_group_name)
        for message_data in history:
            self.send(text_data=json.dumps(message_data))

    def websocket_receive(self, message):
        # 浏览器基于websocket向后端发送数据，自动触发接收消息
        print('222', message)
        data = json.loads(message['text'])
        user_id = data.get('user_id')
        chat_id = data.get('chat_id')
        sysMsgType = data.get('sysMsgType')
        chat_content = data.get('data')
        user_name = data.get('user_name')
        isGuests = data.get('isGuests')
        print('message: ', chat_content)

        # 自己的消息
        # type: 'my'
        # isMy: 'true'

        # 别人的消息
        # type：'other'
        # isMy: 'false'

        # 存入Redis
        redis_key = f"chat_messages:{chat_id}"
        message_to_store = {
            'user_id': user_id,
            'chat_id': chat_id,
            'sysMsgtype': sysMsgType,
            'chat_content': chat_content,
            'user_name': user_name,
            'isGuests': isGuests
        }
        if chat_content is not None:
            if chat_content != '':
                self.redis.lpush(redis_key, json.dumps(message_to_store))

        # 通知组内的所有客户端，执行 chat_message 方法，在此方法中自己可以去定义任意的功能。
        async_to_sync(self.channel_layer.group_send)(
            chat_id, {"type": 'chat_message', 'message': message})

        if chat_content is not None:
            if chat_content.startswith("@chatgpt"):

                ask_prompt = chat_content[8:]

                context = [self.gpt_role]

                history_mes = self.get_history_messages(chat_id)
                for mes in history_mes:
                    user_name = mes.get('user_name')
                    standard_mes = {
                        'role': 'user',
                        'content': f"{user_name}: {mes.get('content')}"
                    }
                    context.append(standard_mes)

                context.append({
                    "role": 'user',
                    'content': ask_prompt
                })

                response = ask_openai(context)
                print(response)
                gpt_message_to_store = {
                    'user_id': "00000000",
                    'chat_id': chat_id,
                    'sysMsgtype': sysMsgType,
                    'chat_content': response,
                    'user_name': 'GPT',
                    'isGuests': 'true'
                }
                self.redis.lpush(redis_key, json.dumps(gpt_message_to_store))

                async_to_sync(self.channel_layer.group_send)(
                    chat_id, {"type": 'chatgpt', 'message': response})

    def chatgpt(self, event):
        message = event['message']
        self.send(text_data=json.dumps({'content': message,
                                        'user_id': '00000000',
                                        'user_name': 'GPT',
                                        'type':'history',
                                        'isGuests': 'true'}))


    # 这个方法对应上面的type，意为向1314组中的所有对象发送信息
    # 回调的方法
    def chat_message(self, event):
        text = event['message']['text']
        self.send(text)


    def websocket_disconnect(self, message):
        print('3333', message)

        chat_id = self.room_name

        # data = json.loads(message['text', '{}'])
        # chat_id = data.get('chat_id')

        history = self.get_history_messages(self.room_group_name)
        try:
            act_data = ActivityData.objects.get(activity_id=self.room_group_name)
            # 如果成功获取到值，则执行以下操作
            act_data.chat_num=len(history)
            act_data.save()
        except ActivityData.DoesNotExist:
            ActivityData.objects.create(activity_id=self.room_group_name, chat_num=len(history))
        # 断开链接要将这个对象从 channel_layer 中移除
        async_to_sync(self.channel_layer.group_discard)(
            chat_id, self.channel_name)
        raise StopConsumer()

    def get_history_messages(self, room_group_name):
        # 从Redis中获取历史消息
        redis_key = f"chat_messages:{room_group_name}"
        messages = []
        message_list = self.redis.lrange(redis_key, 0, -1)

        for message_json in reversed(message_list):
            message_data = json.loads(message_json)
            messages.append(self.process_message(message_data))
        return messages


    def process_message(self, message_data):
        user_id = message_data.get('user_id')
        chat_id = message_data.get('chat_id')
        sysMsgtype = message_data.get('sysMsgtype')
        chat_content = message_data.get('chat_content')
        user_name = message_data.get('user_name')
        isGuests = message_data.get('isGuests')

        mes = {
            'content': chat_content,
            'type': 'history',
            'user_id': user_id,
            'isMy': '',
            'user_name': user_name,
            'isGuests': isGuests,
        }

        return mes

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
