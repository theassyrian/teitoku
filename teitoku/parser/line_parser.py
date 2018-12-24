from teitoku.parser.base_parser import BaseParser
from teitoku.message.text_message import TextMessage


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
    def parse_text(event):
        return TextMessage(
            event.message.text,
            LineParser.parse_source(event),
            event.source.type,
            'line'
        )

    @staticmethod
    def parse_image(message):
        pass

    @staticmethod
    def parse_source(message):
        source = {
            'user_id' : message.source.user_id,
            'group_id' : None,
            'room_id' : None
        }

        if message.source.type == 'group':
            source['group_id'] = message.source.group_id
        elif message.source.type == 'room':
            source['room_id'] = message.source.room_id

        return source
