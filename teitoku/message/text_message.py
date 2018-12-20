from teitoku.message.base_message import Message


class TextMessage(Message):
    def __init__(self, content, sender, sender_type, gateway):
        super().__init__()
        self.content = content
        self.content_type = 'text'
        self.from_gateway = gateway
        self.sender = sender
        self.sender_type = sender_type
