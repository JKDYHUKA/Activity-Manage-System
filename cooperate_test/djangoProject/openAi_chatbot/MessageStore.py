class MessageGenerator:
    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content

    def get_message_object(self):
        return {'role': self.role, 'content': self.content}


class MessageLib:
    def __init__(self):
        self.message_array = []

    def add_message(self, message: MessageGenerator):
        self.message_array.append(message)

    def get_messages(self):
        return self.message_array
