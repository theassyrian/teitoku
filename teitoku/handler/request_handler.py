from teitoku.dispatcher import RequestDispatcher


class RequestHandler:
    def __init__(self):
        self.command = ""
        self.handler = None

    @classmethod
    def register(cls, command, handler):
        dispatcher = RequestDispatcher.load()
        request_handler = cls()
        request_handler.command = command
        request_handler.handler = handler
        dispatcher.register_handler(request_handler)

    def check_applicable(self, message):
        pass

    def execute(self, req, res):
        return self.handler(req, res)

    def callback_done(self):
        pass
