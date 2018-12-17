from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

from .base_gateway import Gateway


class LineGateway(Gateway):
    def __init__(self, channel_access_token, channel_secret,
                 host="localhost", port="5000", webhook_suffix="line"):
        super().__init__()
        self.channel_access_token = channel_access_token
        self.channel_secret = channel_secret
        self.port = port
        self.webhook_suffix = webhook_suffix
        self.host = host

        self.line_bot_api = LineBotApi(self.channel_access_token)
        self.webhook_handler = WebhookHandler(self.channel_secret)

        self.app = Flask("line_gateway")

        @self.app.route("/{}".format(webhook_suffix), methods=['POST', 'GET'])
        def webhook_callback():
            # get X-Line-Signature header value
            signature = request.headers['X-Line-Signature']

            # get request body as text
            body = request.get_data(as_text=True)
            self.app.logger.info("Request body: " + body)

            # handle webhook body
            try:
                self.webhook_handler.handle(body, signature)
            except InvalidSignatureError:
                abort(400)

            return 'OK'

        @self.webhook_handler.add(MessageEvent)
        def handle_message(event):
            print(event)

    def run(self):
        print("Started line webhook on http://{}:{}/{}".format(
              self.host, self.port, self.webhook_suffix))

        self.app.run(self.host, self.port, debug=False)
