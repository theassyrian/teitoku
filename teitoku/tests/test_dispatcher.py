from random import randint

from teitoku.dispatcher.request_dispatcher import RequestDispatcher
from teitoku.intermediate import Request
from teitoku.message import Message

check_value = None


class MockHandler:
    def __init__(self):
        self.command = ""

    def check_applicable(self, req):
        return True

    def execute(self, req, res):
        global check_value
        check_value = req.message.content


class MockFalseHandler:
    def __init__(self):
        self.command = ""

    def check_applicable(self, message):
        return False

    def execute(self, req, res):
        global check_value
        check_value = req.message.content


class MockMessage(Message):
    def __init__(self):
        self.content = str(randint(0, 9999))


def test_dispatch_without_handlers():
    dispatcher = RequestDispatcher.load()
    message = MockMessage()
    req = Request(message)
    dispatcher.dispatch(req) # should do nothing, no exception thrown


def test_dispatch_with_handler():
    dispatcher = RequestDispatcher.load()
    dispatcher.register_handler(MockHandler())
    message = MockMessage()
    req = Request(message)
    dispatcher.dispatch(req)
    assert check_value == message.content


def test_dispatch_none_applicable_handler():
    global check_value
    check_value = None

    dispatcher = RequestDispatcher.load()
    dispatcher.register_handler(MockFalseHandler())
    message = MockMessage()
    req = Request(message)
    dispatcher.dispatch(req)
    assert check_value is None
