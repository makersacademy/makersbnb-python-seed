from uuid import uuid4


class Space:
    def __init__(self, name, description, owner_id, start_date, end_date):
        self.id = str(uuid4())
        self.name = name
        self.description = description
        self.owner_id = owner_id
        self.start_date = start_date
        self.end_date = end_date

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
