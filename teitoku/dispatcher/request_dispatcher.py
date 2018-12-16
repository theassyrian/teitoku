class RequestDispatcher:
    def __init__(self):
        self.handlers = {}
        self.active_events = []
        self.default_message = None

    def dispatch(self, message):
        pass

    def lookup_handler(self, message):
        pass

    def register_handler(self, handler):
        self.handlers[handler.name] = handler

    def handler_callback(self, thread_id):
        pass
