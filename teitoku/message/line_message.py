from teitoku.message.base_message import Message


class LineMessage(Message):
    def __init__(self):
        super().__init__()
        self.from_gateway = "line"

    def reply(self):
        pass
