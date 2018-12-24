from teitoku.source.base_source import Source


class SourceUser(Source):
    """SourceUser"""

    def __init__(self, user_id: str):
        """__init__ method.
        """
        super(SourceUser, self).__init__()
        self.type = 'user'
        self.user_id = user_id


class SourceGroup(Source):
    """SourceUser"""

    def __init__(self, group_id: str, user_id: str):
        """__init__ method."""
        super(SourceGroup, self).__init__()
        self.type = 'group'
        self.user_id = user_id
        self.group_id = group_id


class SourceRoom(Source):
    """SourceUser"""

    def __init__(self, room_id: str, user_id: str):
        """__init__ method."""
        super(SourceRoom, self).__init__()
        self.type = 'room'
        self.user_id = user_id
        self.room_id = room_id
