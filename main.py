from teitoku import Teitoku
from teitoku.dispatcher import RequestDispatcher
from teitoku.message import Message
from time import sleep


app = Teitoku(__name__)


@app.command("test command")
def handle(req, res):
    print(req.message.content)
    res.message.content = "Command succeed : test command"


dispatcher = RequestDispatcher.load()
print(dispatcher.handlers)

message = Message()
message.content = "test command"

dispatcher.dispatch(message)
sleep(5)