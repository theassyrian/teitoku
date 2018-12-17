from teitoku import Teitoku
from teitoku.gateway import LineGateway

from text_registry import text_command_registry

# app initialization
app = Teitoku(__name__)
line_gateway = LineGateway("CHANNEL_SECRET", "CHANNEL_ACCESS_TOKEN")

app.add_gateway(line_gateway)

app.add_registry(text_command_registry)

if __name__ == "__main__":
    app.run()
