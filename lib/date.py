class Date:
    def __init__(self, id, date, confirmed, space_id):
        self.id = id
        self.date = date
        self.confirmed = confirmed
        self.space_id = space_id

    def __repr__(self):
        return f"Date({self.id}, {self.date}, {self.confirmed}, {self.space_id})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
