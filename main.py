from teitoku import Teitoku
from teitoku.dispatcher import RequestDispatcher


app = Teitoku(__name__)


@app.command("test command")
def handle(req, res):
    return "hello world"


dispatcher = RequestDispatcher.load()
print(dispatcher.handlers)

print(dispatcher.handlers["test command"].execute(None, None))
