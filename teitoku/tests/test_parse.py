import linebot.models as models

from teitoku.parser.line_parser import LineParser
from teitoku.message.text_message import TextMessage


def test_parse_text_message_source_user():
    text_message = models.TextMessage("123", "test")
    source = models.SourceUser("user1")
    message_event = models.MessageEvent(
        None, source, "reply_token", text_message)

    parsed_message = LineParser.parse(message_event)  # type: TextMessage

    assert parsed_message.content == "test"
    assert parsed_message.content_type == "text"
    assert parsed_message.from_gateway == "line"
    assert parsed_message.sender_type == "user"
    assert parsed_message.sender == {
        'user_id': "user1",
        'group_id': None,
        'room_id': None
    }


def test_parse_text_message_source_group():
    text_message = models.TextMessage("123", "test")
    source = models.SourceGroup("group1", "user1")
    message_event = models.MessageEvent(
        None, source, "reply_token", text_message)

    parsed_message = LineParser.parse(message_event)  # type: TextMessage

    assert parsed_message.content == "test"
    assert parsed_message.content_type == "text"
    assert parsed_message.from_gateway == "line"
    assert parsed_message.sender_type == "group"
    assert parsed_message.sender == {
        'user_id': "user1",
        'group_id': "group1",
        'room_id': None
    }


def test_parse_text_message_source_room():
    text_message = models.TextMessage("123", "test")
    source = models.SourceRoom("room1", "user1")
    message_event = models.MessageEvent(
        None, source, "reply_token", text_message)

    parsed_message = LineParser.parse(message_event)  # type: TextMessage

    assert parsed_message.content == "test"
    assert parsed_message.content_type == "text"
    assert parsed_message.from_gateway == "line"
    assert parsed_message.sender_type == "room"
    assert parsed_message.sender == {
        'user_id': "user1",
        'group_id': None,
        'room_id': "room1"
    }
