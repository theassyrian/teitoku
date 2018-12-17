from flask import Flask
from .base_gateway import Gateway


class LineGateway(Gateway):
    def __init__(self, channel_access_token, channel_secret,
                 host="localhost", port="5000", webhook_suffix="/line"):
        super().__init__()
        self.channel_access_token = channel_access_token
        self.channel_secret = channel_secret
        self.port = port
        self.webhook_suffix = webhook_suffix
        self.host = host

        self.app = Flask("line_gateway")

    def run(self):
        self.app.run(self.host, self.port)
