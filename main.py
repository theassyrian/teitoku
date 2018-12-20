from teitoku import Teitoku
from teitoku.gateway import LineGateway


app = Teitoku(__name__)
app.register_gateway(LineGateway("n68ONY3J4Vk+vF0kYmeUQIQGBiEMI7k3L4aUIkh1Hx7B8nkCEEALVzBreBkULEYIATpEItFcz9zVAg6Cpa6vwjd2KgM1nFuQsX9fw6DjVTPHWuuiNgSY7mF+zCNG/8eEKIoP6hNJpye+gZp3UnDq7AdB04t89/1O/w1cDnyilFU=", "3a718c3bad0d7b8bdc50adbfb14c4347"))


@app.command("test command")
def handle(req, res):
    print(req.message.content)
    res.message.content = "Command succeed : test command"


app.run()
