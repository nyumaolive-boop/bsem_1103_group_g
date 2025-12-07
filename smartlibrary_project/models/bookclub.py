class BookClub:
    def __init__(self, id_, name, description, meeting_day, is_active=True):
        self.id = id_
        self.name = name
        self.description = description
        self.meeting_day = meeting_day
        self.is_active = is_active
