class ResponseDispatcher:
    instance = None

    def __init__(self):
        self.output_gateways = {}

    @classmethod
    def load(cls):
        if cls.instance is None:
            cls.instance = cls()

        return cls.instance

    def dispatch(self, message):
        print("Gateway : {}".format(message.gateway))
        print("Content : {}".format(message.content))

    def lookup_gateway(self, message):
        return message.from_gateway

    def register_gateway(self, gateway):
        self.output_gateways[gateway.name] = gateway

    def parse_response(self, response):
        message = response.message
        self.dispatch(message)
