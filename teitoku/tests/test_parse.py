import linebot.models as models

from teitoku.parser.line_parser import LineParser
from teitoku.message.text_message import TextMessage
from teitoku.source import SourceUser, SourceGroup, SourceRoom


def test_parse_text_message_source_user():
    text_message = models.TextMessage("123", "test")
    source = models.SourceUser("user1")
    message_event = models.MessageEvent(
        None, source, "reply_token", text_message)

    parsed_message = LineParser.parse(message_event)

    assert parsed_message.content == "test"
    assert parsed_message.content_type == "text"
    assert parsed_message.gateway == "line"
    assert isinstance(parsed_message.source, SourceUser)
    assert parsed_message.source.user_id == 'user1'


def test_parse_text_message_source_group():
    text_message = models.TextMessage("123", "test")
    source = models.SourceGroup("group1", "user1")
    message_event = models.MessageEvent(
        None, source, "reply_token", text_message)

    parsed_message = LineParser.parse(message_event)

    assert parsed_message.content == "test"
    assert parsed_message.content_type == "text"
    assert parsed_message.gateway == "line"
    assert isinstance(parsed_message.source, SourceGroup)
    assert parsed_message.source.user_id == 'user1'
    assert parsed_message.source.group_id == 'group1'


def test_parse_text_message_source_room():
    text_message = models.TextMessage("123", "test")
    source = models.SourceRoom("room1", "user1")
    message_event = models.MessageEvent(
        None, source, "reply_token", text_message)

    parsed_message = LineParser.parse(message_event)

    assert parsed_message.content == "test"
    assert parsed_message.content_type == "text"
    assert parsed_message.gateway == "line"
    assert isinstance(parsed_message.source, SourceRoom)
    assert parsed_message.source.user_id == 'user1'
    assert parsed_message.source.room_id == 'room1'
