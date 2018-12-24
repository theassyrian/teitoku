from teitoku.source import Source

class Message:
    def __init__(self, content=None, content_type: str = None, gateway: str = None, source: Source = None):
        self.content = content
        self.content_type = content_type
        self.gateway = gateway
        self.source = source

    def reply(self):
        pass
