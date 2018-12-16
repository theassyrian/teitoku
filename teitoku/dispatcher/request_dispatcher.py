class RequestDispatcher:
    instance = None

    def __init__(self):
        self.handlers = {}
        self.active_events = []
        self.default_message = None

    @classmethod
    def load(cls):
        if RequestDispatcher.instance is None:
            RequestDispatcher.instance = cls()

        return RequestDispatcher.instance

    def dispatch(self, message):
        pass

    def lookup_handler(self, message):
        pass

    def register_handler(self, handler):
        self.handlers[handler.command] = handler

    def handler_callback(self, thread_id):
        pass
