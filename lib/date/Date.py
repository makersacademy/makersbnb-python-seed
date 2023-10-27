from uuid import uuid4

class Date:
    def __init__(self, space_id, date):
        self.id = str(uuid4())
        self.space_id = space_id
        self.date = date
        self.is_available = True

    def __eq__(self, other):
        return self.__dict__ == other.__dict__