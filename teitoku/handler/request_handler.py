class RequestHandler:
    def __init__(self):
        self.command = ""

    @classmethod
    def register(cls, command):
        pass

    def check_applicable(self, message):
        pass

    def execute(self, *args, **kwargs):
        pass

    def callback_done(self):
        pass
