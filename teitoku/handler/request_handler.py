from teitoku.dispatcher import RequestDispatcher
from teitoku.dispatcher import ResponseDispatcher


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

    def check_applicable(self, request):
        pass

    def execute(self, req, res):
        self.preprocess(req, res)
        self.handler(req, res)
        self.post_process(req, res)
        return

    def preprocess(self, req, res):
        pass

    def post_process(self, req, res):
        res.message.gateway = req.message.gateway
        dispatcher = ResponseDispatcher.load()
        dispatcher.parse_response(res)
