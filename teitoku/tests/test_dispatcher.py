from random import randint

from teitoku.dispatcher.request_dispatcher import RequestDispatcher

check_value = None


class MockHandler:
    def __init__(self):
        self.command = ""

    def check_applicable(self, message):
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


class MockMessage:
    def __init__(self):
        self.content = str(randint(0, 9999))


def test_dispatch_without_handlers():
    dispatcher = RequestDispatcher.load()
    message = MockMessage()
    dispatcher.dispatch(message) # should do nothing, no exception thrown


def test_dispatch_with_handler():
    dispatcher = RequestDispatcher.load()
    dispatcher.register_handler(MockHandler())
    message = MockMessage()
    dispatcher.dispatch(message)
    assert check_value == message.content


def test_dispatch_none_applicable_handler():
    global check_value
    check_value = None

    dispatcher = RequestDispatcher.load()
    dispatcher.register_handler(MockFalseHandler())
    message = MockMessage()
    dispatcher.dispatch(message)
    assert check_value is None
