from datetime import datetime

from teitoku.message import Message


class Request:
    def __init__(self, message: Message = None, timestamp: datetime = None):
        self.message = message
        self.timestamp = timestamp

    @classmethod
    def parse(cls, cmd_str):
        return cls()
