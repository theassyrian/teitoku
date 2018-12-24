from teitoku.message.base_message import Message
from teitoku.source import Source

class TextMessage(Message):
    def __init__(self, content:str, gateway:str, source:Source):
        super(TextMessage, self).__init__(content, 'text', gateway, source)
