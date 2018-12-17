from teitoku.registy import TextCommandRegistry
from teitoku.session import Session

text_command_registry = TextCommandRegistry()


@text_command_registry.simple("call")
def call_handle(req, res):
    res.add_text("Hibiki!")


@text_command_registry.simple("call")
@session.check_role("admin")
def call_handle(req, req):
    res.add_text("Hello admin")
