from teitoku import Teitoku
from teitoku.gateway import LINE

# app initialization
app = Teitoku(__name__)
line_gateway = LINE("CHANNEL_SECRET", "CHANNEL_ACCESS_TOKEN")

app.add_gateway(line_gateway)


@app.command("!call")
def command_call(req, res):
    res.add_text("Active")
    res.reply()
