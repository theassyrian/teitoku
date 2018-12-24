from typing import Union
import datetime

from teitoku.parser.base_parser import BaseParser
from teitoku.message import TextMessage
from teitoku.source import (Source, SourceUser, SourceRoom, SourceGroup)
from teitoku.intermediate import Request

import linebot.models as line


class LineParser(BaseParser):
    @staticmethod
    def parse(event: line.Event) -> Request:
        raw_message = None
        if event.message.type == 'text':
            raw_message =  LineParser.parse_text(event)
        elif event.message.type == 'image':
            raw_message = LineParser.parse_image(event)
        else:
            return None

        timestamp = datetime.datetime.fromtimestamp(event.timestamp)
        return Request(raw_message, timestamp)


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
