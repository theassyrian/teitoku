import bottle

from linebot import (
    LineBotApi, WebhookHandler, WebhookParser
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

from teitoku.gateway.base_gateway import Gateway
from teitoku.parser.line_parser import LineParser
from teitoku.dispatcher.request_dispatcher import RequestDispatcher


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
        self.parser = WebhookParser(self.channel_secret)

        @bottle.route('/')
        def landing():
            return "Running"

        @bottle.post("/{}".format(webhook_suffix))
        def webhook_callback():
            signature = bottle.request.headers['X-Line-Signature']
            body = bottle.request.body.getvalue().decode('utf-8')
            print('%s' % signature)
            try:
                events = self.parser.parse(body, signature)
                for event in events:
                    message = LineParser.parse(event)
                    print(message)
                    if message is not None:
                        dispatcher = RequestDispatcher.load()
                        dispatcher.dispatch(message)
            except InvalidSignatureError as e:
                print(e)
                bottle.abort(400)

            return 'OK'

    def run(self):
        print("Started line webhook on http://{}:{}/{}".format(
              self.host, self.port, self.webhook_suffix))

        bottle.run(host=self.host, port=self.port, debug=True)
