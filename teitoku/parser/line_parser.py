from typing import Union

from teitoku.parser.base_parser import BaseParser
from teitoku.message import TextMessage
from teitoku.source import (Source, SourceUser, SourceRoom, SourceGroup)

import linebot.models as line


class LineParser(BaseParser):
    @staticmethod
    def parse(event):
        if event.message.type == 'text':
            return LineParser.parse_text(event)
        elif event.message.type == 'image':
            return LineParser.parse_image(event)
        else:
            return None

    @staticmethod
    def parse_text(event: line.MessageEvent) -> TextMessage:
        return TextMessage(event.message.text, 'line', LineParser.parse_source(event.source))

    @staticmethod
    def parse_image(message):
        pass

    @staticmethod
    def parse_source(source: line.Source) -> Source:
        if source.type == 'user':
            return SourceUser(source.user_id)
        elif source.type == 'group':
            return SourceGroup(source.group_id, source.user_id)
        elif source.type == 'room':
            return SourceRoom(source.room_id, source.user_id)
        else:
            return None
