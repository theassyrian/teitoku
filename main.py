from teitoku import Teitoku
from teitoku.gateway import LineGateway


app = Teitoku(__name__)
app.register_gateway(LineGateway(
    "Y/sDIn8h58PDewuOSBvQwL96kZqXsGSuX0XP13WsVfwiC7CaYcUZRr5GTsP3t1LnitkrxcUwca82i3Dtge+w0qLrl3T+I3nyMF4OEAuQPfzYJLv5fu1eZdKIyTpyEB678B4sLNEBe9jRNUVZpRTUOgdB04t89/1O/w1cDnyilFU=", "82d5f15b9b83843e05b1377de96af7a2"))


@app.exact("test command")
def handle(req, res):
    print(req.message.content)
    res.message.content = "Command succeed : test command"


app.run()
