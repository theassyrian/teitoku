from teitoku.message import Message


class Response:
    def __init__(self):
        self.message = Message()
        self.session = None
