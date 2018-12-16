class ResponseDispatcher:
    def __init__(self):
        self.output_gateways = {}

    def dispatch(self, message):
        pass

    def lookup_gateway(self, message):
        pass

    def register_gateway(self, gateway):
        self.output_gateways[gateway.name] = gateway
