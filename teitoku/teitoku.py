from threading import Thread
from teitoku.handler import RequestHandler


class Teitoku:
    def __init__(self, name):
        self.name = name
        self.gateways = []
        self.gateway_threads = []

    def command(self, cmd_string):
        def register_handler(handler):
            RequestHandler.register(cmd_string, handler)
            return handler

        return register_handler

    def run(self):
        for gateway in self.gateways:
            self.gateway_threads.append(Thread(target=gateway.listen))
