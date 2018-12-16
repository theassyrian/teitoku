from teitoku.message.base_message import Message


class TelegramMessage(Message):
    def __init__(self):
        super().__init__()
        self.from_gateway = "telegram"

    def reply(self):
        pass
