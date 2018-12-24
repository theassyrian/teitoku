from datetime import datetime

from teitoku.message import Message


class Request:
    def __init__(self, raw_message: Message = None, timestamp: datetime = None):
        self.raw_message = raw_message
        self.timestamp = timestamp

    @classmethod
    def parse(cls, cmd_str):
        return cls()
