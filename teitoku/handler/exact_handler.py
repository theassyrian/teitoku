from teitoku.handler.request_handler import RequestHandler


class ExactHandler(RequestHandler):
    def check_applicable(self, request):
        return request.message.content == self.command
