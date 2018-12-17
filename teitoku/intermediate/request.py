class Request:
    def __init__(self):
        self.session = None
        self.message = None
        self.params = {}

    @classmethod
    def parse(cls, cmd_str):
        return cls()
