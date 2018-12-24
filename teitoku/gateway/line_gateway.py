import bottle

from linebot import (
    LineBotApi, WebhookHandler, WebhookParser
)
from linebot.exceptions import (
    InvalidSignatureError
)

from teitoku.gateway.base_gateway import Gateway
from teitoku.parser.line_parser import LineParser
from teitoku.dispatcher.request_dispatcher import RequestDispatcher


class LineGateway(Gateway):
    def __init__(self, channel_access_token, channel_secret,
                 host="localhost", port="5000", webhook_suffix="line",
                 dispatcher=RequestDispatcher.load(), message_parser=LineParser):
        super().__init__(dispatcher=dispatcher, message_parser=message_parser)
        self.channel_access_token = channel_access_token
        self.channel_secret = channel_secret
        self.port = port
        self.webhook_suffix = webhook_suffix
        self.host = host
        self.line_bot_api = LineBotApi(self.channel_access_token)
        self.webhook_handler = WebhookHandler(self.channel_secret)
        self.parser = WebhookParser(self.channel_secret)
        bottle.default_app().route(path='/', callback=self.landing)
        bottle.default_app().route('/{}'.format(webhook_suffix), callback=self.webhook_callback, method="POST")

    def landing(self):
        return "Running"

    def webhook_callback(self):
        signature = bottle.request.headers['X-Line-Signature']
        body = bottle.request.body.getvalue().decode('utf-8')
        print('%s' % signature)
        try:
            events = self.parser.parse(body, signature)
            for event in events:
                message = self.message_parser.parse(event)
                print(message)
                if message is not None:
                    self.dispatcher.dispatch(message)
        except InvalidSignatureError as e:
            print(e)
            bottle.abort(400)

        return 'OK'

    def run(self):
        print("Started line webhook on http://{}:{}/{}".format(
              self.host, self.port, self.webhook_suffix))

        bottle.run(host=self.host, port=self.port, debug=True)
