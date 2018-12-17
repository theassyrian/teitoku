from threading import Thread
from teitoku.handler import RequestHandler
from time import sleep


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

    def register_gateway(self, gateway):
        self.gateways.append(gateway)

    def run(self):
        print("run teitoku")
        for gateway in self.gateways:
            self.gateway_threads.append(
                Thread(target=gateway.run, name=gateway.__class__.__name__))

        for thread in self.gateway_threads:
            thread.start()
