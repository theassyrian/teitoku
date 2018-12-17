from teitoku import Teitoku
from teitoku.dispatcher import RequestDispatcher
from teitoku.message import Message
from time import sleep
from teitoku.gateway import LineGateway


app = Teitoku(__name__)
app.register_gateway(LineGateway("token", "secret"))


@app.command("test command")
def handle(req, res):
    print(req.message.content)
    res.message.content = "Command succeed : test command"


app.run()
